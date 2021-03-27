from config import use_db
from SQLConnect import query


class StudijniSkupina:
    def __init__(self, id_studijni_skupina, zkratka, nazev, studium, rocnik, semestr, pocet_studentu):
        self.id_studijni_skupina = id_studijni_skupina
        self.zkratka = zkratka
        self.nazev = nazev
        self.studium = studium
        self.rocnik = rocnik
        self.semestr = semestr
        self.pocet_studentu = pocet_studentu

    sloupce = ['id_studijni_skupina', 'zkratka', 'nazev', 'studium', 'rocnik', 'semestr', 'pocet_studentu']

    def update(self, id_studijni_skupina='NULL', zkratka='NULL', nazev='NULL', studium='NULL', rocnik='NULL', 
               semestr='NULL', pocet_studentu='NULL'):
        condition = ''
        if id_studijni_skupina != 'NULL':
            self.id_studijni_skupina = id_studijni_skupina
            condition += 'id_studijni_skupina=' + "'" + str(id_studijni_skupina) + "', " 
        if zkratka != 'NULL':
            self.zkratka = zkratka
            condition += 'zkratka=' + "'" + str(zkratka) + "', " 
        if nazev != 'NULL':
            self.nazev = nazev
            condition += 'nazev=' + "'" + str(nazev) + "', " 
        if studium != 'NULL':
            self.studium = studium
            condition += 'studium=' + "'" + str(studium) + "', " 
        if rocnik != 'NULL':
            self.rocnik = rocnik
            condition += 'rocnik=' + "'" + str(rocnik) + "', " 
        if semestr != 'NULL':
            self.semestr = semestr
            condition += 'semestr=' + "'" + str(semestr) + "', " 
        if pocet_studentu != 'NULL':
            self.pocet_studentu = pocet_studentu
            condition += 'pocet_studentu=' + "'" + str(pocet_studentu) + "', " 
        if use_db == 1:
            condition = condition[:-2]
            sqltext = 'UPDATE StudijniSkupina set %s where id_studijni_skupina = %s ;' % (condition, 
                                                                                          self.id_studijni_skupina)
            query('UPDATE', sqltext)

    def select(self):
        return [self.id_studijni_skupina, self.zkratka, self.nazev, self.studium, self.rocnik, self.semestr, 
                self.pocet_studentu]


def insert(classdict, zkratka, nazev, studium, rocnik, semestr, pocet_studentu):
    if use_db == 1:
        sqltext = """INSERT INTO StudijniSkupina (zkratka, nazev, studium, rocnik, semestr, 
                                                  pocet_studentu) VALUES (""" 
        for var in [zkratka, nazev, studium, rocnik, semestr, pocet_studentu]:
            if var is not None and var != "":
                sqltext += "'" + str(var) + "', "
            else:
                sqltext += "''" + ', ' 
        sqltext = sqltext[:-2] + ");"
        query('INSERT', sqltext)
    new_id = len(classdict) + 1
    new_instance = StudijniSkupina(new_id, zkratka, nazev, studium, rocnik, semestr, pocet_studentu)
    classdict[new_id] = new_instance
    return classdict


def podmineny_select(classdict, id_studijni_skupina='NULL', zkratka='NULL', nazev='NULL', studium='NULL', 
                     rocnik='NULL', semestr='NULL', pocet_studentu='NULL'):
    newdict = {}
    for line in classdict:
        if (classdict[line].id_studijni_skupina == id_studijni_skupina or id_studijni_skupina == 'NULL') and \
                (classdict[line].zkratka == zkratka or zkratka == 'NULL') and \
                (classdict[line].nazev == nazev or nazev == 'NULL') and \
                (classdict[line].studium == studium or studium == 'NULL') and \
                (classdict[line].rocnik == rocnik or rocnik == 'NULL') and \
                (classdict[line].semestr == semestr or semestr == 'NULL') and \
                (classdict[line].pocet_studentu == pocet_studentu or pocet_studentu == 'NULL'):
            newdict[line] = classdict[line]

    return newdict


def initial_values(data):
    data[1] = StudijniSkupina(1, 'K4KYB ', 'Kybernetická bezpečnost', 'kombinované', 1, 'LS', 20)
    return data
