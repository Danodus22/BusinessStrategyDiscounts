import pandas as pd
def data_overview(df, df_name="my_dataframe"):
    # 1. Overview
    print(f"***** Overview {df_name} ***** \n")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    print(f"Total number of values: {df.size} \n")

    # 2. Data types
    print(f"***** Data types of columns in {df_name} ***** \n")
    column_info = pd.DataFrame({
        'Data Type': df.dtypes,
        'Non-Null Count': df.count()
    })
    print(column_info, "\n")

    # 3. Missing values and their percentage share
    print(f"***** Missing values in {df_name} ***** \n")
    missing_values = df.isnull().sum()
    missing_percent = (missing_values / len(df)) * 100
    missing_info = pd.DataFrame({
        'Missing values': missing_values,
        'of': len(df),
        'Percentage': missing_percent
    })
    missing_info = missing_info[missing_info['Missing values'] > 0]
    if not missing_info.empty:
        print(f" {missing_info} \n")
    else:
        print("No missing values \n")

    # 4. Duplicates
    print(f"***** Duplicates in {df_name} ***** \n")
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        print(f"Number of duplicates: {duplicate_count} of {df.shape[0]} ( {round((duplicate_count / len(df)) * 100, 2)}% of rows) \n")
    else:
        print("No duplicates DataFrame \n")

    # 5. Unique values
    print(f"***** Unique values per column in {df_name} ***** \n")
    for col in df.columns:
        unique_count = df[col].nunique()
        print(f"{col}: {unique_count} unique values | Total: {len(df)} rows | Not unique: {len(df)-unique_count} rows")

    # 6. Statistical key figures
    print(f"\n ***** Statistical key figures for {df_name} ***** \n")
    print(round(df.describe(), 2), "\n")