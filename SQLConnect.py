from datetime import datetime
import psycopg2

conn = psycopg2.connect(database="PO", user="postgres", password="admin", host="127.0.0.1", port="5432")
sql = conn.cursor()


def query(typ, dotaz):
    file = open("log.txt", "a")
    cont = False
    while cont is False:
        ld = len(dotaz)
        dotaz = dotaz.replace("\n", "").replace("  ", " ")
        ld2 = len(dotaz)
        if ld == ld2:
            cont = True

    file.write(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " | " + dotaz.replace("\n", "") + "\n")
    file.close()
    sql.execute(dotaz)

    if typ == 'SELECT':
        return sql.fetchall()
    elif typ == 'SELECT1':
        vysl = sql.fetchall()
        return vysl[0][0]
    elif typ == 'INSERT':
        sql.execute("commit;")
    elif typ == 'UPDATE':
        sql.execute("commit;")


