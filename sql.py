
def sql_():
    import pymysql
    conn = pymysql.connect(host='13.124.226.221',
                           user='ljkk1542', port=8056, password='maroon3169!@', db='tell119',
                           charset='utf8mb4', use_unicode=True,
                           cursorclass=pymysql.cursors.DictCursor)
    return conn

def inquire(name, email, text, ip):
    import datetime
    import pymysql
    current = datetime.datetime.now()
    nine_hour_later = current + datetime.timedelta(hours=9)
    date = nine_hour_later.strftime("%Y-%m-%d %H:%M:%S")
    conn = sql_()

    cur = conn.cursor()
    sql ="""INSERT INTO inquire (name, email, text, IP, mmdd)
        VALUES(%s, %s, %s, %s, %s)"""
    cur.execute(sql, ('%s'%(name), '%s'%(email),'%s'%(text), '%s'%(ip), '%s'%(date)))
    conn.commit()
    conn.close()

def connection_ip(ip):
    import datetime
    import pymysql
    current = datetime.datetime.now()
    nine_hour_later = current + datetime.timedelta(hours=9)
    date = nine_hour_later.strftime("%Y-%m-%d")
    yydd = nine_hour_later.strftime("%H:%M:%S")
    conn = sql_()

    cur = conn.cursor()
    sql ="""INSERT INTO Connection_ip (IP,date,yydd)
        VALUES(%s, %s, %s)"""
    cur.execute(sql, ('%s'%(ip), '%s'%(date), '%s'%(yydd)))
    conn.commit()
    conn.close()

def today():
    import datetime
    import pymysql
    current = datetime.datetime.now()
    nine_hour_later = current + datetime.timedelta(hours=9)
    date = nine_hour_later.strftime("%Y-%m-%d")
    conn = sql_()
    cur = conn.cursor()
    sql ="""SELECT COUNT(*) FROM Connection_ip WHERE DATE = (%s)"""
    cur.execute(sql, ('%s'%(date)))
    row = cur.fetchall()
    for pet in row:
        pet_val = list(pet.values())
    today = pet_val[0]
    conn.close()
    return today

def total():
    conn = sql_()
    cur = conn.cursor()
    sql ="""SELECT COUNT(*) FROM Connection_ip"""
    cur.execute(sql)
    row = cur.fetchall()
    for pet in row:
        pet_val = list(pet.values())
    total = pet_val[0]
    conn.close()
    return total