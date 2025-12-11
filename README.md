<div align="center">

# 🚗 Previsão de Preços de Carros Usados
### Projeto de Machine Learning - Análise e Modelagem Preditiva

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-red.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green.svg)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen.svg)

**Disciplina:** Introdução à Machine Learning
**Período:** 2024/2025

</div>

---

## 👥 Equipe

<table align="center">
  <tr>
    <th>Nome</th>
    <th>Matrícula</th>
  </tr>
  <tr>
    <td>João Marcos Ferreira Vilela</td>
    <td>01701949</td>
  </tr>
  <tr>
    <td>João Victor de Lima</td>
    <td>01693174</td>
  </tr>
  <tr>
    <td>David Roberto da Silva Sousa</td>
    <td>01765638</td>
  </tr>
  <tr>
    <td>Lucas Hiago de Paulo Barbosa</td>
    <td>01766908</td>
  </tr>
  <tr>
    <td>Gabriel Batista Vilela Lima</td>
    <td>01701812</td>
  </tr>
</table>

---

## 🎯 Sobre o Projeto

Este projeto desenvolveu um modelo de **Machine Learning** completo para prever o **preço de revenda de carros usados** no mercado brasileiro. O sistema recebe características técnicas do veículo (marca, ano, quilometragem, câmbio, etc.) e estima seu valor de mercado justo.

Utilizamos uma abordagem de *Data Science* ponta a ponta: desde a análise exploratória e limpeza dos dados, passando pela criação de um modelo baseline (Regressão Linear), até a otimização de algoritmos avançados baseados em árvores de decisão (**XGBoost**).

### 🔍 Problema de Negócio
A precificação de veículos seminovos sofre com alta volatilidade e subjetividade. O objetivo é reduzir essa incerteza fornecendo uma estimativa baseada em dados históricos, auxiliando tanto revendedores quanto compradores finais.

---

## 🏆 Resultados Principais (Performance Final)

O modelo final (**XGBoost Otimizado**) foi avaliado em um conjunto de dados de teste isolado (nunca visto durante o treinamento), alcançando performance superior ao baseline.

| Métrica | Modelo Baseline (Linear) | Modelo Final (XGBoost) | Melhoria |
|:--- |:---:|:---:|:---:|
| **MAE (Erro Médio Absoluto)** | R$ 1.003,07 | **R$ 740,43** | **+26.2%** |
| **RMSE (Raiz do Erro Quadrático)** | R$ 7.836,88 | **R$ 5.262,69** | **+32.8%** |
| **R² (Coeficiente de Determinação)** | 0.9432 | **0.9744** | **+3.1 p.p.** |

> **Conclusão:** O modelo final consegue explicar **97.4%** da variação de preços do mercado, com um erro médio de apenas R$ 740,00 para a maioria dos veículos.

---

## 📊 Estrutura do Repositório

O projeto foi organizado seguindo as boas práticas de engenharia de dados e reprodutibilidade:

```text
MLPROJECT/
│
├── data/                  # Base de dados
│   ├── raw/               # Dados originais (used_cars_price.csv)
│   └── processed/         # Dados limpos e tratados (used_cars_clean.csv)
│
├── docs/                  # Documentação
│   └── RELATORIO_FINAL.md # Relatório técnico detalhado das 4 etapas
│
├── models/                # Modelos serializados para produção
│   ├── baseline_model.pkl
│   ├── modelo_final.joblib
│   └── hiperparametros.joblib
│
├── notebooks/             # Pipeline de desenvolvimento
│   ├── 01_EDA.ipynb              # Análise Exploratória e Visualização
│   ├── 02_Preprocessamento.ipynb # Limpeza, Outliers e Feature Engineering
│   ├── 03_Modelagem.ipynb        # Criação do Baseline (Regressão Linear)
│   └── 04_Otimizacao.ipynb       # Tuning de Hiperparâmetros e Avaliação Final
│
├── reports/figures/       # Gráficos gerados para análise de erros
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo