import SQLConnect
import ClassPracovniStitek
import generuj_excel
import odeslat_mail

def generic_web_function(sqltype, valdict, table, idval, idname):
    if sqltype == 'INSERT':
        sqlquery = 'INSERT INTO ' + table + '('
        for i in valdict:
            if i[:2] != 'id':
                sqlquery += i + ', '
        sqlquery = sqlquery[:-2]
        sqlquery += ") VALUES ("
        for i in valdict:
            if i[:2] != 'id':
                sqlquery += "'" + valdict[i] + "', "
        sqlquery = sqlquery[:-2]
        sqlquery += ");"
        sqlquery = sqlquery.replace("'NULL'", "NULL")
        SQLConnect.query('INSERT', sqlquery)
    elif sqltype == 'UPDATE':
        sqlquery = 'UPDATE ' + table + ' SET '
        changed = False
        for i in valdict:
            if valdict[i] != "<same>":
                sqlquery += i + " = '" + valdict[i] + "', "
                changed = True
        sqlquery = sqlquery[:-2] + " where " + idname + " = " + str(idval) + ";"
        if changed:
            SQLConnect.query('UPDATE', sqlquery)
    elif sqltype == 'DELETE':
        sqlquery = 'DELETE FROM ' + table + " where " + idname + " = " + str(idval) + ";"
        SQLConnect.query('DELETE', sqlquery)


def count_class_sizes(all_students, class_capacity):
    class_students = []
    class_num = round((all_students / class_capacity)+0.5)
    print(class_num)
    students_in_class = int(all_students / class_num)
    reminder = all_students - (students_in_class * class_num)
    rem_tmp = 1
    for i in range(class_num):
        if rem_tmp <= reminder:
            class_students.append(students_in_class + 1)
        else:
            class_students.append(students_in_class)
        rem_tmp += 1
    return class_students


def vytvorit_stitky():
    sqlquery = '''
                SELECT * from stitky_ke_zpracovani;
                '''
    list_zmen = SQLConnect.query('SELECT', sqlquery)
    for zmena in list_zmen:
        celkem_studenti = zmena[5]
        velikost_tridy = zmena[3]
        tridy_na_stitcich = zmena[6]
        id_predmet = zmena[0]
        typ_stitku = zmena[1]
        tmp = count_class_sizes(celkem_studenti, velikost_tridy)
        while len(tmp) < tridy_na_stitcich:  # existuje p????li?? mnoho z??znam?? v sql
            tmp.append(0)
        if len(tmp) > tridy_na_stitcich:  # neexistuje dostatek z??znam?? v sql
            sqlquery = 'SELECT * FROM predmet where id_predmet = %s;' % id_predmet
            predmet_info = SQLConnect.query('SELECTROW', sqlquery)
            p_nazev = predmet_info[1]
            p_tydnu = predmet_info[6]
            p_jazyk = predmet_info[7]
            p_semestr = predmet_info[10]
            p_studium = predmet_info[8]
            p_vazba_zapocet = predmet_info[15]
            p_vazba_klasz = predmet_info[16]
            p_vazba_zkouska = predmet_info[17]

            je_zap = False
            je_klas = False
            je_zk = False

            if typ_stitku == 'p??edn????ka':
                ts = 'prednaska'
                p_hodin = predmet_info[3]
                if p_vazba_zapocet == 'p??edn????ka':
                    je_zap = True
                if p_vazba_klasz == 'p??edn????ka':
                    je_klas = True
                if p_vazba_zkouska == 'p??edn????ka':
                    je_zk = True
            elif typ_stitku == 'semin????':
                ts = 'seminar'
                p_hodin = predmet_info[4]
                if p_vazba_zapocet == 'semin????':
                    je_zap = True
                if p_vazba_klasz == 'semin????':
                    je_klas = True
                if p_vazba_zkouska == 'semin????':
                    je_zk = True
            elif typ_stitku == 'cvi??en??':
                ts = 'cviceni'
                p_hodin = predmet_info[5]
                if p_vazba_zapocet == 'cvi??en??':
                    je_zap = True
                if p_vazba_klasz == 'cvi??en??':
                    je_klas = True
                if p_vazba_zkouska == 'cvi??en??':
                    je_zk = True
            else:
                p_hodin = 0
            sqlquery = "SELECT * from zamestnanciupredmetu where cid_predmet = %s and %s = True" % (id_predmet, ts)
            zam = SQLConnect.query('SELECT', sqlquery)
            cid_zamestnanec = None
            if len(zam) == 1:
                cid_zamestnanec = zam[0][2]
            for x in range(len(tmp) - tridy_na_stitcich):
                sqlquery = """INSERT INTO pracovnistitek (nazev, cid_predmet, cid_zamestnanec, typ, semestr, studium, pocet_hodin, pocet_tydnu, jazyk,
                            rozvrhovany_pocet_studentu, je_zapocet, je_klasifikovany_zapocet, je_zkouska)  VALUES ('%s',%s,%s,'%s','%s','%s',%s,%s,'%s',%s,%s,%s,%s);""" \
                           % (p_nazev + " - " + typ_stitku, id_predmet, cid_zamestnanec, typ_stitku, p_semestr,
                              p_studium, p_hodin, p_tydnu, p_jazyk,  velikost_tridy, je_zap, je_klas, je_zk)
                sqlquery = sqlquery.replace(",None,", ",NULL,")
                SQLConnect.query('INSERT', sqlquery)


        sqlquery = "SELECT id_pracovni_stitek FROM pracovnistitek WHERE cid_predmet = %s and typ = '%s' " \
                   "ORDER BY id_pracovni_stitek;" % (id_predmet, typ_stitku)
        idlist = SQLConnect.query('SELECT', sqlquery)
        for i in range(len(tmp)):
            sqlquery = "UPDATE pracovnistitek set pocet_studentu = %s where id_pracovni_stitek = %s " % (tmp[i], idlist[i][0])
            SQLConnect.query('UPDATE', sqlquery)


def doplnit_zamestnance(data):
    for radek in data:
        if data[radek] == '':
            continue
        if data[radek] == '????dn??':
            sqlquery = "UPDATE pracovnistitek set cid_zamestnanec = NULL where id_pracovni_stitek = %s " % radek
        else:
            sqlquery = "UPDATE pracovnistitek set cid_zamestnanec = %s where id_pracovni_stitek = %s " % (data[radek].split("-")[0], radek)
        SQLConnect.query('UPDATE', sqlquery)


def doplnit_predmety_ve_skupinach(data):
    # zjistit, zda zalo??it nov?? z??znam
    if data['0_predmet'] not in ['', 'smazat'] and data['0_skupina'] not in ['', 'smazat']:
        predm = int(data['0_predmet'].split('-')[0])
        skup = int(data['0_skupina'].split('-')[0])
        sqlquery = "INSERT INTO predmetyveskupine (cid_predmet, cid_studijni_skupina) VALUES (%s, %s)" % (predm, skup)
        print(sqlquery)
        SQLConnect.query('INSERT', sqlquery)
    # check jednotliv??ch z??znam??
    idu = 1
    while True:
        try:
            predm = (data[str(idu)+'_predmet'].split('-')[0])
            skup = (data[str(idu)+'_skupina'].split('-')[0])
        except:
            break

        # M?? se ????dek smazat?
        if predm == 'smazat' and skup == 'smazat':
            sqlquery = "DELETE from predmetyveskupine where id_predmety_ve_skupine = %s" % idu
            SQLConnect.query('DELETE', sqlquery)
            idu += 1
            continue
        # Je na ????dku zm??na?
        if predm in ['', 'smazat'] and skup in ['', 'smazat']:
            idu += 1
            continue
        sqlquery = 'UPDATE predmetyveskupine set '
        if predm not in ['', 'smazat']:
            sqlquery += 'cid_predmet = %s, ' % str(predm)
        if skup not in ['', 'smazat']:
            sqlquery += 'cid_studijni_skupina = %s, ' % str(skup)
        sqlquery = sqlquery[:-2] + "where id_predmety_ve_skupine = %s" % str(idu)

        SQLConnect.query('UPDATE', sqlquery)
        idu += 1


def generuj_a_odesli_excel(data):
    seznam = []
    opravdovemaily = False
    for i in data:
        if i != 'opravdovemaily':
            seznam.append(int(i))
        else:
            opravdovemaily = True
    print(seznam)
    for i in seznam:
        generuj_excel.vygenerovat_uvazky(i)
        odeslat_mail.odeslat_mail(i, opravdovemaily)


def generuj_csv(data):
    outputdata = []
    text = 'id_pracovni_stitek;nazev;cid_zamestnanec;cid_predmet;typ;pocet_studentu;pocet_hodin;pocet_tydnu;jazyk;semestr;studium;pracovni_body;rozvrhovany_pocet_studentu;je_zapocet;pracovni_body_zapocet;je_klasifikovany_zapocet;pracovni_body_klasifikovany_zapocet;je_zkouska;pracovni_body_zkouska;jmeno;zkratka;predmet\n'
    outputdata.append(text)
    for radek in data:
        text = ''
        for udaj in radek:
            text += str(udaj) + ";"
        text += "\n"
        outputdata.append(text)

    return outputdata
