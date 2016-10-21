
train.subset <- read.csv('train_subset.csv')

isdatename <- sapply(names(train.subset), function(s) substr(strsplit(s, "_")[[1]][3], 1, 1)) == "D"
datenames <- names(train.subset)[!is.na(isdatename) | isdatename]
r <- stack(train.subset[1, datenames])
r <- r[!is.na(r$values),]
View(r)
