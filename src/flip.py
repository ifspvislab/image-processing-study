from PIL import Image, ImageOps

#ImageOps = modulo com operações de processamento de imagens

#Carregando as imagens
image = Image.open("assets/2.jpg")
image2 = Image.open("assets/1.jpg")

""" Flip/Espelhamento """

# flip - ImageOps
#Inverte a imagem verticalmente (de cima para baixo).
image = ImageOps.flip(image)
image.show()

# mirror - ImageOps
# Inverter a imagem horizontalmente (da esquerda para a direita).
image2 = ImageOps.mirror(image2)
image2.show()

