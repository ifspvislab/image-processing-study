from PIL import ImageFilter, Image

image = Image.open("images/3.jpg")

# MedianFilter - ImageFilter
# Cria um filtro de média. Seleciona o valor médio de pixel em uma janela com o dado tamanho.
# size: O tamanho do kernel, em pixels.
# Kernel: matriz ou máscara que define a vizinhança de pixels
# image.filter(ImageFilter.MedianFilter(size=5)).show()


# ModeFilter - ImageFilter
# Cria um filtro de modo. Seleciona o valor de pixel mais frequente em uma caixa com o dado tamanho.
# size: O tamanho do kernel, em pixels.
# Kernel: matriz ou máscara que define a vizinhança de pixels
# image.filter(ImageFilter.ModeFilter(size=5)).show()

image.filter(ImageFilter.ModeFilter(3)).show()
# image.filter(ImageFilter.MedianFilter()).show()