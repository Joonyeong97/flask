
def sql_():
    import pymysql
    conn = pymysql.connect(host='13.124.226.221',
                           user='ljkk1542', port=8056, password='maroon3169!@', db='tell119',
                           charset='utf8mb4', use_unicode=True,
                           cursorclass=pymysql.cursors.DictCursor)
    return conn

def inquire(name, email, text, ip):
    import time
    import pymysql
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    conn = sql_()

    cur = conn.cursor()
    sql ="""INSERT INTO inquire (name, email, text, IP_address, mmdd)
        VALUES(%s, %s, %s, %s, %s)"""


    cur.execute(sql, ('%s'%(name), '%s'%(email),'%s'%(text), '%s'%(ip), '%s'%(date)))


    conn.commit()