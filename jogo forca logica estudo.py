import random

# Lista de palavras para o jogo da forca
palavras = ["python", "programacao", "desenvolvimento", "computador", "algoritmo", "linguagem", "inteligencia"]

def escolher_palavra(lista_palavras):
    return random.choice(lista_palavras)

def jogar_forca(palavra_secreta):
    letras_certas = []
    letras_erradas = []
    tentativas = 6
    
    while tentativas > 0:
        palavra_descoberta = ""
        for letra in palavra_secreta:
            if letra in letras_certas:
                palavra_descoberta += letra
            else:
                palavra_descoberta += "_"
        
        print("Palavra: ", palavra_descoberta)
        print("Letras Erradas: ", " ".join(letras_erradas))
        
        if palavra_descoberta == palavra_secreta:
            print("Parabéns! Você ganhou!")
            break
        
        tentativa = input("Digite uma letra: ").lower()
        
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue
        
        if tentativa in letras_certas or tentativa in letras_erradas:
            print("Você já tentou essa letra.")
            continue
        
        if tentativa in palavra_secreta:
            print("Letra correta!")
            letras_certas.append(tentativa)
        else:
            print("Letra errada!")
            letras_erradas.append(tentativa)
            tentativas -= 1
        
        print("Tentativas restantes:", tentativas)
        print("-----------------------------")
    else:
        print("Você perdeu! A palavra era:", palavra_secreta)

def main():
    print(" Welcome to Hangman!")
    palavra = escolher_palavra(palavras)
    jogar_forca(palavra)

if __name__ == "__main__":
    main()