© Nicholas Ieng Kit Ho, 2016. All rights reserved. Cannot be copied, re-used, or edited

gibbs <- function(n) {
sA <- c(1); sC <- c(1); sD <- c(1); sS <- c("NA")
dfi <- data.frame("A" = sA, "C" = sC, "D" = sD, "Sampled" = sS);
AB <- c(5,10); AD <- c(100, 1, 1, 100); CB <- c(1, 100); CD <- c(1, 100, 100, 1); DA <- c(100, 1, 1, 100); DC <- c(1, 100, 100, 1);
for (i in 1:n) {
	p0 <- 0; p1 <- 0;
	X <- sample(c("A", "C", "D"), 1, prob=c(1/3, 1/3, 1/3), replace = T);
	if (X == "A") { 
		dval <- sD[i];
		if (dval == 0) {
			p0 <- ((AB[1]*AD[1])/(AB[1]*AD[1]+AB[2]*AD[2]));
			p1 <- 1 - p0; }
		else {
			p0 <- ((AB[1]*AD[3])/(AB[1]*AD[3]+AB[2]*AD[4]));
			p1 <- 1 - p0; } 
	sA[i+1] <- sample(c(0,1), 1, prob = c(p0, p1), replace = T);
	sC[i+1] <- sC[i];
	sD[i+1] <- sD[i];
	sS[i+1] <- X;}
	else if (X == "D") {
		aval <- sA[i]; cval <- sC[i];
		if ( (aval == 1) && (cval == 1) ) {
			p0 <- ((DA[3]*DC[3])/(DA[3]*DC[3]+DA[4]*DC[4]));
			p1 <- 1 - p0; }
		else if ( (aval == 1) && (cval == 0) ) { 
			p0 <- ((DA[3]*DC[1])/(DA[3]*DC[1]+DA[4]*DC[2]));
			p1 <- 1 - p0; }
		else if ( (aval == 0) && (cval == 1) ) { 
			p0 <- ((DA[1]*DC[2])/(DA[1]*DC[3]+DA[2]*DC[4]));
			p1 <- 1 - p0; }
		else { p0 <- ((DA[3]*DC[3])/(DA[1]*DC[1]+DA[2]*DC[2]));
			p1 <- 1 - p0; } 
	sD[i+1] <- sample(c(0,1), 1, prob = c(p0, p1), replace = T);
	sC[i+1] <- sC[i];
	sA[i+1] <- sA[i];
	sS[i+1] <- X;}
	else {
		dval <- sD[i];
		if (dval == 0) {
			p0 <- ((CB[1]*CD[1])/(CB[1]*CD[1]+CB[2]*CD[2]));
			p1 <- 1 - p0; }
		else {
			p0 <- ((CB[1]*CD[3])/(CB[1]*CD[3]+CB[2]*CD[4]));
			p1 <- 1 - p0; }
	sC[i+1] <- sample(c(0,1), 1, prob = c(p0, p1), replace = T);
	sD[i+1] <- sD[i];
	sA[i+1] <- sA[i];
	sS[i+1] <- X;} }
dfi <- data.frame("A" = sA, "C" = sC, "D" = sD, "Sampled" = sS);
prob <- (sum(sA)/(n+1))
print(dfi)
print(prob)
return(prob)
}

N <- 10;
Probability <- c();
for (i in 1:N) {
Probability[i] <- gibbs(i)
}
Sample_Size <- seq(1, N)
plot(Sample_Size,Probability,type="l", col= "blue", xlim=c(0, N), ylim=c(0, 1))
lines(Sample_Size, rep(0.056589, N),col="red")
