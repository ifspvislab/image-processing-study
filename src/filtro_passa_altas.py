from PIL import Image, ImageFilter

imagem = Image.open("assets/foto1.jpg").convert("L")

# Cria a mascara 3x3 do filtro passa-altas
mascara = ImageFilter.Kernel((3, 3), [-1, -1, -1, -1, 8, -1, -1, -1, -1], scale=9)

# Aplica a convolução com a mascara 3x3
imagem_passa_altas = imagem.filter(mascara)

# Mostra a imagem gerada
imagem_passa_altas.show()
