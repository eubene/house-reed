import numpy as np
import pandas as pd

# Keep track of train vs test Ids
df_train = pd.read_csv('../bystation/train_categorical_S1.csv', index_col='Id', dtype=object)
df_test = pd.read_csv('../bystation/test_categorical_S1.csv', index_col='Id', dtype=object)
df_train['Train'] = True
df_test['Train'] = False
df_istrain = pd.concat([df_train, df_test], axis=0)[['Train']]

# Operation A1 = Stations S0 and S12

dfa1 = pd.DataFrame()
dfs0 = pd.read_csv('../bystation/train_date_S0.csv')