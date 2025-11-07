# Etapa 2: Pré-processamento de Dados

**Prazo:** [Consultar calendário]
**Peso:** 20% do projeto (2.0 pontos)
- 1.7 pontos: Notebook e arquivos
- 0.3 pontos: Apresentação

**Tempo estimado:** 6-8 horas

---

## 🎯 Objetivo

Limpar e preparar os dados para a modelagem.

---

## 📦 Entregas

1. **Notebook:** `notebooks/02_Preprocessamento.ipynb`
2. **Dataset limpo:** `data/students_clean.csv`
3. **Scaler salvo:** `models/scaler.pkl`
4. **🎤 Apresentação:** 5 minutos 

---

## 🔧 Tarefas (12 questões)

### **Parte 1: Valores Faltantes** (2 questões)

**Fazer:**
- Imputar numéricas com média ou mediana
- Imputar categóricas com moda
- Criar 2 gráfico (antes vs depois)

👉 **Lembrete rápido**
- Média funciona melhor quando a distribuição é equilibrada (sem outliers fortes).
- Mediana é mais robusta a outliers; use-a quando a coluna for torta ou tiver valores extremos.

**Responder:**

**Q1.** Para cada variável numérica, você usou média ou mediana? Por quê?

**Q2.** Como evitar data leakage na Etapa 3?

---

### **Parte 2: Outliers** (2 questões)

**Fazer:**
- Detectar outliers (método IQR)
- Decidir: remover ou manter
- Criar 1 boxplot (antes vs depois)

📊 **Entendendo o boxplot e o método IQR**
- **Q1 (1º quartil):** 25% dos valores estão abaixo desse ponto.
- **Q3 (3º quartil):** 75% dos valores estão abaixo desse ponto.
- **IQR (Q3 - Q1):** faixa onde está a metade central dos dados.
- **Outliers (regra 1.5×IQR):** valores abaixo de Q1 - 1.5×IQR ou acima de Q3 + 1.5×IQR.
- No boxplot: a caixa vai de Q1 a Q3, a linha no meio é a mediana; os “pontinhos” fora dos bigodes são outliers.

**Responder:**

**Q3.** Quantos outliers você detectou em cada coluna?

**Q4.** Você removeu algum outlier? Por quê?

---

### **Parte 3: Limpeza** (1 questão)

**Fazer:**
- Remover duplicatas

**Responder:**

**Q5.** Quantas duplicatas você removeu?

---

### **Parte 4: Distribuições e Assimetria (Skewness)** (2 questões)

**Fazer:**
- Calcular skewness das colunas numéricas
- Identificar distribuições assimétricas (skew > 0.5 ou < -0.5)
- Aplicar transformação (log ou sqrt) se necessário

💡 **Por que olhar para skewness?** Distribuições muito assimétricas podem prejudicar modelos lineares. Transformações ajudam a aproximar a curva de uma forma mais “normal” e reduzem o impacto de outliers.

**Responder:**

**Q6.** Quais colunas têm distribuição assimétrica (skew > 0.5)?

**Q7.** Você aplicou transformação em alguma coluna? Qual?

**📚 Para entender:**
- **Skewness > 0:** Cauda à direita (assimetria positiva)
- **Skewness < 0:** Cauda à esquerda (assimetria negativa)
- **|Skewness| > 0.5:** Considere transformar (log, sqrt, Box-Cox)

---

### **Parte 5: Encoding** (2 questões)

**Fazer:**
- One-Hot para nominais (usar `drop_first=True`)
- LabelEncoder para variáveis ordinais

🔠 **Qual encoder usar?**
- **One-Hot Encoder:** use para variáveis **nominais** (categorias sem ordem), ex.: `gender`, `city`. Cria uma coluna 0/1 para cada categoria e evita comparar “maior/menor”.
- **LabelEncoder:** use apenas para variáveis **ordinais** (categorias com ordem lógica), ex.: `education = {fundamental < médio < superior}`. Converte as categorias em números inteiros preservando a ordem.
- `drop_first=True` remove uma das colunas One-Hot para evitar multicolinearidade (informação redundante) e funciona como categoria de referência.

**Responder:**

**Q8.** Quantas colunas One-Hot foram criadas?

**Q9.** Por que usar `drop_first=True`?

---

### **Parte 6: Feature Engineering** (1 questão)

**Fazer:**
- Criar **2 novas features**
- Calcular correlação com target(alvo)

**Responder:**

**Q10.** Liste as 2 features criadas e explique cada uma.

---

### **Parte 7: Normalização** (2 questões)

**Fazer:**
- Aplicar StandardScaler
- **Salvar scaler:** `joblib.dump(scaler, 'models/scaler.pkl')`

📏 **O que é um scaler?**
- O `StandardScaler` padroniza colunas numéricas para terem **média 0** e **desvio-padrão 1**.
- Isso evita que variáveis em escalas diferentes (ex.: renda vs. horas de estudo) dominem o modelo.
- Sempre `fit` no treino e `transform` no treino **e** no teste para evitar data leakage.
- Salvar o scaler permite aplicar a mesma transformação em dados futuros (deploy).

**Responder:**

**Q11.** Quantas features você escalou?

**Q12.** Por que salvar o scaler?

---

## 📊 Visualizações (mínimo 4)

1. **Missing:** Barras (antes vs depois)
2. **Outliers:** Boxplot (antes vs depois)
3. **Distribuições:** Histogramas mostrando skewness (antes e depois da transformação)
4. **Normalização:** Histogramas (antes vs depois do StandardScaler)

📌 **Sugestão para interpretar gráficos:** Em cada slide ou resposta, descreva brevemente o que o gráfico mostra, qual decisão você tomou (ex.: remover outliers, usar mediana) e por quê isso melhora o modelo.


## 💡 Dicas de Código

```python
# 1. Imputação
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='median')
df[cols] = imputer.fit_transform(df[cols])

# Fluxo completo (treino x teste) para evitar data leakage
from sklearn.model_selection import train_test_split

# Separar features (X) e target (y)
X = df.drop('final_grade', axis=1)
y = df['final_grade']

# Dividir em treino e teste (80/20)
X_train, X_test, y_train, y_test = train_test_split(
	X, y, test_size=0.2, random_state=42
)

# Selecionar apenas as colunas numéricas para imputação
numeric_cols_train = X_train.select_dtypes(include=np.number).columns

imputer = SimpleImputer(strategy='mean')
imputer.fit(X_train[numeric_cols_train])            # aprende com o TREINO

X_train_imputed = imputer.transform(X_train[numeric_cols_train])
X_test_imputed = imputer.transform(X_test[numeric_cols_train])   # reutiliza médias do treino

# Converter de volta para DataFrame (opcional, mas ajuda na inspeção)
X_train_imputed = pd.DataFrame(X_train_imputed,
							   columns=numeric_cols_train,
							   index=X_train.index)
X_test_imputed = pd.DataFrame(X_test_imputed,
							  columns=numeric_cols_train,
							  index=X_test.index)

print("Imputação concluída sem data leakage!")
print("Treino:", X_train_imputed.shape, "Teste:", X_test_imputed.shape)

# 2. Outliers (IQR)
Q1 = df['col'].quantile(0.25)
Q3 = df['col'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['col'] < Q1-1.5*IQR) | (df['col'] > Q3+1.5*IQR)]

# 3. Duplicatas
df = df.drop_duplicates()

# 4. Skewness (Assimetria)
from scipy.stats import skew
skewness = df.select_dtypes(include=[np.number]).apply(lambda x: skew(x))
print(skewness)

# Transformações para corrigir assimetria
# a) Assimetria positiva (cauda à direita): usar log
import numpy as np
df['col_transformed'] = np.log1p(df['col'])  # log1p = log(1+x), evita log(0)

# b) Assimetria positiva moderada: usar sqrt
df['col_transformed'] = np.sqrt(df['col'])

# c) Box-Cox (mais avançado)
from scipy.stats import boxcox
df['col_transformed'], lambda_param = boxcox(df['col'] + 1)  # +1 se houver zeros

# 5. One-Hot
df = pd.get_dummies(df, columns=['gender'], drop_first=True)

# 6. Normalização (StandardScaler)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[cols] = scaler.fit_transform(df[cols])

# 7. Salvar scaler
import joblib
joblib.dump(scaler, 'models/scaler.pkl')

# 8. Visualizar distribuições antes/depois
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(df['col_original'], bins=30)
axes[0].set_title(f'Antes (skew={skew(df["col_original"]):.2f})')
axes[1].hist(df['col_transformed'], bins=30)
axes[1].set_title(f'Depois (skew={skew(df["col_transformed"]):.2f})')
plt.show()
```

---

## 📚 Links Úteis

- [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html)
- [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
- [get_dummies](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html)
- [scipy.stats.skew](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.skew.html)
- [Transformações Box-Cox](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html)

---

## � Glossário Rápido

- **Data Leakage:** usar informações do conjunto de teste durante o treino (direta ou indiretamente). Sempre calcule médias, mediana, scaler e encoders **só** no treino.
- **Q1 / Q3:** 25º e 75º percentis de uma coluna. O intervalo [Q1, Q3] contém a “faixa central” dos dados.
- **IQR:** `Q3 - Q1`. Ajuda a detectar outliers com a regra `1.5 × IQR`.
- **Boxplot:** gráfico que mostra mediana, Q1, Q3 e outliers. Útil para justificar remoção/manutenção de valores extremos.
- **One-Hot Encoder:** transforma categorias sem ordem em colunas binárias (0/1). Ideal para variáveis nominais.
- **LabelEncoder:** converte categorias com ordem em números (0, 1, 2, …). Ideal para variáveis ordinais.
- **StandardScaler:** padroniza colunas para média 0 e desvio 1. Mantém todas as variáveis na mesma escala.
- **Skewness:** medida de assimetria. Valores altos indicam cauda longa; considere transformar antes de modelar.

---

## �🚫 Evite

❌ Calcular média/mediana com TODO o dataset
❌ Não salvar o scaler
❌ Esquecer `drop_first=True`
❌ Ignorar distribuições assimétricas
❌ Aplicar log em colunas com zeros (use log1p)

---

## 🎤 Apresentação (5 minutos)

### Estrutura dos Slides

**Slide 1: Problemas Corrigidos**
- Valores faltantes: X removidos/imputados
- Outliers: Y detectados, Z removidos
- Duplicatas: W removidas

**Slide 2: Transformações de Distribuição (Skewness)**
- Colunas com alta assimetria identificadas
- Transformações aplicadas (log, sqrt, etc.)
- Mostrar 1 gráfico antes/depois

**Slide 3: Features Criadas**
- Feature 1: [nome] - correlação = X.XX
- Feature 2: [nome] - correlação = X.XX

**Slide 4: Resultado Final**
- Dataset original: X linhas, Y colunas
- Dataset limpo: X linhas, Z colunas
- Pronto para modelagem ✅

### Dicas para Apresentação

✅ **Máximo 5 minutos** - Ensaie com cronômetro
✅ **Todos participam** - ~1 min por pessoa
✅ **Seja objetivo** - Mostre números e gráficos
✅ **Salve os slides** - `docs/apresentacao_etapa2.pdf`

---

## 📂 Template

Use o template em `notebooks/02_Preprocessamento_TEMPLATE.py`

```bash
cd notebooks
cp 02_Preprocessamento_TEMPLATE.py 02_Preprocessamento.py
# Abrir e preencher TODOs
```

---

## 📥 Como Entregar

```bash
# 1. Código
git add notebooks/02_Preprocessamento.py
git add data/students_clean.csv
git add models/scaler.pkl

# 2. Apresentação
git add docs/apresentacao_etapa2.pdf

# 3. Commit e push
git commit -m "feat: Completa Etapa 2 - Pré-processamento"
git push origin main
```

---

**Dúvidas?** Atendimento ou Issues no GitHub
**Boa sorte!** 🚀
