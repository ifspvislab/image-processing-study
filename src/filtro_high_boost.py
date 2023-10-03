from PIL import Image, ImageFilter, ImageOps

imagem = Image.open("assets/foto1.jpg").convert("L")

# Define o fator de realce (A)
A = 1.2

# Aplica o filtro gaussiano
imagem_borrada = imagem.filter(ImageFilter.GaussianBlur(radius=5))

# Calcula a imagem de realce
imagem_high_boost = ImageOps.invert(ImageOps.invert(imagem).point(lambda x: round(A * x)))

# Mostra a imagem 
imagem_high_boost.show()
