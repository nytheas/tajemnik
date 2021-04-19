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
        sql.execute('select * from %s;' % table)
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
    return render_template('index.html')


@app.route('/funkce/vygenerujstitky')
def vygeneruj_stitky():
    procedures.vytvorit_stitky()
    return render_template('index.html')


@app.route('/funkce/vygenerujpracovnilisty')
def vygeneruj_pracovni_listy():
    sql.execute("select id_zamestnanec from zamestnanec;")
    zamestnanci = sql.fetchall()
    for zam in zamestnanci:
        generuj_excel.vygenerovat_uvazky(zam[0])
    return render_template('index.html')


@app.route('/funkce/odeslimail')
def odesli_prilohy_mailem():
    sql.execute("select id_zamestnanec from zamestnanec;")
    zamestnanci = sql.fetchall()
    odeslat_mail.odeslat_mail()
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

