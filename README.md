# Video Distribution Analysis Dashboard

Este projeto é uma aplicação interativa desenvolvida em Python usando Streamlit e Plotly para visualizar dados de vídeos de exercícios. A aplicação lê um arquivo CSV contendo informações sobre vídeos anotados e exibe gráficos interativos para análise de diferentes aspectos dos vídeos.

[Analysis Annotation Repcount App](https://analysis-annotation-repcount.streamlit.app/)

## Funcionalidades

A aplicação oferece as seguintes visualizações:

1. **Distribuição de Vídeos por Tipo**:
   - Mostra a quantidade total de vídeos, vídeos amostrados e vídeos anotados por tipo de exercício.
   - O gráfico interativo de barras permite visualizar e comparar as categorias de vídeos.

2. **Distribuição dos Motivos de Exclusão**:
   - Exibe a distribuição de vídeos excluídos com base em diferentes razões (e.g., execução incorreta, mais de uma pessoa no vídeo, baixa resolução).
   - Este gráfico ajuda a entender quais são os motivos mais comuns para a exclusão de vídeos em cada tipo de exercício.

3. **Distribuição da Contagem de Repetições por Tipo de Exercício**:
   - Apresenta a média de repetições por tipo de exercício para vídeos anotados e o total de vídeos.
   - Permite uma análise do desempenho médio em cada tipo de exercício.

## Como Usar

1. **Pré-requisitos**: Certifique-se de ter o Python e as bibliotecas `streamlit`, `pandas` e `plotly` instaladas.

2. **Instalação**:
   Clone este repositório e navegue até o diretório do projeto:

   ```bash
   git clone https://github.com/laisorim5/Analysis-Annotation-RepCount.git
   cd Analysis-Annotation-RepCount

## Estrutura do CSV
- `type`: Tipo de exercício.
- `subsampled`: Indica se o vídeo foi amostrado (yes ou no).
- `annotation`: Indica se o vídeo foi anotado (yes ou no).
- `primary exclusion reason`: Razão primária para exclusão.
    - 1 execução errada
    - 2 mais de uma pessoa no vídeo
    - 3 não mostra corpo inteiro
    - 4 mudança de ângulo ou de distância
    - 5 mais de um exercício ou variação
    - 6 baixa resolução
    - 7 texto na frente
    - 8 execução incompleta
    - 9 outros motivos
    - 10 exercício excluído
- `count`: Número de repetições no vídeo.

## Tecnologias Utilizadas
- **Streamlit**: Para a criação da interface web interativa.
- **Plotly**: Para a visualização de gráficos interativos.
- **Pandas**: Para a manipulação e análise de dados.

## Contribuição
Sinta-se à vontade para contribuir com o projeto enviando pull requests ou abrindo issues para melhorias e correções.

## Licença
Este projeto está licenciado sob a licença MIT.
