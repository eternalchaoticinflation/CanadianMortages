Calcuates the monthly payment for Canadian Mortages.
compounds biweekly
Uses a descending geometric series, I^m(P), with decreasing m
creates a polynomial of degree n with inputs (degree, paymentinstallments, expo), m elements, n is the heighest degree.

descending geometric series simulates paymentinstallments.

to trial to try payments until, descending geometric series matches the total payment needed

the
CanMortgageBisection uses bisection search to increment the payments tried.
using: 

{ L=(balance/(degree+1));
    U=(FinalPay/(degree+1));
    while abs(match-FinalPay)>0.005:
        p=(L+U)/2.0;
        match=ConSerNPI(degree,p,Expo);
        if match<FinalPay:#the midpoint is too low, so the midpoint is the new low
            L=p; #mid is the new low
        else:
            U=p;#too high
        #print (str(match))
}
************************************************
However, MortgagepayCAN increments by Step size of $1.