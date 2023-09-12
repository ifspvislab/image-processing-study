from PIL import Image, ImageChops

# Carregando as imagens
imagem1 = Image.open('assets/imagem1.jpg')
imagem2 = Image.open('assets/imagem2.jpg')

# Subtração de imagens (apenas para imagens em tons de cinza)
resultado_subtracao = ImageChops.subtract(imagem1, imagem2)
resultado_subtracao.show()
