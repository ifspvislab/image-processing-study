from PIL import Image, ImageFilter

imagem = Image.open("assets/foto2.jpg").convert("L")

# Cria o tamanho do filtro da mediana
raio = 3

# Aplica o filtro na imagem
imagem_filtro_mediana = imagem.filter(ImageFilter.MedianFilter(size=raio))

# Mostra a imagem gerada
imagem_filtro_mediana.show()
