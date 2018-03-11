import time

def algo_eucl(a,b):
    (r , u , v , r_pr , u_pr , v_pr)=(a,1,0,b,0,1)
    while r_pr != 0 :
        q=r//r_pr
        (r , u , v , r_pr , u_pr , v_pr)=(r_pr, u_pr , v_pr , r-q*r_pr , u - q*u_pr , v - q*v_pr)
    return(r,u,v)
def inv_modulaire(a,b):
    (r,u,v)=algo_eucl(a,b)
    while u != int(u) or u < 0 :
        u= (1-b*v)/a
        v=v-1
    return(u)

def cryptage_key(p,q,e):
    n=p*q;
    phi = (p-1)*(q-1);
    d=inv_modulaire(e,phi)
    
    return((n,e),(n,d))

def cryptage(m,n,e):
    c=0
    while (c-m**e)%n !=0:
        c=c+1
    return(c)
def decryptage(c,n,d):
    m=0
    if d >= 0 :
        while (c**d-m)%n !=0:
            m=m+1
    return(m)


#version avec cryptage en un seul programme

def cryptage_keyV2(p,q,e):
    n=p*q;
    phi = (p-1)*(q-1);
    d=inv_modulaire(e,phi)
    
    return((n,e))
def decryptage_keyV2(p,q,e):
    n=p*q;
    phi = (p-1)*(q-1);
    d=inv_modulaire(e,phi)
    
    return((n,d))

def cryptageV2 (p,q,e,m):
    tmps1=time.time()
    (n,e)= cryptage_keyV2(p,q,e)
    c=0
    while (c-m**e)%n !=0:
        c=c+1
    tmps2=time.time()-tmps1
    return("code :",c," Temps d'execution = %f" %tmps2)
    
