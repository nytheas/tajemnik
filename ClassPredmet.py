from config import use_db
from SQLConnect import query


class Predmet:
    def __init__(self, id_predmet, zkratka, nazev, hodin_prednaska, hodin_seminar, hodin_cviceni, pocet_tydnu, jazyk, 
                 studium, rocnik, semestr, ukonceni, pocet_kreditu):
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
        self.ukonceni = ukonceni
        self.pocet_kreditu = pocet_kreditu

    sloupce = ['id_predmet', 'zkratka', 'nazev', 'hodin_prednaska', 'hodin_seminar', 'hodin_cviceni', 'pocet_tydnu', 
             'jazyk', 'studium', 'rocnik', 'semestr', 'ukonceni', 'pocet_kreditu']

    def update(self, id_predmet='NULL', zkratka='NULL', nazev='NULL', hodin_prednaska='NULL', hodin_seminar='NULL', 
               hodin_cviceni='NULL', pocet_tydnu='NULL', jazyk='NULL', studium='NULL', rocnik='NULL', semestr='NULL', 
               ukonceni='NULL', pocet_kreditu='NULL'):
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
        if ukonceni != 'NULL':
            self.ukonceni = ukonceni
            condition += 'ukonceni=' + "'" + str(ukonceni) + "', " 
        if pocet_kreditu != 'NULL':
            self.pocet_kreditu = pocet_kreditu
            condition += 'pocet_kreditu=' + "'" + str(pocet_kreditu) + "', " 
        if use_db == 1:
            condition = condition[:-2]
            sqltext = 'UPDATE Predmet set %s where id_predmet = %s ;' % (condition, self.id_predmet)
            query('UPDATE', sqltext)

    def select(self):
        return [self.id_predmet, self.zkratka, self.nazev, self.hodin_prednaska, self.hodin_seminar, 
                self.hodin_cviceni, self.pocet_tydnu, self.jazyk, self.studium, self.rocnik, self.semestr, 
                self.ukonceni, self.pocet_kreditu]


def insert(classdict, zkratka, nazev, hodin_prednaska, hodin_seminar, hodin_cviceni, pocet_tydnu, jazyk, studium, 
           rocnik, semestr, ukonceni, pocet_kreditu):
    if use_db == 1:
        sqltext = """INSERT INTO Predmet (zkratka, nazev, hodin_prednaska, hodin_seminar, hodin_cviceni, pocet_tydnu, 
                                          jazyk, studium, rocnik, semestr, ukonceni, pocet_kreditu) VALUES (""" 
        for var in [zkratka, nazev, hodin_prednaska, hodin_seminar, hodin_cviceni, pocet_tydnu, jazyk, studium, 
                    rocnik, semestr, ukonceni, pocet_kreditu]:
            if var is not None and var != "":
                sqltext += "'" + str(var) + "', "
            else:
                sqltext += "''" + ', ' 
        sqltext = sqltext[:-2] + ");"
        query('INSERT', sqltext)
    new_id = len(classdict) + 1
    new_instance = Predmet(new_id, zkratka, nazev, hodin_prednaska, hodin_seminar, hodin_cviceni, pocet_tydnu, jazyk, 
                           studium, rocnik, semestr, ukonceni, pocet_kreditu)
    classdict[new_id] = new_instance
    return classdict


def podmineny_select(classdict, id_predmet='NULL', zkratka='NULL', nazev='NULL', hodin_prednaska='NULL', 
                     hodin_seminar='NULL', hodin_cviceni='NULL', pocet_tydnu='NULL', jazyk='NULL', studium='NULL', 
                     rocnik='NULL', semestr='NULL', ukonceni='NULL', pocet_kreditu='NULL'):
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
                (classdict[line].ukonceni == ukonceni or ukonceni == 'NULL') and \
                (classdict[line].pocet_kreditu == pocet_kreditu or pocet_kreditu == 'NULL'):
            newdict[line] = classdict[line]

    return newdict


def initial_values(data):
    return data
