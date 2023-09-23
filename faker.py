import psycopg2
from faker import Faker
from psycopg2.extras import execute_values
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


# 生成测试数据
data = [(fake.name(), random.randint(18, 65), fake.phone_number(),
         fake.email(), fake.address(), random.choice(['Male', 'Female'])) for _ in range(10000000)]

# 定义插入数据的SQL语句
insert_query = "INSERT INTO faker (name, age, phone_number,email,address,gender) VALUES %s"

# 执行批量插入
execute_values(cur, insert_query, data)


# 提交更改并关闭连接
conn.commit()
cur.close()
conn.close()
