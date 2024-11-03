import random

# Passo 1: Escolher uma palavra aleatória
def escolher_palavra():
    palavras = ["desenvolvimento", "tecnologia", "logica", "programacao", "tendencias", "inovacao", "futuro", "inteligencia", "artificial"]
    return random.choice(palavras) #A função choice recebe como argumento uma lista de elementos, que podem ser números ou textos, e retorna aleatoriamente um único elemento dela.

# Passo 2: Exibir os estágios da forca
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

# Passo 3: Função principal do jogo
def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ['_'] * len(palavra)
    tentativas = 0
    letras_tentadas = []
    max_erros = 6
    
    print("Bem-vindo ao jogo da Forca!")
    print("Tema: Desenvolvimento e Tecnologia")
    
    # Passo 4: Loop principal do jogo
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
        
        # Passo 5: Verificação de vitória ou derrota
        if '_' not in palavra_oculta:
            print("\nParabéns! Você adivinhou a palavra:", palavra)
            break
    else:
        exibir_forca(tentativas)
        print("\nVocê perdeu! A palavra correta era:", palavra)

    # Passo 6: Finalização do jogo
    print("\nObrigado por jogar!")

# Executar o jogo
jogar()
