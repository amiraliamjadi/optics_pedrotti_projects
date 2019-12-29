n= float(input('n(zarib shekast mohit avalie)='))
nL = float(input('n pre zarib shekast mohit adasi)='))
np = float(input('n3(zarib shekast mohit sanavie)='))
t = float(input('t(zekhamat adasi)='))
R1 = float(input('R1(shoa enhena aval)='))
R2 = float(input('R2(shoa enhena dovom)='))

A = t * ((n - nL) / (nL * R1)) + 1
B = (t * n) / nL
C = ((nL - np) / (np * R2)) - ((nL - n) / (np * R1)) - (((nL - np) * (nL - n) * t) / (np * nL * R1 * R2))
D = (n / np) + ((nL - np) * n * t) / (np * R2 * nL)

p = D/C
q = -(A/C)
r = (D - (n / np)) / C
s = (1-A)/C
v = (D-1)/C
w = ((n / np) - A) / C
f1 = n / (np * C)
f2 = -(1/C)


print("A = {0} , B = {1} , C = {2} , D = {3}".format(A, B, C, D))
print()
print('p=', p)
print('q=', q)
print('r=', r)
print('s=', s)
print('v=', v)
print('w=', w)
print('f1=', f1)
print('f2=', f2)

