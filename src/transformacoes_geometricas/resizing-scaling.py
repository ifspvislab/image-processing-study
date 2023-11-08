from PIL import Image, ImageOps

#ImageOps = modulo com operações de processamento de imagens

#Carregando as imagens
image = Image.open("assets/2.jpg")
image2 = Image.open("assets/1.jpg")

""" Resizing """
# É imposto as dimensoes finais da imagem, dessa forma, refatorando seu tamanho.
# resize - Image
image_resize = image.resize((2000,100))
print(f"Tamanho original: {image.size} \n Tamanho refatorado: {image_resize.size}")

""" Scaling """
# resize - ImageOps
# É imposto uma escala multiplicativa para redimensionamento.
image_scale = ImageOps.scale(image, 4)
print(f"Tamanho original: {image.size} \n Tamanho refatorado: {image_scale.size}")