# %% [markdown]
# # Etapa 2: Pré-processamento de Dados
#
# **Dataset:** students_performance.csv
# **Grupo:** [Nome do grupo]
# **Data:** [Data]
#
# ---
#
# ## 📌 Continuação da Etapa 1
# Na Etapa 1, você identificou problemas nos dados. Agora vamos **corrigi-los** e preparar para modelagem.

# %% [markdown]
# ---
# ## ✅ CHECKLIST (12 questões + 4 visualizações)
# - [ ] Parte 1: Valores Faltantes (Q1-Q2)
# - [ ] Parte 2: Outliers (Q3-Q4)
# - [ ] Parte 3: Limpeza (Q5)
# - [ ] Parte 4: Distribuições/Skewness (Q6-Q7)
# - [ ] Parte 5: Encoding (Q8-Q9)
# - [ ] Parte 6: Feature Engineering (Q10)
# - [ ] Parte 7: Normalização (Q11-Q12)
# - [ ] Dataset limpo salvo
# - [ ] Scaler salvo

# %% [markdown]
# ---
# ## 📦 SETUP

import os
import warnings

import joblib
import matplotlib.pyplot as plt
import numpy as np
# %%
# Imports
import pandas as pd
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings('ignore')

# Configurações de visualização
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (10, 5)

print("✅ Bibliotecas importadas!")

# %%
# Carregar dataset (mesmo da Etapa 1)
df = pd.read_csv('../data/datasets/students_performance.csv')

print(f"✅ Dataset carregado: {df.shape}")
print(f"\nColunas: {df.columns.tolist()}")

# %%
# Variáveis importantes (definidas na Etapa 1)
target = 'final_grade'
id_col = 'student_id'

# Separar tipos
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

# Remover ID e target das features
if id_col in numeric_cols:
    numeric_cols.remove(id_col)
if target in numeric_cols:
    numeric_cols.remove(target)

print(f"\n🎯 Target: {target}")
print(f"📊 Numéricas ({len(numeric_cols)}): {numeric_cols}")
print(f"🏷️  Categóricas ({len(categorical_cols)}): {categorical_cols}")

# %% [markdown]
# ---
# ## 📋 PARTE 1: VALORES FALTANTES (3 questões)

# %%
# Análise de missing (revisão da Etapa 1)
print("="*60)
print("VALORES FALTANTES")
print("="*60)

missing_info = pd.DataFrame({
    'Coluna': df.columns,
    'Missing': df.isnull().sum(),
    'Pct': (df.isnull().sum() / len(df) * 100).round(2)
})
missing_info = missing_info[missing_info['Missing'] > 0].sort_values('Pct', ascending=False)

print("\n📊 Resumo:")
print(missing_info.to_string(index=False))

rows_before = len(df)

# %% [markdown]
# ### 🔍 Exemplo da aula (Etapa 2 - Imputação)
# Durante a demonstração, analisamos duas colunas reais do dataset:
# - `sleep_hours`: skew ≈ 0.60 → distribuição quase simétrica → imputação com **média ≈ 7.00h**.
# - `study_hours_week`: skew ≈ 7.11 → distribuição muito assimétrica → imputação com **mediana ≈ 9.96h**, pois a média (≃10.60h) foi puxada por outliers (até 113h/semana!).
#
# Use esse raciocínio como referência. Você deve recalcular os valores ao executar o notebook e registrar suas decisões nas respostas (Q1 e Q2).

# %%
# TODO 1.1: Remover linhas com muitos valores faltantes (> 50%)
# Dica: df[df.isnull().sum(axis=1) > threshold].index

# %%
# TODO 1.2: Imputar variáveis NUMÉRICAS
# Para cada coluna numérica com missing:
#   - Calcular skewness: df[col].skew()
#   - Se |skew| > 1.0 → mediana, senão → média
#   - Aplicar: df[col].fillna(valor, inplace=True)

print("\n🔢 IMPUTAÇÃO NUMÉRICA:")

# for col in numeric_cols:
#     if df[col].isnull().sum() > 0:
#         skew = df[col].skew()
#         if abs(skew) > 1.0:
#             valor = df[col].median()
#             estrategia = 'mediana'
#         else:
#             valor = df[col].mean()
#             estrategia = 'média'
#         df[col].fillna(valor, inplace=True)
#         print(f"  ✅ {col}: {estrategia} = {valor:.2f} (skew={skew:.2f})")

# %%
# TODO 1.3: Imputar variáveis CATEGÓRICAS (moda)

print("\n🏷️  IMPUTAÇÃO CATEGÓRICA:")

# for col in categorical_cols:
#     if df[col].isnull().sum() > 0:
#         moda = df[col].mode()[0]
#         df[col].fillna(moda, inplace=True)
#         print(f"  ✅ {col}: moda = '{moda}'")

# %%
# VISUALIZAÇÃO 1: Missing antes vs depois

fig, ax = plt.subplots(figsize=(10, 5))

if len(missing_info) > 0:
    ax.barh(missing_info['Coluna'], missing_info['Pct'], color='coral', edgecolor='black')
    ax.set_xlabel('% Valores Faltantes', fontsize=11)
    ax.set_title('Valores Faltantes (ANTES do tratamento)', fontsize=12, fontweight='bold')
    ax.grid(alpha=0.3, axis='x')
    plt.tight_layout()
    plt.show()

# Verificar depois
print(f"\n✅ Missing restantes: {df.isnull().sum().sum()}")

# %% [markdown]
# ### 📝 RESPOSTAS - PARTE 1

# %% [markdown]
# **Q1. Quantas linhas você removeu? Que % do dataset?**
#
# Resposta:
# ```
# Linhas removidas: X
# Percentual: X.XX%
# ```

# %% [markdown]
# **Q2. Para cada variável numérica, você usou média ou mediana? Por quê?**
#
# Resposta:
# ```
# | Variável | Skewness | Estratégia | Justificativa |
# |----------|----------|------------|---------------|
# | idade    | 0.45     | média      | Distribuição próxima da normal |
# ```

# %% [markdown]
# **Q3. Como evitar data leakage na Etapa 3?**
#
# Resposta:
# ```
# Na Etapa 3, devemos calcular as estatísticas (média, mediana, moda) APENAS
# no conjunto de TREINO e aplicar ao conjunto de TESTE.
#
# CORRETO:
# imputer.fit(X_train)  # Aprende do treino
# X_train = imputer.transform(X_train)
# X_test = imputer.transform(X_test)  # Usa estatísticas do treino
# ```

# %% [markdown]
# ---
# ## 📋 PARTE 2: OUTLIERS (3 questões)

# %%
# Detecção de outliers (método IQR)
def detect_outliers_iqr(data, column):
    """Detecta outliers usando método IQR"""
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower) | (data[column] > upper)]
    return outliers, lower, upper

print("="*60)
print("OUTLIERS")
print("="*60)

outlier_summary = []

for col in numeric_cols:
    outliers, lower, upper = detect_outliers_iqr(df, col)
    outlier_summary.append({
        'Coluna': col,
        'Outliers': len(outliers),
        'Pct': f"{len(outliers)/len(df)*100:.1f}%"
    })

outlier_df = pd.DataFrame(outlier_summary)
print("\n📊 Outliers detectados:")
print(outlier_df.to_string(index=False))

total_outliers = outlier_df['Outliers'].sum()

# %% [markdown]
# ### 📊 Lendo um boxplot (relembrando da aula)
# - **Linha central**: mediana (valor típico da turma).
# - **Caixa**: intervalo interquartil (entre Q1 e Q3) onde estão 50% dos alunos.
# - **Bigodes**: limites Q1 − 1.5×IQR e Q3 + 1.5×IQR.
# - **Pontinhos fora dos bigodes**: outliers que merecem investigação.
# Use esse gráfico para justificar decisões (ex.: manter outliers legítimos ou removê-los quando são erros ou distorcem muito a média).

# %%
# TODO 2.1: Decidir estratégia para cada variável
# Exemplos:
#   - age: remover se < 17 ou > 30
#   - attendance_rate: remover se < 0 ou > 100
#   - sleep_hours: remover se < 3 ou > 12
#   - study_hours_week: na aula vimos outliers > 50h/semana; avalie se faz sentido tratá-los ou mantê-los

# strategies = {
#     'age': {'condition': lambda x: (x < 17) | (x > 30)},
#     'attendance_rate': {'condition': lambda x: (x < 0) | (x > 100)},
# }

# rows_removed_outliers = 0
# for col, strategy in strategies.items():
#     if col in df.columns:
#         condition = strategy['condition']
#         to_remove = df[condition(df[col])].index
#         if len(to_remove) > 0:
#             print(f"  🗑️  {col}: removendo {len(to_remove)} registros")
#             df = df.drop(to_remove)
#             rows_removed_outliers += len(to_remove)

# %%
# VISUALIZAÇÃO 2: Boxplots (antes vs depois)

# Escolher 3 variáveis para visualizar
cols_to_plot = numeric_cols[:3] if len(numeric_cols) >= 3 else numeric_cols

fig, axes = plt.subplots(1, len(cols_to_plot), figsize=(12, 4))

if len(cols_to_plot) == 1:
    axes = [axes]

for idx, col in enumerate(cols_to_plot):
    axes[idx].boxplot(df[col].dropna(), patch_artist=True,
                      boxprops=dict(facecolor='lightblue', color='black'),
                      medianprops=dict(color='red', linewidth=2))
    axes[idx].set_title(col, fontsize=11, fontweight='bold')
    axes[idx].set_ylabel('Valor')
    axes[idx].grid(alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

# %% [markdown]
# ### 📝 RESPOSTAS - PARTE 2

# %% [markdown]
# **Q4. Quantos outliers você detectou?**
#
# Resposta:
# ```
# Total de outliers: X (em todas as variáveis)
# ```

# %% [markdown]
# **Q5. Quais você removeu? Por quê?**
#
# Resposta:
# ```
# | Variável | Removidos | Justificativa |
# |----------|-----------|---------------|
# | age      | 8         | < 17 ou > 30 são idades improváveis |
# ```

# %% [markdown]
# **Q6. Quantas linhas perdeu removendo outliers?**
#
# Resposta:
# ```
# Linhas perdidas: X
# ```

# %% [markdown]
# ---
# ## 📋 PARTE 3: LIMPEZA (2 questões)

# %%
print("="*60)
print("LIMPEZA E DUPLICATAS")
print("="*60)

# TODO 3.1: Padronizar texto em categóricas
# for col in categorical_cols:
#     df[col] = df[col].str.strip()  # Remover espaços
#     df[col] = df[col].str.title()  # Capitalizar

# %%
# TODO 3.2: Remover duplicatas

# Duplicatas exatas
duplicates_exact = df.duplicated().sum()
print(f"\n🗑️  Duplicatas exatas: {duplicates_exact}")
# df = df.drop_duplicates()

# Duplicatas de ID
if id_col in df.columns:
    duplicates_id = df.duplicated(subset=[id_col]).sum()
    print(f"   Duplicatas de ID: {duplicates_id}")
    # df = df.drop_duplicates(subset=[id_col], keep='first')

print(f"\n✅ Shape após limpeza: {df.shape}")

# %% [markdown]
# ### 📝 RESPOSTAS - PARTE 3

# %% [markdown]
# **Q7. Quantas duplicatas removeu?**
#
# Resposta:
# ```
# Duplicatas exatas: X
# Duplicatas de ID: X
# Total: X
# ```

# %% [markdown]
# **Q8. Dê 1 exemplo de padronização feita.**
#
# Resposta:
# ```
# Antes: 'yes', 'Yes', 'YES', ' yes '
# Depois: 'Yes'
# ```

# %% [markdown]
# ---
# ## 📋 PARTE 4: DISTRIBUIÇÕES E ASSIMETRIA (SKEWNESS) (2 questões)

# %% [markdown]
# ### 🎯 Objetivo
# Identificar distribuições assimétricas e aplicar transformações para normalizar.
#
# **Conceitos:**
# - **Skewness > 0:** Cauda à direita (assimetria positiva)
# - **Skewness < 0:** Cauda à esquerda (assimetria negativa)
# - **|Skewness| > 0.5:** Considere transformar (log, sqrt, Box-Cox)

# %%
from scipy.stats import skew

print("="*60)
print("ANÁLISE DE ASSIMETRIA (SKEWNESS)")
print("="*60)

# TODO 4.1: Calcular skewness das colunas numéricas
# Dica: df[numeric_cols].apply(lambda x: skew(x.dropna()))

# skewness_vals = df[numeric_cols].apply(lambda x: skew(x.dropna()))
# skewness_df = pd.DataFrame({
#     'Coluna': skewness_vals.index,
#     'Skewness': skewness_vals.values
# }).sort_values('Skewness', key=abs, ascending=False)
#
# print("\n📊 Skewness por coluna:")
# print(skewness_df.to_string(index=False))
#
# # Identificar colunas com alta assimetria
# high_skew_cols = skewness_df[abs(skewness_df['Skewness']) > 0.5]['Coluna'].tolist()
# print(f"\n⚠️  Colunas com |skew| > 0.5: {high_skew_cols}")

# %%
# VISUALIZAÇÃO 3: Distribuições antes da transformação

# if len(high_skew_cols) > 0:
#     n_cols = min(3, len(high_skew_cols))  # Mostrar até 3 colunas
#     fig, axes = plt.subplots(1, n_cols, figsize=(15, 4))
#     if n_cols == 1:
#         axes = [axes]
#
#     for idx, col in enumerate(high_skew_cols[:n_cols]):
#         axes[idx].hist(df[col].dropna(), bins=30, color='coral', edgecolor='black')
#         axes[idx].set_title(f'{col}\n(skew={skew(df[col].dropna()):.2f})')
#         axes[idx].set_xlabel('Valor')
#         axes[idx].set_ylabel('Frequência')
#
#     plt.suptitle('Distribuições Assimétricas (ANTES)', fontsize=14, fontweight='bold', y=1.02)
#     plt.tight_layout()
#     plt.show()

# %%
# TODO 4.2: Aplicar transformações para corrigir skewness

# # Para cada coluna com alta assimetria:
# #   - Se skew > 0 (cauda à direita): aplicar log1p ou sqrt
# #   - Se skew < 0 (cauda à esquerda): pode inverter ou usar Box-Cox
#
# transformed_cols = []
#
# for col in high_skew_cols:
#     col_skew = skew(df[col].dropna())
#
#     if col_skew > 0.5:  # Assimetria positiva
#         # Opção 1: Log transform (para skew muito alto)
#         if col_skew > 1.0:
#             df[f'{col}_log'] = np.log1p(df[col])  # log1p = log(1+x), evita log(0)
#             transformed_cols.append((col, 'log', f'{col}_log'))
#             print(f"  ✅ {col}: log transform (skew={col_skew:.2f})")
#         # Opção 2: Sqrt (para skew moderado)
#         else:
#             df[f'{col}_sqrt'] = np.sqrt(df[col])
#             transformed_cols.append((col, 'sqrt', f'{col}_sqrt'))
#             print(f"  ✅ {col}: sqrt transform (skew={col_skew:.2f})")
#
#     elif col_skew < -0.5:  # Assimetria negativa
#         # Para assimetria negativa, podemos inverter e aplicar log
#         max_val = df[col].max()
#         df[f'{col}_inv'] = np.log1p(max_val - df[col])
#         transformed_cols.append((col, 'inverse_log', f'{col}_inv'))
#         print(f"  ✅ {col}: inverse log transform (skew={col_skew:.2f})")

# %%
# VISUALIZAÇÃO 4: Comparação antes vs depois da transformação

# if len(transformed_cols) > 0:
#     n_rows = min(3, len(transformed_cols))
#     fig, axes = plt.subplots(n_rows, 2, figsize=(12, 4*n_rows))
#     if n_rows == 1:
#         axes = axes.reshape(1, -1)
#
#     for idx, (orig_col, transform, new_col) in enumerate(transformed_cols[:3]):
#         # Antes
#         axes[idx, 0].hist(df[orig_col].dropna(), bins=30, color='coral', edgecolor='black')
#         axes[idx, 0].set_title(f'ANTES: {orig_col}\n(skew={skew(df[orig_col].dropna()):.2f})')
#         axes[idx, 0].set_ylabel('Frequência')
#
#         # Depois
#         axes[idx, 1].hist(df[new_col].dropna(), bins=30, color='lightgreen', edgecolor='black')
#         axes[idx, 1].set_title(f'DEPOIS: {new_col}\n(skew={skew(df[new_col].dropna()):.2f})')
#
#     plt.suptitle('Transformação de Distribuições', fontsize=14, fontweight='bold', y=1.00)
#     plt.tight_layout()
#     plt.show()
#
# # Opcional: Remover colunas originais se preferir usar apenas as transformadas
# # for orig_col, _, new_col in transformed_cols:
# #     df = df.drop(columns=[orig_col])

# %% [markdown]
# ### 📝 RESPOSTAS - PARTE 4

# %% [markdown]
# **Q6. Quais colunas têm distribuição assimétrica (|skew| > 0.5)?**
#
# Resposta:
# ```
# Colunas com alta assimetria:
# 1. study_hours_week: skew = 1.23 (cauda à direita)
# 2. previous_scores: skew = -0.67 (cauda à esquerda)
# ```

# %% [markdown]
# **Q7. Você aplicou transformação em alguma coluna? Qual e por quê?**
#
# Resposta:
# ```
# Sim, apliquei:
# 1. study_hours_week → log transform
#    - Motivo: skew muito alto (1.23), log reduz assimetria
#    - Resultado: skew após transform = 0.12
#
# 2. previous_scores → inverse log
#    - Motivo: skew negativo (-0.67)
#    - Resultado: skew após transform = 0.08
# ```

# %% [markdown]
# ---
# ## 📋 PARTE 5: ENCODING (2 questões)

# %%
print("="*60)
print("ENCODING DE CATEGÓRICAS")
print("="*60)

# TODO 5.1: One-Hot para nominais
# Nota: Não vamos usar ordinais neste nível iniciante, apenas One-Hot para todas

# Nominais (todas as categóricas)
nominal_vars = categorical_cols.copy()

print(f"\n🏷️  Categóricas: {nominal_vars}")

# %%
# TODO 5.2: Aplicar One-Hot Encoding

# df = pd.get_dummies(df, columns=nominal_vars, drop_first=True, dtype=int)

# Contar novas colunas
# new_cols = [col for col in df.columns if any(nom in col for nom in nominal_vars)]
# print(f"\n✅ Colunas One-Hot criadas: {len(new_cols)}")

print(f"\n✅ Shape após encoding: {df.shape}")

# %% [markdown]
# ### 📝 RESPOSTAS - PARTE 5

# %% [markdown]
# **Q8. Quantas colunas One-Hot foram criadas?**
#
# Resposta:
# ```
# Total: X colunas
#
# Exemplos:
# - gender_M
# - tutoring_Yes
# - extracurricular_Yes
# ```

# %% [markdown]
# **Q9. Por que usar `drop_first=True`?**
#
# Resposta:
# ```
# Para evitar MULTICOLINEARIDADE (dummy variable trap).
#
# Exemplo: gender (M, F)
# SEM drop_first: gender_M + gender_F (redundante!)
# COM drop_first: apenas gender_M (suficiente)
#
# Se gender_M=0 → sabemos que é F
# ```

# %% [markdown]
# ---
# ## 📋 PARTE 6: FEATURE ENGINEERING (1 questão)

# %%
print("="*60)
print("CRIAÇÃO DE FEATURES")
print("="*60)

# TODO 6.1: Criar 2 novas features (simplificado)

# Exemplos:
# 1. Razão/Proporção
# df['study_sleep_ratio'] = df['study_hours_week'] / (df['sleep_hours'] * 7)

# 2. Produto/Interação
# df['engagement'] = df['attendance_rate'] * df['study_hours_week'] / 100

new_features = []  # TODO: adicionar nomes das 2 features criadas

# %%
# TODO 6.2: Calcular correlação com target

# correlations = []
# for feat in new_features:
#     if feat in df.columns:
#         corr = df[feat].corr(df[target])
#         correlations.append({'Feature': feat, 'Correlação': round(corr, 4)})

# corr_df = pd.DataFrame(correlations).sort_values('Correlação', key=abs, ascending=False)
# print("\n📊 Correlação com target:")
# print(corr_df.to_string(index=False))

# %% [markdown]
# ### 📝 RESPOSTAS - PARTE 6

# %% [markdown]
# **Q10. Liste as 2 features criadas e explique cada uma.**
#
# Resposta:
# ```
# 1. study_sleep_ratio:
#    Lógica: Razão entre horas de estudo e sono semanal
#    Por quê: Mede balanço entre dedicação e descanso
#    Correlação com target: 0.XX
#
# 2. engagement:
#    Lógica: Produto de attendance e study_hours
#    Por quê: Captura engajamento geral do aluno
#    Correlação com target: 0.XX
# ```

# %% [markdown]
# ---
# ## 📋 PARTE 7: NORMALIZAÇÃO (2 questões)

# %%
print("="*60)
print("NORMALIZAÇÃO")
print("="*60)

# TODO 7.1: Identificar features a escalar
# Excluir: ID, target, binárias (0/1)

features_to_scale = []

# for col in df.columns:
#     if col == id_col or col == target:
#         continue
#     if df[col].nunique() == 2 and set(df[col].unique()).issubset({0, 1}):
#         continue
#     if df[col].dtype in ['int64', 'float64']:
#         features_to_scale.append(col)

print(f"\n📊 Features a escalar: {len(features_to_scale)}")

# %%
# TODO 7.2: Aplicar StandardScaler

# scaler = StandardScaler()
# df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

# Verificar
# print("\n✅ Estatísticas (deve ter mean≈0, std≈1):")
# print(df[features_to_scale].describe().loc[['mean', 'std']].T.round(4))

# %%
# TODO 7.3: SALVAR o scaler

# os.makedirs('../models', exist_ok=True)
# joblib.dump(scaler, '../models/scaler.pkl')
# print("\n✅ Scaler salvo em: models/scaler.pkl")

# %%
# VISUALIZAÇÃO 5: Distribuições antes vs depois (normalização)

# if len(features_to_scale) > 0:
#     # Selecionar 2 features para comparar
#     sample_features = features_to_scale[:2]
#
#     fig, axes = plt.subplots(2, 2, figsize=(12, 8))
#
#     for idx, feat in enumerate(sample_features):
#         # Antes (carregar novamente os dados originais para comparação)
#         df_orig = pd.read_csv('../data/datasets/students_performance.csv')
#         axes[idx, 0].hist(df_orig[feat].dropna(), bins=30, color='coral', edgecolor='black')
#         axes[idx, 0].set_title(f'ANTES: {feat}')
#         axes[idx, 0].set_ylabel('Frequência')
#
#         # Depois
#         axes[idx, 1].hist(df[feat].dropna(), bins=30, color='lightgreen', edgecolor='black')
#         axes[idx, 1].set_title(f'DEPOIS: {feat} (mean≈0, std≈1)')
#
#     plt.suptitle('Normalização (StandardScaler)', fontsize=14, fontweight='bold')
#     plt.tight_layout()
#     plt.show()

# %% [markdown]
# ### 📝 RESPOSTAS - PARTE 7

# %% [markdown]
# **Q11. Quantas features você escalou?**
#
# Resposta:
# ```
# Features escaladas: X
#
# Excluídas:
# - student_id (ID)
# - final_grade (target)
# - tutoring_Yes, extracurricular_Yes (binárias 0/1)
# ```

# %% [markdown]
# **Q12. Por que salvar o scaler?**
#
# Resposta:
# ```
# CRÍTICO para produção!
#
# Quando novos dados chegarem, devemos transformá-los com as
# MESMAS estatísticas (média e desvio padrão) do treino.
#
# Código futuro:
# scaler = joblib.load('scaler.pkl')
# X_novo_scaled = scaler.transform(X_novo)
# ```

# %% [markdown]
# ---
# ## 💾 SALVAMENTO FINAL

# %%
# Salvar dataset limpo
os.makedirs('../data', exist_ok=True)
df.to_csv('../data/students_clean.csv', index=False)

print("="*60)
print("✅ ETAPA 2 CONCLUÍDA!")
print("="*60)
print(f"\n📊 Dataset final:")
print(f"   Registros: {len(df)}")
print(f"   Features: {df.shape[1]}")
print(f"   Missing: {df.isnull().sum().sum()}")
print(f"\n📁 Arquivos gerados:")
print(f"   ✅ data/students_clean.csv")
print(f"   ✅ models/scaler.pkl")
print(f"\n🚀 Próximo: Etapa 3 - Modelagem")
print("="*60)

# %%
# Preview final
print("\n👀 Preview do dataset limpo:")
print(df.head())

print("\nℹ️  Info do dataset:")
print(df.info())

# %% [markdown]
# ### ℹ️ Nota sobre R² (coeficiente de determinação)
# Na próxima etapa de modelagem, você avaliará os modelos com métricas como **R²**.
# - **O que significa:** porcentagem da variação da `final_grade` explicada pelas features. Vai de 0 a 1 (quanto mais próximo de 1, melhor o ajuste). Valores negativos indicam que o modelo performou pior do que usar a média como previsão.
# - **Por que importa aqui:** um pré-processamento consistente (tratamento de missing, outliers, encoding, normalização) ajuda o modelo a alcançar R² mais alto e mais confiável.
# - **Aplicação prática:** quando comparar modelos na Etapa 3, registre a métrica R² e comente como as escolhas desta etapa (ex.: remover outliers extremos) impactaram o resultado.

# %% [markdown]
# ---
# ## ✅ CHECKLIST FINAL
#
# Antes de entregar, verifique:
#
# - [ ] 15 questões respondidas (Q1-Q15)
# - [ ] 3 visualizações criadas (missing, outliers, correlação)
# - [ ] Dataset salvo sem valores faltantes
# - [ ] Scaler salvo em models/scaler.pkl
# - [ ] Notebook executa sem erros (Restart & Run All)
# - [ ] Código documentado com markdown
# - [ ] Commit no GitHub
#
# **Parabéns! Etapa 2 completa!** 🎉
# **Próximo passo:** Etapa 3 - Modelos de Machine Learning
# **Parabéns! Etapa 2 completa!** 🎉
# **Próximo passo:** Etapa 3 - Modelos de Machine Learning
