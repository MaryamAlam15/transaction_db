import pandas as pd

from extract import get_exchange_rates


# task 1
def visitor_with_most_revenue(transactions_df):
    """
    takes df as param and returns the visitor id who generated most revenue.
    """
    trans_without_tax_df = _get_rev_without_tax(transactions_df)
    return trans_without_tax_df.groupby('visitor_id')['rev_without_tax'].sum().nlargest(1, keep='first').keys()[0]


# task 2
def day_with_most_mobile_revenue(transactions_df):
    """
    takes df as param and returns the date on which most mobile revenue is generated.
    """
    trans_without_tax_df = _get_rev_without_tax(transactions_df)
    trans_without_tax_df['date_time'] = pd.to_datetime(trans_without_tax_df['datetime'], format='%Y-%m-%d %H:%M:%S')
    return trans_without_tax_df[trans_without_tax_df.device_type == 3] \
        .groupby([trans_without_tax_df['date_time'].dt.date])['rev_without_tax'] \
        .sum().nlargest(1, keep='first').keys()[0]


# task 3
def combine_data(transactions_df, devices_df):
    """
    takes transactions and devices as df and merges them.
    """
    trans_with_devices_df = transactions_df.merge(devices_df, left_on='device_type', right_on='id') \
        .drop(['id_x', 'id_y'], axis=1)
    return trans_with_devices_df


# task 4
def convert_rev_to_eur(transactions_df):
    """
    takes transactions df as param and add a new column with revenue in EURs.
    """
    exchange_rate_per_day_df = _get_exchange_rates_in_date_range_of_df(transactions_df)
    trans_with_exchange_rate_df = transactions_df.merge(
        exchange_rate_per_day_df,
        on='date',
        how='left'
    )
    trans_with_exchange_rate_df['revenue_eur'] = (
            trans_with_exchange_rate_df['revenue'] * trans_with_exchange_rate_df['rate']
    )
    return trans_with_exchange_rate_df


def _get_rev_without_tax(df):
    """
    helper method to subtract tax from revenue.
    """
    df['rev_without_tax'] = df['revenue'] - (df['tax'] * df['revenue'])
    return df


def _get_exchange_rates_in_date_range_of_df(transactions_df):
    """
    takes transaction df as param;
    gets min and max date ranges from the df
    and finds the exchange rate from a currency to EUR.
    """
    exchange_rate_df = get_exchange_rates()
    transactions_df['date'] = pd.to_datetime(transactions_df['datetime']).dt.date.astype('str')
    min_date = pd.to_datetime(transactions_df['date']).dt.date.min()
    max_date = pd.to_datetime(transactions_df['date']).dt.date.max()

    # # get all dates till today.
    date_range_df = pd.date_range(start=min_date, end=max_date).to_frame(index=False, name='date').astype('str')
    # # left join with exchange rates.
    exchange_rate_per_day_df = pd.merge(date_range_df, exchange_rate_df, on='date', how='left')
    # # f-fill wrt row.
    return exchange_rate_per_day_df.ffill(axis=0)
