import psycopg2
from faker import Faker
import random

# 连接到 PostgreSQL 数据库
conn = psycopg2.connect(
    dbname="faker",
    user="postgres",
    password="llyzmz",
    host="localhost"
)

# 创建一个游标对象
cur = conn.cursor()

# 创建 Faker 实例
fake = Faker(locale='zh_CN')

# 插入 1000 万条测试数据
for _ in range(10000000):
    # 生成随机数据
    name = fake.name()
    email = fake.email()
    address = fake.address()
    gender = random.choice(['Male', 'Female'])
    age = random.randint(18, 65)

    # 构建 SQL 插入语句
    sql = "INSERT INTO faker (name, email, age,gender,address) VALUES (%s, %s,%s, %s,%s)"
    data = (name, email, age,gender,address)

    # 执行 SQL 插入
    cur.execute(sql, data)

# 提交更改并关闭连接
conn.commit()
conn.close()
