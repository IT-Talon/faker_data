import psycopg2
from faker import Faker
from psycopg2.extras import execute_batch
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

data = []
# 插入 1000 万条测试数据
for _ in range(10000000):
    row = (fake.name(), random.randint(18, 65), fake.phone_number(),
           fake.email(), fake.address(), random.choice(['Male', 'Female']))
    data.append(row)


query = "INSERT INTO faker (name, age, phone_number,email,address,gender) VALUES (%s,%s,%s,%s, %s, %s)"
execute_batch(cur, query, data)


# 提交更改并关闭连接
conn.commit()
cur.close()
conn.close()
