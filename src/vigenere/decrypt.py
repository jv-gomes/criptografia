key = "35035"
initVector = "AEIOU"


def vigenereDec(bloco, chave):
    r = ""
    for i in range(5):
        value = (ord(bloco[i]) - 32) - (ord(chave[i]) - 32)
        r += chr((value % 95) + 32)
    return r

def vigenereEnc(bloco, chave):
    r = ""
    for i in range(5):
        value = (ord(bloco[i]) - 32) + (ord(chave[i]) - 32)
        r += chr((value % 95) + 32)
    return r

def xor_blocks(a, b):
    r = ""
    for i in range(5):
        value = (ord(a[i]) - 32) ^ (ord(b[i]) - 32)
        r += chr((value % 95) + 32)
    return r

def ebcDecrypt(cifrado, chave):
    blocos = []
    for i in range(0, len(cifrado), 5):
        bloco = cifrado[i:i+5]
        blocos.append(vigenereDec(bloco, chave))
    return "".join(blocos)

def cfbDecrypt(cifrado, chave, iv):
    blocos = []
    prev = iv
    for i in range(0, len(cifrado), 5):
        bloco = cifrado[i:i+5]
        keystream = vigenereEnc(prev, chave)
        p = xor_blocks(bloco, keystream)
        blocos.append(p)
        prev = bloco
    return "".join(blocos)




cif_ebc = open("output/vigenere-enc-ebc.txt").read()
cif_cfb = open("output/vigenere-enc-cfb.txt").read()

texto_ebc = ebcDecrypt(cif_ebc, key)[:12]
texto_cfb = cfbDecrypt(cif_cfb, key, initVector)[:12]

open("output/plain_ebc.txt", "w").write(texto_ebc)
open("output/plain_cfb.txt", "w").write(texto_cfb)

print("Textos decifrados salvos em output/:")
print(" - plain_ebc.txt")
print(" - plain_cfb.txt")


