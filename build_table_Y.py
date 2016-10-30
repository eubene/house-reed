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

#
# Operation Y1 = Station S39
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S39')
index1 = df1[df1.columns[0]].notnull()

# station not meaningful
# dfo['Station'] = ''
# dfo.loc[index1, 'Station'] = 'S39'

# all date values are the same, so just use first column
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]

# categorical: all 63 columns look identical, so copy only first
df1 = loadboth('categorical', 'S39')
dfo['C1'] = ''
dfo.loc[index1, 'C1'] = df1.loc[index1, df1.columns[0]]

# numeric: lots of duplicate columns. only keep unique
df1 = loadboth('numeric', 'S39')
for i, j in enumerate([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 20, 21, 28, 32, 33, 34, 35, 42, 43, 46, 47, 48, 49, 50, 51, 52]):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[j]]

dfo.to_csv('../byop/all_Y1.csv')

