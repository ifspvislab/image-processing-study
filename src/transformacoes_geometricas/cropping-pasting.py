from PIL import Image, ImageOps

#ImageOps = modulo com operações de processamento de imagens

#Carregando as imagens
image = Image.open("assets/1.jpg")
image2 = Image.open("assets/2.jpg")
fundo_vermelho = Image.open("assets/fundo-vermelho.jpg")

""" -=Cropping/Cortar=- """ 
#crop - ImageOps
image_cropped = ImageOps.crop(image, border=20) #Retira a borda
#image_cropped.show()

# crop - Images
# box = tupla(left, upper, right, lower)
image_cropped2 = image.crop(box=(30, 30, 50, 300)) #Box que sobrará da imagem
#image_cropped2.show()

# fit - ImagesOps
image_cropped3 = ImageOps.fit(image, size=(200,500)) #Resize cortando a imagem
# image_cropped3.show()

""" -=Pasting/Colar=- """
# box = tupla(left, upper)
# mask:Image = ......
image2.paste(fundo_vermelho, box=(10,200))
# image2.show()