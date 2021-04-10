import SQLConnect


def generic_web_function(sqltype, valdict, table, idval, idname):
    if sqltype == 'INSERT':
        sqlquery = 'INSERT INTO ' + table + '('
        for i in valdict:
            if i[:2] != 'id':
                sqlquery += i + ', '
        sqlquery = sqlquery[:-2]
        sqlquery += ") VALUES ("
        for i in valdict:
            if i[:2] != 'id':
                sqlquery += "'" + valdict[i] + "', "
        sqlquery = sqlquery[:-2]
        sqlquery += ");"
        SQLConnect.query('INSERT', sqlquery)
    elif sqltype == 'UPDATE':
        sqlquery = 'UPDATE ' + table + ' SET '
        for i in valdict:
            if valdict[i] != "<same>":
                sqlquery += i + " = '" + valdict[i] + "', "
        sqlquery = sqlquery[:-2] + " where " + idname + " = " + str(idval) + ";"
        SQLConnect.query('UPDATE', sqlquery)
    elif sqltype == 'DELETE':
        sqlquery = 'DELETE FROM ' + table + " where " + idname + " = " + str(idval) + ";"
        SQLConnect.query('DELETE', sqlquery)


def count_class_sizes(all_students, class_capacity):
    class_students = []
    class_num = round((all_students / class_capacity)+0.5)
    print(class_num)
    students_in_class = int(all_students / class_num)
    reminder = all_students - (students_in_class * class_num)
    rem_tmp = 1
    for i in range(class_num):
        if rem_tmp <= reminder:
            class_students.append(students_in_class + 1)
        else:
            class_students.append(students_in_class)
        rem_tmp += 1
    return class_students


print(count_class_sizes(105, 27))
