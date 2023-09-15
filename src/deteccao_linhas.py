from PIL import Image, ImageFilter

imagem = Image.open("assets/foto1.jpg").convert("L")

mascara_horizontal = ImageFilter.Kernel((3, 3), [-1, -1, -1, 2, 2, 2, -1, -1, -1], scale=1)
mascara_vertical = ImageFilter.Kernel((3, 3), [-1, 2, -1, -1, 2, -1, -1, 2, -1], scale=1)
mascara_diagonal_ascendente = ImageFilter.Kernel((3, 3), [-1, -1, 2, -1, 2, -1, 2, -1, -1], scale=1)
mascara_diagonal_descendente = ImageFilter.Kernel(
    (3, 3), [2, -1, -1, -1, 2, -1, -1, -1, 2], scale=1
)

# Aplica as mascaras
imagem_linhas_horizontais = imagem.filter(mascara_horizontal)
imagem_linhas_verticais = imagem.filter(mascara_vertical)
imagem_linhas_diagonais_ascendentes = imagem.filter(mascara_diagonal_ascendente)
imagem_linhas_diagonais_descendentes = imagem.filter(mascara_diagonal_descendente)

# Salva as imagens
imagem_linhas_horizontais.save("assets/foto1_linhas_horizontais.jpg")
imagem_linhas_verticais.save("assets/foto1_linhas_verticais.jpg")
imagem_linhas_diagonais_ascendentes.save("assets/foto1_linhas_diagonais_ascendentes.jpg")
imagem_linhas_diagonais_descendentes.save("assets/foto1_linhas_diagonais_descendentes.jpg")

# Mostra as imagens
imagem_linhas_horizontais.show()
imagem_linhas_verticais.show()
imagem_linhas_diagonais_ascendentes.show()
imagem_linhas_diagonais_descendentes.show()
