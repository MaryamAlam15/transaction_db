from extract import extract_db_data
from load import write_df_to_csv
from transform import (
    convert_rev_to_eur,
    combine_data,
    visitor_with_most_revenue,
    day_with_most_mobile_revenue
)

if __name__ == '__main__':
    transactions_df, devices_df = extract_db_data()
    print(f"Task 1: Visitor id with most revenue: {visitor_with_most_revenue(transactions_df)}")
    print(f"Task 2: Day with most Mobile revenue: {day_with_most_mobile_revenue(transactions_df)}")
    transactions_with_devices = combine_data(transactions_df, devices_df)
    write_df_to_csv(transactions_with_devices, 'combine_data')
    print("Task 3: Transactions with Device names are stored in /output folder.")
    convert_rev_to_eur(transactions_df)
    print(f"Task 4: Added Revenue in EUR as a new column:\n {convert_rev_to_eur(transactions_df).head()}")
