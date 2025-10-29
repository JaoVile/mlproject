# 🎓 Projeto Final: Machine Learning - Previsão de Desempenho Acadêmico

**Disciplina:** Introdução à Machine Learning
**Professor:** [Nome do Professor]
**Formato:** Trabalho em Grupo (até 5 pessoas)
**Duração:** 5 semanas (1 etapa por semana)

---

## 🎯 Objetivo do Projeto

Desenvolver um modelo de **Machine Learning** completo para resolver um problema de regressão do mundo real, desde análise exploratória até apresentação final.

**Tipo de problema:** Regressão (prever valores contínuos)
**Datasets disponíveis:** 10 opções (cada grupo escolhe 1)
**Exemplos:** Prever nota de aluno, vendas, salário TI, visualizações YouTube, preço de carro usado, produtividade de funcionários, etc.

---

## 📅 CRONOGRAMA DO PROJETO

### ⚠️ IMPORTANTE: Projeto Progressivo

Este projeto **NÃO** é entregue tudo de uma vez! Você fará **5 etapas sequenciais**, uma por semana.

Cada etapa tem:
- 📋 Instruções específicas detalhadas
- 💻 Entregável técnico (notebook ou arquivo)
- 🎤 **Apresentação obrigatória**
- ✅ Critérios de avaliação claros

| Semana | Etapa | Entregáveis | Apresentação |
|:------:|-------|-------------|:------------:|
| **1** | [📊 EDA - Análise Exploratória](#-etapa-1-eda) | `notebooks/01_EDA.ipynb` | ✅ Sim |
| **2** | [🔧 Pré-processamento](#-etapa-2-pré-processamento) | Notebook + Dataset limpo | ✅ 10 min |
| **3** | [🤖 Modelagem](#-etapa-3-modelagem) | `notebooks/03_Modelagem.ipynb` | ✅ 15 min |
| **4** | [⚡ Otimização](#-etapa-4-otimização) | Notebook + Modelo final | ✅ 15 min |
| **5** | [🎤 Apresentação Final](#-etapa-5-apresentação-final) | Relatório completo | ✅ 20-25 min |

**Total de apresentações:** 4 apresentações (Etapas 2, 3, 4, e 5)

---

## 📖 ETAPAS DETALHADAS

### 📊 Etapa 1: EDA

**O que fazer:** Conhecer e entender profundamente os dados
**Entregáveis:** `notebooks/01_EDA.ipynb`
**Apresentação:** Não há apresentação nesta etapa
**Peso:** 20%

**Principais análises:**
- Estatísticas descritivas
- Valores faltantes
- Distribuições
- Outliers
- Correlações

📄 **[Ver instruções completas →](etapas/etapa1/README.md)**

---

### 🔧 Etapa 2: Pré-processamento

**O que fazer:** Limpar e preparar dados para modelagem
**Entregáveis:**
- `notebooks/02_Preprocessamento.ipynb`
- `data/processed/dataset_clean.csv`
- **🎤 Apresentação de 10 minutos**

**Peso:** 20% (15% notebook + 5% apresentação)

**Principais tarefas:**
- Tratamento de missing values
- Tratamento de outliers
- Encoding de categóricas
- Feature engineering (criar novas features)
- Normalização/Padronização

**Apresentação deve incluir:**
- Problemas identificados
- Decisões de tratamento e justificativas
- Features criadas
- Comparação antes vs depois

📄 **[Ver instruções completas →](etapas/etapa2/README.md)**

---

### 🤖 Etapa 3: Modelagem

**O que fazer:** Treinar e comparar múltiplos modelos de ML
**Entregáveis:**
- `notebooks/03_Modelagem.ipynb`
- **🎤 Apresentação de 15 minutos**

**Peso:** 20% (15% notebook + 5% apresentação)

**Principais tarefas:**
- Modelo baseline (Regressão Linear)
- Testar pelo menos 3 modelos diferentes
- Validação cruzada
- Comparar métricas (MAE, RMSE, R²)
- Selecionar melhor modelo

**Apresentação deve incluir:**
- Modelos testados
- Comparação de desempenho (gráficos!)
- Melhor modelo e justificativa
- Análise de erros

📄 **[Ver instruções completas →](etapas/etapa3/README.md)**

---

### ⚡ Etapa 4: Otimização

**O que fazer:** Otimizar hiperparâmetros do melhor modelo
**Entregáveis:**
- `notebooks/04_Otimizacao.ipynb`
- `models/modelo_final.joblib`
- **🎤 Apresentação de 15 minutos**

**Peso:** 20% (15% notebook + 5% apresentação)

**Principais tarefas:**
- Grid Search ou Random Search
- Otimização de hiperparâmetros
- Avaliação final no conjunto de teste
- Análise de erros detalhada
- Salvamento do modelo

**Apresentação deve incluir:**
- Processo de otimização
- Hiperparâmetros antes vs depois
- Desempenho final no teste
- Limitações do modelo

📄 **[Ver instruções completas →](etapas/etapa4/README.md)**

---

### 🎤 Etapa 5: Apresentação Final

**O que fazer:** Documentar e apresentar todo o projeto
**Entregáveis:**
- `docs/RELATORIO_FINAL.md` (10-15 páginas)
- **🎤 Apresentação de 20-25 minutos**
- Repositório completo e organizado

**Peso:** 20% (10% relatório + 10% apresentação)

**Relatório deve incluir:**
- Resumo executivo
- EDA e descobertas
- Pré-processamento e decisões
- Modelagem e comparações
- Resultados finais
- Conclusões e trabalhos futuros

**Apresentação deve incluir:**
- Todas as etapas do projeto
- Resultados alcançados
- Demonstração ao vivo
- Conclusões

📄 **[Ver instruções completas →](etapas/etapa5/README.md)**

---

## 🚀 COMO COMEÇAR

### 1️⃣ Clone o Repositório

```bash
git clone [URL-DO-SEU-REPOSITORIO]
cd [nome-do-repositorio]
```

### 2️⃣ Configure o Ambiente

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
source venv/bin/activate  # Linux/Mac
# OU
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt
```

### 3️⃣ Explore os Datasets

```bash
# Iniciar Jupyter
jupyter notebook

# Abra: notebooks/00_EXEMPLO_STARTER.py
# Ou navegue até: data/datasets/ (escolha 1 dos 5 CSVs)
```

### 4️⃣ Leia as Instruções da Etapa Atual

**Etapa 1:** Leia `etapas/etapa1/README.md` antes de começar!

---

## 📁 ESTRUTURA DO REPOSITÓRIO

```
.
├── README.md                    # ⭐ Este arquivo - LEIA PRIMEIRO!
│
├── etapas/                      # 📖 INSTRUÇÕES DE CADA ETAPA
│   ├── etapa1/
│   │   └── README.md           # ⭐ Instruções detalhadas Etapa 1
│   ├── etapa2/
│   │   └── README.md           # ⭐ Instruções detalhadas Etapa 2
│   ├── etapa3/
│   │   └── README.md           # ⭐ Instruções detalhadas Etapa 3
│   ├── etapa4/
│   │   └── README.md           # ⭐ Instruções detalhadas Etapa 4
│   └── etapa5/
│       ├── README.md           # ⭐ Instruções detalhadas Etapa 5
│       └── TEMPLATE_RELATORIO_FINAL.md
│
├── data/
│   ├── datasets/               # 10 datasets disponíveis (NÃO MODIFICAR!)
│   │   ├── students_performance.csv
│   │   ├── ecommerce_sales.csv
│   │   ├── energy_consumption.csv
│   │   ├── housing_prices.csv
│   │   ├── delivery_time.csv
│   │   └── README.md          # ⭐ Descrição de TODOS os 10 datasets
│   └── processed/             # Dados limpos (você cria na Etapa 2)
│
├── notebooks/                  # Seus notebooks Jupyter
│   ├── 00_EXEMPLO_STARTER.py  # Código de exemplo
│   ├── 01_EDA.ipynb           # (você cria - Etapa 1)
│   ├── 02_Preprocessamento.ipynb # (você cria - Etapa 2)
│   ├── 03_Modelagem.ipynb     # (você cria - Etapa 3)
│   └── 04_Otimizacao.ipynb    # (você cria - Etapa 4)
│
├── models/                     # Modelos treinados
│   └── modelo_final.joblib    # (você cria - Etapa 4)
│
├── docs/                       # Documentação e apresentações
│   ├── BOAS_PRATICAS.md       # ⭐ Leia! Guia de boas práticas
│   ├── apresentacao_etapa2.pdf # (você cria)
│   ├── apresentacao_etapa3.pdf # (você cria)
│   ├── apresentacao_etapa4.pdf # (você cria)
│   ├── apresentacao_final.pdf  # (você cria - Etapa 5)
│   └── RELATORIO_FINAL.md     # (você cria - Etapa 5)
│
├── requirements.txt            # Dependências Python
└── .gitignore                 # Arquivos ignorados pelo Git
```

---

## 👥 TRABALHO EM GRUPO

### Como Funciona no GitHub Classroom

- Este é um **repositório compartilhado** do grupo
- Todos os membros têm acesso completo
- Trabalhem em colaboração

### 🤝 Boas Práticas de Colaboração

**1. Comuniquem-se sempre**
- Decidam quem faz o quê
- Usem Issues do GitHub para organizar tarefas

**2. Commits frequentes**
```bash
# Antes de trabalhar
git pull origin main

# Depois de mudanças
git add .
git commit -m "Descrição clara"
git push origin main
```

**3. Divisão de tarefas**
- 📊 Analista de Dados: EDA e visualizações
- 🔧 Engenheiro de Dados: Pré-processamento
- 🤖 Cientista ML: Modelagem
- 📝 Documentador: Relatórios
- 🎤 Apresentador: Preparar slides

*Grupos menores: membros acumulam funções*

**4. Apresentações: TODOS devem participar!**
- Etapa 2: ~2-3 min por pessoa
- Etapa 3: ~3 min por pessoa
- Etapa 4: ~3 min por pessoa
- Etapa 5: ~4-5 min por pessoa

---

## 📊 SOBRE OS DATASETS

**10 datasets disponíveis** - Cada grupo escolhe 1

### Opções de Datasets:

1. **🎓 Desempenho Acadêmico de Estudantes** (Recomendado para iniciantes)
   - Prever nota final (0-100)
   - 2.510 registros, 13 features
   - Dificuldade: ⭐⭐

2. **🛒 Vendas de E-commerce**
   - Prever vendas mensais (R$)
   - 2.510 registros, 16 features
   - Dificuldade: ⭐⭐⭐

3. **⚡ Consumo de Energia Residencial**
   - Prever consumo mensal (kWh)
   - 2.510 registros, 16 features
   - Dificuldade: ⭐⭐⭐

4. **🏠 Preços de Imóveis**
   - Prever preço de venda (R$)
   - 2.510 registros, 17 features
   - Dificuldade: ⭐⭐⭐⭐

5. **🚚 Tempo de Entrega de Pedidos**
   - Prever tempo de entrega (horas)
   - 2.510 registros, 16 features
   - Dificuldade: ⭐⭐⭐

6. **💼 Salário de Profissionais de TI**
   - Prever salário anual (R$)
   - 2.520 registros, 17 features
   - Dificuldade: ⭐⭐⭐

7. **📺 Visualizações de Vídeos no YouTube**
   - Prever número de visualizações
   - 2.520 registros, 21 features
   - Dificuldade: ⭐⭐⭐

8. **🍽️ Avaliação de Restaurantes**
   - Prever nota média (1-5 estrelas)
   - 2.520 registros, 24 features
   - Dificuldade: ⭐⭐

9. **🚗 Preço de Carros Usados**
   - Prever preço de revenda (R$)
   - 2.520 registros, 25 features
   - Dificuldade: ⭐⭐⭐

10. **📊 Produtividade de Funcionários**
    - Prever horas produtivas por semana
    - 2.520 registros, 28 features
    - Dificuldade: ⭐⭐

### ⚠️ Desafios Comuns

TODOS os datasets contêm problemas intencionais (dados do mundo real):
- Valores faltantes (~8%)
- Outliers e valores impossíveis
- Inconsistências e erros de formatação
- Duplicatas

**Você precisará identificar e tratar!**

📖 **Documentação completa de todos os datasets:** `data/datasets/README.md`

---

## ✅ REGRAS IMPORTANTES

### O Que Você DEVE Fazer

- ✅ Seguir o cronograma semanal
- ✅ Ler as instruções da etapa ANTES de começar
- ✅ Documentar TUDO em markdown
- ✅ Preparar apresentações com antecedência
- ✅ TODOS os membros devem apresentar
- ✅ Fazer commits frequentes
- ✅ Executar "Restart & Run All" antes de entregar

### O Que Você NÃO DEVE Fazer

- ❌ Pular etapas ou tentar fazer tudo de uma vez
- ❌ Modificar `data/raw/` (dados originais)
- ❌ Copiar código sem entender (= plágio)
- ❌ Deixar uma pessoa fazer tudo sozinha
- ❌ Fazer apresentação sem ensaiar
- ❌ Um membro dominar toda a apresentação

---

## 🎤 APRESENTAÇÕES - DICAS IMPORTANTES

### Preparação

1. **Dividam o tempo** igualmente entre membros
2. **Ensaiem** pelo menos 2x antes da apresentação
3. **Criem slides** profissionais e legíveis
4. **Preparem para perguntas** dos colegas e professor

### Design dos Slides

- ✅ Fonte mínima: 24pt (título), 18pt (corpo)
- ✅ Máximo 5-6 bullets por slide
- ✅ Gráficos grandes e legíveis
- ❌ Evitem texto em excesso
- ❌ Evitem copiar/colar código

### Apresentação Oral

- ✅ Olhem para a audiência
- ✅ Expliquem os gráficos
- ✅ Sejam objetivos
- ❌ Não leiam os slides
- ❌ Não ultrapassem o tempo

---

## 📚 RECURSOS ÚTEIS

### Documentação Incluída

| Arquivo | Utilidade |
|---------|-----------|
| `data/datasets/README.md` | Descrição completa dos 10 datasets |
| `notebooks/00_EXEMPLO_STARTER.py` | Código exemplo de EDA |
| `docs/BOAS_PRATICAS.md` | Guia de código limpo |
| `etapas/etapaX/README.md` | Instruções detalhadas de cada etapa |

### Bibliotecas Principais

- **pandas** - Manipulação de dados
- **numpy** - Operações numéricas
- **matplotlib / seaborn** - Visualizações
- **scikit-learn** - Machine Learning
- **xgboost / lightgbm** - Modelos avançados

### Links Externos

- [Pandas Docs](https://pandas.pydata.org/docs/)
- [Scikit-learn Guide](https://scikit-learn.org/stable/user_guide.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

---

## 🆘 PRECISA DE AJUDA?

### Dúvidas Técnicas

1. Leia as **instruções da etapa** (`etapas/etapaX/README.md`)
2. Consulte a **documentação dos datasets** (`data/datasets/README.md`)
3. Veja o **código de exemplo** (`notebooks/00_EXEMPLO_STARTER.py`)
4. Consulte **boas práticas** (`docs/BOAS_PRATICAS.md`)
5. Procure o professor no horário de atendimento

### Dúvidas sobre Apresentações

- Veja critérios de avaliação em cada `etapas/etapaX/README.md`
- Consulte dicas de apresentação na Etapa 5
- Ensaie com o grupo e peça feedback

### Problemas com Git

**Conflitos de merge:**
```bash
git pull origin main
# Resolva conflitos nos arquivos
git add .
git commit -m "Resolve conflitos"
git push origin main
```

---

## 🎯 CHECKLIST GERAL

Antes de cada entrega:

- [ ] Li as instruções da etapa completas
- [ ] Notebook executa "Restart & Run All" sem erros
- [ ] Código está documentado em markdown
- [ ] Commits foram feitos com mensagens descritivas
- [ ] (Se aplicável) Apresentação está preparada
- [ ] (Se aplicável) Todos os membros sabem sua parte
- [ ] (Se aplicável) Ensaiamos a apresentação

---

## 💡 DICAS DE SUCESSO

### Para o Grupo

- 🤝 Comuniquem-se constantemente
- 📅 Marquem reuniões semanais
- 🎯 Definam metas claras
- 🔄 Revisem o trabalho uns dos outros

### Para o Código

- 💬 Comentem TUDO
- 📝 Usem markdown para explicar
- 🎨 Caprichem nas visualizações
- 🧪 Testem antes de commitar

### Para Apresentações

- ⏱️ Cronometre durante ensaios
- 🎤 Pratique falar claramente
- 📊 Use gráficos, não tabelas de números
- 🤝 Distribua tempo igualmente

---

## 📖 PRÓXIMOS PASSOS

**AGORA:**
1. ✅ Formar grupo (até 5 pessoas)
2. ✅ Todos clonarem o repositório
3. ✅ Configurar ambiente Python
4. ✅ Ler `data/datasets/README.md` e escolher 1 dataset
5. ✅ Ler `etapas/etapa1/README.md`

**DEPOIS:**
6. Começar Etapa 1 - EDA
7. Seguir cronograma semanal
8. Consultar instruções de cada etapa

---

## 🎉 Boa Sorte!

Vocês têm tudo que precisam para desenvolver um projeto completo de Machine Learning. Sigam o cronograma, trabalhem em equipe, preparem boas apresentações e consultem a documentação quando necessário.

**Vamos nessa!** 🚀

---

**📌 Próximo Passo:** Leia **[etapas/etapa1/README.md](etapas/etapa1/README.md)** para começar!

*Última atualização: 29 de outubro 2025*
