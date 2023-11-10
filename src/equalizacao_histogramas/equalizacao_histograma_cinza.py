from PIL import Image
import matplotlib.pyplot as plt

def equalizacao_cinza(nome_imagem):
    # Abre a imagem e converte-a para cinza.
    imagem_cinza = Image.open(nome_imagem).convert("L")

    #Cria os subplots para a imagem e histograma originais.
    plt.subplot(221).axis('off')
    plt.imshow(imagem_cinza, cmap="gray")
    plt.title("Imagem original.")

    plt.subplot(223)
    plt.plot(imagem_cinza.histogram())
    plt.title("Histograma original")
    plt.xlabel("Níveis de cinza")
    plt.ylabel("Frequência original")

    imagem_equalizada = imagem_cinza

    # Calcula a quantidade de pixels se baseando na largura e altura da imagem.
    largura, altura = imagem_cinza.size
    quantidade_pixels = largura * altura


    valores_equalizados = []
    pixels_niveis_cinza = []
    soma_frequencia = 0

    for i in range (256):
        pixels_niveis_cinza.append(0)

    # Calcula o histograma da imagem.
    for i in range(largura):
        for j in range(altura):
            pixels_niveis_cinza[imagem_cinza.getpixel((i, j))] += 1

    # Calcula a função distributiva acumulativa (CDF) do histograma e o normaliza.
    # Após esse cálculo, os valores são convertidos para números inteiros de 0 a 255 e
    # são adicionados para os valores equalizados.
    for i in range(256):
        frequency = pixels_niveis_cinza[i] / quantidade_pixels
        soma_frequencia += frequency
        valores_equalizados.append(round(soma_frequencia * 255))

    # Troca a tonalidade de cada pixel da imagem original pela nova tonalidade equalizada.
    for i in range(largura):
        for j in range(altura):
            valor_original = imagem_cinza.getpixel((i, j))
            imagem_equalizada.putpixel((i, j), valores_equalizados[valor_original])

    # Cria os subplots da imagem e histograma equalizados.
    plt.subplot(222).axis('off')
    plt.imshow(imagem_equalizada, cmap="gray")
    plt.title("Imagem equalizada.")

    plt.subplot(224)
    plt.plot(imagem_equalizada.histogram())
    plt.title("Histograma equalizado")
    plt.xlabel("Níveis de cinza")
    plt.ylabel("Frequência equalizada")

    plt.suptitle("Demonstração de equalização de imagens cinzas.")
    plt.show()

equalizacao_cinza("assets/passaro.png")
