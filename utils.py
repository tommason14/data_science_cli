def data_from_stdin():
    """
    Retuns a dataframe from a csv file piped in from stdin.
    """
    import pandas as pd
    import sys
    data = [line.strip() for line in sys.stdin]
    data = [line.split(',') for line in data]
    header, *data = data
    indexes = [i for i in range(len(data))]
    df = pd.DataFrame(data, columns = header, index = indexes)
    return df

