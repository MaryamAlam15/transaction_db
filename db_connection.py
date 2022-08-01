
import pandas as pd

# only for SQLite. Uncomment if using any other DB.
import sqlite3

cnx = sqlite3.connect('data/transactions.db')

# uncomment to use Postgres DB.
# import psycopg2
# cnx = psycopg2.connect(
#     host="localhost",
#     database="transactions",
#     user="<db username>",
#     password="<db password>")


def get_transactions_df():
    return pd.read_sql_query("""
        select *
        from Transactions
        ;
    """, cnx)


def get_devices_df():
    return pd.read_sql_query("""
        select * from Devices;
    """, cnx)