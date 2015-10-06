def con_query(acno):
    acno = 'WBAC000229'
    cur = connection.cursor()
    data = {}
    sql = "select Gender,Count(*) from Constituency Natural Join Polling Natural Join Voter where Acno='"+acno+"' Group By Gender"
    cur.execute(sql)
    x = cur.fetchall()
    print x
    for y in x:
        if y[0]=='female':
            data['female'] = y[1]
        else:
            data['male'] = y[1]

    sql = "select Caste,Count(*) from Constituency Natural Join Polling Natural Join Voter where Acno='"+acno+"' Group By Caste"
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

def next_query():
    sql = 'select year,FemaleVotes,MaleVotes,STVotes,SCVotes,OBCVotes,GENVotes,PartyName from Party natural join Election_Statistics natural join Election'
    cur = connection.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    print res
    data =[]
    for x in res:
        dict1 = {}
        dict1['femalevotes']=x[1]
        dict1['malevotes']=x[2]
        dict1['stvotes']=x[3]
        dict1['scvotes']=x[4]
        dict1['obcvotes']=x[5]
        dict1['genvotes']=x[6]
        dict1['partyname']=x[7]
        dict1['year']=x[0]
        data.append(dict1)



def global_election_query(year):
    year = 2004
    sql = "select Partyid,FemaleVotes+MaleVotes as votes from Election_Statistics Natural Join Election where year = "+str(year)+""
    cur = connection.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    print res
    data ={}
    data['year']=year


    dict1 = {}
    for x in res:
        dict1[str(x[0])]=x[1]

    data['data']=dict1

