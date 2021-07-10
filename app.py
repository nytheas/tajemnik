# -*- coding: ISO-8859-2 -*-

from flask import Flask, request, redirect
from flask import render_template

from SQLConnect import sql
from config import use_db

import ClassPredmet
import ClassZamestnanec
import ClassPracovniStitek
import ClassStudijniSkupina
import procedures
import generuj_excel
import odeslat_mail

app = Flask(__name__)

predmet = {}
predmet = ClassPredmet.initial_values(predmet)
zamestnanec = {}
zamestnanec = ClassZamestnanec.initial_values(zamestnanec)
studijni_skupina = {}
studijni_skupina = ClassStudijniSkupina.initial_values(studijni_skupina)
pracovni_stitek = {}
pracovni_stitek = ClassPracovniStitek.initial_values(pracovni_stitek)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/data/')
@app.route('/data')
def list_of_tables():
    table_list = ['predmet', 'zamestnanec', 'studijniskupina', 'pracovnistitek', 'predmetyveskupine',
                  'zamestnanciupredmetu', 'pracovnibody']
    return render_template('select_list.html', values=table_list)


@app.route('/data/<string:table>')
def select_class(table):

    if use_db == 1:
        sql.execute('select * from %s order by 1;' % table)
        query = sql.fetchall()
        sql.execute("select column_name from information_schema.columns where table_name = '%s' order by "
                    "ordinal_position; " % table.lower())
        query2 = sql.fetchall()
        x = []
        for i in query2:
            x.append(i[0])
        return render_template('sql_table.html', table=query, header=x, tabname=table)

    if table == 'Predmet':
        if len(predmet) > 0:
            return render_template('table.html', table=predmet, header=predmet[1].sloupce)
    elif table == 'Zamestnanec':
        if len(zamestnanec) > 0:
            return render_template('table.html', table=zamestnanec, header=zamestnanec[1].sloupce)
    elif table == 'StudijniSkupina':
        if len(studijni_skupina) > 0:
            return render_template('table.html', table=studijni_skupina, header=studijni_skupina[1].sloupce)
    elif table == 'PracovniStitek':
        if len(pracovni_stitek) > 0:
            return render_template('table.html', table=pracovni_stitek, header=pracovni_stitek[1].sloupce)
    return render_template('table.html')


@app.route('/data/<string:table>/<int:idval>/<string:sqltype>', methods=['GET', 'POST'])
# @app.route('/<string:sqltype>/<string:table>/<int:idval>', methods=['GET', 'POST'])
def tmp(sqltype, table, idval):

    sql.execute("select column_name from information_schema.columns where table_name = '%s' order by "
                "ordinal_position; " % table.lower())
    query2 = sql.fetchall()
    sql.execute('select * from %s where %s = %s;' % (table, query2[0][0], idval))
    query = sql.fetchall()
    values = []
    if sqltype.lower() != 'insert':
        for i in query[0]:
            values.append(i)
    columns = []
    for i in query2:
        columns.append(i[0])
    sqltype = sqltype.upper()
    if request.method == 'GET':
        return render_template('generic_sql.html', itr=len(columns), columns=columns, values=values,
                               sqltype=sqltype, table=table, idval=idval)
    elif request.method == 'POST':
        procedures.generic_web_function(sqltype, request.form.to_dict(), table, idval, query2[0][0])
    return redirect('/data')


@app.route('/funkce/stitky_k_prirazeni', methods=['GET', 'POST'])
@app.route('/funkce/stitky_k_prirazeni/<string:filt>', methods=['GET', 'POST'])
def stitky_k_prirazeni(filt=''):
    sqlquery = """select id_pracovni_stitek, ps.nazev, ps.cid_zamestnanec || ' - ' || z.jmeno || ' ' || z.prijmeni as jmeno_zamestnance, p.nazev, typ, ps.jazyk, je_zapocet, je_klasifikovany_zapocet, je_zkouska, pracovni_body + pracovni_body_zapocet + pracovni_body_klasifikovany_zapocet + pracovni_body_zkouska as body_celkem from pracovnistitek ps
                LEFT JOIN predmet p on p.id_predmet = ps.cid_predmet
                LEFT JOIN zamestnanec z on z.id_zamestnanec = ps.cid_zamestnanec """
    if filt == "neprirazene":
        sqlquery += "where cid_zamestnanec is NULL"
    else:
        sqlquery += ""
    sqlquery += " order by id_pracovni_stitek;"

    sql.execute(sqlquery)
    data = sql.fetchall()
    hlavicka = ['ID', 'Název štítku', 'Zaměstnanec', 'Předmět', 'Typ', 'Jazyk', 'Zápočet', 'Klasifikovaný zápočet',
                'Zkouška', 'Body celkem']
    sql.execute("select id_zamestnanec || ' - ' || jmeno || ' ' || prijmeni from zamestnanec;")
    query = sql.fetchall()
    seznam_zamestnanci = ['', 'žádný']
    for i in query:
        seznam_zamestnanci.append(i[0])

    sqlquery2 = """select cid_zamestnanec, max(Z.jmeno || ' ' || Z.prijmeni) as jmeno, round(sum(pracovni_body + pracovni_body_zapocet + pracovni_body_klasifikovany_zapocet + pracovni_body_zkouska)) as pracovni_body  from pracovnistitek PS
                join zamestnanec Z on Z.id_zamestnanec = PS.cid_zamestnanec
                group by cid_zamestnanec;"""
    sql.execute(sqlquery2)
    prehled = sql.fetchall()
    prehled_hlavicka = ['ID', 'Jméno', 'Pracovní body']

    if request.method == 'GET':
        return render_template('seznam_zamestnanci.html', hlavicka=hlavicka, data=data, zamestnanci=seznam_zamestnanci,
                               prehled=prehled, prehled_hlavicka=prehled_hlavicka)
    elif request.method == 'POST':
        procedures.doplnit_zamestnance(request.form.to_dict())
    if filt == 'neprirazene':
        return redirect(f"/funkce/stitky_k_prirazeni/neprirazene")
    else:
        return redirect(f"/funkce/stitky_k_prirazeni")


@app.route('/funkce/predmety_ve_skupinach', methods=['GET', 'POST'])
def predmety_ve_skupinach():
    sql.execute(""" select * from predmety_ve_skupinach
                    UNION select 0,'--- Vložit','Nový záznam ---' from predmety_ve_skupinach
                    order by 1;""")
    data = sql.fetchall()
    hlavicka = ['ID', 'Předmět', 'Skupina']
    sql.execute("select id_predmet || ' - ' || zkratka || ' ' || nazev from predmet;")
    query = sql.fetchall()
    sql.execute("select id_studijni_skupina || ' - ' || zkratka || ' ' || nazev from studijniskupina;")
    query2 = sql.fetchall()
    seznam_predmety = ['', 'smazat']
    seznam_skupiny = ['', 'smazat']
    for i in query:
        seznam_predmety.append(i[0])
    for i in query2:
        seznam_skupiny.append(i[0])

    if request.method == 'GET':
        return render_template('predmety_ve_skupinach.html', hlavicka=hlavicka, data=data, predmet=seznam_predmety,
                               skupina=seznam_skupiny)
    elif request.method == 'POST':
        procedures.doplnit_predmety_ve_skupinach(request.form.to_dict())
    return redirect(f"/funkce/predmety_ve_skupinach")


@app.route('/funkce/vygenerujstitky')
def vygeneruj_stitky():
    procedures.vytvorit_stitky()
    return redirect(f"/funkce/nevyresenestitky")


@app.route('/funkce/nevyresenestitky')
def nevyresene_stitky():
    header = ['Id předmět', 'Typ štítku', 'Hodin', 'Studentů ve třídě', 'Očekávané třídy', 'Celkem studentů', 'Tříd na štítcích', 'Studentů na štítcích', 'Rozvrhovaný počet studentů']
    sql.execute("""select * from stitky_ke_zpracovani;""")
    table = sql.fetchall()
    return render_template('nevyresenestitky.html', header=header, table=table)

#
# @app.route('/funkce/vygenerujpracovnilisty')
# def vygeneruj_pracovni_listy():
#     sql.execute("select id_zamestnanec from zamestnanec;")
#     zamestnanci = sql.fetchall()
#     for zam in zamestnanci:
#         generuj_excel.vygenerovat_uvazky(zam[0])
#     return render_template('index.html')
#
#
# @app.route('/funkce/odeslimail')
# def odesli_prilohy_mailem():
#     sql.execute("select id_zamestnanec from zamestnanec;")
#     zamestnanci = sql.fetchall()
#     odeslat_mail.odeslat_mail()
#     return render_template('index.html')


@app.route('/funkce/pracovnilisty', methods=['GET', 'POST'])
def pracovnilisty():
    sql.execute("""select id_zamestnanec, jmeno || ' ' || prijmeni from zamestnanec;""")
    tabulka = sql.fetchall()
    hlavicka = ['Id zaměstnance', 'Jméno', 'Zpracovat']

    if request.method == 'GET':
        return render_template('odeslani_stitku.html', hlavicka=hlavicka, tabulka=tabulka)

    if request.method == 'POST':
        print(request.form.to_dict())
        procedures.generuj_a_odesli_excel(request.form.to_dict())
        return render_template('odeslani_stitku.html', hlavicka=hlavicka, tabulka=tabulka)


@app.route('/funkce/generujcsv')
def generujcsv():
    sql.execute("""select PS.*, Z.jmeno || ' ' || Z.prijmeni as jmeno, P.zkratka as zkratka, P.nazev as predmet from pracovnistitek PS
    left join zamestnanec Z on Z.id_zamestnanec = PS.cid_zamestnanec
    left join predmet P on P.id_predmet = PS.cid_predmet
    order by id_pracovni_stitek;""")
    data = sql.fetchall()
    text = procedures.generuj_csv(data)
    return render_template('csv.html', text=text)


if __name__ == "__main__":
    app.run(debug=True)

