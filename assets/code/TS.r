© Nicholas Ieng Kit Ho, 2016. All rights reserved. Cannot be copied, re-used, or edited

# SAMPLE CODE

data <- read.table("sp500futures.csv", header=T, sep=",")
x <- ts(rev(data$Price), frequency = 5, start = as.Date("2015-11-30"))
library(hydroGOF)
# Plot the original time series, acf, pacf
plot(x)
acf(x)
pacf(x)

Model 1:
# Fitting an ARIMA model with method “CSS”
ArimaModel2 <- arima(x, order = c(1,0,0), method = "CSS")
predict(ArimaModel2 , n.ahead = 4)
mse(c(2024.919, 2021.514, 2018.276, 2015.197), c(2047.5, 2055.25, 2051.5, 2065))
# Fitting an ARIMA model with method “ML”
ArimaModel3 <- arima(x, order = c(1,0,0), method = "ML")
predict(ArimaModel3 , n.ahead = 4)
library(forecast)
# Plot fitted model against the original series
plot(data$Price,col="red", type="l")
lines(fitted(ArimaModel1),col="blue")
# MSE for the model
mse(c(2028.499, 2028.497, 2028.496, 2028.494), c(2047.5, 2055.25, 2051.5, 2065))

Model 2:
#find and analyze the differenced time series
y <- diff(x)
acf(y); pacf(y)
#fit, observe and analyze the ARIMA model
m2 <- arima(x, order=c(0,1,0))
m2
tsdiag(m2)
#predict the next 4 values
predict(m2,4)

Model 3:
# SARIMA model fitting
sarima1 <- arima(x, order = c(3, 1, 0), seasonal = list(order = c(1, 0, 0)))
tsdiag(sarima1)
# Plot fitted model against the original series
plot(data$Price,col="red", type="l")
lines(fitted(sarima1 ),col="blue")
predict(sarima1 , n.ahead = 4)
# MSE for the model
mse(c(2025.779, 2027.103, 2027.392, 2025.798), c(2047.5, 2055.25, 2051.5, 2065))

Model 4:
# exponential smoothing
x.exp <- HoltWinters(x, beta=FALSE, gamma=FALSE)
plot(x.exp)
forecast(x.exp, n.ahead=4)
# MSE for the model
mse(c(2029.002, 2029.002, 2029.002, 2029.002), c(2047.5, 2055.25, 2051.5, 2065))

# Holt smoothing
x.holt <- HoltWinters(xt,gamma=FALSE)
plot(x.holt)
forecast(x.holt, n.ahead=4)
# MSE for the model
mse(c(2030.247, 2031.125, 2032.003, 2032.881), c(2047.5, 2055.25, 2051.5, 2065))

# Holt-Winters smoothing       
x.hw <- HoltWinters(x, seasonal="additive")
plot(x.hw)
forecast(x.hw, n.ahead=4)
# MSE for the model
mse(c(2028.127, 2031.852, 2039.724, 2045.399), c(2047.5, 2055.25, 2051.5, 2065))

Frequency domain:
# looking for the most important frequencies
x.spec <- spec.pgram(xt, log="no") 
x.spec$spec # reading the output for the biggest spectrum densities
dom_f1 <- 1/86; dom_f2 <- 2/86; dom_f3 <- 3/86; dom_f4 <- 5/86
wavelength1 <- 1/dom_f1; wavelength2 <- 1/dom_f2; wavelength3 <- 1/dom_f3; wavelength4 <- 1/dom_f4

# fitting a simple model for the most contributing frequency 1/86; other frequencies use similar commands
p1 <- 86 / wavelength1 # p is the number of cycles completed over the duration of the data
omega_p1 = (2 * pi * p1) # given by the formula (2*pi)/omega_p = N/p
t <- 1:86 
cs1 <- cos(omega_p1 * t) 
sn1 <- sin(omega_p1 * t) 
lma1 <- lm(xt ~ cs1 + sn1) 
summary(lma1)
plot(xt)
lines(lma1$coefficients[1] + lma1$coefficients[2]*cs1 + lma1$coefficients[3]*sn1, col='red', lty = 2) 

# white noise test
x.cumspec <- cumsum(x.spec$spec)/sum(x.spec$spec)
y <- x.spec$freq
plot(y, x.cumspec, type="l")
D <- max(abs(x.cumspec - 1:45/45)) # 0.8233388
D_c <- 1.358 / sqrt(43 - 1) # 0.2095439