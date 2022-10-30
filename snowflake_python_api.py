import snowflake.connector
from product_categorisation import *
from sqlalchemy import create_engine
from snowflake.connector.pandas_tools import pd_writer
from snowflake.sqlalchemy import URL

# connect to snowflake using credentials
ctx1 = snowflake.connector.connect(
    user='JOSEPH',
    password='6AZLiMZXhejPufk@!vwxfaBhaeR6Y7',
    account='az91838.eu-west-1',
    role = 'PYTHON'
    )

# create cursor
cursor = ctx1.cursor()
# extract all the product names from ORDERPAY.DOMAIN.ORDER_ITEM
cursor.execute('SELECT PRODUCT_NAME FROM ORDERPAY.DOMAIN.ORDER_ITEM')
# clean the data and add them to a list
product_names = [i[0] for i in cursor.fetchall() if i[0] != None]

# create PRODUCT_CATEGORY_PYTHON table in ORDERPAY -> LOOKUP
sql = "USE DATABASE ORDERPAY"
cursor.execute(sql)

sql = "USE SCHEMA LOOKUP"
cursor.execute(sql)

sql = "CREATE TABLE IF NOT EXISTS PRODUCT_CATEGORY_PYTHON (CATEGORY_1 TEXT, CATEGORY_2 TEXT, CATEGORY_3 TEXT)"
cursor.execute(sql)

# close cursor and connection
cursor.close()
ctx1.close()

# use ML models to predict categories of retrieved data and format them into a df
final_df = generate_categories(product_names)

# connect to snowflake using sqlalchemy and define credentials of the table location
engine = create_engine(URL(
    user='JOSEPH',
    password='6AZLiMZXhejPufk@!vwxfaBhaeR6Y7',
    account='az91838.eu-west-1',
    database = 'ORDERPAY',
    schema = 'LOOKUP',
    role = 'PYTHON'
    )).connect()

# feed the table with the dataframe created
with engine as con:
    final_df.to_sql(name='product_category_python', con=con, if_exists='replace', method=pd_writer, index = False)

