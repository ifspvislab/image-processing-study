from PIL import Image, ImageFilter

imagem = Image.open("assets/foto2.jpg").convert("L")

# Cria a mascara 3x3 do filtro da media
mascara = ImageFilter.Kernel((3, 3), [1, 1, 1, 1, 1, 1, 1, 1, 1], scale=9)

# Aplica a convolução com a mascara 3x3
imagem_filtro_media = imagem.filter(mascara)

# Mostra a imagem gerada
imagem_filtro_media.show()
