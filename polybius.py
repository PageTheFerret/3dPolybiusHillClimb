import random

size = 5
symbols = [' ', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def Decode(plyb, ciphertext):
    plaintext = ""
    split = [ciphertext[i:i+3] for i in range(0, len(ciphertext), 3)]
    for c in split:
        plaintext += plyb.cipher(c)
    return plaintext

def Encode(plyb, plaintext):
    ciphertext = ""
    for s in plaintext:
        if s in plyb.alphabet:
            ciphertext += pad(to_base_5(plyb.alphabet.index(s)))
        else:
            return "_Invalid_"
    return ciphertext
    
def to_base_5(n):
    s = ""
    while n:
        s = str(n % 5) + s
        n /= 5
        n=int(n)
    return s

def pad(n):
    while(len(n) < 3):
        n = '0' + n
    return n

#3d version of polybius square
class polybius:
    def __init__(self, orig=None):
        if orig is None:
            self.non_copy_constructor()
        else:
            self.copy_constructor(orig)
    def non_copy_constructor(self):
        self.alphabet = ['!']*pow(size,3)
    def copy_constructor(self, orig):
        self.alphabet = list(orig.alphabet)
        
    def cipher(self,s):

        return self.alphabet[25 * int(s[0]) + 5 * int(s[1]) + int(s[2])];
   
    def randomize(self):
        for i in range(pow(size,3)):
            self.alphabet[i] = random.choice(symbols)
    
    def smallRnd(self,step = 1):
        for i in range(step):
            self.alphabet[random.randint(0, len(self.alphabet)-1)] = random.choice(symbols)
     
     


