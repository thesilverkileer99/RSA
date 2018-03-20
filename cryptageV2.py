import time

def pgcd(a,b):
    while a != b:
        if a > b :
            a = a - b
        else :
            b = b - a
    return a ;

p = int(input("Entrez p : "))
q = int(input("Entrez q : "))
tmps1=time.time()

n = p * q

test = 0

PGCD1 = 0

e = 0

phi = (p-1)*(q-1)

while PGCD1 != 1 :
        while test == 0 :
            e = e + 1
            if ((p < e) and (q < e) and ( e < phi)):
                test = 1
        e = e + 1
        PGCD1 = pgcd(e,phi)

print("cle de cryptage : n= ",n," e= ",e)
tmps2=time.time()-tmps1
print("Temps d'execution = %f" %tmps2)

mot = input('\nEntrez le mot ou la phrase à chiffrer : ')
tmps1=time.time()
longueur_mot = len(mot)

i = 0

liste_code = []
while i < longueur_mot :
    ascii = ord(mot[i])
    code = pow(ascii,e)%n
    print(code)
    liste_code = liste_code + [code]
    i = i + 1

tmps2=time.time()-tmps1    
print("code : ",liste_code)
print("Temps d'execution = %f" %tmps2)
input('\n\nFin\n\n')

