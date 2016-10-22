import numpy as np
import pandas as pd
import csv

def extract_column(filename, colname, chunksize=10000):
    chunker = pd.read_csv(filename, chunksize=chunksize)
    piece = chunker.__next__()
    if colname not in piece.columns:
        raise ValueError('not a valid column name', colname, filename)
    col = piece[colname]
    for piece in chunker:
        col = pd.concat([col, piece[colname]])
    return col

def extract_process_flow(filename, chunksize=10000):
    # Read just the first line to get column names
    chunker = pd.read_csv(filename, index_col='Id', chunksize=1)
    piece = chunker.__next__() 

    # Each column name is like Lx_Sy_Dz; extract middle portion
    stations = [s.split('_')[1] for s in piece.columns]
    # Get just the unique station names
    stations, icol = np.unique(np.array(stations), return_index=True)
    # But get the original order back by sorting on icol
    stations = stations[np.argsort(icol)]
    icol = np.sort(icol)

    # Set up chunker with full chunksize
    chunker = pd.read_csv(filename, index_col='Id', chunksize=chunksize)

    ids = []
    pflows = []
    for piece in chunker:
        for ii, row in piece.iterrows():
            # Save index, which is "Id"
            ids.append(ii)
            # Drop missing, sort by value (date), and take the index (colname)
            colorder = row[icol].dropna().sort_values().index
            # Join station names in order of process flow and save string
            pflows.append('-'.join([s.split('_')[1] for s in colorder]))
            print(ii, '\r', end = '')
    print('')
    return pd.DataFrame({'Id': ids, 'PFlow': pflows})

df_train = extract_process_flow('../train_date.csv')
df_test = extract_process_flow('../test_date.csv')
df_pflow = pd.concatenate([df_train, df_test], ignore_index = True)
df_pflow.to_csv('../all_pflow.csv')
