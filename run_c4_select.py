import pymysql
connectiont = pymysql.connect(
    host = 'localhost', # 主机名
    user = 'root',      # 数据库用户名
    password = '',  # 数据库密码
    db = 'hello_database',      # 数据库名
    charset = 'utf8',   # 字符集编码
    cursorclass = pymysql.cursors.DictCursor # 游标类型
)

cursor = connectiont.cursor() # 获取游标对象

# sql = """
#  select * from books;
# """
sql = """
 select * from books order by price;
"""
cursor.execute(sql) # 执行SQL语句


# data = cursor.fetchone()
# print(data)

# print(data)
data = cursor.fetchall()
num = 0
for book in data:
    num = num + 1
    print("第" + str(num) + "条")
    print(book)


cursor.close()      # 关闭游标
connectiont.close() # 关闭连接