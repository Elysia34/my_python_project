import pymysql
connectiont = pymysql.connect(
    host = 'localhost', # 主机名
    user = 'root',      # 数据库用户名
    password = '123456',  # 数据库密码
    db = 'hello_database',      # 数据库名
    charset = 'utf8',   # 字符集编码
    cursorclass = pymysql.cursors.DictCursor # 游标类型
)

cursor = connectiont.cursor() # 获取游标对象
sql = """
insert into books(name, category, price, publish_time) values ("零基础学Python",'Python','79.80','2018-5-20'); 
"""
print(sql)


cursor.execute(sql) # 执行SQL语句

connectiont.commit()

cursor.close()      # 关闭游标
connectiont.close() # 关闭连接