from config import use_db
from SQLConnect import query


class PracovniStitek:
    def __init__(self, id_pracovni_stitek, nazev, cid_zamestnanec, cid_predmet, typ, pocet_studentu, pocet_hodin, 
                 pocet_tydnu, jazyk, pracovni_body):
        self.id_pracovni_stitek = id_pracovni_stitek
        self.nazev = nazev
        self.cid_zamestnanec = cid_zamestnanec
        self.cid_predmet = cid_predmet
        self.typ = typ
        self.pocet_studentu = pocet_studentu
        self.pocet_hodin = pocet_hodin
        self.pocet_tydnu = pocet_tydnu
        self.jazyk = jazyk
        self.pracovni_body = pracovni_body

    sloupce = ['id_pracovni_stitek', 'nazev', 'cid_zamestnanec', 'cid_predmet', 'typ', 'pocet_studentu', 
             'pocet_hodin', 'pocet_tydnu', 'jazyk', 'pracovni_body']

    def update(self, id_pracovni_stitek='NULL', nazev='NULL', cid_zamestnanec='NULL', cid_predmet='NULL', typ='NULL', 
               pocet_studentu='NULL', pocet_hodin='NULL', pocet_tydnu='NULL', jazyk='NULL', pracovni_body='NULL'):
        condition = ''
        if id_pracovni_stitek != 'NULL':
            self.id_pracovni_stitek = id_pracovni_stitek
            condition += 'id_pracovni_stitek=' + "'" + str(id_pracovni_stitek) + "', " 
        if nazev != 'NULL':
            self.nazev = nazev
            condition += 'nazev=' + "'" + str(nazev) + "', " 
        if cid_zamestnanec != 'NULL':
            self.cid_zamestnanec = cid_zamestnanec
            condition += 'cid_zamestnanec=' + "'" + str(cid_zamestnanec) + "', " 
        if cid_predmet != 'NULL':
            self.cid_predmet = cid_predmet
            condition += 'cid_predmet=' + "'" + str(cid_predmet) + "', " 
        if typ != 'NULL':
            self.typ = typ
            condition += 'typ=' + "'" + str(typ) + "', " 
        if pocet_studentu != 'NULL':
            self.pocet_studentu = pocet_studentu
            condition += 'pocet_studentu=' + "'" + str(pocet_studentu) + "', " 
        if pocet_hodin != 'NULL':
            self.pocet_hodin = pocet_hodin
            condition += 'pocet_hodin=' + "'" + str(pocet_hodin) + "', " 
        if pocet_tydnu != 'NULL':
            self.pocet_tydnu = pocet_tydnu
            condition += 'pocet_tydnu=' + "'" + str(pocet_tydnu) + "', " 
        if jazyk != 'NULL':
            self.jazyk = jazyk
            condition += 'jazyk=' + "'" + str(jazyk) + "', " 
        if pracovni_body != 'NULL':
            self.pracovni_body = pracovni_body
            condition += 'pracovni_body=' + "'" + str(pracovni_body) + "', " 
        if use_db == 1:
            condition = condition[:-2]
            sqltext = 'UPDATE PracovniStitek set %s where id_pracovni_stitek = %s ;' % (condition, 
                                                                                        self.id_pracovni_stitek)
            query('UPDATE', sqltext)

    def select(self):
        return [self.id_pracovni_stitek, self.nazev, self.cid_zamestnanec, self.cid_predmet, self.typ, 
                self.pocet_studentu, self.pocet_hodin, self.pocet_tydnu, self.jazyk, self.pracovni_body]


def insert(classdict, nazev, cid_zamestnanec, cid_predmet, typ, pocet_studentu, pocet_hodin, pocet_tydnu, jazyk, 
           pracovni_body):
    if use_db == 1:
        sqltext = """INSERT INTO PracovniStitek (nazev, cid_zamestnanec, cid_predmet, typ, pocet_studentu, 
                                                 pocet_hodin, pocet_tydnu, jazyk, pracovni_body) VALUES (""" 
        for var in [nazev, cid_zamestnanec, cid_predmet, typ, pocet_studentu, pocet_hodin, pocet_tydnu, jazyk, 
                    pracovni_body]:
            if var is not None and var != "":
                sqltext += "'" + str(var) + "', "
            else:
                sqltext += "''" + ', ' 
        sqltext = sqltext[:-2] + ");"
        query('INSERT', sqltext)
    new_id = len(classdict) + 1
    new_instance = PracovniStitek(new_id, nazev, cid_zamestnanec, cid_predmet, typ, pocet_studentu, pocet_hodin, 
                                  pocet_tydnu, jazyk, pracovni_body)
    classdict[new_id] = new_instance
    return classdict


def podmineny_select(classdict, id_pracovni_stitek='NULL', nazev='NULL', cid_zamestnanec='NULL', cid_predmet='NULL', 
                     typ='NULL', pocet_studentu='NULL', pocet_hodin='NULL', pocet_tydnu='NULL', jazyk='NULL', 
                     pracovni_body='NULL'):
    newdict = {}
    for line in classdict:
        if (classdict[line].id_pracovni_stitek == id_pracovni_stitek or id_pracovni_stitek == 'NULL') and \
                (classdict[line].nazev == nazev or nazev == 'NULL') and \
                (classdict[line].cid_zamestnanec == cid_zamestnanec or cid_zamestnanec == 'NULL') and \
                (classdict[line].cid_predmet == cid_predmet or cid_predmet == 'NULL') and \
                (classdict[line].typ == typ or typ == 'NULL') and \
                (classdict[line].pocet_studentu == pocet_studentu or pocet_studentu == 'NULL') and \
                (classdict[line].pocet_hodin == pocet_hodin or pocet_hodin == 'NULL') and \
                (classdict[line].pocet_tydnu == pocet_tydnu or pocet_tydnu == 'NULL') and \
                (classdict[line].jazyk == jazyk or jazyk == 'NULL') and \
                (classdict[line].pracovni_body == pracovni_body or pracovni_body == 'NULL'):
            newdict[line] = classdict[line]

    return newdict


def initial_values(data):
    return data
