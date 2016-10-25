# Execute several instances of cut, where syntax is
# cut -f 1,4,5,6 -d ',' file.csv > newfile.csv

import numpy as np
import pandas as pd
from subprocess import call

indir = '../'
outdir = '../bystation/'
filelist = ['test_categorical.csv', 'test_date.csv', 'test_numeric.csv', 'train_categorical.csv', 'train_date.csv', 'train_numeric.csv']

for filename in filelist:
    # Read just the first line to get column names
    chunker = pd.read_csv(indir + filename, index_col='Id', chunksize=1)
    piece = chunker.__next__()

    # Each column name is like Lx_Sy_Dz; extract middle portion
    colstations = np.array([s.split('_')[1] for s in piece.columns])
    # Get the unique station names
    stations, icol = np.unique(np.array(colstations), return_index=True)
    # But get the original order back by sorting on icol
    stations = stations[np.argsort(icol)]

    for station in stations:
    	# list of column numbers
    	# need to add 2, since it starts from 1 and first column is 'Id'
    	collist = ','.join(np.char.mod('%d', np.where(colstations == station)[0] + 2))
    	newfile = filename.rsplit('.', 1)[0] + '_' + station + '.csv'
    	cmd = 'cut -f 1,' + collist + ' -d \',\' ' + indir + filename + ' > ' + outdir + newfile
    	print(cmd)
    	call(cmd, shell=True)
