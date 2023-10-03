from PIL import Image, ImageFilter

imagem = Image.open("assets/foto3.jpg").convert("L")

# Define o valor de k (número de vizinhos)
k = 2

# Aplica um filtro de vizinhos próximos para suavização
imagem_media_k_vizinhos = imagem.filter(ImageFilter.ModeFilter(size=k))

# Mostra a imagem gerada
imagem_media_k_vizinhos.show()
