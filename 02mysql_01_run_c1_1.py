import pymysql
connectiont = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    db='test',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor# 游标类型
)

cursor = connectiont.cursor()

sql = """
create table user_table(
)
"""

cursor.execute(sql)
cursor.close()
connectiont.close()
