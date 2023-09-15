from PIL import Image, ImageFilter

# Abre a imagem
imagem = Image.open("assets/foto1.jpg")

# Converte ela para cinza
imagem_cinza = imagem.convert("L")

# Cria a mascara
mascara = ImageFilter.Kernel((3, 3), [-1, -1, -1, -1, 8, -1, -1, -1, -1], scale=1)

# Aplica a mascara
imagem_gerada = imagem_cinza.filter(mascara)

# Salva imagem gerada
imagem_gerada.save("assets/foto1_gerada.jpg")

# Mostra imagem gerada
imagem_gerada.show()
