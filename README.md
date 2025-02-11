# Descrição do Projeto
Este projeto utiliza técnicas de análise de imagens de satélite e aprendizado de máquina para realizar a detecção de desmatamento e a análise de risco climático. 
Ele também gera um relatório ESG (Environmental, Social, and Governance) que pode ser aplicado a avaliações no setor de agronegócio.

## Funcionalidades
1. Carregamento de imagens de satélite: Utiliza o Rasterio para manipular imagens geoespaciais.
2. Detecção de desmatamento: Compara duas imagens de satélite para identificar áreas desmatadas com base em um limite de diferença.
3. Análise de risco climático: Usa dados simulados de temperatura e precipitação, aplicando o algoritmo KMeans para classificar áreas de risco climático.
4. Geração de relatório ESG: Calcula o percentual de áreas desmatadas e de alto risco climático, fornecendo métricas úteis para decisões sustentáveis.

## Requisitos
1. Python 3.7 ou superior
2. Bibliotecas
   - rasterio
   - numpy
   - matplotlib
   - geopandas (instalado, mas não utilizado no script atual)
   - scikit-learn

## Instale as dependências com:
pip install rasterio numpy matplotlib geopandas scikit-learn

## Estrutura do Código
1. Carregamento e visualização de imagens de satélite:
   - A função carregar_imagem carrega uma imagem no formato GeoTIFF.
   - A imagem pode ser exibida em escala de cinza.
2. Detecção de desmatamento:
   - Compara duas imagens (antes e depois) para identificar alterações significativas (desmatamento).
   - As áreas de desmatamento são destacadas em vermelho.
3. Clustering para análise de risco climático:
   - Utiliza dados simulados de temperatura e precipitação para classificar áreas de risco com KMeans.
   - Exibe um mapa indicando regiões com diferentes níveis de risco.
4. Geração de relatório ESG:
   - Gera métricas relacionadas ao percentual de desmatamento e áreas de alto risco climático.

## Como Usar
1. Substitua os caminhos dos arquivos GeoTIFF nas chamadas de carregar_imagem pelos caminhos das suas imagens de satélite:
imagem_satelite_antes, _ = carregar_imagem('caminho/para/imagem_antes.tif')
imagem_satelite_depois, _ = carregar_imagem('caminho/para/imagem_depois.tif')

2. Configure o parâmetro threshold da função detectar_desmatamento para ajustar a sensibilidade na detecção de mudanças:
desmatamento = detectar_desmatamento(imagem_satelite_antes, imagem_satelite_depois, threshold=50)

3. Personalize os dados climáticos simulados, se necessário, ou substitua por dados reais.
4. Execute o script para gerar as análises e o relatório ESG.

## Visualizações
- Imagem de Satélite: Mostra a imagem de entrada carregada
- Áreas de Desmatamento: Exibe as áreas onde houve alterações significativas.
- Mapa de Risco Climático: Classifica regiões em diferentes níveis de risco (ex.: baixo, médio, alto)

## Aplicações
1. Este projeto pode ser aplicado em:
   - Monitoramento de áreas protegidas ou agrícolas.
   - Análises de impacto ambiental.
   - Estudos de sustentabilidade no contexto ESG.
   - Planejamento estratégico no agronegócio.
2. Exemplo de Saída
   - Relatório ESG:
Relatório ESG para financiamento agronegócio:
Percentual de áreas desmatadas: 12.45%
Percentual de áreas em alto risco climático: 8.32%

3. 
