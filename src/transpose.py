from PIL import Image

#Carregando as imagens
image = Image.open("assets/2.jpg")

# Transpose
""" 
method: FLIP_LEFT_RIGHT, FLIP_TOP_BOTTOM, ROTATE_90, 
ROTATE_180, ROTATE_270, TRANSPOSE, TRANSVERSE.
"""
image.transpose(
    method=Image.Transpose.TRANSVERSE
).show()