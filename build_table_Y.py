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

# categorical: all are virtually the same, take the first one
df1 = loadboth('categorical', 'S39')
dfo['C1'] = ''
dfo.loc[index1, 'C1'] = df1.loc[index1, df1.columns[0]]

# numeric
df1 = loadboth('numeric', 'S39')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]

dfo.to_csv('../byop/all_Y1.csv')

#
# Operation Y2 = Station S40
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S40')
index1 = df1[df1.columns[2]].notnull()

# station not meaningful
# dfo['Station'] = ''
# dfo.loc[index1, 'Station'] = 'S40'

# third column has more data
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[2]]

# no categorical
# df1 = loadboth('categorical', 'S40')
# dfo['C1'] = ''
# dfo.loc[index1, 'C1'] = df1.loc[index1, df1.columns[0]]

# numeric
df1 = loadboth('numeric', 'S40')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]

dfo.to_csv('../byop/all_Y2.csv')

#
# Operation Y3 = Station S41
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S41')
index1 = df1[df1.columns[0]].notnull()

# station not meaningful
# dfo['Station'] = ''
# dfo.loc[index1, 'Station'] = 'S41'

# all columns the same, so take the first
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]

# no categorical
# df1 = loadboth('categorical', 'S41')
# dfo['C1'] = ''
# dfo.loc[index1, 'C1'] = df1.loc[index1, df1.columns[0]]

# numeric
df1 = loadboth('numeric', 'S41')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]

dfo.to_csv('../byop/all_Y3.csv')

#
# Operation Y4 = Stations S43, S44
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S43')
df2 = loadboth('date', 'S44')
index1 = df1[df1.columns[0]].notnull()
index2 = df2[df2.columns[0]].notnull()

# station
dfo['Station'] = ''
dfo.loc[index1, 'Station'] = 'S43'
dfo.loc[index2, 'Station'] = 'S44'

# 1st column seems like a good choice
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]
dfo.loc[index2, 'Date'] = df2.loc[index2, df2.columns[0]]

# categorical: take first three
df1 = loadboth('categorical', 'S43')
df2 = loadboth('categorical', 'S44')
for i in [0, 1, 2]:
	dfo['C' + str(i+1)] = ''
	dfo.loc[index1, 'C' + str(i+1)] = df1.loc[index1, df1.columns[i]]
	dfo.loc[index2, 'C' + str(i+1)] = df2.loc[index2, df2.columns[i]]

# numeric
df1 = loadboth('numeric', 'S43')
df2 = loadboth('numeric', 'S44')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]
	dfo.loc[index2, 'N' + str(i+1)] = df2.loc[index2, df2.columns[i]]

dfo.to_csv('../byop/all_Y4.csv')

#
# Operation Y5 = Station S45
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S45')
index1 = df1[df1.columns[0]].notnull()

# station not meaningful
# dfo['Station'] = ''
# dfo.loc[index1, 'Station'] = 'S45'

# all columns the same, so take the first
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]

# no categorical
# df1 = loadboth('categorical', 'S45')
# dfo['C1'] = ''
# dfo.loc[index1, 'C1'] = df1.loc[index1, df1.columns[0]]

# numeric
df1 = loadboth('numeric', 'S45')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]

dfo.to_csv('../byop/all_Y5.csv')

#
# Operation Y6 = Station S47
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S47')
index1 = df1[df1.columns[0]].notnull()

# station not meaningful
# dfo['Station'] = ''
# dfo.loc[index1, 'Station'] = 'S47'

# all columns the same, so take the first
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]

# categorical: either only one or all the same, so don't include
# df1 = loadboth('categorical', 'S47')
# dfo['C1'] = ''
# dfo.loc[index1, 'C1'] = df1.loc[index1, df1.columns[1]]

# numeric. one duplicate column
df1 = loadboth('numeric', 'S47')
for i, j in enumerate([0, 1, 2, 3, 4, 5, 7, 8, 9, 10]):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]

dfo.to_csv('../byop/all_Y6.csv')

#
# Operation Y7 = Station S48
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S48')
index1 = df1[df1.columns[0]].notnull()

# station not meaningful
# dfo['Station'] = ''
# dfo.loc[index1, 'Station'] = 'S48'

# all columns the same, so take the first
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]

# categorical: either only one or all the same, so don't include
# df1 = loadboth('categorical', 'S48')
# dfo['C1'] = ''
# dfo.loc[index1, 'C1'] = df1.loc[index1, df1.columns[1]]

# numeric. one duplicate column
df1 = loadboth('numeric', 'S48')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]

dfo.to_csv('../byop/all_Y7.csv')

#
# Operation Y8 = Stations S49, S50
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S49')
df2 = loadboth('date', 'S50')
index1 = df1[df1.columns[0]].notnull()
index2 = df2[df2.columns[0]].notnull()

# station
dfo['Station'] = ''
dfo.loc[index1, 'Station'] = 'S49'
dfo.loc[index2, 'Station'] = 'S50'

# all columns identical, take the first column
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]
dfo.loc[index2, 'Date'] = df2.loc[index2, df2.columns[0]]

# categorical: only S49 has. take first column.
df1 = loadboth('categorical', 'S49')
dfo['C1'] = ''
dfo.loc[index1, 'C1'] = df1.loc[index1, df1.columns[0]]

# numeric
df1 = loadboth('numeric', 'S49')
df2 = loadboth('numeric', 'S50')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]
	dfo.loc[index2, 'N' + str(i+1)] = df2.loc[index2, df2.columns[i]]

dfo.to_csv('../byop/all_Y8.csv')

#
# Operation Y9 = Station S51
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S51')
index1 = df1[df1.columns[0]].notnull()

# station not meaningful
# dfo['Station'] = ''
# dfo.loc[index1, 'Station'] = 'S51'

# all columns the same, so take the first
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]

# categorical: none
# df1 = loadboth('categorical', 'S51')
# dfo['C1'] = ''
# dfo.loc[index1, 'C1'] = df1.loc[index1, df1.columns[1]]

# numeric. one duplicate column
df1 = loadboth('numeric', 'S51')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]

dfo.to_csv('../byop/all_Y9.csv')
