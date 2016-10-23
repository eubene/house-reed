import numpy as np
import pandas as pd

df_train_pflow = pd.read_csv('../train_pflow.csv', index_col='Id')
df_test_pflow = pd.read_csv('../test_pflow.csv', index_col='Id')
df_all_pflow = pd.concat([df_train_pflow, df_test_pflow])

pflow_group = df_all_pflow.PFlow
pflow_group = pflow_group.str.replace('S0-','A1-')
pflow_group = pflow_group.str.replace('S1-','A2-')
pflow_group = pflow_group.str.replace('S2-','A3-')
pflow_group = pflow_group.str.replace('S3-','A3-')
pflow_group = pflow_group.str.replace('S4-','A4-')
pflow_group = pflow_group.str.replace('S5-','A4-')
pflow_group = pflow_group.str.replace('S6','A5')
pflow_group = pflow_group.str.replace('S7','A5')
pflow_group = pflow_group.str.replace('S8','A6')
pflow_group = pflow_group.str.replace('S9','A7')
pflow_group = pflow_group.str.replace('S10','A7')
pflow_group = pflow_group.str.replace('S11','A7')
pflow_group = pflow_group.str.replace('S12','A1')
pflow_group = pflow_group.str.replace('S13','A2')
pflow_group = pflow_group.str.replace('S14','A3')
pflow_group = pflow_group.str.replace('S15','A3')
pflow_group = pflow_group.str.replace('S16','A4')
pflow_group = pflow_group.str.replace('S17','A4')
pflow_group = pflow_group.str.replace('S18','A5')
pflow_group = pflow_group.str.replace('S19','A5')
pflow_group = pflow_group.str.replace('S24','M1')
pflow_group = pflow_group.str.replace('S25','M1')
pflow_group = pflow_group.str.replace('S26','M2')
pflow_group = pflow_group.str.replace('S27','M2')
pflow_group = pflow_group.str.replace('S28','M2')
pflow_group = pflow_group.str.replace('S20','A6')
pflow_group = pflow_group.str.replace('S21','A7')
pflow_group = pflow_group.str.replace('S22','A7')
pflow_group = pflow_group.str.replace('S23','A7')
pflow_group = pflow_group.str.replace('S29','Z1')
pflow_group = pflow_group.str.replace('S30','Z2')
pflow_group = pflow_group.str.replace('S31','ZE')
pflow_group = pflow_group.str.replace('S32','ZE')
pflow_group = pflow_group.str.replace('S33','Z3')
pflow_group = pflow_group.str.replace('S34','Z4')
pflow_group = pflow_group.str.replace('S35','Z5')
pflow_group = pflow_group.str.replace('S36','Z5')
pflow_group = pflow_group.str.replace('S37','Z6')
pflow_group = pflow_group.str.replace('S38','Z7')
pflow_group = pflow_group.str.replace('S39','Y1')
pflow_group = pflow_group.str.replace('S40','Y2')
pflow_group = pflow_group.str.replace('S41','Y3')
pflow_group = pflow_group.str.replace('S43','Y4')
pflow_group = pflow_group.str.replace('S44','Y4')
pflow_group = pflow_group.str.replace('S45','Y5')
pflow_group = pflow_group.str.replace('S47','Y6')
pflow_group = pflow_group.str.replace('S48','Y7')
pflow_group = pflow_group.str.replace('S49','Y8')
pflow_group = pflow_group.str.replace('S50','Y8')
pflow_group = pflow_group.str.replace('S51','Y9')

pflow_length = pflow_group.fillna('').str.count('-') + 1
pflow_length[pflow_group.isnull()] = 0

def route_from_group(s):
	if isinstance(s, float):
		r = ''
	else:
		r = ('A' if 'A' in s else '')
		r = r + ('Z' if 'Z' in s else '')
		r = r + ('Y' if 'Y' in s else '')
	return(r)
pflow_route = pflow_group.apply(route_from_group)
pflow_route[pflow_length < 4] = ''

df_all_pflow['PFlowGroup'] = pflow_group
df_all_pflow['PFlowLength'] = pflow_length
df_all_pflow['PFlowRoute'] = pflow_route

df_all_pflow.to_csv('../all_pflow.csv')
