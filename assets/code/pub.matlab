© Ieng Kit Ho, 2016. All rights reserved. Cannot be copied, re-used, or edited

% SAMPLE CODE

%Guass Stieltjes procedure for computing recurrence coefficients
% alpha and beta for weight function w(x)=x*x*exp(-x*x)
format long e
%nint=# of intervals; npts=# of pts per interval [xmin,xmax]
pwmd = mdquad(nint,npts,xmin,xmax); ntot=nint*npts;
%multi-domain matrix of quad pts p and wts w:
%weight function w(x)=x*x*exp(-x*x)
p=pwmd(:,1); w=pwmd(:,2); psq=p.*p; wtfcn=psq.*exp(-psq);
b0=ones(ntot,1);
%First two integrals
s1=sum(w.*wtfcn); s2=sum(w.*(p.*wtfcn));
h(1)=s1; alfa(1)=s2/s1; beta(1)=0;k=1;
%Norm and alpha_1 and betta_1
myfile = fopen('abmaxp22.dat', 'wt');
fprintf(myfile,'%20.12f %20.12f\n',alfa(k),beta(k));
%Polynomial P_1(x)
b1=p-alfa(1);
%Next two integrals
s1=sum(w.*(wtfcn.*(b1.^2))); s2=sum(w.*(p.*(wtfcn.*(b1.^2))));
alfa(2)=s2/s1; h(2)=s1; beta(2)=h(2)/h(1);k=2;
%alpha_2, norm and betta_2
fprintf(myfile,'%20.12f %20.12f\n',alfa(k),beta(k));
for k=3:m
pma=p-alfa(k-1);
%Recurrence for the next polynomial
b2=pma.*b1-beta(k-1)*b0;
s1=sum(w.*(wtfcn.*(b2.^2)));
s2=sum(w.*(p.*(wtfcn.*(b2.^2))));
alfa(k)=s2/s1; h(k)=s1; beta(k)=h(k)/h(k-1);
%alfa_kl, norm and betta_k
fprintf(myfile,'%20.12f %20.12f\n',alfa(k),beta(k));
b0=b1; b1=b2;
end
toc