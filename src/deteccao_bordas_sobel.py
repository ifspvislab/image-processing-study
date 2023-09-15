from PIL import Image, ImageFilter

imagem = Image.open('assets/foto1.jpg').convert("L")

# Cria as mascaras de Sobel 3X3
mascara_horizontal = ImageFilter.Kernel((3, 3), [1, 0, -1, 2, 0, -2, 1, 0, -1], scale=1)
mascara_vertical= ImageFilter.Kernel((3, 3), [-1, -2, -1, 0, 0, 0, 1, 2, 1], scale=1)

# Aplica a convolução com as máscaras de Sobel
gradiente_x = imagem.filter(mascara_horizontal)
gradiente_y = imagem.filter(mascara_vertical)

# Combina o gradiente_x e o gradiente_y para a obtencao da magnitude do gradiente
imagem_borda = Image.new("L", imagem.size)
pixels_borda = imagem_borda.load()
pixels_x = gradiente_x.load()
pixels_y = gradiente_y.load()

largura, altura = imagem.size

for x in range(largura):
    for y in range(altura):
        magnitude = int((pixels_x[x, y]**2 + pixels_y[x, y]**2)**0.5)
        pixels_borda[x, y] = magnitude

# Salva a imagem
imagem_borda.save("assets/foto1_sobel.jpg")

# Exibe a imagem
imagem_borda.show()
