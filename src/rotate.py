from PIL import Image

#Carregando as imagens
image = Image.open("assets/2.jpg")

""" Rotate/Rotação 
Parametros:
angle (float) = angulo em float 
fillcolor =  Opcional/ Cor para área fora da imagem girada
exapnd:bool = Padrao False, quando True toda a imagem acompanha a rotacao
resample = Opcional/Tipos de reamostragem
translate(left,upper) = Optional/Movimentação
center(upper, left) = Opcional/Rotacionar com base no centro.
"""

#Exemplo 1:
image.rotate(
    angle=50,
    center=(500,500),
    fillcolor='white',
    resample=Image.Resampling.BICUBIC,
    translate=(10,10),
).show()

#Exemplo 2:
image.rotate(
    angle=100,
    fillcolor='red',
    translate=(50,10),
    expand=True
).show()