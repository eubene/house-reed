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
# Operation Z1 = Station S29
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S29')
index1 = df1[df1.columns[0]].notnull()

# station not meaningful
# dfo['Station'] = ''
# dfo.loc[index1, 'Station'] = 'S29'

# all date values are the same, so just use first column
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]

# categorical: all 63 columns look identical, so copy only first
df1 = loadboth('categorical', 'S29')
dfo['C1'] = ''
dfo.loc[index1, 'C1'] = df1.loc[index1, df1.columns[0]]

# numeric: lots of duplicate columns. only keep unique
df1 = loadboth('numeric', 'S29')
for i, j in enumerate([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 20, 21, 28, 32, 33, 34, 35, 42, 43, 46, 47, 48, 49, 50, 51, 52]):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[j]]

dfo.to_csv('../byop/all_Z1.csv')

#
# Operation Z2 = Station S30
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S30')
index1 = df1[df1.columns[0]].notnull()

# station not meaningful
# dfo['Station'] = ''
# dfo.loc[index1, 'Station'] = 'S30'

# first column has the most data (values match across columns)
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]

# categorical: 204 columns, take only the ones that look unique
df1 = loadboth('categorical', 'S30')
for i, j in enumerate([0, 1, 2, 6, 7, 8]):
	dfo['C' + str(i+1)] = ''
	dfo.loc[index1, 'C' + str(i+1)] = df1.loc[index1, df1.columns[j]]

# numeric: some duplicate columns. only keep unique
df1 = loadboth('numeric', 'S30')
for i, j in enumerate([ 0,  2,  3,  4,  5,  6,  8, 10, 12, 14, 15, 16, 17, 18, 19, 20, 22,
        23, 26, 27, 28, 29, 30, 31, 34, 35, 36, 37, 38, 39, 42, 43, 46, 47,
        48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 65, 67]):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[j]]

dfo.to_csv('../byop/all_Z2.csv')

#
# Operation ZE1 = Station S31
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S31')
index1 = df1[df1.columns[0]].notnull()

# station - need to keep track of whether S31 was used
dfo['Station'] = ''
dfo.loc[index1, 'Station'] = 'S31'

# all columns are the same, so take the first
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]

# categorical: first two only
df1 = loadboth('categorical', 'S31')
for i in [0, 1]:
	dfo['C' + str(i+1)] = ''
	dfo.loc[index1, 'C' + str(i+1)] = df1.loc[index1, df1.columns[i]]

# numeric: some duplicate columns. only keep unique
df1 = loadboth('numeric', 'S31')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]

dfo.to_csv('../byop/all_ZE1.csv')

#
# Operation ZE2 = Station S32
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S32')
index1 = df1[df1.columns[0]].notnull()

# station - need to keep track of whether S31 was used
dfo['Station'] = ''
dfo.loc[index1, 'Station'] = 'S32'

# all columns are the same, so take the first
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]

# categorical: all three
df1 = loadboth('categorical', 'S32')
for i in range(len(df1.columns)):
	dfo['C' + str(i+1)] = ''
	dfo.loc[index1, 'C' + str(i+1)] = df1.loc[index1, df1.columns[i]]

# numeric: only one column
df1 = loadboth('numeric', 'S32')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]

dfo.to_csv('../byop/all_ZE2.csv')

#
# Operation Z3 = Station S33
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S33')
index1 = df1[df1.columns[0]].notnull()

# station is redundant
# dfo['Station'] = ''
# dfo.loc[index1, 'Station'] = 'S33'

# all columns are the same, so take the first
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]

# no categorical
# df1 = loadboth('categorical', 'S33')
# for i in range(len(df1.columns)):
# 	dfo['C' + str(i+1)] = ''
# 	dfo.loc[index1, 'C' + str(i+1)] = df1.loc[index1, df1.columns[i]]

# numeric: some duplicates
df1 = loadboth('numeric', 'S33')
for i, j in enumerate([0, 1, 2, 5, 6, 7, 8, 9]):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[j]]

dfo.to_csv('../byop/all_Z3.csv')

#
# Operation Z4 = Station S34
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S34')
index1 = df1[df1.columns[0]].notnull()

# station is redundant
# dfo['Station'] = ''
# dfo.loc[index1, 'Station'] = 'S34'

# all columns are the same, so take the first
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]

# no categorical
# df1 = loadboth('categorical', 'S34')
# for i in range(len(df1.columns)):
# 	dfo['C' + str(i+1)] = ''
# 	dfo.loc[index1, 'C' + str(i+1)] = df1.loc[index1, df1.columns[i]]

# numeric
df1 = loadboth('numeric', 'S34')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]

dfo.to_csv('../byop/all_Z4.csv')

#
# Operation Z5 = Stations S35, S36
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S35')
df2 = loadboth('date', 'S36')
index1 = df1[df1.columns[4]].notnull()
index2 = df2[df2.columns[4]].notnull()

# station
dfo['Station'] = ''
dfo.loc[index1, 'Station'] = 'S35'
dfo.loc[index2, 'Station'] = 'S36'

# 5th column has the most data for both
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[4]]
dfo.loc[index2, 'Date'] = df2.loc[index2, df2.columns[4]]

# categorical: take three
df1 = loadboth('categorical', 'S35')
df2 = loadboth('categorical', 'S36')
dfo['C1'] = ''
dfo.loc[index1, 'C1'] = df1.loc[index1, df1.columns[6]]
dfo.loc[index2, 'C1'] = df2.loc[index2, df2.columns[0]]
dfo['C2'] = ''
dfo.loc[index1, 'C2'] = df1.loc[index1, df1.columns[7]]
dfo.loc[index2, 'C2'] = df2.loc[index2, df2.columns[0]]
dfo['C3'] = ''
dfo.loc[index1, 'C3'] = df1.loc[index1, df1.columns[8]]
dfo.loc[index2, 'C3'] = df2.loc[index2, df2.columns[1]]

# numeric
df1 = loadboth('numeric', 'S35')
df2 = loadboth('numeric', 'S36')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]
	dfo.loc[index2, 'N' + str(i+1)] = df2.loc[index2, df2.columns[i]]

dfo.to_csv('../byop/all_Z5.csv')

#
# Operation Z6 = Station S37
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S37')
index1 = df1[df1.columns[0]].notnull()

# station is redundant
# dfo['Station'] = ''
# dfo.loc[index1, 'Station'] = 'S37'

# all columns are the same, so take the first
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]

# no categorical
# df1 = loadboth('categorical', 'S37')
# for i in range(len(df1.columns)):
# 	dfo['C' + str(i+1)] = ''
# 	dfo.loc[index1, 'C' + str(i+1)] = df1.loc[index1, df1.columns[i]]

# numeric
df1 = loadboth('numeric', 'S37')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]

dfo.to_csv('../byop/all_Z6.csv')

#
# Operation Z7 = Station S38
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S38')
index1 = df1[df1.columns[0]].notnull()

# station, since it's a rare op
dfo['Station'] = ''
dfo.loc[index1, 'Station'] = 'S38'

# all columns are the same, so take the first
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]

# categorical: first two are unique
df1 = loadboth('categorical', 'S38')
for i in [0, 1]:
	dfo['C' + str(i+1)] = ''
	dfo.loc[index1, 'C' + str(i+1)] = df1.loc[index1, df1.columns[i]]

# numeric
df1 = loadboth('numeric', 'S38')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]

dfo.to_csv('../byop/all_Z7.csv')
