from config import use_db
from SQLConnect import query


class Zamestnanec:
    def __init__(self, id_zamestnanec, jmeno, prijmeni, mobilni_telefon, telefon_pracovni, email_pracovni, 
                 email_nahradni, je_doktorand, uvazek, pracovni_body, pracovni_body_anglictina):
        self.id_zamestnanec = id_zamestnanec
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.mobilni_telefon = mobilni_telefon
        self.telefon_pracovni = telefon_pracovni
        self.email_pracovni = email_pracovni
        self.email_nahradni = email_nahradni
        self.je_doktorand = je_doktorand
        self.uvazek = uvazek
        self.pracovni_body = pracovni_body
        self.pracovni_body_anglictina = pracovni_body_anglictina

    sloupce = ['id_zamestnanec', 'jmeno', 'prijmeni', 'mobilni_telefon', 'telefon_pracovni', 'email_pracovni', 
             'email_nahradni', 'je_doktorand', 'uvazek', 'pracovni_body', 'pracovni_body_anglictina']

    def update(self, id_zamestnanec='NULL', jmeno='NULL', prijmeni='NULL', mobilni_telefon='NULL', 
               telefon_pracovni='NULL', email_pracovni='NULL', email_nahradni='NULL', je_doktorand='NULL', 
               uvazek='NULL', pracovni_body='NULL', pracovni_body_anglictina='NULL'):
        condition = ''
        if id_zamestnanec != 'NULL':
            self.id_zamestnanec = id_zamestnanec
            condition += 'id_zamestnanec=' + "'" + str(id_zamestnanec) + "', " 
        if jmeno != 'NULL':
            self.jmeno = jmeno
            condition += 'jmeno=' + "'" + str(jmeno) + "', " 
        if prijmeni != 'NULL':
            self.prijmeni = prijmeni
            condition += 'prijmeni=' + "'" + str(prijmeni) + "', " 
        if mobilni_telefon != 'NULL':
            self.mobilni_telefon = mobilni_telefon
            condition += 'mobilni_telefon=' + "'" + str(mobilni_telefon) + "', " 
        if telefon_pracovni != 'NULL':
            self.telefon_pracovni = telefon_pracovni
            condition += 'telefon_pracovni=' + "'" + str(telefon_pracovni) + "', " 
        if email_pracovni != 'NULL':
            self.email_pracovni = email_pracovni
            condition += 'email_pracovni=' + "'" + str(email_pracovni) + "', " 
        if email_nahradni != 'NULL':
            self.email_nahradni = email_nahradni
            condition += 'email_nahradni=' + "'" + str(email_nahradni) + "', " 
        if je_doktorand != 'NULL':
            self.je_doktorand = je_doktorand
            condition += 'je_doktorand=' + "'" + str(je_doktorand) + "', " 
        if uvazek != 'NULL':
            self.uvazek = uvazek
            condition += 'uvazek=' + "'" + str(uvazek) + "', " 
        if pracovni_body != 'NULL':
            self.pracovni_body = pracovni_body
            condition += 'pracovni_body=' + "'" + str(pracovni_body) + "', " 
        if pracovni_body_anglictina != 'NULL':
            self.pracovni_body_anglictina = pracovni_body_anglictina
            condition += 'pracovni_body_anglictina=' + "'" + str(pracovni_body_anglictina) + "', " 
        if use_db == 1:
            condition = condition[:-2]
            sqltext = 'UPDATE Zamestnanec set %s where id_zamestnanec = %s ;' % (condition, self.id_zamestnanec)
            query('UPDATE', sqltext)

    def select(self):
        return [self.id_zamestnanec, self.jmeno, self.prijmeni, self.mobilni_telefon, self.telefon_pracovni, 
                self.email_pracovni, self.email_nahradni, self.je_doktorand, self.uvazek, self.pracovni_body, 
                self.pracovni_body_anglictina]


def insert(classdict, jmeno, prijmeni, mobilni_telefon, telefon_pracovni, email_pracovni, email_nahradni, 
           je_doktorand, uvazek, pracovni_body, pracovni_body_anglictina):
    if use_db == 1:
        sqltext = """INSERT INTO Zamestnanec (jmeno, prijmeni, mobilni_telefon, telefon_pracovni, email_pracovni, 
                                              email_nahradni, je_doktorand, uvazek, pracovni_body, 
                                              pracovni_body_anglictina) VALUES (""" 
        for var in [jmeno, prijmeni, mobilni_telefon, telefon_pracovni, email_pracovni, email_nahradni, je_doktorand, 
                    uvazek, pracovni_body, pracovni_body_anglictina]:
            if var is not None and var != "":
                sqltext += "'" + str(var) + "', "
            else:
                sqltext += "''" + ', ' 
        sqltext = sqltext[:-2] + ");"
        query('INSERT', sqltext)
    new_id = len(classdict) + 1
    new_instance = Zamestnanec(new_id, jmeno, prijmeni, mobilni_telefon, telefon_pracovni, email_pracovni, 
                               email_nahradni, je_doktorand, uvazek, pracovni_body, pracovni_body_anglictina)
    classdict[new_id] = new_instance
    return classdict


def podmineny_select(classdict, id_zamestnanec='NULL', jmeno='NULL', prijmeni='NULL', mobilni_telefon='NULL', 
                     telefon_pracovni='NULL', email_pracovni='NULL', email_nahradni='NULL', je_doktorand='NULL', 
                     uvazek='NULL', pracovni_body='NULL', pracovni_body_anglictina='NULL'):
    newdict = {}
    for line in classdict:
        if (classdict[line].id_zamestnanec == id_zamestnanec or id_zamestnanec == 'NULL') and \
                (classdict[line].jmeno == jmeno or jmeno == 'NULL') and \
                (classdict[line].prijmeni == prijmeni or prijmeni == 'NULL') and \
                (classdict[line].mobilni_telefon == mobilni_telefon or mobilni_telefon == 'NULL') and \
                (classdict[line].telefon_pracovni == telefon_pracovni or telefon_pracovni == 'NULL') and \
                (classdict[line].email_pracovni == email_pracovni or email_pracovni == 'NULL') and \
                (classdict[line].email_nahradni == email_nahradni or email_nahradni == 'NULL') and \
                (classdict[line].je_doktorand == je_doktorand or je_doktorand == 'NULL') and \
                (classdict[line].uvazek == uvazek or uvazek == 'NULL') and \
                (classdict[line].pracovni_body == pracovni_body or pracovni_body == 'NULL') and \
                (classdict[line].pracovni_body_anglictina == pracovni_body_anglictina or pracovni_body_anglictina ==
                 'NULL'):
            newdict[line] = classdict[line]

    return newdict


def initial_values(data):
    data[1] = Zamestnanec(1, 'Pavel', 'Vařacha', '605605605', '777777777', 'varacha@utb.cz', 'varacha@neutb.cz', 
                          False, 1, 0, 0)
    return data
