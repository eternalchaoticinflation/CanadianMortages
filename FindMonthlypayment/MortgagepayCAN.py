def CanadianMortgage(annualInterestRate, balance, years):
    
    #annualInterestRate=0.02
    #balance=385000
    degree=(years*(52/2.0)-1)
    #will use converging geomentric series. b*I-(series descending (I^12)P), increment
    #though P
    def ConSerNPI(n,p,i):
        '''
        this function gives return of decending geo series, I^m(P), with decreasing m
        m=highest degree
        creates a polynomial of degree n
        '''
        latch=0
        m=0;
        while m<=n:#  i is the "interest"
            
            latch=latch+p*(i**m);
            #print(p)
            m=m+1;
        return latch;
    #print(str(ConSerNPI(4,7,3)));
    
    #balance = 4773;
    #annualInterestRate = 0.2;
    Expo=((1.0+(annualInterestRate/2.0))**2.0)**(1.0/26);
    print Expo
    #http://www.yorku.ca/amarshal/mortgage.htm
    #degree=12*20-1;
    FinalPay=balance*(Expo**degree); #12 payments degree 11
    Step=1; err=0.01; p=0;match=0; #payment degree of 10
    '''
    FinalPay=balance*(Expo**11); #12 payments degree 11
 
p=0;
match=0; 
degree=11;#payment degree of 10

L=(balance/12); # lowest is no interest, balance over 12 payments
U=(FinalPay/12)

while abs(match-FinalPay)>0.05:
    p=(L+U)/2;
    match=ConSerNPI(degree,p,Expo);
    if match<FinalPay:#the midpoint is too low, so the midpoint is the new low
        L=p; #mid is the new low
    else:
        U=p;#too high
    print (str(match))
'''
    
    while match<FinalPay:
        match=ConSerNPI(degree,p,Expo);
        if match<FinalPay:
            p=p+Step;
        else:
            break
        #print (str(match))
    #trying to find root of positve polynomial degree m.
    #print ('FinalPay is: '+str(FinalPay))
    #print ('Match polynomial is: '+str(match))
    BiWpay='Lowest Payment: '+str(p)
    return BiWpay;

def CanInterestLoop(n):
    n=True;
    Choice=raw_input('Enter E to end, or anykey to continue...  ');
    if Choice=='E':
        
        return '';
    else:
    
        InList=['interest', 'balance', 'years'];
        varDict={'interest':0, 'balance':0, 'years':0}
        for item in InList:
            varDict[item]=raw_input('Enter ' +item+ ' : ');
        #print varDict['interest'];
        #print type(varDict['years'])
    
        print CanadianMortgage(float(varDict['interest']), float(varDict['balance']), float(varDict['years']));
        return CanInterestLoop(True);
CanInterestLoop(True);