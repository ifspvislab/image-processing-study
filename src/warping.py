from PIL import Image

# Abre a imagem
imagem1 = Image.open("assets/imagem1.jpg")

# Realiza o warp para um formato de losango
resultado = imagem1.transform(imagem1.size,
                            Image.PERSPECTIVE,
                            [
                                2, -0.5, 1,
                                -0.5, 2, 1,
                                0, 0 
                            ], # Coeficientes passados no livro, convertidos para o tamanho da imagem
                            Image.BILINEAR 
                            )

resultado.show()
