# Notebooks - Análises Semanais

Esta pasta contém os notebooks Jupyter para cada etapa semanal do projeto.

---

## 📂 Estrutura Esperada

Ao final do projeto, você deverá ter:

```
notebooks/
├── README.md                           # Este arquivo
├── 00_EXEMPLO_STARTER.py              # Código exemplo (starter)
├── 01_EDA.ipynb                       # Semana 1: Análise Exploratória
├── 02_Preprocessamento_Baseline.ipynb # Semana 2: Pré-processamento + Baseline
├── 03_Modelos_Avancados.ipynb         # Semana 3: Modelos Avançados
└── 04_Otimizacao_Final.ipynb          # Semana 4: Otimização e Conclusão
```

---

## 🚀 Como Usar o Starter Code

### 1. Converter para Jupyter Notebook

O arquivo `00_EXEMPLO_STARTER.py` é um código Python que você pode usar como ponto de partida.

**Opção A: Copiar e Colar**
1. Abra Jupyter Notebook: `jupyter notebook`
2. Crie um novo notebook: `01_EDA.ipynb`
3. Copie seções do `00_EXEMPLO_STARTER.py` para células de código
4. Adicione células markdown para documentar

**Opção B: Converter Automaticamente**
```bash
# Instalar jupytext (se não tiver)
pip install jupytext

# Converter .py para .ipynb
jupytext --to notebook 00_EXEMPLO_STARTER.py -o 01_EDA.ipynb
```

### 2. Executar e Expandir

O código starter fornece:
- ✅ Estrutura básica de análise
- ✅ Exemplos de visualizações
- ✅ Código para análises fundamentais

**Você DEVE:**
- ⚠️ Adicionar análises adicionais
- ⚠️ Criar visualizações customizadas
- ⚠️ Documentar descobertas em markdown
- ⚠️ Ir além do básico!

---

## 📋 Checklist por Notebook

### Notebook 01: EDA (Semana 1)

- [ ] Carregar e inspecionar dados
- [ ] Analisar valores faltantes
- [ ] Estatísticas descritivas da variável alvo
- [ ] Distribuições de features numéricas
- [ ] Frequências de features categóricas
- [ ] Matriz de correlação
- [ ] Análise bivariada (categóricas vs target)
- [ ] Identificação de outliers
- [ ] Documentar descobertas em markdown
- [ ] Executar "Restart & Run All" sem erros

### Notebook 02: Pré-processamento + Baseline (Semana 2)

- [ ] Carregar dados processados da Etapa 1
- [ ] Tratar valores faltantes (imputação)
- [ ] Tratar outliers (decisão justificada)
- [ ] Encoding de variáveis categóricas
- [ ] Feature Engineering (criar 3+ features)
- [ ] Normalização/Padronização
- [ ] Train-test split (60/20/20)
- [ ] Treinar modelo baseline (Regressão Linear)
- [ ] Avaliar com RMSE, MAE, R²
- [ ] Salvar dados processados em `data/processed/`
- [ ] Executar "Restart & Run All" sem erros

### Notebook 03: Modelos Avançados (Semana 3)

- [ ] Carregar dados processados
- [ ] Implementar 5+ modelos diferentes
- [ ] Ridge Regression
- [ ] Lasso Regression
- [ ] Random Forest
- [ ] Gradient Boosting (XGBoost/LightGBM)
- [ ] Outros modelos (SVM, ElasticNet, etc.)
- [ ] Comparar performance de todos os modelos
- [ ] Análise de Feature Importance
- [ ] Selecionar melhor modelo
- [ ] Executar "Restart & Run All" sem erros

### Notebook 04: Otimização + Conclusão (Semana 4)

- [ ] Otimização de hiperparâmetros (GridSearch/RandomSearch)
- [ ] Validação cruzada (k-fold)
- [ ] Treinar modelo final otimizado
- [ ] Avaliar no conjunto de TESTE (nunca visto)
- [ ] Análise de resíduos
- [ ] Interpretação de resultados
- [ ] Visualizações finais
- [ ] Salvar modelo treinado (`.pkl` ou `.joblib`)
- [ ] Documentar conclusões
- [ ] Executar "Restart & Run All" sem erros

---

## 📊 Boas Práticas para Notebooks

### 1. Organização

✅ Use seções claras com headers markdown:
```markdown
# 1. Importação de Bibliotecas
# 2. Carregamento de Dados
# 3. Análise Exploratória
## 3.1 Valores Faltantes
## 3.2 Distribuições
# 4. Conclusões
```

### 2. Código Limpo

✅ Adicione comentários explicativos:
```python
# Calcular correlação de Pearson entre features numéricas e target
correlations = df[numeric_cols].corr()['final_grade'].sort_values(ascending=False)
```

### 3. Visualizações

✅ Sempre inclua:
- Títulos descritivos
- Labels nos eixos
- Legendas (quando aplicável)
- Grid para facilitar leitura

```python
plt.figure(figsize=(10, 6))
plt.hist(df['final_grade'], bins=30, edgecolor='black')
plt.title('Distribuição das Notas Finais', fontsize=14, 
```

### 4. Documentação

Após cada análise, adicione célula markdown explicando:
```markdown
### Descoberta Principal

A análise de correlação revelou que `previous_scores` tem a maior
correlação com `final_grade` (r=0.75, p<0.001), seguido por
`study_hours_week` (r=0.45). Isso sugere que o desempenho anterior
é o melhor preditor da nota final.
```

### 5. Antes de Fazer Commit

✅ Execute "Restart Kernel & Run All Cells"
✅ Verifique se não há erros
✅ Certifique-se de que todas as visualizações aparecem
✅ Revise markdown para erros de digitação
✅ Remova células de teste/debug desnecessárias

---

### Células Fora de Ordem

⚠️ Garanta que as células podem ser executadas **sequencialmente** do início ao fim.

Teste com: **Kernel → Restart & Run All**

---

## 📚 Recursos Adicionais

### Jupyter Notebook Tips
- [Atalhos de Teclado](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)

### Análise de Dados
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)

### Machine Learning
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)

---

**Última atualização:** Outubro 2027
