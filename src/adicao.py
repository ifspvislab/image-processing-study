from PIL import Image

# Carregando as imagens
imagem1 = Image.open('assets/imagem1.jpg')
imagem2 = Image.open('assets/imagem2.jpg')

# Adição de imagens
resultado_adicao = Image.blend(imagem1, imagem2, alpha=0.5)  # Alpha define a intensidade da mistura
resultado_adicao.show()
