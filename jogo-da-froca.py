import random

def escolher_palavra():
    palavras = ["desenvolvimento", "tecnologia", "logica", "programacao", "tendencias", "inovacao", "futuro", "inteligencia", "artificial"]
    return random.choice(palavras) 
def exibir_forca(tentativas):
    estagios = [
        '''
           +---+
           |   |
               |
               |
               |
               |
         =========''', '''
           +---+
           |   |
           O   |
               |
               |
               |
         =========''', '''
           +---+
           |   |
           O   |
           |   |
               |
               |
         =========''', '''
           +---+
           |   |
           O   |
          /|   |
               |
               |
         =========''', '''
           +---+
           |   |
           O   |
          /|\  |
               |
               |
         =========''', '''
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
         =========''', '''
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
         ========='''
    ]
    print(estagios[tentativas])

def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ['_'] * len(palavra)
    tentativas = 0
    letras_tentadas = []
    max_erros = 6
    
    print("Bem-vindo ao jogo da Forca!")
    print("Tema: Desenvolvimento e Tecnologia")
    
    while tentativas < max_erros:
        print("\nPalavra:", ' '.join(palavra_oculta))
        exibir_forca(tentativas)
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_tentadas:
            print("Você já tentou essa letra.")
            continue
        
        letras_tentadas.append(letra)
        
        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas += 1
        
        if '_' not in palavra_oculta:
            print("\nParabéns! Você adivinhou a palavra:", palavra)
            break
    else:
        exibir_forca(tentativas)
        print("\nVocê perdeu! A palavra correta era:", palavra)

    print("\nObrigado por jogar!")

jogar()
