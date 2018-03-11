p = int(input("entrer p : "))
q = int(input("entrer q : "))
e = int(input("entrer e : "))

n = p * q

test = 0

PGCD1 = 0

phi = (p-1)*(q-1)

d = 0

while test == 0 :
    if (( e * d % phi == 1) and (p < d) and (q < d) and (d < phi)):
        test = 1
    d = d + 1
d = d - 1

print("cle de decryptage : n= ",n," d= ",d)

s = input('\nEntrez la liste à déchiffrer : ')
code = list(map(int, s.split()))

i = 0
message = ""
while i < len(code) :
    lettre_crypt = code[i]
    ascii = pow(lettre_crypt,d)%n
    message = message + str(ascii)
print("message décrypté : ",message)

input('\n\nFin\n\n')
