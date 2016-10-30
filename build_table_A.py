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
# Operation A1 = Stations S0 and S12
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S0')
index1 = df1[df1.columns[0]].notnull()
df2 = loadboth('date', 'S12')
index2 = df2[df2.columns[0]].notnull()

# station
dfo['Station'] = ''
dfo.loc[index1, 'Station'] = 'S0'
dfo.loc[index2, 'Station'] = 'S12'

# all date values are the same, so just use one column
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]
dfo.loc[index2, 'Date'] = df2.loc[index2, df2.columns[0]]

# no categorical

# numeric
df1 = loadboth('numeric', 'S0')
df2 = loadboth('numeric', 'S12')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]
	dfo.loc[index2, 'N' + str(i+1)] = df2.loc[index2, df2.columns[i]]

dfo.to_csv('../byop/all_A1.csv')

#
# Operation A2 = Stations S1 and S13
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S1')
index1 = df1[df1.columns[1]].notnull()
df2 = loadboth('date', 'S13')
index2 = df2[df2.columns[1]].notnull()

# skip station since it's redundant with A1 station

# use second column as date (has slightly fewer missing values)
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[1]]
dfo.loc[index2, 'Date'] = df2.loc[index2, df2.columns[1]]

# only S1 has categorical columns, but only ~50 with non-missing
# values. probably will drop
df1 = loadboth('categorical', 'S1')
for i in range(len(df1.columns)):
	dfo['C' + str(i+1)] = ''
	dfo.loc[index1, 'C' + str(i+1)] = df1.loc[index1, df1.columns[i]]

# numeric
df1 = loadboth('numeric', 'S1')
df2 = loadboth('numeric', 'S13')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]
	dfo.loc[index2, 'N' + str(i+1)] = df2.loc[index2, df2.columns[i]]

dfo.to_csv('../byop/all_A2.csv')

#
# Operation A3 = Stations S2, S3, S14, S15
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S2')
index1 = df1[df1.columns[0]].notnull()
df2 = loadboth('date', 'S3')
index2 = df2[df2.columns[0]].notnull()
df3 = loadboth('date', 'S14')
index3 = df3[df3.columns[0]].notnull()
df4 = loadboth('date', 'S15')
index4 = df4[df4.columns[0]].notnull()

# station
dfo['Station'] = ''
dfo.loc[index1, 'Station'] = 'S2'
dfo.loc[index2, 'Station'] = 'S3'
dfo.loc[index3, 'Station'] = 'S14'
dfo.loc[index4, 'Station'] = 'S15'

# use first column as date since they are all identical
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]
dfo.loc[index2, 'Date'] = df2.loc[index2, df2.columns[0]]
dfo.loc[index3, 'Date'] = df3.loc[index3, df3.columns[0]]
dfo.loc[index4, 'Date'] = df4.loc[index4, df4.columns[0]]

# categorical: only first two columns unique. S15 has only one
# non-missing row, and it's only in the training set, so drop it.
df1 = loadboth('categorical', 'S2')
df2 = loadboth('categorical', 'S3')
df3 = loadboth('categorical', 'S14')
# df4 = loadboth('categorical', 'S15')
for i in [0, 1]:
	dfo['C' + str(i+1)] = ''
	dfo.loc[index1, 'C' + str(i+1)] = df1.loc[index1, df1.columns[i]]
	dfo.loc[index2, 'C' + str(i+1)] = df2.loc[index2, df2.columns[i]]
	dfo.loc[index3, 'C' + str(i+1)] = df3.loc[index3, df3.columns[i]]

# numeric
df1 = loadboth('numeric', 'S2')
df2 = loadboth('numeric', 'S3')
df3 = loadboth('numeric', 'S14')
df4 = loadboth('numeric', 'S15')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]
	dfo.loc[index2, 'N' + str(i+1)] = df2.loc[index2, df2.columns[i]]
	dfo.loc[index3, 'N' + str(i+1)] = df3.loc[index3, df3.columns[i]]
	dfo.loc[index4, 'N' + str(i+1)] = df4.loc[index4, df4.columns[i]]

dfo.to_csv('../byop/all_A3.csv')

#
# Operation A4 = Stations S4, S5, S16, S17
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S4')
index1 = df1[df1.columns[0]].notnull()
df2 = loadboth('date', 'S5')
index2 = df2[df2.columns[0]].notnull()
df3 = loadboth('date', 'S16')
index3 = df3[df3.columns[0]].notnull()
df4 = loadboth('date', 'S17')
index4 = df4[df4.columns[0]].notnull()

# station
dfo['Station'] = ''
dfo.loc[index1, 'Station'] = 'S4'
dfo.loc[index2, 'Station'] = 'S5'
dfo.loc[index3, 'Station'] = 'S16'
dfo.loc[index4, 'Station'] = 'S17'

# use first column as date since in S4 it has slightly more data
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]
dfo.loc[index2, 'Date'] = df2.loc[index2, df2.columns[0]]
dfo.loc[index3, 'Date'] = df3.loc[index3, df3.columns[0]]
dfo.loc[index4, 'Date'] = df4.loc[index4, df4.columns[0]]

# categorical: only S4 and S16 have data. fortunately same number
# of columns. all columns look to be unique.
df1 = loadboth('categorical', 'S4')
df3 = loadboth('categorical', 'S16')
for i in range(len(df1.columns)):
	dfo['C' + str(i+1)] = ''
	dfo.loc[index1, 'C' + str(i+1)] = df1.loc[index1, df1.columns[i]]
	dfo.loc[index3, 'C' + str(i+1)] = df3.loc[index3, df3.columns[i]]

# numeric
df1 = loadboth('numeric', 'S4')
df2 = loadboth('numeric', 'S5')
df3 = loadboth('numeric', 'S16')
df4 = loadboth('numeric', 'S17')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]
	dfo.loc[index2, 'N' + str(i+1)] = df2.loc[index2, df2.columns[i]]
	dfo.loc[index3, 'N' + str(i+1)] = df3.loc[index3, df3.columns[i]]
	dfo.loc[index4, 'N' + str(i+1)] = df4.loc[index4, df4.columns[i]]

dfo.to_csv('../byop/all_A4.csv')

#
# Operation A5 = Stations S6, S7, S18, S19
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S6')
index1 = df1[df1.columns[0]].notnull()
df2 = loadboth('date', 'S7')
index2 = df2[df2.columns[0]].notnull()
df3 = loadboth('date', 'S18')
index3 = df3[df3.columns[0]].notnull()
df4 = loadboth('date', 'S19')
index4 = df4[df4.columns[0]].notnull()

# station
dfo['Station'] = ''
dfo.loc[index1, 'Station'] = 'S6'
dfo.loc[index2, 'Station'] = 'S7'
dfo.loc[index3, 'Station'] = 'S18'
dfo.loc[index4, 'Station'] = 'S19'

# use first column as date since they are all identical
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]
dfo.loc[index2, 'Date'] = df2.loc[index2, df2.columns[0]]
dfo.loc[index3, 'Date'] = df3.loc[index3, df3.columns[0]]
dfo.loc[index4, 'Date'] = df4.loc[index4, df4.columns[0]]

# categorical: only S6 and S18 have data. only first two columns
# are unique
df1 = loadboth('categorical', 'S6')
df3 = loadboth('categorical', 'S18')
for i in [0, 1]:
	dfo['C' + str(i+1)] = ''
	dfo.loc[index1, 'C' + str(i+1)] = df1.loc[index1, df1.columns[i]]
	dfo.loc[index3, 'C' + str(i+1)] = df3.loc[index3, df3.columns[i]]

# numeric
df1 = loadboth('numeric', 'S6')
df2 = loadboth('numeric', 'S7')
df3 = loadboth('numeric', 'S18')
df4 = loadboth('numeric', 'S19')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]
	dfo.loc[index2, 'N' + str(i+1)] = df2.loc[index2, df2.columns[i]]
	dfo.loc[index3, 'N' + str(i+1)] = df3.loc[index3, df3.columns[i]]
	dfo.loc[index4, 'N' + str(i+1)] = df4.loc[index4, df4.columns[i]]

dfo.to_csv('../byop/all_A5.csv')

#
# Operation A6 = Stations S8 and S20
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S8')
index1 = df1[df1.columns[0]].notnull()
df2 = loadboth('date', 'S20')
index2 = df2[df2.columns[0]].notnull()

# station is redundant with A1

# all date values are the same, so just use first column
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]
dfo.loc[index2, 'Date'] = df2.loc[index2, df2.columns[0]]

# no categorical

# numeric
df1 = loadboth('numeric', 'S8')
df2 = loadboth('numeric', 'S20')
for i in range(len(df1.columns)):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]
	dfo.loc[index2, 'N' + str(i+1)] = df2.loc[index2, df2.columns[i]]

dfo.to_csv('../byop/all_A6.csv')

#
# Operation A7 = Stations S9, S10, S11, S21, S22, S23
#
dfo = pd.DataFrame(index=df_istrain.index)
df1 = loadboth('date', 'S9')
index1 = df1[df1.columns[0]].notnull()
df2 = loadboth('date', 'S10')
index2 = df2[df2.columns[0]].notnull()
df3 = loadboth('date', 'S11')
index3 = df3[df3.columns[0]].notnull()
df4 = loadboth('date', 'S21')
index4 = df4[df4.columns[0]].notnull()
df5 = loadboth('date', 'S22')
index5 = df5[df5.columns[0]].notnull()
df6 = loadboth('date', 'S23')
index6 = df6[df6.columns[0]].notnull()

# station
dfo['Station'] = ''
dfo.loc[index1, 'Station'] = 'S9'
dfo.loc[index2, 'Station'] = 'S10'
dfo.loc[index3, 'Station'] = 'S11'
dfo.loc[index4, 'Station'] = 'S21'
dfo.loc[index5, 'Station'] = 'S22'
dfo.loc[index6, 'Station'] = 'S23'

# use first column, since it has slightly more data for all stations
dfo['Date'] = ''
dfo.loc[index1, 'Date'] = df1.loc[index1, df1.columns[0]]
dfo.loc[index2, 'Date'] = df2.loc[index2, df2.columns[0]]
dfo.loc[index3, 'Date'] = df3.loc[index3, df3.columns[0]]
dfo.loc[index4, 'Date'] = df4.loc[index4, df4.columns[0]]
dfo.loc[index5, 'Date'] = df5.loc[index5, df5.columns[0]]
dfo.loc[index6, 'Date'] = df6.loc[index6, df6.columns[0]]

# categorical: this is a tough one. 21/22/23 have more columns than
# 9/10/11. And within both groups, 11 and 23 have 1/3 fewer columns.
# Lots of columns with almost identical data. Going to take a
# guess and take first three columns. 11 and 23 will repeat
# their first columns as first and second column of the rest.
df1 = loadboth('categorical', 'S9')
df2 = loadboth('categorical', 'S10')
df3 = loadboth('categorical', 'S11')
df4 = loadboth('categorical', 'S21')
df5 = loadboth('categorical', 'S22')
df6 = loadboth('categorical', 'S23')
dfo['C1'] = ''
dfo.loc[index1, 'C1'] = df1.loc[index1, df1.columns[0]]
dfo.loc[index2, 'C1'] = df2.loc[index2, df2.columns[0]]
dfo.loc[index3, 'C1'] = df3.loc[index3, df3.columns[0]]
dfo.loc[index4, 'C1'] = df4.loc[index4, df4.columns[0]]
dfo.loc[index5, 'C1'] = df5.loc[index5, df5.columns[0]]
dfo.loc[index6, 'C1'] = df6.loc[index6, df6.columns[0]]
dfo['C2'] = ''
dfo.loc[index1, 'C2'] = df1.loc[index1, df1.columns[1]]
dfo.loc[index2, 'C2'] = df2.loc[index2, df2.columns[1]]
dfo.loc[index3, 'C2'] = df3.loc[index3, df3.columns[0]]
dfo.loc[index4, 'C2'] = df4.loc[index4, df4.columns[1]]
dfo.loc[index5, 'C2'] = df5.loc[index5, df5.columns[1]]
dfo.loc[index6, 'C2'] = df6.loc[index6, df6.columns[0]]
dfo['C3'] = ''
dfo.loc[index1, 'C3'] = df1.loc[index1, df1.columns[2]]
dfo.loc[index2, 'C3'] = df2.loc[index2, df2.columns[2]]
dfo.loc[index3, 'C3'] = df3.loc[index3, df3.columns[1]]
dfo.loc[index4, 'C3'] = df4.loc[index4, df4.columns[2]]
dfo.loc[index5, 'C3'] = df5.loc[index5, df5.columns[2]]
dfo.loc[index6, 'C3'] = df6.loc[index6, df6.columns[1]]

# numeric: 21/22/23 have two more columns than 9/10/11. From the
# distributions, making a guess that the first 7 and last 5 match
# up, and thus columns N8 and N9 are thus the extra ones. Keep
# those values for 9/10/11 empty for now.
df1 = loadboth('numeric', 'S9')
df2 = loadboth('numeric', 'S10')
df3 = loadboth('numeric', 'S11')
df4 = loadboth('numeric', 'S21')
df5 = loadboth('numeric', 'S22')
df6 = loadboth('numeric', 'S23')
for i in range(7):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i]]
	dfo.loc[index2, 'N' + str(i+1)] = df2.loc[index2, df2.columns[i]]
	dfo.loc[index3, 'N' + str(i+1)] = df3.loc[index3, df3.columns[i]]
	dfo.loc[index4, 'N' + str(i+1)] = df4.loc[index4, df4.columns[i]]
	dfo.loc[index5, 'N' + str(i+1)] = df5.loc[index5, df5.columns[i]]
	dfo.loc[index6, 'N' + str(i+1)] = df6.loc[index6, df6.columns[i]]
for i in [7, 8]:
	dfo['N' + str(i+1)] = ''
	dfo.loc[index4, 'N' + str(i+1)] = df4.loc[index4, df4.columns[i]]
	dfo.loc[index5, 'N' + str(i+1)] = df5.loc[index5, df5.columns[i]]
	dfo.loc[index6, 'N' + str(i+1)] = df6.loc[index6, df6.columns[i]]
for i in range(9, 14):
	dfo['N' + str(i+1)] = ''
	dfo.loc[index1, 'N' + str(i+1)] = df1.loc[index1, df1.columns[i-2]]
	dfo.loc[index2, 'N' + str(i+1)] = df2.loc[index2, df2.columns[i-2]]
	dfo.loc[index3, 'N' + str(i+1)] = df3.loc[index3, df3.columns[i-2]]
	dfo.loc[index4, 'N' + str(i+1)] = df4.loc[index4, df4.columns[i]]
	dfo.loc[index5, 'N' + str(i+1)] = df5.loc[index5, df5.columns[i]]
	dfo.loc[index6, 'N' + str(i+1)] = df6.loc[index6, df6.columns[i]]

dfo.to_csv('../byop/all_A7.csv')
