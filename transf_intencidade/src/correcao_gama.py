from PIL import Image

img = Image.open('../../imagem1.jpg')

matriz = img.load()

gamma = 0.5
for i in range(img.size[0]):
  for j in range(img.size[1]):
    r = (matriz[i,j][0] / 255) ** gamma * 255
    g = (matriz[i,j][1] / 255) ** gamma * 255
    b = (matriz[i,j][2] / 255) ** gamma * 255
    matriz[i,j] = (int(r),int(g),int(b))

img.show()