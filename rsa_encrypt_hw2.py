import random
def primes(x, y):
    p_list = []
    for n in range(x, y):
        isPrime = True
        for num in range(2, n):
            if n % num == 0:
                isPrime = False
        if isPrime:
            p_list.append(n)
    return p_list
p_list = primes(0,1000)
p = random.choice(p_list)
q = random.choice(p_list)
n = (p * q)
phiN = (p - 1) * (q - 1)

def s_phi_N(u, v):
    p_n_prime = []
    for t in range(u, v):
        isPrime = True
        for num in range(2, t):
            if t % num == 0:
                isPrime = False
        if isPrime:
            p_n_prime.append(t)
    return p_n_prime
p_n_prime = s_phi_N(1, 500)
e = random.choice(p_n_prime)

d = pow(e, -1, phiN)

pu_key = (e,n)
pr_key =  (d,n)

plain_mess = (input("Please enter your message "))
msg_split = plain_mess.split(",")

def encrypt(pu_key,n_text):
    e,n=pu_key
    f=[]
    m=0
    for k in n_text:
        if k!= 0:
            m = int(k)
            c = (m**e)%n
            f.append(c)

    return f

def decrypt(pr_key,e_msg):
    d,n=pr_key
    txt=e_msg
    f=[]
    m=0
    for k in txt:
        if(k != 0):
            m = (k ** d) % n
            c = int(m)
            f.append(c)
    return f

e_msg = encrypt(pu_key, msg_split)
d_msg = decrypt(pr_key, e_msg)
print (f"Your encrypted message is: {e_msg}")
print (f"Your decrypted message is: {d_msg}")