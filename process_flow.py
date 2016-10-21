import numpy as np
import pandas as pd
import csv

def extract_process_flow(filename):
    f = open(filename, 'r')

    # First line of the csv is the column names
    # Trim newline, split, then remove first item "Id"
    colnames = f.readline()[:-1].split(',')[1:]
    # Each colname is like Lx_Sy_Dz; extract middle portion
    stations = [s.split('_')[1] for s in colnames]

    # Initialize
    ids = []
    pflows = []
    # Process each line
    reader = csv.reader(f)
    for row in reader:
        # Extract dates as floats with NaN when missing
        dates = [(float(s) if (s != '') else np.nan) for s in row[1:]]
        # Create temporary dataframe, dropna, drop_duplicates, sort by date
        rowdf = pd.DataFrame({'station': stations, 'date': dates})
        rowdf = rowdf.dropna().drop_duplicates().sort_values(by = 'date')
        # Save ID and flow string
        ids.append(int(row[0]))
        pflows.append('-'.join(rowdf['station'].tolist()))
        print(row[0], '\r', end = '')
    f.close()
    print('')
    return pd.DataFrame({'Id': ids, 'PFlow': pflows})

df_train = extract_process_flow('../train_date.csv')
df_test = extract_process_flow('../test_date.csv')
df_pflow = pd.concatenate([df_train, df_test], ignore_index = True)
df_pflow.to_csv('../all_pflow.csv')
