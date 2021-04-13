from config import use_db
from SQLConnect import query


class Predmet:
    def __init__(self, id_predmet, zkratka, nazev, hodin_prednaska, hodin_seminar, hodin_cviceni, pocet_tydnu, jazyk, 
                 studium, rocnik, semestr, pocet_kreditu, studentu_prednaska, studentu_seminar, studentu_cviceni, 
                 vazba_zapocet, vazba_klasifikovany_zapocet, vazba_zkouska):
        self.id_predmet = id_predmet
        self.zkratka = zkratka
        self.nazev = nazev
        self.hodin_prednaska = hodin_prednaska
        self.hodin_seminar = hodin_seminar
        self.hodin_cviceni = hodin_cviceni
        self.pocet_tydnu = pocet_tydnu
        self.jazyk = jazyk
        self.studium = studium
        self.rocnik = rocnik
        self.semestr = semestr
        self.pocet_kreditu = pocet_kreditu
        self.studentu_prednaska = studentu_prednaska
        self.studentu_seminar = studentu_seminar
        self.studentu_cviceni = studentu_cviceni
        self.vazba_zapocet = vazba_zapocet
        self.vazba_klasifikovany_zapocet = vazba_klasifikovany_zapocet
        self.vazba_zkouska = vazba_zkouska

    sloupce = ['id_predmet', 'zkratka', 'nazev', 'hodin_prednaska', 'hodin_seminar', 'hodin_cviceni', 'pocet_tydnu', 
             'jazyk', 'studium', 'rocnik', 'semestr', 'pocet_kreditu', 'studentu_prednaska', 'studentu_seminar', 
             'studentu_cviceni', 'vazba_zapocet', 'vazba_klasifikovany_zapocet', 'vazba_zkouska']

    def update(self, id_predmet='NULL', zkratka='NULL', nazev='NULL', hodin_prednaska='NULL', hodin_seminar='NULL', 
               hodin_cviceni='NULL', pocet_tydnu='NULL', jazyk='NULL', studium='NULL', rocnik='NULL', semestr='NULL', 
               pocet_kreditu='NULL', studentu_prednaska='NULL', studentu_seminar='NULL', studentu_cviceni='NULL', 
               vazba_zapocet='NULL', vazba_klasifikovany_zapocet='NULL', vazba_zkouska='NULL'):
        condition = ''
        if id_predmet != 'NULL':
            self.id_predmet = id_predmet
            condition += 'id_predmet=' + "'" + str(id_predmet) + "', " 
        if zkratka != 'NULL':
            self.zkratka = zkratka
            condition += 'zkratka=' + "'" + str(zkratka) + "', " 
        if nazev != 'NULL':
            self.nazev = nazev
            condition += 'nazev=' + "'" + str(nazev) + "', " 
        if hodin_prednaska != 'NULL':
            self.hodin_prednaska = hodin_prednaska
            condition += 'hodin_prednaska=' + "'" + str(hodin_prednaska) + "', " 
        if hodin_seminar != 'NULL':
            self.hodin_seminar = hodin_seminar
            condition += 'hodin_seminar=' + "'" + str(hodin_seminar) + "', " 
        if hodin_cviceni != 'NULL':
            self.hodin_cviceni = hodin_cviceni
            condition += 'hodin_cviceni=' + "'" + str(hodin_cviceni) + "', " 
        if pocet_tydnu != 'NULL':
            self.pocet_tydnu = pocet_tydnu
            condition += 'pocet_tydnu=' + "'" + str(pocet_tydnu) + "', " 
        if jazyk != 'NULL':
            self.jazyk = jazyk
            condition += 'jazyk=' + "'" + str(jazyk) + "', " 
        if studium != 'NULL':
            self.studium = studium
            condition += 'studium=' + "'" + str(studium) + "', " 
        if rocnik != 'NULL':
            self.rocnik = rocnik
            condition += 'rocnik=' + "'" + str(rocnik) + "', " 
        if semestr != 'NULL':
            self.semestr = semestr
            condition += 'semestr=' + "'" + str(semestr) + "', " 
        if pocet_kreditu != 'NULL':
            self.pocet_kreditu = pocet_kreditu
            condition += 'pocet_kreditu=' + "'" + str(pocet_kreditu) + "', " 
        if studentu_prednaska != 'NULL':
            self.studentu_prednaska = studentu_prednaska
            condition += 'studentu_prednaska=' + "'" + str(studentu_prednaska) + "', " 
        if studentu_seminar != 'NULL':
            self.studentu_seminar = studentu_seminar
            condition += 'studentu_seminar=' + "'" + str(studentu_seminar) + "', " 
        if studentu_cviceni != 'NULL':
            self.studentu_cviceni = studentu_cviceni
            condition += 'studentu_cviceni=' + "'" + str(studentu_cviceni) + "', " 
        if vazba_zapocet != 'NULL':
            self.vazba_zapocet = vazba_zapocet
            condition += 'vazba_zapocet=' + "'" + str(vazba_zapocet) + "', " 
        if vazba_klasifikovany_zapocet != 'NULL':
            self.vazba_klasifikovany_zapocet = vazba_klasifikovany_zapocet
            condition += 'vazba_klasifikovany_zapocet=' + "'" + str(vazba_klasifikovany_zapocet) + "', " 
        if vazba_zkouska != 'NULL':
            self.vazba_zkouska = vazba_zkouska
            condition += 'vazba_zkouska=' + "'" + str(vazba_zkouska) + "', " 
        if use_db == 1:
            condition = condition[:-2]
            sqltext = 'UPDATE Predmet set %s where id_predmet = %s ;' % (condition, self.id_predmet)
            query('UPDATE', sqltext)

    def select(self):
        return [self.id_predmet, self.zkratka, self.nazev, self.hodin_prednaska, self.hodin_seminar, 
                self.hodin_cviceni, self.pocet_tydnu, self.jazyk, self.studium, self.rocnik, self.semestr, 
                self.pocet_kreditu, self.studentu_prednaska, self.studentu_seminar, self.studentu_cviceni, 
                self.vazba_zapocet, self.vazba_klasifikovany_zapocet, self.vazba_zkouska]


def insert(classdict, zkratka, nazev, hodin_prednaska, hodin_seminar, hodin_cviceni, pocet_tydnu, jazyk, studium, 
           rocnik, semestr, pocet_kreditu, studentu_prednaska, studentu_seminar, studentu_cviceni, vazba_zapocet, 
           vazba_klasifikovany_zapocet, vazba_zkouska):
    if use_db == 1:
        sqltext = """INSERT INTO Predmet (zkratka, nazev, hodin_prednaska, hodin_seminar, hodin_cviceni, pocet_tydnu, 
                                          jazyk, studium, rocnik, semestr, pocet_kreditu, studentu_prednaska, 
                                          studentu_seminar, studentu_cviceni, vazba_zapocet, 
                                          vazba_klasifikovany_zapocet, vazba_zkouska) VALUES (""" 
        for var in [zkratka, nazev, hodin_prednaska, hodin_seminar, hodin_cviceni, pocet_tydnu, jazyk, studium, 
                    rocnik, semestr, pocet_kreditu, studentu_prednaska, studentu_seminar, studentu_cviceni, 
                    vazba_zapocet, vazba_klasifikovany_zapocet, vazba_zkouska]:
            if var is not None and var != "":
                sqltext += "'" + str(var) + "', "
            else:
                sqltext += "''" + ', ' 
        sqltext = sqltext[:-2] + ");"
        query('INSERT', sqltext)
    new_id = len(classdict) + 1
    new_instance = Predmet(new_id, zkratka, nazev, hodin_prednaska, hodin_seminar, hodin_cviceni, pocet_tydnu, jazyk, 
                           studium, rocnik, semestr, pocet_kreditu, studentu_prednaska, studentu_seminar, 
                           studentu_cviceni, vazba_zapocet, vazba_klasifikovany_zapocet, vazba_zkouska)
    classdict[new_id] = new_instance
    return classdict


def podmineny_select(classdict, id_predmet='NULL', zkratka='NULL', nazev='NULL', hodin_prednaska='NULL', 
                     hodin_seminar='NULL', hodin_cviceni='NULL', pocet_tydnu='NULL', jazyk='NULL', studium='NULL', 
                     rocnik='NULL', semestr='NULL', pocet_kreditu='NULL', studentu_prednaska='NULL', 
                     studentu_seminar='NULL', studentu_cviceni='NULL', vazba_zapocet='NULL', 
                     vazba_klasifikovany_zapocet='NULL', vazba_zkouska='NULL'):
    newdict = {}
    for line in classdict:
        if (classdict[line].id_predmet == id_predmet or id_predmet == 'NULL') and \
                (classdict[line].zkratka == zkratka or zkratka == 'NULL') and \
                (classdict[line].nazev == nazev or nazev == 'NULL') and \
                (classdict[line].hodin_prednaska == hodin_prednaska or hodin_prednaska == 'NULL') and \
                (classdict[line].hodin_seminar == hodin_seminar or hodin_seminar == 'NULL') and \
                (classdict[line].hodin_cviceni == hodin_cviceni or hodin_cviceni == 'NULL') and \
                (classdict[line].pocet_tydnu == pocet_tydnu or pocet_tydnu == 'NULL') and \
                (classdict[line].jazyk == jazyk or jazyk == 'NULL') and \
                (classdict[line].studium == studium or studium == 'NULL') and \
                (classdict[line].rocnik == rocnik or rocnik == 'NULL') and \
                (classdict[line].semestr == semestr or semestr == 'NULL') and \
                (classdict[line].pocet_kreditu == pocet_kreditu or pocet_kreditu == 'NULL') and \
                (classdict[line].studentu_prednaska == studentu_prednaska or studentu_prednaska == 'NULL') and \
                (classdict[line].studentu_seminar == studentu_seminar or studentu_seminar == 'NULL') and \
                (classdict[line].studentu_cviceni == studentu_cviceni or studentu_cviceni == 'NULL') and \
                (classdict[line].vazba_zapocet == vazba_zapocet or vazba_zapocet == 'NULL') and \
                (classdict[line].vazba_klasifikovany_zapocet == vazba_klasifikovany_zapocet or v
                 azba_klasifikovany_zapocet == 'NULL') and \
                (classdict[line].vazba_zkouska == vazba_zkouska or vazba_zkouska == 'NULL'):
            newdict[line] = classdict[line]

    return newdict


def initial_values(data):
    data[1] = Predmet(1, 'AK8PO', 'Pokročilé programování ', 15, 0, 0, 14, 'český', 'kombinované', 1, 'LS', 3, 999, 
                      24, 21, 'seminář', '', 'přednáška')
    data[2] = Predmet(1, 'AK8MI', 'Matematická informatika ', 15, 0, 0, 14, 'český', 'kombinované', 1, 'LS', 3, 999, 
                      24, 21, '', 'přednáška', '')
    return data
