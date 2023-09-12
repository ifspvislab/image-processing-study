from PIL import Image, ImageOps

# Carregue a imagem
imagem = Image.open('assets/imagem1.jpg')

# Certifique-se de que a imagem esteja no modo binário (1-bit)
imagem_bin = imagem.convert('1')

# Aplique a operação NOT
imagem_not = ImageOps.invert(imagem_bin)
imagem_not.show()
