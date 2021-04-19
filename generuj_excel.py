import openpyxl
import SQLConnect


def vygenerovat_uvazky(id_zamestnanec):
    sqlquery = "SELECT * from prehled_vyuky_do_excelu WHERE cid_zamestnanec = %s" % id_zamestnanec
    radky = SQLConnect.query("SELECT", sqlquery)
    sqlquery = "SELECT * from prehled_zkousek_do_excelu WHERE cid_zamestnanec = %s" % id_zamestnanec
    zkousky = SQLConnect.query("SELECT", sqlquery)
    sqlquery = "SELECT jmeno || ' ' || prijmeni from zamestnanec WHERE id_zamestnanec = %s" % id_zamestnanec
    zam = SQLConnect.query("SELECT1", sqlquery)
    if len(radky) > 10 or len(zkousky) > 8:
        print("Příliš mnoho řádků!")
        return 0
    mywb = openpyxl.load_workbook('static\\uvazky_template.xlsx')
    s = mywb.active
    s['B3'] = zam
    rid = 11
    for r in radky:
        row = str(rid)
        s['A'+row] = r[1]
        if r[2] == 'LS':
            s['C'+row] = r[3]
        else:
            s['D'+row] = r[3]
        if r[4] > 0:
            s['E'+row] = r[4]
        if r[5] > 0:
            s['F' + row] = r[5]
        if r[6] > 0:
            s['G' + row] = r[6]
        if r[7] > 0:
            s['I'+row] = r[7]
        if r[8] > 0:
            s['J' + row] = r[8]
        if r[9] > 0:
            s['K' + row] = r[9]
        rid += 1

    rid = 25
    for r in zkousky:
        row = str(rid)
        s['A' + row] = r[1]
        if r[2] > 0:
            s['B' + row] = r[2]
        if r[3] > 0:
            s['C' + row] = r[3]
        if r[4] > 0:
            s['D' + row] = r[4]

        rid += 1

    mywb.save('uvazky\\úvazek ' + zam + ".xlsx")
    mywb.close()
