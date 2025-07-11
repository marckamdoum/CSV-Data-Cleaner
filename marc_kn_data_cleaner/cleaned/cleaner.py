import pandas as pd

def clean_data(df, column_types, remove_duplicates, remove_na):
    # Typkonvertierung
    for column, dtype in column_types.items():
        df[column] = df[column].astype(dtype)


    # Duplikate entfernen
    if remove_duplicates:
        df = df.drop_duplicates()

    # fehlende Werte entfernen
    if remove_na:
        df = df.dropna()

    return df