from math import sqrt

A=input("Saisir A :")
V=float(2.5)
N=int(0)
A_PlusPetit=True

while A_PlusPetit==True :
    if V<A :
        V=sqrt(1+(V**2))
        N+=1
    else :
        print ("N={}".format(N))
        A_PlusPetit = False