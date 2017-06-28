© Nicholas Ieng Kit Ho, 2016. All rights reserved. Cannot be copied, re-used, or edited

k <- 5
set.seed(17)
N <- 50
mspe.f <- mspe.st <- rep(0, N)
pr.f <- pr.st <- rep(0, n)
for(i in 1:N) {
#sdat<-sample(dat)
sdat<-dat
# divide dat into k folds in random order for each run
folds <- sample(cut(seq(1,nrow(sdat)),breaks=k,labels=FALSE))
  for(j in 1:k) {
    # divide train into k folds
    index <- which(folds==j,arr.ind=TRUE)
    #train using dat not in fold j
    train <- sdat[-index,]
    tmp.st <- update(step.lm, data=train)
    tmp.f <- update(full, data=train)
    #test in fold j
    test <- sdat[index,]
    pr.st[folds==j] <- predict(tmp.st, newdata=test)
    pr.f[folds==j] <- predict(tmp.f, newdata=test)
  }