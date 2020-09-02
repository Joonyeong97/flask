
def sql_():
    import pymysql
    conn = pymysql.connect(host='13.124.226.221',
                           user='ljkk1542', port=8056, password='maroon3169!@', db='tell119',
                           charset='utf8mb4', use_unicode=True,
                           cursorclass=pymysql.cursors.DictCursor)
    return conn


def word_dictionary():
    conn = sql_()
    cur = conn.cursor()
    sql = """select word from word_dictionary"""
    cur.execute(sql)
    row = cur.fetchall()
    # data = pd.DataFrame(row[0])
    pet_val = []
    for pet in row:
        # print(list(pet.values()))
        pet_val.append(list(pet.values())[0])

    conn.close()
    return pet_val

def word_input(word):
    conn = sql_()
    cur = conn.cursor()
    sql = """insert into word_dictionary(word) values(%s)"""
    cur.execute(sql, ('%s'%(word)))
    conn.commit()
    conn.close()

def twi1(date,search_n):
    conn = sql_()
    cur = conn.cursor()
    date = int(date)
    sql ="""INSERT INTO Twitter_info (dates,search_n) VALUES(%s, %s)"""
    cur.execute(sql, ('%s'%(date), '%s'%(search_n)))
    conn.commit()
    conn.close()

def twi2(date):
    conn = sql_()
    cur = conn.cursor()
    sql ="""SELECT search_n FROM Twitter_info WHERE dates = (%s)"""
    cur.execute(sql, ('%s'%(date)))
    row = cur.fetchall()
    for pet in row:
        pet_val = list(pet.values())
    search_n = pet_val[0]
    conn.close()
    return search_n

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

def admin(PASS,date1):
    try:
        if len(str(date1)) != 8:
            ip = 'X'
            date = 'X'
            wi = 1
            return ip, date, wi
        if len(str(date1)) == 0:
            conn = sql_()
            cur = conn.cursor()
            sql = """SELECT * FROM Connection_ip"""
            cur.execute(sql)
            row = cur.fetchall()
            real = []
            for pet in row:
                pet_val = list(pet.values())
                real.append(pet_val)
            ip = []
            date = []
            for i, q in enumerate(real):
                ip.append(q[0])
                date.append(q[1].strftime('%Y%m%d'))
            wi = len(ip)
            conn.close()
            return ip, date , wi
        date = int(date1)
        conn = sql_()
        cur = conn.cursor()
        sql = """SELECT * FROM Connection_ip where date >= (%s)"""
        cur.execute(sql, '%s' % (date))
        row = cur.fetchall()
        real = []
        for pet in row:
            pet_val = list(pet.values())
            real.append(pet_val)
        ip = []
        date = []
        for i, q in enumerate(real):
            ip.append(q[0])
            date.append(q[1].strftime('%Y%m%d'))
        wi = len(ip)
        conn.close()
        return ip, date, wi
    except:
        ip = 'X'
        date = 'X'
        wi = 1
        return ip, date, wi