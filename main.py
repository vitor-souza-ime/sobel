import cv2
import numpy as np
import urllib.request
import matplotlib.pyplot as plt

# URL da imagem (troque por outra se quiser testar)
url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Johannes_Vermeer_%281632-1675%29_-_The_Girl_With_The_Pearl_Earring_%281665%29.jpg/800px-Johannes_Vermeer_%281632-1675%29_-_The_Girl_With_The_Pearl_Earring_%281665%29.jpg"

# Criar request com User-Agent
req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'}
)

# Baixar a imagem da internet
resp = urllib.request.urlopen(req)
image_array = np.asarray(bytearray(resp.read()), dtype=np.uint8)

# Converter para formato OpenCV
image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

# Converter para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detecção de bordas com Sobel
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)  # Gradiente na direção X
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)  # Gradiente na direção Y
sobel_edges = cv2.magnitude(sobel_x, sobel_y)  # Magnitude do gradiente

# Mostrar as imagens (original e com filtro Sobel) em uma grade
titles = ["Original", "Filtro Sobel"]
images = [image, sobel_edges]

plt.figure(figsize=(10, 5))

for i in range(2):
    plt.subplot(1, 2, i+1)
    if len(images[i].shape) == 2:  # Imagem em escala de cinza
        plt.imshow(images[i], cmap="gray")
    else:  # Imagem colorida
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis("off")

plt.show()
