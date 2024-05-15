import pymysql
connectiont = pymysql.connect(
    host = 'localhost', # 主机名
    user = 'root',      # 数据库用户名
    password = '123456',  # 数据库密码
    db = 'hello_database',      # 数据库名
    charset = 'utf8',   # 字符集编码
    cursorclass = pymysql.cursors.DictCursor # 游标类型
)# 数据列表
data = [("零基础学Python",'Python','79.80','2018-5-20'),
        ("Python从入门到精通",'Python','69.80','2018-6-18'),
        ("零基础学PHP",'PHP','69.80','2017-5-21'),
        ("PHP项目开发实战入门",'PHP','79.80','2016-5-21'),
        ("零基础学Java",'Java','69.80','2017-5-21'),
        ]
cursor = connectiont.cursor() # 获取游标对象
try:
    # 执行sql语句，插入多条数据
    cursor.executemany("insert into books(name, category, price, publish_time) values (%s,%s,%s,%s)", data)
    # 提交数据
    connectiont.commit()
except:
    # 发生错误时回滚
    connectiont.rollback()
connectiont.commit()
cursor.close()      # 关闭游标
connectiont.close() # 关闭连接