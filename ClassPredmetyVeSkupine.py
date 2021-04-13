from config import use_db
from SQLConnect import query


class PredmetyVeSkupine:
    def __init__(self, id_predmety_ve_skupine, cid_predmet, cid_studijni_skupina):
        self.id_predmety_ve_skupine = id_predmety_ve_skupine
        self.cid_predmet = cid_predmet
        self.cid_studijni_skupina = cid_studijni_skupina

    sloupce = ['id_predmety_ve_skupine', 'cid_predmet', 'cid_studijni_skupina']

    def update(self, id_predmety_ve_skupine='NULL', cid_predmet='NULL', cid_studijni_skupina='NULL'):
        condition = ''
        if id_predmety_ve_skupine != 'NULL':
            self.id_predmety_ve_skupine = id_predmety_ve_skupine
            condition += 'id_predmety_ve_skupine=' + "'" + str(id_predmety_ve_skupine) + "', " 
        if cid_predmet != 'NULL':
            self.cid_predmet = cid_predmet
            condition += 'cid_predmet=' + "'" + str(cid_predmet) + "', " 
        if cid_studijni_skupina != 'NULL':
            self.cid_studijni_skupina = cid_studijni_skupina
            condition += 'cid_studijni_skupina=' + "'" + str(cid_studijni_skupina) + "', " 
        if use_db == 1:
            condition = condition[:-2]
            sqltext = 'UPDATE PredmetyVeSkupine set %s where id_predmety_ve_skupine = %s ;' % (condition,
                                                                                               self.id_predmety_ve_skupine)
            query('UPDATE', sqltext)

    def select(self):
        return [self.id_predmety_ve_skupine, self.cid_predmet, self.cid_studijni_skupina]


def insert(classdict, id_predmety_ve_skupine, cid_predmet, cid_studijni_skupina):
    if use_db == 1:
        sqltext = """INSERT INTO PredmetyVeSkupine (id_predmety_ve_skupine, cid_predmet, 
                                                    cid_studijni_skupina) VALUES (""" 
        for var in [id_predmety_ve_skupine, cid_predmet, cid_studijni_skupina]:
            if var is not None and var != "":
                sqltext += "'" + str(var) + "', "
            else:
                sqltext += "''" + ', ' 
        sqltext = sqltext[:-2] + ");"
        query('INSERT', sqltext)
    new_id = len(classdict) + 1
    new_instance = PredmetyVeSkupine(id_predmety_ve_skupine, cid_predmet, cid_studijni_skupina)
    classdict[new_id] = new_instance
    return classdict


def podmineny_select(classdict, id_predmety_ve_skupine='NULL', cid_predmet='NULL', cid_studijni_skupina='NULL'):
    newdict = {}
    for line in classdict:
        if (classdict[line].id_predmety_ve_skupine == id_predmety_ve_skupine or id_predmety_ve_skupine == 'NULL') and \
                (classdict[line].cid_predmet == cid_predmet or cid_predmet == 'NULL') and \
                (classdict[line].cid_studijni_skupina == cid_studijni_skupina or cid_studijni_skupina == 'NULL'):
            newdict[line] = classdict[line]

    return newdict


def initial_values(data):
    data[1] = PredmetyVeSkupine(1, 1, 1)
    data[2] = PredmetyVeSkupine(2, 1, 2)
    return data
