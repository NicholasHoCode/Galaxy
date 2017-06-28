© Nicholas Ieng Kit Ho, 2016. All rights reserved. Cannot be copied, re-used, or edited

#PROBABILITY ESTIMATION ALGORITHM FOR REJECTION SAMPLING
options(max.print=100000)
dat <- read.table("rs_1.csv")
dat <- as.matrix(dat)
4
bigN <- nrow(dat)
pa <- c()
pa[1] = 0
n2 <- 0; n1 <- 0;
accepted <- c()
inc <- function(x)
{
 eval.parent(substitute(x <- x + 1))
}
N <- bigN
for (i in 1:N) {
pa[1] = 0
accepted[1] = 0
if (i != N) {
 p <- 0; t <- 0; pr <- 0; x<-0
 for (j in i:i+1) {
if (dat[j] == 1) {
inc(p)
n1= p + n1
}
if (dat[j] == 2) {
inc(x)
n2 = x+n2
}}
t = i+1
pr <- n1/(n1+n2)
pa[t] <- pr

# ERROR BOUNDS WITH HOEFFDING INEQUALITY
accepted[t] <- n1+n2}
pa <- as.matrix(pa)
accepted <- as.vector(accepted)}
epsilon <- c()
epsilon <- sqrt((log(2/0.05)/accepted)/2)
epsilon[1] <- 0
lower <- c(); upper <- c();
upper <- as.vector(pa) + epsilon
lower <- as.vector(pa) - epsilon
y <- as.vector(pa)
5
x<-as.vector(log10(seq(0, N-1)))
plot(x,y, xlab = "log10(x)", ylab = "Probability", ylim=c(0,1))
lines(x, upper, lty = 'dashed', col = 'red')
lines(x, lower, lty = 'dashed', col = 'red')
k = 0;
for (i in 1:100000) {
if(dat[i] == 2) {
k = k + 1;}}

#PROBABILITY ESTIMATION ALGORITHM FOR LIKELIHOOD WEIGHTING
options(max.print=1000000)
dat <- read.table("lw_1.csv", header = TRUE, sep = ",")
e <- as.vector(dat[,2])
o <- as.vector(dat[,1])
bigN <- nrow(dat)
pa <- c()
pa[1] = 0
N = bigN;
weight1 = 0; weight2 = 0.450;
weighttotal = 0;
for (i in 1:N) {
pa[1] = 0
if (i != N) {
p = 0; t = 0; pr = 0; x = 0;
for (j in i:i+1) {
if (o[j] == 1) {
weight1 = e[j] + weight1}
if (o[j] == 2) {
weight2 = e[j] + weight2}}
t = i + 1;
weighttotal = weight1+weight2
pr = weight1 / weighttotal
pa[t] = pr;}
pa <- as.matrix(pa)}
y <- as.vector(pa)
x<-as.vector(log10(seq(0, N-1)))
6
plot(x,y, xlab = "log10(x)", ylab = "Probability", ylim=c(0,1))
