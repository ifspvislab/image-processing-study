from PIL import Image, ImageFilter

imagem = Image.open('assets/foto1.jpg').convert("L")

# Cria a máscara de Laplaciano 3x3
mascara_laplaciano = ImageFilter.Kernel((3, 3), [0, -1, 0, -1, 4, -1, 0, -1, 0], scale=1)

# Aplica a convolução com a máscara de Laplaciano
imagem_realce_laplaciano = imagem.filter(mascara_laplaciano)

# Salva a imagem
imagem_realce_laplaciano.save("assets/foto1_laplaciano.jpg")

# Exibe a imagem
imagem_realce_laplaciano.show()
