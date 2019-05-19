import pandas as pd

def data_from_stdin():
    """
    Retuns a dataframe from a csv file piped in from stdin.
    """
    import sys
    data = [line.strip() for line in sys.stdin]
    data = [line.split(',') for line in data]
    header, *data = data
    indexes = [i for i in range(len(data))]
    df = pd.DataFrame(data, columns = header, index = indexes)
    # need to make sure columns are correct type
    df = convert_col_to_numeric(df)
    return df

def convert_col_to_numeric(df):
    """
    Checks if every item in the column can be converted to
    a numeric type.
    If yes, converts to numeric.
    Necessary as reading from stdin creates strings
    """
    # using pandas apply
    for col in df.columns:
        results = []
        numeric = False
        for value in df[col]:
            try:
                value = float(value)
                numeric = True
            except ValueError:
                pass
            results.append(numeric)
        if all(item for item in results): 
            df[col] = pd.to_numeric(df[col])
    return df
