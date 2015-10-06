def query(acno):
    cur = connection.cursor()
    data = {}
    sql = "select Gender,Count(*) from Constituency Natural Join Polling Natural Join Voter where Acno='"+acno+"' Group By Gender;"
    cur.execute(sql)
    x = cur.fetchall()
    for y in x:
        if y[0]=='female':
            data['female'] = y[1]
        else:
            data['male'] = y[1]

    sql = "select Caste,Count(*) from Constituency Natural Join Polling Natural Join Voter where Acno='"+acno+"' Group By Caste;"
    cur.execute(sql)
    x = cur.fetchall()
    data['obc'] = 0
    data['sc'] = 0
    data['st'] = 0
    data['gen'] = 0
    for y in x:
        if y[0]=='OBC':
            data['obc'] = y[1]
        elif y[0]=='SC':
            data['sc'] = y[1]
        elif y[0]=='ST':
            data['st'] = y[1]
        else:
            data['gen'] = y[1]

    sql = "select Count(*) from Constituency Natural Join Polling Natural Join Voter where Acno='"+acno+"'"
    cur.execute(sql)
    data['population']=cur.fetchone()[0]
    print data
    return data