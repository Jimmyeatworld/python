
__author__ = 'Rodionov Dmitriy'

print("FOR")

S = str(input("vvedite chislo "))

B = len(S)

i = 0

for i in range(B):
    print(S[i])
    i += 1

print("WHILE")

i = 0

while i < B:
    print(S[i])
    i += 1