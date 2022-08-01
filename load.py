def write_df_to_csv(df, file_name, index=False):
    """
    writes the df to the given csv file.
    """
    df.to_csv(f'output/{file_name}.csv', index=index)
