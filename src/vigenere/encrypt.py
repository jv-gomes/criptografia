texto = "aulasegcomp1"
key = "35035"
initVector = "AEIOU"


def idx(ch):
    return ord(ch) - 32

def ch(i):
    return chr((i % 95) + 32)

def vigenere_encrypt_block(bloco, chave):
    resultado = ""
    for i in range(5):
        soma = idx(bloco[i]) + idx(chave[i])
        resultado += ch(soma)
    return resultado


def xor_blocks(a, b):
    resultado = ""
    for i in range(5):
        resultado += ch(idx(a[i]) ^ idx(b[i]))
    return resultado

def ebcEncrypt(texto, chave):
    blocos = []

    for i in range(0, len(texto), 5):
        bloco = texto[i:i+5]

        if len(bloco) < 5:
            bloco += " " * (5 - len(bloco))

        cifrado = vigenere_encrypt_block(bloco, chave)
        blocos.append(cifrado)

    return "".join(blocos)


def cfbEncrypt(texto, chave, initVector):
    blocos = []
    anterior = initVector

    for i in range(0, len(texto), 5):
        bloco = texto[i:i+5]

        if len(bloco) < 5:
            bloco += " " * (5 - len(bloco))

        keystream = vigenere_encrypt_block(anterior, chave)

        cifrado = xor_blocks(bloco, keystream)
        blocos.append(cifrado)

        anterior = cifrado

    return "".join(blocos)




cif_ebc = ebcEncrypt(texto, key)
cab_ebc = "modo = EBC|bloco = 5|tamanho texto = 12\n"

with open("./output/vigenere-enc-ebc.txt", "w") as f:
    f.write(cif_ebc)

print('cabecalho ebc --> ',cab_ebc)




cif_cfb = cfbEncrypt(texto, key, initVector)
cab_cfb = "modo = CFB|bloco = 5|tamanho texto = 12|initVector = AEIOU\n"

with open("./output/vigenere-enc-cfb.txt", "w") as f:
    f.write(cif_cfb)

print('cabecalho cfb --> ',cab_cfb)







