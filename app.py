# -*- coding: ISO-8859-2 -*-

from flask import Flask, request, redirect
from flask import render_template

from SQLConnect import sql
from config import use_db

import ClassPredmet
import ClassZamestnanec
import ClassPracovniStitek
import ClassStudijniSkupina

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


@app.route('/select/<string:table>')
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
        return render_template('sql_table.html', table=query, header=x)

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


@app.route('/select/')
def select_list():
    values = ['Predmet', 'Zamestnanec', 'StudijniSkupina', 'PracovniStitek']
    return render_template('select_list.html', values=values)


if __name__ == "__main__":
    app.run(debug=True)

