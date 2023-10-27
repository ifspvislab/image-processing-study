from PIL import Image

img = Image.open('../../imagem1.jpg')

matriz = img.load()

for i in range(img.size[0]):
  for j in range(img.size[1]):
    r = 255 - matriz[i,j][0]
    g = 255 - matriz[i,j][1]
    b = 255 - matriz[i,j][2]
    matriz[i,j] = (r,g,b)

img.show()
