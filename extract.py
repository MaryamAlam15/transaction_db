import xml.etree.ElementTree as ET

import pandas as pd

from db_connection import cnx


def extract_db_data():
    """
    method to get data from DB.
    """
    transactions_df = _get_transactions_df()
    devices_df = _get_devices_df()
    return transactions_df, devices_df


def get_exchange_rates(currency='USD'):
    """
    takes `currency` as param and reads the exchange rates for EUR.
    returns respective exchange rates as df.
    """
    etree = ET.parse('data/currency_exchange_rate.xml')
    root = etree.getroot()
    namespaces = {'ex': 'http://www.ecb.int/vocabulary/2002-08-01/eurofxref'}
    exchange_rate_dict = {}
    date_list = []
    rate_list = []
    for dt in root.findall('.//ex:Cube[@time]', namespaces=namespaces):
        date = dt.attrib['time']
        rate = dt.find(f'.//ex:Cube[@currency="{currency}"]', namespaces=namespaces).attrib['rate']
        date_list.append(date)
        rate_list.append(float(rate))

    exchange_rate_dict.update({'date': date_list, 'rate': rate_list})
    exchange_rate_df = pd.DataFrame.from_dict(exchange_rate_dict)
    return exchange_rate_df


def _get_transactions_df():
    """
    reads the transaction data from DB and returns as df.
    """
    return pd.read_sql_query("""
        select *
        from Transactions
        ;
    """, cnx)


def _get_devices_df():
    """
    reads the devices' data from DB and returns as df.
    """
    return pd.read_sql_query("""
        select * from Devices;
    """, cnx)
