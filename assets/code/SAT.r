© Nicholas Ieng Kit Ho, 2016. All rights reserved. Cannot be copied, re-used, or edited

# CHOOSE NUMBER OF RUNS
runs <- 50;
fres <- c();
6
for (g in 1:runs) {
# INITIALIZE
flips <- c();
# CHOOSE NUMBER OF MAXFLIPS
maxflips = 100;
# FIXED N
N <- 20;
# CHOOSE NUMBER OF CLAUSES
C <- 20;
var <- c(seq(1, N));
notvar <- c(seq(-1, -N));
prob <- 1/(2*N);
var <- as.character(var);
notvar <- as.character(notvar);
allvar <- c(var, notvar);
val0 <- sample(c(0,1), length(var), c(1/2, 1/2), replace = T);
notvv <- abs(val0-1);
df0 <- data.frame(var, val0);
df01 <- data.frame(notvar, notvv);
names(df01) <- (names(df0));
dff <- rbind(df0, df01);
dff <- dff[sample(nrow(dff), C*3, replace=T),];
dff <- c(dff); dff <- as.data.frame(dff);
oe <- c();
e <- c();
res <- c();
for (i in seq(1, C*3, 3)) {
if ( (sum(as.numeric(dff$val0[i:(i+2)]))) >= 1) {
print("yes")
res[i] <- 1;}
else {print("no"); res[i] <- 0; print(dff$var[i:(i+2)]);
e <- append(e, as.numeric(as.vector((dff$var[i:(i+2)])))) }}
e
res <- as.vector(na.omit(res));
if ( sum(res) == C ) { x <- 1 } else {x <- 0}
7
if ( x == 1 ) {print("SATISFIED")
flips <- NA;
fres[g] <- flips;}
else {
# PERMUTE CLAUSES
sum(res)
mat <- matrix(e, nrow = (length(e)/3), ncol = 3, byrow = T)
mat <- as.data.frame(mat)
mat <- na.omit(mat[,sample(ncol(mat), ncol(mat), replace = F)])
mat <- mat[sample(nrow(mat), (length(e)/3), prob = c(rep((1/(nrow(mat))), nrow(mat))) ,replace =
F), ]
mat2 <- split(mat, seq(nrow(mat)))
matlist <- c()
for ( i in 1:nrow(mat) ) { matlist <- append(matlist, as.numeric(unlist(mat2[i])) ) }
e <- matlist
oe <- e
odff <- dff
s <- 0;
s1 <- 0;
inc <- function(x){eval.parent(substitute(x <- x + 1))}
e
# FIRST FLIP
for ( k in 1:1 ) {
e <- oe;
dff <- odff;
for ( i in 1:nrow(dff) ) {
if ( e[k] == as.numeric(as.vector(dff$var[i])) ) {
dff$val0[i] <- as.numeric(1);}
if ( (-e[k]) == as.numeric(as.vector(dff$var[i])) ) {
dff$val0[i] <- as.numeric(0);}}
res <- c()
for (i in seq(1, C*3, 3)) {
if ( (sum(as.numeric(dff$val0[i:(i+2)]))) >= 1) {
res[i] <- 1;}
else {res[i] <- 0;
e <- as.numeric(as.vector((dff$var[i:(i+2)]))) }}
res <- as.vector(na.omit(res));
if ( sum(res) == C ) { x <- 1 } else {x <- 0}
if ( x == 1 ) {print("SATISFIED")
inc(s1); flips <- append(flips, 1) }
8
else {print("UNSATISFIED")
flips <- append(flips, 1) }
if ( s1 == 1 ){
flips <- sum(flips)
print(sum(flips))
fres[g] <- flips;
break;
}}
############################# DO ADDITIONAL FLIPS
########################################
if (s1 != 1) {
for ( h in 1:(maxflips-1) ) {
sum(res)
mat <- matrix(e, nrow = (length(e)/3), ncol = 3, byrow = T)
mat <- as.data.frame(mat)
mat <- na.omit(mat[,sample(ncol(mat), ncol(mat), replace = F)])
mat <- mat[sample(nrow(mat), (length(e)/3), prob = c(rep((1/(nrow(mat))), nrow(mat)))
,replace = F), ]
mat2 <- split(mat, seq(nrow(mat)))
matlist <- c()
for ( i in 1:nrow(mat) ) { matlist <- append(matlist, as.numeric(unlist(mat2[i])) ) }
e <- matlist
oe <- e
odff <- dff
s <- 0;
inc <- function(x){eval.parent(substitute(x <- x + 1))}
e
for ( k in 1:1 ) {
e <- oe;
dff <- odff;
for ( i in 1:nrow(dff) ) {
if ( e[k] == as.numeric(as.vector(dff$var[i])) ) {
dff$val0[i] <- as.numeric(1);}
if ( (-e[k]) == as.numeric(as.vector(dff$var[i])) ) {
dff$val0[i] <- as.numeric(0);}}
res <- c()
for (i in seq(1, C*3, 3)) {
if ( (sum(as.numeric(dff$val0[i:(i+2)]))) >= 1) { res[i] <- 1; }
else {res[i] <- 0;
e <- as.numeric(as.vector((dff$var[i:(i+2)]))) }}
res <- as.vector(na.omit(res));
9
if ( sum(res) == C ) { x <- 1 } else {x <- 0}
if ( x == 1 ) {print("SATISFIED")
inc(s); flips <- append(flips, 1) }
else {print("UNSATISFIED")
flips <- append(flips, 1) }}
if ( s == 1 ){
flips <- sum(flips)
print(sum(flips))
fres[g] <- flips;
break;}
else if ( h == (maxflips - 1) ) {
flips <- NA;
fres[g] <- flips;} } } } }
