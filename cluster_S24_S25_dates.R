
s24.dist <- read.csv('../S24_dist.csv', header=FALSE)
hc24 <- hclust(as.dist(s24.dist), method='complete')

s25.dist <- read.csv('../S25_dist.csv', header=FALSE)
hc25 <- hclust(as.dist(s25.dist), method='complete')

plot(hc24)
hc24.clusters <- cutree(hc24, 16)

plot(hc25)
hc25.clusters <- cutree(hc25, 17)
