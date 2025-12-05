# Relatório Final - Projeto de Machine Learning
## Predição de Desempenho Acadêmico de Estudantes
 
**Dataset:** students_performance.csv  
**Disciplina:** Introdução à Machine Learning - 2025.2

---

## 📋 Sumário Executivo

Este projeto teve como objetivo desenvolver um modelo preditivo capaz de estimar o desempenho acadêmico final de estudantes universitários utilizando técnicas de Machine Learning. O dataset utilizado contém informações de 2.495 estudantes com 23 features (após feature engineering) relacionadas a hábitos de estudo, condições socioeconômicas, fatores de saúde e engajamento acadêmico.

Após um processo rigoroso de análise exploratória, pré-processamento, modelagem e otimização, foi desenvolvido um modelo Random Forest otimizado capaz de prever notas finais com **MAE de 3.45 pontos** e **R² de 0.89** no conjunto de teste. O modelo demonstrou capacidade de generalização consistente e pode ser utilizado para identificar estudantes em risco de baixo desempenho, permitindo intervenções preventivas.

**Principais Resultados:**
- **Modelo Final:** Random Forest com hiperparâmetros otimizados
- **Performance:** MAE = 3.45, RMSE = 4.67, R² = 0.89
- **Melhoria:** 12.3% de redução no MAE comparado ao baseline
- **Features Importantes:** previous_scores (28%), study_hours (19%), attendance_rate (15%)

---

## 🎯 1. Introdução

### 1.1 Contextualização do Problema

No contexto educacional moderno, universidades e instituições de ensino enfrentam o desafio constante de identificar precocemente estudantes em risco de baixo desempenho acadêmico. A detecção antecipada desses casos permite a implementação de estratégias de intervenção, como programas de tutoria personalizada, aconselhamento acadêmico e suporte adicional, resultando em melhores taxas de sucesso e redução da evasão escolar.

Tradicionalmente, a identificação de estudantes em risco ocorre apenas após avaliações parciais ou quando já há sinais evidentes de dificuldade. Com técnicas de Machine Learning, é possível analisar múltiplos fatores simultaneamente e realizar predições mais precisas e antecipadas, considerando características demográficas, hábitos de estudo, condições socioeconômicas e indicadores de engajamento.

### 1.2 Objetivos

**Objetivo Geral:**
Desenvolver um modelo de Machine Learning capaz de prever com precisão a nota final de estudantes universitários com base em características observáveis no início do período letivo.

**Objetivos Específicos:**
1. Realizar análise exploratória completa para identificar padrões e relações nos dados
2. Implementar pipeline de pré-processamento robusto com tratamento de dados ausentes e outliers
3. Comparar diferentes algoritmos de regressão (Linear Regression, Ridge, Lasso, Random Forest)
4. Otimizar hiperparâmetros do melhor modelo usando Grid Search com validação cruzada
5. Avaliar o modelo final no conjunto de teste e analisar erros de predição
6. Identificar as features mais importantes para o desempenho acadêmico
7. Alcançar RMSE inferior a 6.0 pontos na escala de 0-100

### 1.3 Dataset

**Características Principais:**

| Atributo | Descrição |
|----------|-----------|
| **Nome** | Students Performance Dataset |
| **Fonte** | Dataset educacional sintético baseado em padrões reais |
| **Tamanho Original** | 2.495 estudantes × 13 features |
| **Tamanho Processado** | 2.495 estudantes × 23 features (após feature engineering) |
| **Variável Alvo** | `final_grade` - Nota final do estudante (escala 0-100) |
| **Tipo de Problema** | Regressão |
| **Missing Values** | Sim - 5.2% dos dados (tratados na Etapa 2) |
| **Outliers** | Sim - Identificados e tratados seletivamente |

**Features Originais:**
- **Demográficas:** age, gender, parental_education, family_income
- **Acadêmicas:** previous_scores, attendance_rate
- **Hábitos:** study_hours_per_week, sleep_hours_per_night, extracurricular_activities
- **Suporte:** tutoring_sessions, internet_quality
- **Saúde:** health_status, access_to_resources

---

## 📊 2. Análise Exploratória de Dados (EDA)

### 2.1 Visão Geral dos Dados

**Estatísticas do Dataset Original:**

| Métrica | Valor |
|---------|-------|
| Total de Registros | 2.495 |
| Total de Features | 13 (originais) |
| Features Numéricas | 5 |
| Features Categóricas | 8 |
| Valores Faltantes | 129 (5.2%) |
| Registros Duplicados | 0 |
| Faixa da Variável Alvo | 45.23 - 100.00 |

**Distribuição de Missing Values:**

| Feature | Missing Count | Missing % |
|---------|--------------|-----------|
| study_hours_per_week | 48 | 1.92% |
| sleep_hours_per_night | 45 | 1.80% |
| tutoring_sessions | 36 | 1.44% |
| **Total** | **129** | **5.17%** |

### 2.2 Análise da Variável Alvo

**Estatísticas de `final_grade`:**

```
Métrica          | Valor
-----------------|--------
Média            | 82.47
Mediana          | 84.12
Desvio Padrão    | 11.85
Mínimo           | 45.23
Q1 (25%)         | 74.56
Q3 (75%)         | 91.38
Máximo           | 100.00
Assimetria       | -0.42 (leve assimetria à esquerda)
Curtose          | -0.15 (distribuição aproximadamente normal)
```

**Interpretação:**
- Distribuição aproximadamente normal com leve concentração em notas mais altas
- Média de 82.47 indica que a maioria dos estudantes tem bom desempenho
- Desvio padrão de 11.85 pontos mostra variabilidade moderada
- Ausência de valores extremos fora do intervalo esperado (0-100)

### 2.3 Análise de Correlações

**Top 10 Features Mais Correlacionadas com final_grade:**

| Feature | Correlação | Interpretação |
|---------|-----------|---------------|
| previous_scores | 0.78 | Forte - Desempenho passado é forte preditor |
| attendance_rate | 0.62 | Moderada/Forte - Presença impacta positivamente |
| study_hours_per_week | 0.58 | Moderada - Mais horas de estudo = melhores notas |
| tutoring_sessions | 0.45 | Moderada - Suporte adicional ajuda |
| sleep_hours_per_night | 0.38 | Fraca/Moderada - Sono adequado é importante |
| health_status | 0.34 | Fraca/Moderada - Saúde afeta desempenho |
| internet_quality | 0.28 | Fraca - Acesso a recursos digitais importa |
| parental_education | 0.25 | Fraca - Background familiar tem influência |
| access_to_resources | 0.22 | Fraca - Recursos materiais ajudam |
| extracurricular_activities | -0.08 | Muito Fraca - Correlação negativa leve |

**Descobertas Importantes:**
1. **previous_scores** é o preditor mais forte (r=0.78) - histórico acadêmico é crucial
2. Fatores comportamentais (attendance, study_hours) têm correlações moderadas
3. Fatores socioeconômicos têm correlações fracas, mas presentes
4. Atividades extracurriculares têm correlação negativa leve (pode indicar sobrecarga)

### 2.4 Análise por Grupos Categóricos

**Desempenho Médio por Gênero:**
```
Gênero     | Média  | Desvio Padrão | Contagem
-----------|--------|---------------|----------
Female     | 83.2   | 11.4          | 1.247
Male       | 81.7   | 12.2          | 1.184
Non-binary | 82.5   | 11.9          | 64
```

**Desempenho por Nível Educacional dos Pais:**
```
Educação Parental | Média  | Contagem
------------------|--------|----------
High School       | 78.3   | 623
Bachelor          | 82.1   | 987
Master            | 85.4   | 542
Doctorate         | 87.2   | 343
```
**Observação:** Correlação positiva entre educação dos pais e desempenho dos filhos.

**Desempenho por Faixa de Renda Familiar:**
```
Renda      | Média  | Mediana | Contagem
-----------|--------|---------|----------
Low        | 79.1   | 80.5    | 798
Medium     | 83.5   | 85.1    | 1.124
High       | 86.8   | 88.4    | 573
```

### 2.5 Análise de Outliers

**Outliers Identificados (método IQR):**

| Feature | Outliers Detectados | % do Dataset | Ação Tomada |
|---------|-------------------|--------------|-------------|
| study_hours_per_week | 34 | 1.36% | Mantidos (valores válidos) |
| sleep_hours_per_night | 28 | 1.12% | Mantidos (valores válidos) |
| previous_scores | 12 | 0.48% | Investigados individualmente |
| final_grade | 8 | 0.32% | Mantidos (notas legítimas) |

**Decisão:** Outliers foram mantidos por representarem casos extremos mas válidos (ex: estudantes excepcionais ou com dificuldades severas).

### 2.6 Principais Insights da EDA

✅ **Achados Relevantes:**

1. **Preditor Principal:** Notas anteriores (previous_scores) são o melhor preditor individual
2. **Importância da Frequência:** Attendance rate tem forte correlação - presença é crucial
3. **Horas de Estudo:** Correlação moderada positiva - quantidade de estudo importa
4. **Fatores Socioeconômicos:** Impacto moderado - renda e educação parental influenciam
5. **Saúde e Sono:** Correlações fracas mas presentes - bem-estar afeta aprendizado
6. **Qualidade de Dados:** 94.8% dos dados completos - boa qualidade geral
7. **Distribuição Balanceada:** Sem desbalanceamento severo entre categorias

---

## 🔧 3. Pré-processamento e Feature Engineering

### 3.1 Tratamento de Valores Faltantes

**Estratégia Aplicada:**

| Feature | Tipo | Missing % | Estratégia | Justificativa |
|---------|------|-----------|------------|---------------|
| study_hours_per_week | Numérica | 1.92% | Mediana | Robusta a outliers, preserva distribuição |
| sleep_hours_per_night | Numérica | 1.80% | Mediana | Menos sensível a valores extremos |
| tutoring_sessions | Numérica | 1.44% | Zero | Missing = sem tutoria (MNAR) |

**Abordagem MNAR (Missing Not At Random):**
Para `tutoring_sessions`, valores ausentes foram interpretados como "nenhuma sessão de tutoria", sendo preenchidos com 0. Esta decisão foi baseada na hipótese de que estudantes que não preencheram este campo provavelmente não participaram de tutoria.

**Resultados:**
- ✅ 100% dos dados completos após tratamento
- ✅ Distribuições originais preservadas
- ✅ Nenhum viés introduzido pela imputação

### 3.2 Feature Engineering

**Novas Features Criadas:**

#### 3.2.1 Transformações Matemáticas

```python
# Transformação Logarítmica (reduzir skewness)
study_hours_week_log = log(study_hours_per_week + 1)

# Transformação de Raiz Quadrada (estabilizar variância)
sleep_hours_sqrt = sqrt(sleep_hours_per_night)
```

**Justificativa:** Transformações não-lineares capturam relações não-lineares e melhoram normalidade.

#### 3.2.2 Features de Interação

```python
# Razão entre horas de estudo e sono
study_sleep_ratio = study_hours_per_week / sleep_hours_per_night

# Indicador de engajamento geral
engagement = (attendance_rate * study_hours_per_week) / 100
```

**Justificativa:** Capturar sinergias entre variáveis que interagem.

#### 3.2.3 Normalização/Padronização

**Técnica:** StandardScaler (z-score normalization)

```python
# Fórmula: z = (x - μ) / σ
z_score = (value - mean) / std_dev
```

**Features Padronizadas:**
- age, previous_scores, attendance_rate
- study_hours_week_log, sleep_hours_sqrt
- study_sleep_ratio, engagement

**Resultado:** Todas as features numéricas com média ≈ 0 e desvio padrão = 1

#### 3.2.4 Encoding de Variáveis Categóricas

**One-Hot Encoding aplicado em:**
- gender (3 categorias → 3 features binárias)
- parental_education (4 categorias → 4 features)
- family_income (3 categorias → 3 features)
- extracurricular_activities (Yes/No → 1 feature)
- tutoring (Yes/No → 1 feature)
- internet_quality (Good/Poor → 2 features)
- health_status (Good/Poor → 2 features)

**Total de Features Após Encoding:** 13 originais → 23 finais

### 3.3 Divisão dos Dados

**Estratégia de Split:**

```
Dataset Completo (2.495 estudantes)
    ↓
    ├─ Treino (60%):     1.497 estudantes  ← Treinar modelos
    ├─ Validação (20%):    499 estudantes  ← Tuning e seleção
    └─ Teste (20%):        499 estudantes  ← Avaliação final
```

**Justificativas:**
- **60% Treino:** Volume suficiente para aprendizado
- **20% Validação:** Adequado para comparação de modelos e tuning
- **20% Teste:** Hold-out final para avaliação não enviesada
- **random_state=42:** Reprodutibilidade dos resultados

**Verificação de Distribuição:**
- ✅ Distribuição de final_grade similar nos 3 conjuntos
- ✅ Proporções de categorias preservadas
- ✅ Sem data leakage entre conjuntos

---

## 🤖 4. Modelagem e Comparação

### 4.1 Modelos Testados

Foram implementados e comparados 4 modelos de regressão:

#### Modelo 1: Regressão Linear
```python
LinearRegression()
```
**Características:**
- Modelo baseline mais simples
- Assume relação linear entre features e target
- Sem hiperparâmetros para tuning
- Alta interpretabilidade

#### Modelo 2: Ridge Regression (Regularização L2)
```python
Ridge(alpha=1.0)
```
**Características:**
- Adiciona penalização L2: λ∑(β²)
- Reduz overfitting em datasets com multicolinearidade
- Mantém todas as features (coeficientes pequenos, não zero)

#### Modelo 3: Lasso Regression (Regularização L1)
```python
Lasso(alpha=0.1)
```
**Características:**
- Adiciona penalização L1: λ∑|β|
- Feature selection automática (alguns coeficientes = 0)
- Útil quando há muitas features irrelevantes

#### Modelo 4: Random Forest Regressor
```python
RandomForestRegressor(n_estimators=100, random_state=42)
```
**Características:**
- Ensemble de árvores de decisão
- Captura relações não-lineares
- Robusto a outliers
- Feature importance nativa

### 4.2 Resultados no Conjunto de Validação

**Comparação de Performance:**

| Modelo | MAE ↓ | RMSE ↓ | R² ↑ | Tempo Treino |
|--------|-------|--------|------|--------------|
| **Random Forest** | **3.54** | **4.78** | **0.88** | 2.3s |
| Ridge | 4.12 | 5.45 | 0.84 | 0.02s |
| Lasso | 4.23 | 5.52 | 0.83 | 0.05s |
| Linear Regression | 4.18 | 5.48 | 0.84 | 0.01s |

**Análise dos Resultados:**

✅ **Random Forest: MELHOR PERFORMANCE**
- MAE mais baixo (3.54 pontos)
- Melhor R² (0.88 - explica 88% da variância)
- Captura relações não-lineares efetivamente

⚠️ **Modelos Lineares: Performance Similar**
- Ridge e Linear Regression praticamente empatados
- Lasso ligeiramente pior (pode ter removido features úteis)
- Extremamente rápidos (< 0.05s)

💡 **Trade-off:**
- Random Forest: Melhor acurácia × Maior complexidade
- Modelos Lineares: Menor acurácia × Maior interpretabilidade

### 4.3 Seleção do Modelo Final

**Decisão:** Random Forest foi selecionado como modelo base para otimização.

**Justificativa:**
1. ✅ Melhor performance em todas as métricas
2. ✅ Melhoria significativa de 14% no MAE vs modelos lineares
3. ✅ Captura interações complexas entre features
4. ✅ Fornece feature importance (interpretabilidade parcial)
5. ✅ Robusto a outliers e dados ruidosos
6. ⚠️ Trade-off aceitável: complexidade × ganho de performance

---

## ⚙️ 5. Otimização de Hiperparâmetros

### 5.1 Processo de Tuning

**Técnica:** Grid Search com 5-Fold Cross-Validation

**Estratégia:**
```python
GridSearchCV(
    estimator=RandomForestRegressor(random_state=42),
    param_grid={...},
    cv=5,
    scoring='neg_mean_absolute_error',
    n_jobs=-1
)
```

**Hiperparâmetros Testados:**

| Hiperparâmetro | Valores Testados | Total |
|----------------|------------------|-------|
| n_estimators | [100, 200, 300] | 3 |
| max_depth | [10, 15, 20, None] | 4 |
| min_samples_split | [2, 5, 10] | 3 |
| min_samples_leaf | [1, 2, 4] | 3 |

**Total de Combinações:** 3 × 4 × 3 × 3 = **108 configurações**  
**Total de Modelos Treinados:** 108 × 5 (CV) = **540 modelos**  
**Tempo Total:** ~8 minutos em CPU de 8 cores

### 5.2 Melhores Hiperparâmetros Encontrados

**Configuração Ótima:**

```python
{
    'n_estimators': 300,        # Mais árvores = maior estabilidade
    'max_depth': 20,            # Profundidade controlada evita overfitting
    'min_samples_split': 2,     # Permite divisões mais específicas
    'min_samples_leaf': 1       # Folhas podem ter 1 amostra
}
```

**Interpretação:**

- **n_estimators=300:** Número alto de árvores melhora estabilidade sem overfitting significativo
- **max_depth=20:** Profundidade moderada balanceia complexidade e generalização
- **min_samples_split=2:** Permite capturar padrões específicos sem forçar generalização excessiva
- **min_samples_leaf=1:** Maior flexibilidade nas folhas (Random Forest é resistente a overfitting)

### 5.3 Comparação: Baseline vs Otimizado

**Resultados no Conjunto de Validação (Cross-Validation):**

| Modelo | MAE | Melhoria |
|--------|-----|----------|
| Random Forest Baseline (default) | 3.54 | - |
| Random Forest Otimizado (Grid Search) | 3.21 | **-9.3%** ↓ |

**Análise:**
- ✅ Otimização reduziu MAE em 0.33 pontos (9.3% de melhoria)
- ✅ Melhoria consistente através dos 5 folds de CV
- ✅ Desvio padrão reduzido (modelo mais estável)

### 5.4 Top 5 Configurações Encontradas

| Rank | n_estimators | max_depth | min_samples_split | min_samples_leaf | MAE (CV) |
|------|-------------|-----------|-------------------|------------------|----------|
| 1 | 300 | 20 | 2 | 1 | 3.21 |
| 2 | 300 | None | 2 | 1 | 3.23 |
| 3 | 200 | 20 | 2 | 1 | 3.25 |
| 4 | 300 | 15 | 2 | 1 | 3.27 |
| 5 | 200 | None | 2 | 1 | 3.28 |

**Observação:** As 5 melhores configurações são muito próximas (diferença < 0.1 ponto), indicando que o modelo é robusto a pequenas variações nos hiperparâmetros.

---

## 📊 6. Avaliação Final no Conjunto de Teste

### 6.1 Performance do Modelo Final

**Modelo:** Random Forest Otimizado (treino + validação combinados)

**Métricas no Conjunto de Teste:**

```
┌─────────────────────────────────────┐
│  MODELO FINAL - CONJUNTO DE TESTE  │
├─────────────────────────────────────┤
│  MAE:   3.45 pontos                 │
│  RMSE:  4.67 pontos                 │
│  R²:    0.89                        │
└─────────────────────────────────────┘
```

**Interpretação das Métricas:**

📊 **MAE = 3.45 pontos**
- Em média, as predições erram por ±3.45 pontos na escala 0-100
- Erro relativo: 3.45/82.47 = **4.18%** da média de notas
- **Excelente** para aplicação prática

📊 **RMSE = 4.67 pontos**
- Penaliza erros grandes mais fortemente
- RMSE > MAE indica presença de alguns erros maiores
- Diferença RMSE-MAE = 1.22 pontos (aceitável)

📊 **R² = 0.89**
- Modelo explica **89% da variância** das notas
- **Excelente** capacidade preditiva
- 11% da variância devido a fatores não capturados

### 6.2 Comparação Final: Baseline vs Otimizado

**Teste Final (hold-out set):**

| Modelo | MAE | RMSE | R² | Melhoria MAE |
|--------|-----|------|-----|--------------|
| Baseline (default) | 3.93 | 5.21 | 0.86 | - |
| Otimizado (Grid Search) | 3.45 | 4.67 | 0.89 | **-12.3%** ↓ |

**Ganhos com Otimização:**
- ✅ MAE: -0.48 pontos (**-12.3%**)
- ✅ RMSE: -0.54 pontos (**-10.4%**)
- ✅ R²: +0.03 (**+3.5%**)

**Conclusão:** A otimização de hiperparâmetros resultou em melhorias significativas e consistentes em todas as métricas.

### 6.3 Análise de Resíduos

**Estatísticas dos Erros de Predição:**

```
Resíduo = Valor Real - Valor Predito

Média dos Resíduos:     -0.08    ← Próximo de zero ✅ (não enviesado)
Mediana dos Resíduos:    0.12
Desvio Padrão:           4.65
Resíduo Mínimo:        -18.34    ← Subestimou em 18 pontos
Resíduo Máximo:         15.67    ← Superestimou em 16 pontos
```

**Interpretação:**
- ✅ Média ≈ 0: Modelo não é enviesado (não tende a super/subestimar sistematicamente)
- ✅ Mediana ≈ 0: Confirmação de ausência de viés
- ✅ Distribuição aproximadamente simétrica
- ⚠️ Alguns casos extremos com erros > 15 pontos (1.2% do teste)

**Distribuição dos Resíduos:**
- 68% dos erros dentro de ±4.65 pontos (1 desvio padrão)
- 95% dos erros dentro de ±9.30 pontos (2 desvios padrão)
- Distribuição aproximadamente normal (bom sinal!)

### 6.4 Análise dos Piores Casos

**10 Predições com Maiores Erros Absolutos:**

| Valor Real | Predito | Erro | Erro Abs | Categoria |
|-----------|---------|------|----------|-----------|
| 95.3 | 76.9 | +18.4 | 18.4 | Subestimado |
| 52.1 | 67.8 | -15.7 | 15.7 | Superestimado |
| 89.7 | 74.5 | +15.2 | 15.2 | Subestimado |
| 98.2 | 84.3 | +13.9 | 13.9 | Subestimado |
| 55.8 | 69.5 | -13.7 | 13.7 | Superestimado |
| 91.4 | 78.2 | +13.2 | 13.2 | Subestimado |
| 58.3 | 71.1 | -12.8 | 12.8 | Superestimado |
| 93.6 | 81.2 | +12.4 | 12.4 | Subestimado |
| 60.1 | 72.3 | -12.2 | 12.2 | Superestimado |
| 87.9 | 75.9 | +12.0 | 12.0 | Subestimado |

**Padrões Identificados:**
- 6 subestimações vs 4 superestimações (razoavelmente balanceado)
- Erros maiores concentrados em extremos da distribuição
- Modelo tende a "regredir à média" em casos extremos
- Possível falta de features para capturar casos outliers

### 6.5 Feature Importance

**Top 15 Features Mais Importantes:**

| Rank | Feature | Importance | Importância Acumulada |
|------|---------|-----------|----------------------|
| 1 | previous_scores | 0.284 | 28.4% |
| 2 | study_hours_week_log | 0.186 | 47.0% |
| 3 | attendance_rate | 0.148 | 61.8% |
| 4 | engagement | 0.092 | 71.0% |
| 5 | age | 0.067 | 77.7% |
| 6 | study_sleep_ratio | 0.054 | 83.1% |
| 7 | sleep_hours_sqrt | 0.042 | 87.3% |
| 8 | tutoring_Yes | 0.031 | 90.4% |
| 9 | health_status_Good | 0.024 | 92.8% |
| 10 | parental_education_Master | 0.019 | 94.7% |
| 11 | internet_quality_Good | 0.015 | 96.2% |
| 12 | family_income_Medium | 0.012 | 97.4% |
| 13 | extracurricular_Yes | 0.009 | 98.3% |
| 14 | gender_Female | 0.007 | 99.0% |
| 15 | family_income_High | 0.005 | 99.5% |

**Principais Insights:**

🔑 **Top 3 Features (61.8% da importância):**
1. **previous_scores (28.4%):** Histórico acadêmico é o preditor dominante
2. **study_hours (18.6%):** Tempo dedicado aos estudos é crucial
3. **attendance_rate (14.8%):** Presença em aulas tem forte impacto

📈 **Features Criadas por Engineering:**
- `engagement` (rank 4): Feature de interação entre attendance e study_hours
- `study_sleep_ratio` (rank 6): Balanceamento estudo/descanso importa
- Transformações log/sqrt melhoraram captura de relações não-lineares

👥 **Fatores Socioeconômicos:**
- Impacto moderado (educação parental, renda familiar)
- Menos importantes que fatores comportamentais
- Ainda presentes no top 15

---

## 💡 7. Conclusões e Discussão

### 7.1 Principais Resultados Alcançados

✅ **Objetivo Principal ATINGIDO:**
- Desenvolvido modelo capaz de prever notas finais com **MAE = 3.45 pontos**
- Performance superior ao objetivo (RMSE < 6.0): **RMSE = 4.67**
- Modelo explica **89% da variância** (R² = 0.89)

✅ **Modelo Robusto e Generalizado:**
- Performance consistente entre validação e teste
- Diferença mínima entre CV e teste (3.21 vs 3.45)
- Ausência de overfitting significativo

✅ **Identificação de Features Críticas:**
- Histórico acadêmico (previous_scores) é o preditor mais forte
- Hábitos de estudo (attendance, study_hours) são cruciais
- Fatores criados por feature engineering agregaram valor

### 7.2 Resposta às Questões de Pesquisa

**Q1: É possível prever com precisão o desempenho acadêmico final?**
> **Resposta:** Sim. O modelo Random Forest otimizado alcançou MAE de 3.45 pontos (erro médio de ~4.2%), demonstrando que é possível fazer predições úteis e precisas.

**Q2: Quais fatores mais influenciam o desempenho acadêmico?**
> **Resposta:** Em ordem de importância:
> 1. Histórico acadêmico anterior (28.4%)
> 2. Horas de estudo dedicadas (18.6%)
> 3. Taxa de frequência às aulas (14.8%)
> 4. Engajamento geral (9.2%)
> 5. Idade/maturidade (6.7%)

**Q3: Fatores socioeconômicos impactam significativamente?**
> **Resposta:** Sim, mas com impacto moderado. Educação parental e renda familiar aparecem entre as 15 features mais importantes, porém com menor peso que fatores comportamentais modificáveis.

**Q4: O modelo pode ser usado para intervenções preventivas?**
> **Resposta:** Sim. Com erro médio de 3.45 pontos, o modelo pode identificar com confiança estudantes em risco de desempenho abaixo de 70 pontos, permitindo intervenções antecipadas.

### 7.3 Limitações do Estudo

⚠️ **Limitações Identificadas:**

1. **Dataset Sintético:**
   - Dados gerados artificialmente podem não capturar toda complexidade do mundo real
   - Relações entre variáveis podem ser simplificadas

2. **Features Faltantes:**
   - Fatores psicológicos não incluídos (motivação, ansiedade, autoestima)
   - Qualidade dos professores e métodos de ensino não considerados
   - Eventos de vida significativos (problemas familiares, saúde mental)

3. **Causalidade vs Correlação:**
   - Modelo identifica correlações, não causalidade
   - Não é possível afirmar que aumentar study_hours CAUSA melhores notas (pode ser correlação)

4. **Casos Extremos:**
   - Erros maiores (>15 pontos) em ~1% dos casos
   - Modelo tende a "regredir à média" em outliers

5. **Generalização:**
   - Modelo treinado em uma população específica
   - Pode não generalizar bem para outras instituições/países/contextos

6. **Temporalidade:**
   - Predições assumem que características se mantêm constantes
   - Mudanças ao longo do semestre não são capturadas

### 7.4 Aplicações Práticas

🎓 **Usos Recomendados do Modelo:**

1. **Sistema de Alerta Precoce:**
   - Identificar estudantes com predição < 70 pontos no início do semestre
   - Acionar programas de tutoria e suporte acadêmico

2. **Alocação de Recursos:**
   - Priorizar estudantes com maior risco de baixo desempenho
   - Otimizar distribuição de tutores e recursos de apoio

3. **Análise de Fatores:**
   - Identificar quais características podem ser modificadas (attendance, study_hours)
   - Focar intervenções em fatores controláveis

4. **Monitoramento Institucional:**
   - Acompanhar tendências de desempenho ao longo dos semestres
   - Avaliar efetividade de intervenções implementadas

5. **Aconselhamento Personalizado:**
   - Fornecer feedback individualizado baseado em predições
   - Sugerir mudanças específicas nos hábitos de estudo

### 7.5 Trabalhos Futuros

🔮 **Melhorias e Extensões Propostas:**

1. **Dados Temporais:**
   - Coletar dados ao longo do semestre (não apenas início)
   - Implementar modelos de séries temporais ou LSTM
   - Capturar trajetórias de aprendizado

2. **Features Adicionais:**
   - Métricas de engajamento online (se EAD)
   - Dados de avaliações parciais
   - Histórico de interações com professores
   - Fatores psicológicos (surveys de motivação/ansiedade)

3. **Modelos Avançados:**
   - Testar XGBoost, LightGBM, CatBoost
   - Implementar ensemble stacking
   - Redes neurais profundas

4. **Interpretabilidade:**
   - SHAP values para explicações individuais
   - LIME para casos específicos
   - Curvas de dependência parcial (PDP)

5. **Deployment:**
   - API REST para predições em tempo real
   - Dashboard interativo para gestores acadêmicos
   - Integração com sistemas acadêmicos existentes

6. **Validação Externa:**
   - Testar modelo em outras instituições
   - Avaliar generalização cross-domain
   - Ajuste fino para diferentes contextos

7. **Análise de Intervenções:**
   - Estudos A/B para medir impacto de ações sugeridas pelo modelo
   - Avaliação de cost-benefit das intervenções
   - Refinamento contínuo baseado em feedback

### 7.6 Lições Aprendidas

📚 **Principais Aprendizados:**

**Técnicos:**
1. Feature engineering é crucial - features criadas (engagement, study_sleep_ratio) tiveram alto impacto
2. Otimização de hiperparâmetros vale o esforço - 12% de melhoria no MAE
3. Validação cruzada é essencial para confiabilidade dos resultados
4. Random Forest balanceia bem interpretabilidade e performance

**Práticos:**
1. Qualidade dos dados é fundamental - tratamento adequado de missing values importa
2. Análise exploratória direciona decisões de modelagem
3. Comparação de múltiplos modelos evita viés de seleção
4. Documentação clara facilita reprodutibilidade

**Conceituais:**
1. Trade-off entre interpretabilidade e acurácia é real
2. Métricas devem ser escolhidas de acordo com o problema de negócio
3. Modelo não captura causalidade - cuidado com interpretações
4. Validação no mundo real é crítica antes de deployment

---

## 📚 8. Referências

**Documentação Técnica:**

1. **Scikit-learn Documentation**  
   https://scikit-learn.org/stable/  
   Referência principal para implementação de modelos e métricas

2. **Pandas Documentation**  
   https://pandas.pydata.org/docs/  
   Manipulação e análise de dados

3. **Matplotlib & Seaborn**  
   https://matplotlib.org/ e https://seaborn.pydata.org/  
   Visualização de dados

**Artigos e Livros:**

4. Breiman, L. (2001). "Random Forests". Machine Learning, 45(1), 5-32.  
   Artigo original sobre Random Forests

5. Hastie, T., Tibshirani, R., & Friedman, J. (2009). "The Elements of Statistical Learning"  
   Referência clássica em Machine Learning

6. Géron, A. (2019). "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow"  
   Guia prático de implementação

**Tutoriais e Recursos Online:**

7. Kaggle Learn - Machine Learning  
   https://www.kaggle.com/learn/machine-learning  
   Tutoriais práticos sobre ML

8. Google's Machine Learning Crash Course  
   https://developers.google.com/machine-learning/crash-course  
   Curso introdutório gratuito

9. Cross Validated (Stack Exchange)  
   https://stats.stackexchange.com/  
   Comunidade para dúvidas técnicas

**Trabalhos Relacionados:**

10. Romero, C., & Ventura, S. (2020). "Educational data mining and learning analytics"  
    Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 10(3)

11. Kabathova, J., & Drlik, M. (2021). "Towards Predicting Student's Dropout in University Courses"  
    Applied Sciences, 11(7), 3103

---

## 📎 Anexos

### Anexo A: Estrutura do Repositório

```
template-repo/
├── README.md                                 # Visão geral do projeto
├── requirements.txt                          # Dependências Python
│
├── data/                                     # Dados do projeto
│   ├── students_performance.csv             # Dataset original
│   ├── students_clean.csv                   # Dados após limpeza
│   ├── X_train.csv, X_val.csv, X_test.csv  # Features dos conjuntos
│   ├── y_train.csv, y_val.csv, y_test.csv  # Targets dos conjuntos
│   └── baseline_metrics.csv                 # Métricas baseline
│
├── etapas/                                   # Notebooks das etapas
│   ├── etapa1/
│   │   └── GABARITO_ETAPA1_students.ipynb  # EDA completa
│   ├── etapa2/
│   │   └── GABARITO_ETAPA2_students.ipynb  # Pré-processamento
│   ├── etapa3/
│   │   └── GABARITO_ETAPA3_students.ipynb  # Modelagem baseline
│   ├── etapa4/
│   │   └── GABARITO_ETAPA4_students.ipynb  # Otimização
│   └── etapa5/
│       └── GABARITO_RELATORIO_FINAL_students.md  # Este relatório
│
└── models/                                   # Modelos treinados
    ├── modelo_final_rf_otimizado.joblib     # Modelo final
    └── modelo_info.json                     # Metadados do modelo
```

### Anexo B: Comandos para Reprodução

**1. Configurar Ambiente:**
```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente (Linux/Mac)
source .venv/bin/activate

# Ativar ambiente (Windows)
.venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

**2. Executar Análises:**
```bash
# Navegar para diretório do projeto
cd template-repo/

# Executar notebooks em ordem
jupyter notebook etapas/etapa1/GABARITO_ETAPA1_students.ipynb
jupyter notebook etapas/etapa2/GABARITO_ETAPA2_students.ipynb
jupyter notebook etapas/etapa3/GABARITO_ETAPA3_students.ipynb
jupyter notebook etapas/etapa4/GABARITO_ETAPA4_students.ipynb
```

**3. Verificar Resultados:**
```bash
# Listar arquivos gerados
ls -lh data/
ls -lh models/

# Verificar modelo salvo
python -c "import joblib; model = joblib.load('models/modelo_final_rf_otimizado.joblib'); print(model)"
```

### Anexo C: Ambiente Computacional

**Especificações do Sistema:**
- **OS:** Ubuntu 20.04 LTS / Windows 11 / macOS Monterey
- **Python:** 3.10.12
- **CPU:** Intel i7 / AMD Ryzen 7 (8 cores)
- **RAM:** 16 GB
- **Tempo Total de Execução:** ~15 minutos

**Bibliotecas Principais:**
```
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
matplotlib==3.7.2
seaborn==0.12.2
joblib==1.3.1
scipy==1.11.1
jupyter==1.0.0
```

### Anexo D: Resultados Detalhados das Etapas

**Etapa 1 - EDA:**
- ✅ 2.495 registros analisados
- ✅ 13 features originais exploradas
- ✅ 5.2% missing values identificados
- ✅ Correlações calculadas e visualizadas
- ✅ Outliers identificados (mantidos)

**Etapa 2 - Pré-processamento:**
- ✅ 100% dos dados completados (imputação)
- ✅ 23 features após feature engineering
- ✅ Normalização aplicada (StandardScaler)
- ✅ One-hot encoding em 8 variáveis categóricas
- ✅ Split 60/20/20 realizado

**Etapa 3 - Modelagem:**
- ✅ 4 modelos testados e comparados
- ✅ Random Forest selecionado (MAE=3.54)
- ✅ Baseline estabelecido
- ✅ Modelo e dados salvos

**Etapa 4 - Otimização:**
- ✅ Grid Search com 108 combinações
- ✅ 5-fold CV em cada configuração
- ✅ Melhor configuração identificada
- ✅ Melhoria de 12.3% no MAE
- ✅ Modelo final avaliado no teste (MAE=3.45)

---

## 🎯 Considerações Finais

Este projeto demonstrou com sucesso a aplicação de técnicas de Machine Learning para predição de desempenho acadêmico. O modelo desenvolvido alcançou performance excelente (MAE = 3.45, R² = 0.89) e pode ser utilizado como ferramenta de suporte à decisão para intervenções educacionais preventivas.

Os principais fatores identificados como determinantes do desempenho acadêmico foram:
1. Histórico acadêmico anterior (28.4% de importância)
2. Horas de estudo dedicadas (18.6%)
3. Taxa de frequência às aulas (14.8%)

Estes resultados reforçam a importância de hábitos de estudo consistentes e presença regular, fatores modificáveis que podem ser alvos de intervenções institucionais.

O processo completo - desde EDA até otimização - seguiu boas práticas de Machine Learning, incluindo validação cruzada, análise de resíduos, feature engineering e documentação detalhada, garantindo reprodutibilidade e confiabilidade dos resultados.

---

**Projeto desenvolvido como parte da disciplina:**  
**Introdução à Machine Learning - 2025.2**  
**Professor:** Professor Durval  
**Instituição:** [Nome da Instituição]

**Repositório:** https://github.com/professor-durval-ml/uninassau-atividade-alunos-ml-regressao

---

*Fim do Relatório Final*
