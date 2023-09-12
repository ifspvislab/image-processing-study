from PIL import Image, ImageChops

# Carregue as imagens
imagem1 = Image.open('assets/imagem1.jpg')
imagem2 = Image.open('assets/imagem2.jpg')

# Certifique-se de que as imagens tenham o mesmo tamanho
if imagem1.size != imagem2.size:
    raise ValueError("As imagens devem ter o mesmo tamanho.")

# Realize a multiplicação pixel a pixel
imagem_resultante = ImageChops.multiply(imagem1, imagem2)
imagem_resultante.show()
