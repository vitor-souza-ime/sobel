# Sobel Edge Detection

Este repositório contém um exemplo em Python que demonstra a **detecção de bordas** em imagens usando o **filtro Sobel**. O código baixa uma imagem da internet, converte para escala de cinza e aplica o filtro Sobel para realçar os contornos.

O exemplo utiliza a biblioteca **OpenCV** para processamento de imagens e **Matplotlib** para visualização.

---

## Arquivo Principal

- **main.py**: Script principal que realiza o download da imagem, aplica o filtro Sobel e exibe a imagem original e a resultante lado a lado.

---

## Pré-requisitos

Certifique-se de ter o Python 3 instalado e as bibliotecas abaixo:

```bash
pip install opencv-python numpy matplotlib
````

---

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/vitor-souza-ime/sobel.git
cd sobel
```

2. Execute o script:

```bash
python main.py
```

O script exibirá a imagem original à esquerda e a imagem com o filtro Sobel aplicado à direita.

---

## Personalização

* Para testar com outras imagens, altere a variável `url` em `main.py` para o link da imagem desejada.
* O script utiliza `User-Agent` para garantir que a imagem seja baixada corretamente mesmo de servidores que bloqueiam requisições automáticas.
* O tamanho do kernel do filtro Sobel pode ser ajustado alterando o parâmetro `ksize` nas linhas:

```python
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
```

---

## Exemplo de Resultado

Ao executar o script com a imagem:

<img width="711" height="427" alt="image" src="https://github.com/user-attachments/assets/b1fb74a2-158f-4f7d-93a3-9ae256987d7c" />

O resultado será exibido em duas colunas: **Original** e **Filtro Sobel**.

---

## Licença

Este projeto está disponível sob a licença **MIT**.

---

## Referências

* [OpenCV Documentation](https://docs.opencv.org/)
* [Matplotlib Documentation](https://matplotlib.org/)

