import numpy as np
import pandas as pd

def extract_column(filename, colname, chunksize=10000):
    chunker = pd.read_csv(filename, chunksize=chunksize, index_col='Id')
    piece = chunker.__next__()
    if colname not in piece.columns:
        raise ValueError('not a valid column name', colname, filename)
    col = piece[[colname]]
    for piece in chunker:
        col = pd.concat([col, piece[[colname]]])
        print(piece.index[len(piece.index)-1], '\r', end = '')
    print('')
    return col

df_train_response = extract_column('../train_numeric.csv', 'Response')
df_train_response.to_csv('../train_response.csv')