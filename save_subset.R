# saves a random subset of the training data to explore more easily
# with equal amounts of Response == 0 and Response == 1

setwd("C:/Users/emotoyam/Desktop/Kaggle")
train.numeric <- read.csv('train_numeric.csv')

train.response <- train.numeric[,c("Id", "Response")]
table(train.response$Response)
# result:
# 0       1 
# 1176868    6879
# Response == 1 only makes up a tiny fraction

# take all of Response == 1 and an equal-size subset of Response == 0
set.seed(777)
id.r0.subset <- sample(train.response[train.response$Response == 0, "Id"], 6879)
id.r1.all <- train.response[train.response$Response == 1, "Id"]
id.subset <- sort(union(id.r0.subset, id.r1.all))

# join numeric, categorical, and date for the subset of Ids we chose
train.subset <- train.numeric[train.numeric$Id %in% id.subset,]
rm(train.numeric)
train.categorical <- read.csv('train_categorical.csv')
train.subset <- merge(train.subset, train.categorical, by = "Id")
rm(train.categorical)
train.date <- read.csv('train_date.csv')
train.subset <- merge(train.subset, train.date, by = "Id")
rm(train.date)
write.csv(train.subset, 'train_subset.csv')
