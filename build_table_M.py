import numpy as np
import pandas as pd
import glob

# Keep track of train vs test Ids
df_train = pd.read_csv('../bystation/train_categorical_S1.csv', usecols = ['Id'], index_col='Id', dtype=str)
df_test = pd.read_csv('../bystation/test_categorical_S1.csv', usecols = ['Id'], index_col='Id', dtype=str)
df_train['Train'] = True
df_test['Train'] = False
df_istrain = pd.concat([df_train, df_test], axis=0)[['Train']]

# Functions
def loadboth(type, station):
	filelist = glob.glob('../bystation/*_' + type + '_' + station + '.csv')
	return(pd.concat([pd.read_csv(file, index_col='Id', dtype=str) for file in filelist], axis=0))
def loadboth_num(type, station):
	filelist = glob.glob('../bystation/*_' + type + '_' + station + '.csv')
	return(pd.concat([pd.read_csv(file, index_col='Id') for file in filelist], axis=0))

def distance(col1, col2):
	return(pd.np.linalg.norm(col1 - col2))

df1 = loadboth_num('date', 'S24')
df1.dropna(how='all', inplace=True)
df1.fillna(0, inplace=True)
dist = df1.apply(lambda col1: df1.apply(lambda col2: distance(col1, col2)))
dist.to_csv('../S24_dist.csv', header=False, index=False)
del(df1)

df2 = loadboth_num('date', 'S25')
df2.dropna(how='all', inplace=True)
df2.fillna(0, inplace=True)
dist = df2.apply(lambda col1: df2.apply(lambda col2: distance(col1, col2)))
dist.to_csv('../S25_dist.csv', header=False, index=False)
del(df2)
