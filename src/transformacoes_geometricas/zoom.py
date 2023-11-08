from PIL import Image

#Carregando as imagens
image = Image.open("assets/1.jpg")

#Função Zoom
def zoom(image, x, y, zoom):
    w, h = image.size
    zoom2 = zoom * 2
    image = image.crop((x - w / zoom2, y - h / zoom2, 
                    x + w / zoom2, y + h / zoom2))
    return image.resize((w, h), Image.Resampling.LANCZOS)

zoom(image, 400, 400, 6).show()