from PIL import Image, ImageOps
import matplotlib.pyplot as plt

def equalizacao_histograma_colorido(imagem_original):

    # Converte a imagem para o espaço de cores YUV.
    imagem_yuv = imagem_original.convert('YCbCr')

    # Separa os canais Y, Cb, e Cr.
    y, cb, cr = imagem_yuv.split()

    # Equaliza o canal Y (luminância).
    equalizacao_iluminancia = ImageOps.equalize(y)

    # Combina os canais equalizados de volta.
    imagem_yuv_equalizada = Image.merge('YCbCr', (equalizacao_iluminancia, cb, cr))

    # Converte de volta para o espaço de cores RGB.
    imagem_rgb_equalizada = imagem_yuv_equalizada.convert('RGB')

    return imagem_rgb_equalizada

# Carrega a imagem colorida.
imagem_entrada = Image.open('assets/cidade.jpg')

# Aplica a equalização de histograma.
imagem_equalizada = equalizacao_histograma_colorido(imagem_entrada)

# Mostra as imagens.
plt.subplot(221).axis('off')
plt.imshow(imagem_entrada)
plt.title('Imagem Original')

plt.subplot(222).axis('off')
plt.imshow(imagem_equalizada)
plt.title('Imagem Equalizada')

# Plota os histogramas dos canais Y (luminância)
plt.subplot(223)
plt.plot(imagem_entrada.histogram())
plt.title('Histograma Original (Canal Y)')

plt.subplot(224)
plt.plot(imagem_equalizada.histogram())
plt.title('Histograma Equalizado (Canal Y)')

plt.suptitle("Demonstração de equalização de imagens coloridas.")
plt.show()
