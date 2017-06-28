Nicholas Ieng Kit Ho, 2016. All rights reserved. Cannot be copied, re-used, or edited

#METHOD 1 - Tree-based Classifier: Recursive Partitioning

library(rpart)
url <- "http://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
# read data
mushrooms <- read.table(file=url, header=F, sep=",")
set.seed(120)
# split data into train and test
ind = sample(2,nrow(mushrooms), replace=T, prob=c(0.7,0.3))
train.mushrooms = mushrooms[ind==1,]
test.mushrooms = mushrooms[ind==2,]
# set control parameter
myc <- rpart.control(minsplit=3,cp=1e-8)
# fit the model
tree <- rpart(V1~., data=train.mushrooms, method="class")
cpt <- tree$cptable[which.min(tree$cptable[,"xerror"]),"CP"]
# prune tree
ptree <- prune(tree, cp=cpt)
# determine the estimated future misclassification rate 
pred.ptree <- predict(ptree, newdata=test.mushrooms[,-1], type='class')
tab <- table(as.vector(test.mushrooms$V1),as.vector(pred.ptree))
fmr.rpart <- sum(tab[row(tab)!=col(tab)])/sum(tab)
fmr.rpart

set.seed(121)

#METHOD 2 - Classification Tree

require(tree)
train.dat <- train.mushrooms
train.dat$V1 <- as.factor(train.dat$V1)
tree2 <- tree(V1~., data = train.dat)
test.dat <- test.mushrooms
test.dat$V1 <- as.factor(test.dat$V1)  
pred.tree2 <- predict(tree2, newdata=test.dat[,-1], type ='class') 
tab2<-table(as.vector(test.dat$V1),as.vector(pred.tree2))
fmr.tree <- sum(tab2[row(tab2) != col(tab2)]) / sum(tab2)
fmr.tree

set.seed(122)

# METHOD 1 - Ensemble: Bagging

library(adabag)
mushrooms.bagging <- bagging(V1~.,data=train.mushrooms,mfinal=100)
mushrooms.predbagging <- predict.bagging(mushrooms.bagging, newdata=test.mushrooms[,-1])
mushrooms.predbagging <- as.factor(mushrooms.predbagging$class)
mushrooms.predbagging <- as.factor(mushrooms.predbagging)
# estimate future misclassfication rate
tab.bag<-table(as.vector(test.mushrooms$V1),as.vector(mushrooms.predbagging))
fmr.bag <- sum(tab.bag[row(tab.bag) != col(tab.bag)]) / sum(tab.bag)
fmr.bag

set.seed(123)
library(adabag)
library(rpart)

# METHOD 2 - Ensemble: Boosting (AdaBoost)
mushrooms.boosting <- boosting(V1~.,data=train.mushrooms)
mushrooms.predboosting <- predict.boosting(mushrooms.boosting, newdata=test.mushrooms[,-1])
mushrooms.predboosting <- mushrooms.predboosting$class
mushrooms.predboosting <- as.factor(mushrooms.predboosting)
# estimate future misclassification rate
tab.boosting <-table(as.vector(test.mushrooms$V1),as.vector(mushrooms.predboosting))
fmr.boosting <- sum(tab.boosting[row(tab.boosting) != col(tab.boosting)]) / sum(tab.boosting)
fmr.boosting
