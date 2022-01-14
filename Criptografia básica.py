'''1)
        Fazer um programa que codifique uma mensagem utilizando a cifra de César.
        Em sequência fazer um programa que descodifique a mensagem.'''

método_encriptar=1
método_desencriptar=0

def caesar(frase,posição,método):
    alfabeto="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nova_frase=""

    for x in frase:
        índice=alfabeto.find(x)
        if índice == -1:
            nova_frase+=x
        else:
            if método==1:
                novo_índice = índice + posição
            else:
                novo_índice = índice - posição
            novo_índice = novo_índice % len(alfabeto)
            nova_frase+=alfabeto[novo_índice:novo_índice+1]
    return nova_frase

print(caesar("Olá Mundo!",3,1))