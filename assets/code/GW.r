# AUTHOR : IENG KIT NICHOLAS, HO 
# DATE : MARCH 2017
#########################################################################################

# INITIALIZATION

# Please install the appropriate packages before running this program

library(foreach)
library(doParallel)
cl <- makeCluster(detectCores() - 1)
registerDoParallel(cl)
setwd("")
rw <- read.csv(file="",header=FALSE,sep=",");
p <- sweep(rw,1,rowSums(rw),'/')
p <- matrix(unlist(p), ncol = length(p), nrow = length(p), byrow = FALSE)
ver <- c(names(rw))
ver <- matrix(unlist(ver), ncol = length(names(rw)), nrow = 1, byrow = FALSE)
allVer <- ver[1,]
inc <- function(x){eval.parent(substitute(x <- x + 1))}
index <- 0; dist <- c()

#########################################################################################

# IMPLEMENTATION

# The graph walk algorithm :

graphwalk <- function(from, to, number_of_random_walks, threshold) {
	verFrom <- ver[1,from];verTo <- ver[1,to];pFrom <- p[from,]
	for (j in 1:number_of_random_walks) {	
		counter <- matrix(c(rep(0,length(ver))), ncol = length(ver), nrow = 1, byrow = FALSE)
		v <- sample(allVer, 1, FALSE, pFrom)
		index <- match(v, allVer)
        inc(counter[1,index])
		if (v == verTo) {
			ifelse((v == verFrom), dist <- c(dist,0), dist <- c(dist,1))
			next}
		else if ((p[from,index] == 1)&(!(v == verTo))) {
			dist <- c(dist, NA)
			break} 
		for (i in 1:threshold) { 
				if (v == ver[1,index]) {
					inc(counter[1,index])
					v <- sample(allVer, 1, FALSE, p[index,])
					index <- match(v, allVer)
					inc(counter[1,index])
					if (v == verTo) {
						dist <- c(dist,sum(counter))
						break}}
					else if ((i == threshold) & (!(v == verTo))) {
						dist <- c(dist,NA)}}}
	dist<-na.omit(dist)
	if (length(dist) > 0) {
		dist <- matrix(unlist(dist), ncol = length(dist), nrow = 1, byrow = FALSE)
		sol <- sum(dist)/length(dist) }
	else sol <- NA 
	return(sol)}

#########################################################################################

# COMPUTATION

# Nested for loop version

nr = length(rw)

# The maximum traversal distance allowed for v_i to find v_j
# This value should be set high enough to gurantee convergence (but will increase computation time)
# For large_g.csv set this value to be at least 3000 to ensure coverage
# For small_g.csv set this value to be at least 700 to ensure coverage
th = 1000

result.mat <- matrix(c(rep(0, nr^2)), nrow=nr, ncol=nr, byrow=TRUE)

# Number of random walks for each pair of vertices must be at least 1000 times by default
nw = 1000

system.time({
for (i in 1:nr){
	for (k in 1:nr){
		result.mat[i,k] <- graphwalk(i,k,nw,th)}}})

#########################################################################################

# Parallel Version - This is a faster version

system.time({
foreach(i=1:nr) %:% 
	foreach (k=1:nr)  %do% {
    	result.mat[i,k] <- graphwalk(i,k,nw,th)} })

#########################################################################################

# DATA EXPORTATION

# Write data to csv

write.csv(result_mat, file = "")
