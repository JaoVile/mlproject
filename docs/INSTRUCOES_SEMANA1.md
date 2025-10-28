# 📊 Semana 1: Análise Exploratória de Dados (EDA)

**Prazo de Entrega:** [Data será informada pelo professor]
**Peso:** 25% da nota do projeto (1.0 ponto)
**Entregável:** `notebooks/01_EDA.ipynb`

---

## 🎯 Objetivos da Semana

Ao final desta semana, você deve:

1. **Conhecer profundamente o dataset** - Entender cada variável, seus valores e significados
2. **Identificar problemas de qualidade** - Encontrar valores faltantes, outliers, inconsistências
3. **Explorar relações entre variáveis** - Descobrir correlações e padrões
4. **Comunicar descobertas** - Documentar tudo em um notebook claro e organizado

**⚠️ IMPORTANTE:** Esta etapa é APENAS análise. **NÃO** trate/corrija problemas ainda!

---

## 📋 O Que Você Vai Entregar

### Arquivo Principal
- **`notebooks/01_EDA.ipynb`** - Notebook Jupyter com toda a análise exploratória

### Conteúdo Obrigatório do Notebook

O notebook deve incluir as seguintes seções (use headers markdown):

```markdown
# 1. Importação de Bibliotecas
# 2. Carregamento dos Dados
# 3. Visão Geral do Dataset
# 4. Análise de Valores Faltantes
# 5. Análise da Variável Alvo (final_grade)
# 6. Análise Univariada - Variáveis Numéricas
# 7. Análise Univariada - Variáveis Categóricas
# 8. Análise de Correlações
# 9. Análise Bivariada (Features vs Target)
# 10. Identificação de Outliers
# 11. Conclusões e Descobertas Principais
```

---

## 🔍 Análises Obrigatórias

### 1. Importação de Bibliotecas (5 min)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Configurações
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
pd.set_option('display.max_columns', None)
```

**📝 Documente:** Explique para que serve cada biblioteca

---

### 2. Carregamento dos Dados (10 min)

```python
df = pd.read_csv('../data/raw/students_performance.csv')
```

**Análises obrigatórias:**
- `df.head(10)` - Primeiras linhas
- `df.tail(10)` - Últimas linhas
- `df.shape` - Dimensões
- `df.info()` - Tipos de dados
- `df.describe()` - Estatísticas descritivas

**📝 Documente:** Quantas linhas? Quantas colunas? Primeiras observações?

---

### 3. Visão Geral do Dataset (15 min)

**Separe variáveis por tipo:**

```python
# Identificar tipos
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

print(f"Variáveis numéricas ({len(numeric_cols)}): {numeric_cols}")
print(f"Variáveis categóricas ({len(categorical_cols)}): {categorical_cols}")
```

**Checklist:**
- [ ] Listou todas as variáveis numéricas
- [ ] Listou todas as variáveis categóricas
- [ ] Identificou a variável alvo (`final_grade`)
- [ ] Identificou variáveis de identificação (`student_id`)

**📝 Documente:** Qual é a variável alvo? Quais são as features?

---

### 4. Análise de Valores Faltantes (30 min)

**Análises obrigatórias:**

```python
# Contar valores faltantes
missing = df.isnull().sum()
missing_pct = (df.isnull().sum() / len(df)) * 100

# Criar DataFrame de missing
missing_df = pd.DataFrame({
    'Missing': missing,
    'Percentage': missing_pct
}).sort_values('Percentage', ascending=False)

print(missing_df[missing_df['Missing'] > 0])
```

**Visualização obrigatória:**
- Gráfico de barras mostrando % de missing por variável

**Checklist:**
- [ ] Calculou total de valores faltantes
- [ ] Calculou % de missing por variável
- [ ] Criou visualização (barras ou heatmap)
- [ ] Identificou padrões de missing (aleatório ou sistemático?)
- [ ] Listou variáveis com maior % de missing

**📝 Documente:**
- Qual variável tem mais missing?
- Missing é aleatório ou há padrão?
- Sugestões de tratamento (não implementar ainda!)

---

### 5. Análise da Variável Alvo: final_grade (45 min)

**Estatísticas obrigatórias:**
```python
print(f"Média: {df['final_grade'].mean():.2f}")
print(f"Mediana: {df['final_grade'].median():.2f}")
print(f"Desvio Padrão: {df['final_grade'].std():.2f}")
print(f"Mínimo: {df['final_grade'].min():.2f}")
print(f"Máximo: {df['final_grade'].max():.2f}")
print(f"Assimetria (Skewness): {df['final_grade'].skew():.2f}")
print(f"Curtose (Kurtosis): {df['final_grade'].kurtosis():.2f}")
```

**Visualizações obrigatórias:**
1. **Histograma** com linha de densidade (KDE)
2. **Boxplot** para identificar outliers
3. **Q-Q Plot** para testar normalidade

**Testes estatísticos:**
```python
# Teste de normalidade (Shapiro-Wilk)
from scipy.stats import shapiro
stat, p_value = shapiro(df['final_grade'].dropna())
print(f"Shapiro-Wilk p-value: {p_value:.4f}")
# Se p > 0.05: distribuição normal
# Se p < 0.05: distribuição NÃO normal
```

**Checklist:**
- [ ] Calculou todas as estatísticas descritivas
- [ ] Criou histograma com KDE
- [ ] Criou boxplot
- [ ] Criou Q-Q plot
- [ ] Executou teste de normalidade
- [ ] Identificou presença de outliers

**📝 Documente:**
- A distribuição é normal?
- Há assimetria? Para qual lado?
- Há outliers? Quantos?
- Faixa de valores mais comum?

---

### 6. Análise Univariada - Variáveis Numéricas (60 min)

**Para CADA variável numérica (exceto student_id e final_grade):**

1. **Estatísticas descritivas**
2. **Histograma**
3. **Boxplot**
4. **Identificação de outliers (método IQR)**

**Exemplo de código:**
```python
# Para cada variável numérica
for col in ['study_hours_week', 'attendance_rate', 'previous_scores', 'sleep_hours', 'age']:
    print(f"\n{'='*50}")
    print(f"Análise de: {col}")
    print(f"{'='*50}")

    # Estatísticas
    print(df[col].describe())

    # Visualização (histograma + boxplot)
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    axes[0].hist(df[col].dropna(), bins=30, edgecolor='black')
    axes[0].set_title(f'Histograma: {col}')
    axes[0].set_xlabel(col)

    axes[1].boxplot(df[col].dropna(), vert=True)
    axes[1].set_title(f'Boxplot: {col}')
    axes[1].set_ylabel(col)

    plt.tight_layout()
    plt.show()

    # Outliers (método IQR)
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"Outliers: {len(outliers)} ({len(outliers)/len(df)*100:.2f}%)")
```

**Checklist:**
- [ ] Analisou todas as variáveis numéricas
- [ ] Criou visualizações para cada uma
- [ ] Identificou outliers em cada uma
- [ ] Documentou descobertas importantes

**📝 Documente para cada variável:**
- Faixa de valores (min, max)
- Distribuição (normal, assimétrica, bimodal?)
- Presença de outliers
- Valores impossíveis ou suspeitos

---

### 7. Análise Univariada - Variáveis Categóricas (45 min)

**Para CADA variável categórica:**

1. **Contagem de valores únicos**
2. **Frequência de cada categoria**
3. **Gráfico de barras**
4. **Identificação de problemas (formatação, erros)**

**Exemplo de código:**
```python
for col in categorical_cols:
    if col == 'student_id':
        continue  # Pular ID

    print(f"\n{'='*50}")
    print(f"Análise de: {col}")
    print(f"{'='*50}")

    # Contagens
    print(df[col].value_counts())
    print(f"\nValores únicos: {df[col].nunique()}")
    print(f"Missing: {df[col].isnull().sum()} ({df[col].isnull().sum()/len(df)*100:.2f}%)")

    # Visualização
    plt.figure(figsize=(10, 4))
    df[col].value_counts().plot(kind='barh')
    plt.title(f'Distribuição: {col}')
    plt.xlabel('Frequência')
    plt.tight_layout()
    plt.show()
```

**Checklist:**
- [ ] Analisou todas as variáveis categóricas
- [ ] Listou valores únicos de cada uma
- [ ] Criou gráfico de barras para cada uma
- [ ] Identificou problemas de formatação

**📝 Documente:**
- Desbalanceamento entre categorias?
- Problemas de formatação (espaços, maiúsculas)?
- Categorias inesperadas?

---

### 8. Análise de Correlações (45 min)

**Matriz de correlação completa:**

```python
# Calcular correlações (apenas numéricas)
corr_matrix = df[numeric_cols].corr()

# Visualização: Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, square=True, linewidths=1)
plt.title('Matriz de Correlação - Features Numéricas', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Correlação com a variável alvo:**
```python
# Correlação com final_grade
target_corr = df[numeric_cols].corr()['final_grade'].sort_values(ascending=False)
print("Correlação com final_grade:")
print(target_corr)

# Visualização
plt.figure(figsize=(10, 6))
target_corr.drop('final_grade').plot(kind='barh')
plt.title('Correlação das Features com final_grade')
plt.xlabel('Correlação')
plt.axvline(0, color='black', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
```

**Checklist:**
- [ ] Criou matriz de correlação completa (heatmap)
- [ ] Listou correlações com final_grade (ordenadas)
- [ ] Criou gráfico de correlação com target
- [ ] Identificou multicolinearidade (correlação alta entre features)

**📝 Documente:**
- Qual feature tem maior correlação com final_grade?
- Há features muito correlacionadas entre si (multicolinearidade)?
- Correlações surpreendentes ou contraintuitivas?

---

### 9. Análise Bivariada (60 min)

**Features Categóricas vs final_grade:**

Para cada variável categórica, analise como ela afeta a nota final:

```python
for col in categorical_cols:
    if col == 'student_id':
        continue

    print(f"\n{'='*50}")
    print(f"{col} vs final_grade")
    print(f"{'='*50}")

    # Estatísticas por categoria
    print(df.groupby(col)['final_grade'].describe())

    # Visualização: Boxplot
    plt.figure(figsize=(10, 6))
    df.boxplot(column='final_grade', by=col, figsize=(10, 6))
    plt.suptitle('')  # Remove título automático
    plt.title(f'Distribuição de final_grade por {col}')
    plt.ylabel('Nota Final')
    plt.xlabel(col)
    plt.tight_layout()
    plt.show()
```

**Checklist:**
- [ ] Analisou todas as categóricas vs final_grade
- [ ] Criou boxplots para visualizar diferenças
- [ ] Calculou média/mediana por categoria
- [ ] Identificou categorias com melhor/pior desempenho

**📝 Documente:**
- Quais categorias têm melhor desempenho?
- Diferenças são significativas?
- Há sobreposição entre distribuições?

---

### 10. Identificação de Outliers (30 min)

**Resumo consolidado de outliers:**

```python
print("RESUMO DE OUTLIERS (Método IQR)")
print("="*50)

outlier_summary = {}

for col in numeric_cols:
    if col in ['student_id']:
        continue

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)]

    outlier_summary[col] = {
        'count': len(outliers),
        'percentage': len(outliers)/len(df)*100,
        'lower_bound': lower,
        'upper_bound': upper
    }

# Exibir resumo
for col, info in outlier_summary.items():
    print(f"\n{col}:")
    print(f"  Outliers: {info['count']} ({info['percentage']:.2f}%)")
    print(f"  Limites: [{info['lower_bound']:.2f}, {info['upper_bound']:.2f}]")
```

**Checklist:**
- [ ] Identificou outliers em todas as variáveis numéricas
- [ ] Listou quantidade e % de outliers
- [ ] Diferenciou outliers legítimos de erros

**📝 Documente:**
- Quais variáveis têm mais outliers?
- Outliers são legítimos ou erros?
- Valores impossíveis encontrados?

---

### 11. Conclusões e Descobertas (30 min)

**Escreva um resumo executivo da sua análise:**

Use células markdown para responder:

1. **Principais Características do Dataset**
   - Tamanho, tipos de variáveis
   - Qualidade geral dos dados

2. **Problemas Identificados**
   - Valores faltantes (onde e quanto)
   - Outliers (quais variáveis)
   - Valores impossíveis ou inconsistências
   - Problemas de formatação

3. **Descobertas sobre a Variável Alvo**
   - Distribuição de final_grade
   - Faixa de valores mais comum
   - Presença de outliers

4. **Features Mais Importantes**
   - Quais têm maior correlação com final_grade?
   - Quais categorias impactam mais o desempenho?

5. **Próximos Passos (Semana 2)**
   - Como tratar valores faltantes?
   - Como tratar outliers?
   - Que transformações serão necessárias?

**📝 Exemplo de conclusão:**
```markdown
## Principais Descobertas

1. **Qualidade dos Dados:**
   - Dataset tem 2.510 registros e 13 features
   - ~8% de valores faltantes, principalmente em internet_quality (6.2%)
   - 42 outliers em study_hours_week, 18 em attendance_rate

2. **Variável Alvo (final_grade):**
   - Distribuição aproximadamente normal (Shapiro p=0.06)
   - Média: 82.5, Mediana: 84.0, Std: 12.3
   - Faixa: 45-100 pontos

3. **Features Mais Correlacionadas:**
   - previous_scores (r=0.75) ⭐ Melhor preditor
   - study_hours_week (r=0.45)
   - attendance_rate (r=0.38)

4. **Insights Importantes:**
   - Alunos com tutoria têm média 5 pontos superior
   - Renda familiar tem correlação fraca (r=0.12)
   - Existe multicolinearidade entre study_hours e attendance (r=0.62)
```

---

## ✅ Critérios de Avaliação

Seu notebook será avaliado pelos seguintes critérios:

| Critério | Peso | Descrição |
|----------|:----:|-----------|
| **Completude** | 30% | Todas as análises obrigatórias foram feitas? |
| **Visualizações** | 20% | Gráficos claros, com títulos, labels e legendas? |
| **Documentação** | 25% | Interpretações em markdown? Descobertas explicadas? |
| **Qualidade Técnica** | 15% | Código funciona? Sem erros? Organizado? |
| **Insights** | 10% | Identificou padrões interessantes? Conclusões válidas? |

### Detalhamento:

**Completude (30%):**
- ✅ Todas as 11 seções estão presentes
- ✅ Análises obrigatórias realizadas
- ✅ Todas as variáveis analisadas

**Visualizações (20%):**
- ✅ Mínimo 15 gráficos
- ✅ Títulos descritivos
- ✅ Labels nos eixos
- ✅ Legendas quando necessário
- ✅ Tamanho apropriado (figsize)

**Documentação (25%):**
- ✅ Células markdown explicando cada análise
- ✅ Interpretação dos resultados
- ✅ Conclusões em seção final
- ✅ Código comentado (quando complexo)

**Qualidade Técnica (15%):**
- ✅ Notebook executa do início ao fim ("Restart & Run All")
- ✅ Sem erros
- ✅ Código organizado e limpo
- ✅ Nomes de variáveis descritivos

**Insights (10%):**
- ✅ Descobertas interessantes
- ✅ Padrões identificados
- ✅ Recomendações para próximas etapas

---

## 🚫 Erros Comuns a Evitar

### ❌ NÃO FAÇA:

1. **Tratar dados nesta etapa**
   - NÃO preencha valores faltantes
   - NÃO remova outliers
   - NÃO faça encoding de categóricas
   - **Esta etapa é APENAS análise!**

2. **Visualizações sem contexto**
   - NÃO crie gráficos sem título
   - NÃO esqueça labels nos eixos
   - NÃO use cores confusas

3. **Código sem documentação**
   - NÃO deixe apenas código
   - NÃO esqueça de interpretar resultados
   - NÃO omita conclusões

4. **Análise superficial**
   - NÃO faça apenas o mínimo
   - NÃO ignore variáveis
   - NÃO copie código sem entender

---

## 💡 Dicas de Sucesso

### 📚 Recursos Úteis

- **Código exemplo:** `notebooks/00_EXEMPLO_STARTER.py`
- **Boas práticas:** `docs/BOAS_PRATICAS.md`
- **Documentação dataset:** `data/raw/README.md`

### 🎯 Organização

1. **Use headers markdown** para separar seções
2. **Adicione índice** no início do notebook
3. **Numere suas descobertas** para facilitar referência
4. **Use cores consistentes** nas visualizações

### 🔍 Exploração Profunda

- Vá **além do obrigatório**
- Teste **hipóteses** sobre os dados
- Procure **padrões interessantes**
- Seja **curioso**!

### 🧪 Antes de Entregar

**Checklist final:**
- [ ] Execute "Restart Kernel & Run All Cells"
- [ ] Verifique que não há erros
- [ ] Todas as visualizações aparecem
- [ ] Markdown sem erros de digitação
- [ ] Conclusões escritas
- [ ] Commit e push realizados

---

## 📦 Como Entregar

### 1. Certifique-se de que está na branch correta

```bash
# Ver branch atual
git branch

# Se não estiver na main, volte
git checkout main
```

### 2. Salve e teste o notebook

- Salve o notebook
- Execute "Kernel → Restart & Run All"
- Verifique que tudo funciona

### 3. Commit e Push

```bash
git add notebooks/01_EDA.ipynb
git commit -m "feat: Adiciona análise exploratória completa (Semana 1)

- Análise de valores faltantes
- Análise univariada de todas as variáveis
- Matriz de correlação
- Análise bivariada
- Identificação de outliers
- Conclusões e descobertas"

git push origin main
```

### 4. Verifique no GitHub

- Acesse seu repositório no GitHub
- Confirme que o arquivo aparece
- Teste se o notebook renderiza corretamente

---

## ⏰ Gestão de Tempo Sugerida

| Atividade | Tempo Estimado |
|-----------|:--------------:|
| Setup e leitura das instruções | 30 min |
| Carregamento e visão geral | 30 min |
| Análise de missing values | 30 min |
| Análise da variável alvo | 45 min |
| Análise univariada (numéricas) | 90 min |
| Análise univariada (categóricas) | 45 min |
| Análise de correlações | 45 min |
| Análise bivariada | 60 min |
| Identificação de outliers | 30 min |
| Conclusões e documentação | 45 min |
| Revisão e testes finais | 30 min |
| **TOTAL** | **~8 horas** |

**Dica:** Divida em múltiplas sessões ao longo da semana!

---

## 🆘 Precisa de Ajuda?

- 📖 Consulte `docs/BOAS_PRATICAS.md`
- 💻 Veja `notebooks/00_EXEMPLO_STARTER.py`
- 📚 Leia `data/raw/README.md`
- 👥 Discuta com seu grupo
- 👨‍🏫 Procure o professor

---

**Boa análise! Descubra os segredos escondidos nos dados!** 🔍🚀

*Última atualização: Outubro 2027*
