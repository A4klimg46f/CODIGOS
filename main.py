pip install rasterio numpy matplotlib geopandas scikit-learn

import rasterio
import numpy as np
import matplotlib.pyplot as plt
from rasterio.plot import show

# Função para carregar a imagem de satélite
def carregar_imagem(caminho_imagem):
    with rasterio.open(caminho_imagem) as src:
        imagem = src.read(1)  # Ler a primeira banda (geralmente RED ou RGB)
        perfil = src.profile
    return imagem, perfil

# Exemplo: Carregar uma imagem de satélite
imagem_satelite, perfil = carregar_imagem('caminho/para/sua_imagem.tif')

# Exibir a imagem de satélite
plt.imshow(imagem_satelite, cmap='gray')
plt.title('Imagem de Satélite')
plt.show()

# Função para detectar mudanças entre duas imagens (antes e depois)
def detectar_desmatamento(imagem_antes, imagem_depois, threshold=50):
    diferenca = np.abs(imagem_depois - imagem_antes)
    desmatamento = diferenca > threshold
    return desmatamento

# Carregar a segunda imagem de satélite (momento posterior)
imagem_satelite_antes, _ = carregar_imagem('caminho/para/imagem_antes.tif')
imagem_satelite_depois, _ = carregar_imagem('caminho/para/imagem_depois.tif')

# Detectar desmatamento
desmatamento = detectar_desmatamento(imagem_satelite_antes, imagem_satelite_depois)

# Exibir as áreas de desmatamento
plt.imshow(desmatamento, cmap='Reds')
plt.title('Áreas de Desmatamento')
plt.show()

from sklearn.cluster import KMeans

# Exemplo de dados climáticos para a região (simulação)
temperatura = np.random.uniform(20, 40, size=(100, 100))  # Simulação de temperatura
precipitacao = np.random.uniform(0, 200, size=(100, 100))  # Simulação de precipitação

# Concatenar as variáveis temperatura e precipitação para o modelo de clustering
dados_climaticos = np.dstack((temperatura, precipitacao)).reshape(-1, 2)

# Usar KMeans para classificar áreas de risco climático
kmeans = KMeans(n_clusters=3, random_state=42).fit(dados_climaticos)
riscos_climaticos = kmeans.labels_.reshape(100, 100)

# Exibir o mapa de risco climático
plt.imshow(riscos_climaticos, cmap='coolwarm')
plt.title('Mapa de Risco Climático')
plt.show()

def gerar_relatorio_esg(desmatamento, riscos_climaticos):
    area_total = desmatamento.size
    area_desmatada = np.sum(desmatamento)
    area_risco_alto = np.sum(riscos_climaticos == 2)  # Classe 2 representando alto risco

    percentual_desmatado = (area_desmatada / area_total) * 100
    percentual_risco_alto = (area_risco_alto / area_total) * 100

    print("Relatório ESG para financiamento agronegócio:")
    print(f"Percentual de áreas desmatadas: {percentual_desmatado:.2f}%")
    print(f"Percentual de áreas em alto risco climático: {percentual_risco_alto:.2f}%")

# Gerar o relatório ESG
gerar_relatorio_esg(desmatamento, riscos_climaticos)

