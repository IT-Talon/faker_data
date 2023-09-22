CREATE TABLE faker (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age INT,
    gender VARCHAR(10),  -- 性别字段，可以是字符串类型
    address TEXT          -- 地址字段，可以使用 TEXT 类型来存储较长的文本
);
