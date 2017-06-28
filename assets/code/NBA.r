© Nicholas Ieng Kit Ho, 2016. All rights reserved. Cannot be copied, re-used, or edited

# SAMPLE CODE

options(na.action=na.omit)
dat <-read.table("dataset.txt", header=T)
previous10.home = (dat$X1points + dat$X2points + dat$X3points + dat$X4points + dat$X5points + dat$X6points + dat$X7points + dat$X8points + dat$X9points + dat$X10points)/10
previous10.away = (dat$o1points + dat$o2points + dat$o3points + dat$o4points + dat$o5points + dat$o6points + dat$o7points + dat$o8points + dat$o9points + dat$o10points)/10

dat$previous10.home <- previous10.home;
dat$previous10.away <- previous10.away;

# remove columns that are not needed
dat$game = NULL
dat$team = NULL

png("scatterplots1.png", width=1920, height=1920)
par(mfrow=c(3,3))

plot(points ~ X1points, data=dat, xlab="Previous 1 Game Points", ylab="Points", pch=20)
abline(lm(points ~ X1points, data=dat), col="red")

plot(points ~ X2points, data=dat, xlab="Previous 2 Game Points", ylab="Points", pch=20)
abline(lm(points ~ X2points, data=dat), col="red")

plot(points ~ X3points, data=dat, xlab="Previous 3 Game Points", ylab="Points", pch=20)
abline(lm(points ~ X3points, data=dat), col="red")

plot(points ~ X4points, data=dat, xlab="Previous 4 Game Points", ylab="Points", pch=20)
abline(lm(points ~ X4points, data=dat), col="red")

plot(points ~ X5points, data=dat, xlab="Previous 5 Game Points", ylab="Points", pch=20)
abline(lm(points ~ X5points, data=dat), col="red")

plot(points ~ X6points, data=dat, xlab="Previous 6 Game Points", ylab="Points", pch=20)
abline(lm(points ~ X6points, data=dat), col="red")

plot(points ~ X7points, data=dat, xlab="Previous 7 Game Points", ylab="Points", pch=20)
abline(lm(points ~ X7points, data=dat), col="red")

plot(points ~ X8points, data=dat, xlab="Previous 8 Game Points", ylab="Points", pch=20)
abline(lm(points ~ X8points, data=dat), col="red")

plot(points ~ X9points, data=dat, xlab="Previous 9 Game Points", ylab="Points", pch=20)
abline(lm(points ~ X9points, data=dat), col="red")

dev.off()

png("scatterplots2.png", width=1920, height=1920)
par(mfrow=c(3,3))

plot(points ~ X10points, data=dat, xlab="Previous 10 Game Points", ylab="Points", pch=20)
abline(lm(points ~ X10points, data=dat), col="red")

plot(points ~ fieldgoalsattempted, data=dat, xlab="Field Goals Attempted", ylab="Points", pch=20)
abline(lm(points ~ fieldgoalsattempted, data=dat), col="red")

plot(points ~ fieldgoalsmade, data=dat, xlab="Field Goals Made", ylab="Points", pch=20)
abline(lm(points ~ fieldgoalsmade, data=dat), col="red")

plot(points ~ fouls, data=dat, xlab="fouls", ylab="Points", pch=20)
abline(lm(points ~ fouls, data=dat), col="red")

plot(points ~ ofouls, data=dat, xlab="ofouls", ylab="Points", pch=20)
abline(lm(points ~ ofouls, data=dat), col="red")

plot(points ~ freethrowsattempted, data=dat, xlab="Free Throws Attempted", ylab="Points", pch=20)
abline(lm(points ~ freethrowsattempted, data=dat), col="red")

plot(points ~ freethrowsmade, data=dat, xlab="Free Throws Made", ylab="Points", pch=20)
abline(lm(points ~ freethrowsmade, data=dat), col="red")

plot(points ~ threepointersattempted, data=dat, xlab="Three Pointers Attempted", ylab="Points", pch=20)
abline(lm(points ~ threepointersattempted, data=dat), col="red")

plot(points ~ threepointersmade, data=dat, xlab="Three Pointers Made", ylab="Points", pch=20)
abline(lm(points ~ threepointersmade, data=dat), col="red")

dev.off()

png("scatterplots3.png", width=1920, height=1920)
par(mfrow=c(3,3))

plot(points ~ wins, data=dat, xlab="Wins", ylab="Points", pch=20)
abline(lm(points ~ wins, data=dat), col="red")

plot(points ~ owins, data=dat, xlab="Opponents Wins", ylab="Points", pch=20)
abline(lm(points ~ owins, data=dat), col="red")

plot(points ~ opoints, data=dat, xlab="Opponents Points", ylab="Points", pch=20)
abline(lm(points ~ opoints, data=dat), col="red")

plot(points ~ o1points, data=dat, xlab="Previous 1 Game Opponents Points", ylab="Points", pch=20)
abline(lm(points ~ o1points, data=dat), col="red")

plot(points ~ o2points, data=dat, xlab="Previous 2 Game Opponents Points", ylab="Points", pch=20)
abline(lm(points ~ o2points, data=dat), col="red")

plot(points ~ o3points, data=dat, xlab="Previous 3 Game Opponents Points", ylab="Points", pch=20)
abline(lm(points ~ o3points, data=dat), col="red")

plot(points ~ o4points, data=dat, xlab="Previous 4 Game Opponents Points", ylab="Points", pch=20)
abline(lm(points ~ o4points, data=dat), col="red")

plot(points ~ o4points, data=dat, xlab="Previous 5 Game Opponents Points", ylab="Points", pch=20)
abline(lm(points ~ o4points, data=dat), col="red")

plot(points ~ o6points, data=dat, xlab="Previous 6 Game Opponents Points", ylab="Points", pch=20)
abline(lm(points ~ o6points, data=dat), col="red")

dev.off()

png("scatterplots4.png", width=1920, height=1920)
par(mfrow=c(3,3))

plot(points ~ o7points, data=dat, xlab="Previous 7 Game Opponents Points", ylab="Points", pch=20)
abline(lm(points ~ o7points, data=dat), col="red")

plot(points ~ o8points, data=dat, xlab="Previous 8 Game Opponents Points", ylab="Points", pch=20)
abline(lm(points ~ o8points, data=dat), col="red")

plot(points ~ o9points, data=dat, xlab="Previous 9 Game Opponents Points", ylab="Points", pch=20)
abline(lm(points ~ o9points, data=dat), col="red")

plot(points ~ o10points, data=dat, xlab="Previous 10 Game Opponents Points", ylab="Points", pch=20)
abline(lm(points ~ o10points, data=dat), col="red")

plot(points ~ site, data=dat, xlab="Home/Away", ylab="Points", pch=20)
abline(lm(points ~ site, data=dat), col="red")

plot(points ~ previous10.home, data=dat, xlab="Average Points in Previous 10 Games", ylab="Points", pch=20)
abline(lm(points ~ previous10.home, data=dat), col="red")

plot(points ~ previous10.away, data=dat, xlab="Average Points in Opponents Previous 10 Games", ylab="Points", pch=20)
abline(lm(points ~ previous10.away, data=dat), col="red")

plot(points ~ oteam, data=dat, xlab="Opposing Team", ylab="Points", pch=20)
abline(lm(points ~ oteam, data=dat), col="red")

dev.off()

library(car)

png("qqplots1.png", width=1920, height=1920)
par(mfrow=c(3,3))

qqPlot(lm(points ~X1points, data=dat), main="QQ Plot")
qqPlot(lm(points ~X4points, data=dat), main="QQ Plot")
qqPlot(lm(points ~X7points, data=dat), main="QQ Plot")
qqPlot(lm(points ~X10points, data=dat), main="QQ Plot")
qqPlot(lm(points ~fouls, data=dat), main="QQ Plot")
qqPlot(lm(points ~freethrowsmade, data=dat), main="QQ Plot")
qqPlot(lm(points ~wins, data=dat), main="QQ Plot")
qqPlot(lm(points ~opoints, data=dat), main="QQ Plot")
qqPlot(lm(points ~o3points, data=dat), main="QQ Plot")

dev.off()

png("qqplots2.png", width=1920, height=1920)
par(mfrow=c(3,3))

qqPlot(lm(points ~o6points, data=dat), main="QQ Plot")
qqPlot(lm(points ~o9points, data=dat), main="QQ Plot")
qqPlot(lm(points ~previous10.home, data=dat), main="QQ Plot")
qqPlot(lm(points ~X2points, data=dat), main="QQ Plot")    
qqPlot(lm(points ~X5points, data=dat), main="QQ Plot")
qqPlot(lm(points ~X8points, data=dat), main="QQ Plot")
qqPlot(lm(points ~fieldgoalsattempted, data=dat), main="QQ Plot")
qqPlot(lm(points ~ofouls, data=dat), main="QQ Plot")
qqPlot(lm(points ~site, data=dat), main="QQ Plot")

dev.off()

png("qqplots3.png", width=1920, height=1920)
par(mfrow=c(3,3))

qqPlot(lm(points ~threepointersattempted, data=dat), main="QQ Plot")
qqPlot(lm(points ~oteam, data=dat), main="QQ Plot")
qqPlot(lm(points ~o1points, data=dat), main="QQ Plot")
qqPlot(lm(points ~o4points, data=dat), main="QQ Plot")
qqPlot(lm(points ~o7points, data=dat), main="QQ Plot")
qqPlot(lm(points ~o10points, data=dat), main="QQ Plot")
qqPlot(lm(points ~previous10.away, data=dat), main="QQ Plot")
qqPlot(lm(points ~X3points, data=dat), main="QQ Plot")
qqPlot(lm(points ~X6points, data=dat), main="QQ Plot")

dev.off()

png("qqplots4.png", width=1920, height=1920)
par(mfrow=c(3,3))

qqPlot(lm(points ~X9points, data=dat), main="QQ Plot")
qqPlot(lm(points ~fieldgoalsmade, data=dat), main="QQ Plot")
qqPlot(lm(points ~freethrowsattempted, data=dat), main="QQ Plot")
qqPlot(lm(points ~threepointersmade, data=dat), main="QQ Plot")
qqPlot(lm(points ~owins, data=dat), main="QQ Plot")
qqPlot(lm(points ~o2points, data=dat), main="QQ Plot")
qqPlot(lm(points ~o5points, data=dat), main="QQ Plot")
qqPlot(lm(points ~o8points, data=dat), main="QQ Plot")

dev.off()


# Use leaps to find best model
library(leaps)

# TODO: need to exclude some variables
# https://cran.r-project.org/web/packages/leaps/leaps.pdf
# either define the variables that we want using x= or force out some variables
s1<- regsubsets(points~., data=dat, method="exhaustive", really.big=T)
ss1 <- summary(s1)

#This table can be accessed directly via
ss1$which
#where "TRUE" is in the place of "*"

#Get the adjusted R^2 of each model
ss1$adjr2
which.max(ss1$adjr2)
#Best model is with 6 variables according to adj-R^2

#Get the cp of each model
ss1$cp
which.min(ss1$cp)
#Best model is with 6 variables according to Cp

######################################
##Leave-one-out Cross validaion.
######################################

#Function to calculate the leave-one-out cross validation error.
ls.cvrmse <- function(ls.out)
# Compute the leave-one-out cross-validated root mean squared error of prediction.
# Handles missing values.
# ls.out is a fitted regression model from lsreg or lm.
# (c) Copyright William J. Welch 1997
{
  res.cv <- ls.out$residuals / (1.0 - ls.diag(ls.out)$hat)
  # Identify NA's and remove them.
  is.na.res <- is.na(res.cv)
  res.cv <- res.cv[!is.na.res]
  cvrmse <- sqrt(sum(res.cv^2) / length(res.cv))
  return(cvrmse)
}


#Compare the full model and best model found by regsubsets
dat2<-dat[,-35]
dat2 <-dat2[-35]
names(dat2)
fullModel <- lm(points~., data=dat2)
summary(fullModel)
#best model based on adjusted R^2
bestModeladj <- lm(points~fieldgoalsmade+freethrowsmade+threepointersmade, data=dat)
# best model based on Mallow's cp
bestModelcp <- lm(points~dat$X1points+X2points+X3points+X4points+X5points+fieldgoalsmade+freethrowsmade+threepointersmade, data=dat)
summary(bestModeladj)
summary(bestModelcp)

#Calculate the leave-one-out CV RMSE for the full model
fullModel.cvrmse <- ls.cvrmse(fullModel)

#Calculate the leave-one-out CV RMSE for the best models via regsubsets
bestModeladj.cvrmse <- ls.cvrmse(bestModeladj)
bestModelcp.cvrmse <- ls.cvrmse(bestModelcp)

print(c(fullModel.cvrmse, bestModeladj.cvrmse))
which.min(c(fullModel.cvrmse, bestModeladj.cvrmse))
print(c(fullModel.cvrmse, bestModelcp.cvrmse))
which.min(c(fullModel.cvrmse, bestModelcp.cvrmse))
which.min(c(bestModeladj.cvrmse, bestModelcp.cvrmse))
#The best model has smaller cvrmse
#Result : bestModeladj.cvrmse has a smaller cvrmse compare to fullModel
# bestModelcp.cvrmse has a smaller cvrmse compare to fullModel
# bestModeladj.cvrmse has the smallest cvrmse out of all three

library(hydroGOF)
actual <-c(70, 80, 81, 82, 83)
predF = predict(fullModel,interval = "prediction", se.fit = TRUE)
predR = predict(bestModeladj,interval = "prediction", se.fit = TRUE)
predC = predict(bestModelcp,interval = "prediction", se.fit = TRUE)
predRv <- c(predR$fit[1:5])
predFv <- c(predF$fit[1:5])
predCv <- c(predC$fit[1:5])
mseF = mse(predFv, actual)
mseR = mse(predRv,actual)
mseC = mse(predCv, actual)
mseF;mseR;mseC





