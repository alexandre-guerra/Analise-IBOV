# Tech Challenge - Pós-Graduação em Data Analytics

**Instituição:** FIAP - Turma 2DTAT

![](https://github.com/alexandre-guerra/Analise-IBOV/blob/master/imagem_tech.png)

## POSTECH FIAP - Fase 2 - Machine Learning and Time Series

### Título

**Prevendo valores do IBOV com algoritmos de machine learning**
---

### Objetivo

Desenvolver um modelo preditivo com dados da IBOVESPA para criar uma série temporal e prever diariamente o valor de fechamento.

---

### Introdução

No universo financeiro, a previsão de índices de mercado, como o IBOVESPA, representa um desafio notável, tanto para analistas experientes quanto para modelos preditivos avançados. Este projeto nasce do entendimento de que o mercado de ações é inerentemente complexo e imprevisível, caracterizado por um comportamento que muitas vezes parece caótico e influenciado por uma miríade de fatores.

Primeiramente, é fundamental reconhecer que o mercado de ações não segue padrões lineares ou previsíveis de maneira simples. Ele é influenciado por uma vasta gama de variáveis que vão desde indicadores econômicos macroscópicos até eventos geopolíticos imprevisíveis, passando por mudanças nas políticas governamentais e até mesmo por sentimentos e comportamentos dos investidores, que muitas vezes são reativos e emocionais.

Além disso, a própria natureza do mercado, com sua dinâmica de oferta e demanda, cria um ambiente onde a volatilidade é uma constante. Ações individuais e índices podem experimentar flutuações significativas em curtos períodos de tempo, tornando a tarefa de prever o fechamento diário do IBOVESPA extremamente desafiadora.

Neste contexto, o uso de algoritmos de machine learning surge como uma abordagem promissora, pois oferece a possibilidade de identificar padrões ocultos e correlações em grandes conjuntos de dados que seriam difíceis, se não impossíveis, de serem analisados manualmente. No entanto, mesmo essas técnicas sofisticadas não são infalíveis e enfrentam desafios significativos devido à natureza imprevisível do mercado.

Este projeto busca explorar essa complexidade, utilizando metodologias de ponta em machine learning, como Prophet e Redes Neurais Recorrentes (RNNs), especificamente Long Short-Term Memory (LSTM), 
para construir modelos preditivos. Nosso objetivo é não apenas desenvolver modelos que possam prever o fechamento diário do IBOVESPA com uma precisão razoável, mas também entender as limitações e desafios enfrentados ao longo deste percurso.

---
### Desenvolvimento do Projeto em Três Fases

1. **Análise exploratória de dados**
   - Descrição da análise realizada
   - Principais insights encontrados

2. **Criação de um modelo preditivo utilizando Prophet**
   - Implementação do modelo Prophet
   - Avaliação dos resultados

3. **Criação de um modelo preditivo utilizando RNNs (LSTM)**
   - Implementação do modelo LSTM
   - Avaliação dos resultados
---

### Principais Bibliotecas Utilizadas

Este projeto utiliza várias bibliotecas Python no campo de análise de dados e machine learning, incluindo:

- **Numpy**: Uma biblioteca fundamental para computação científica com Python, utilizada para operações eficientes em arrays multidimensionais.
- **Pandas**: Ferramenta de manipulação e análise de dados de alto desempenho, utilizada para a manipulação de datasets.
- **Plotly**: Biblioteca gráfica para criar visualizações de dados interativas.
- **yfinance**: Usada para baixar dados históricos do mercado financeiro diretamente do Yahoo Finance.
- **Statsmodels**: Fornecendo implementações de várias estatísticas, modelos e testes estatísticos.
- **Prophet**: Biblioteca para previsões de séries temporais, desenvolvida pelo Facebook.
- **TensorFlow e Keras**: Utilizadas para a construção e treinamento de modelos de deep learning, incluindo redes neurais recorrentes (LSTM).
- **Scikit-Learn**: Empregada para diversas tarefas de machine learning, incluindo o pré-processamento de dados e a avaliação de modelos.

Essas bibliotecas são integradas para coletar dados, processá-los, construir modelos preditivos e avaliar seu desempenho.

---

