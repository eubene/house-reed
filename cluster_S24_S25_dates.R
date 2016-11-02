
s24.dist <- read.csv('../S24_dist.csv', header=FALSE)
hc <- hclust(as.dist(s24.dist), method='complete')
plot(hc)
