import math
from PIL import Image

img = Image.open('../../imagem1.jpg')

matriz = img.load()

c = 255 / math.log(1 + 255)

for i in range(img.size[0]):
  for j in range(img.size[1]):
    r = c * math.log(1 + matriz[i,j][0])
    g = c * math.log(1 + matriz[i,j][1])
    b = c * math.log(1 + matriz[i,j][2])
    matriz[i,j] = (int(r),int(g),int(b))

img.show()
