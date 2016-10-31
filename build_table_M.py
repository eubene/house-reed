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

df1 = loadboth('date', 'S24')
df2 = loadboth('date', 'S25')
df1.T.to_csv('../all_S24_date_T.csv')
df2.T.to_csv('../all_S25_date_T.csv')