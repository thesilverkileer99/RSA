import time

p = int(input("entrer p : "))
q = int(input("entrer q : "))
e = int(input("entrer e : "))

tmps1=time.time()

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
tmps2=time.time() - tmps1
print("Temps d'exécution = %f" %tmps2)
tmps1=time.time()
code = list(input('\nEntrez la liste à déchiffrer : ').split(','))


i = 0
message = ""
while i < len(code) :
    lettre_crypt = int(code[i])
    ascii = pow(lettre_crypt,d)%n
    lettre_decryptee = chr(ascii)
    message = message + str(lettre_decryptee)
    i = i + 1

tmps2=time.time() - tmps1
print(" Voici le message décrypté : ",message)
print("Temps d'exécution = %f" %tmps2)
input('\n\nFin\n\n')
