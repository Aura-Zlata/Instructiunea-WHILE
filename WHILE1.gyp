"""
Se introduc succesiv numere nenule până la introducerea numărului 0. 
Să se afişeze suma tuturor numerelor introduse. 
Exemplu: Date de intrare   3  5  4  2  0  Date de ieşire 14.
"""

n=eval(input('Introduceti un numar:'))
s=0
while n!=0:
    s+=n
    n=eval(input('Introduceti un numar:'))

print('Suma numerelor este:',s)
