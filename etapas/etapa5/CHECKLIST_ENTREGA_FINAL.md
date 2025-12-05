# ✅ Checklist de Entrega - Etapa 5
## Projeto de Machine Learning: Predição de Desempenho Acadêmico

**Gabarito do Professor**  
**Disciplina:** Introdução à Machine Learning - 2025.2  
**Data de Entrega:** 4 de dezembro de 2025

---

## ⚠️ IMPORTANTE: O Que É a Etapa 5?

A Etapa 5 **NÃO é uma apresentação oral**. É a **entrega final organizada** de todo o projeto no GitHub.

### 🎯 Objetivo:
Consolidar todo o trabalho das Etapas 1-4 em um repositório profissional e bem documentado.

### 📦 O Que Entregar:
1. ✅ Repositório GitHub completo e organizado
2. ✅ README.md profissional
3. ✅ Relatório final técnico (consolidação das 4 etapas)
4. ✅ Todos os notebooks funcionando ("Restart & Run All")

**Não há apresentação oral!** Apenas entrega do link do repositório.

---

## 📊 Critérios de Avaliação (Total: 25% da nota final)

| Critério | Peso | Pontos | O Que Avaliamos |
|----------|:----:|:------:|-----------------|
| **Repositório Organizado** | 40% | 1.0 | Estrutura correta, arquivos nomeados adequadamente |
| **README.md Completo** | 25% | 0.625 | Profissional, informativo, com instruções claras |
| **Relatório Final** | 20% | 0.5 | Documentação técnica completa das 4 etapas |
| **Reprodutibilidade** | 15% | 0.375 | Notebooks executam sem erros, requirements.txt correto |

**Total:** 2.5 pontos (25% da nota do projeto)

---

## 📁 PARTE 1: Estrutura do Repositório (40% - 1.0 ponto)

### ✅ Estrutura Obrigatória:

```
seu-repositorio-ml/
│
├── README.md                          ⭐ OBRIGATÓRIO (ver Parte 2)
├── requirements.txt                   ⭐ OBRIGATÓRIO
├── .gitignore                         ⭐ RECOMENDADO
│
├── data/                              📊 Dados
│   ├── raw/                          (opcional)
│   │   └── [dataset_original].csv
│   └── processed/                    (opcional)
│       ├── X_train.csv
│       ├── X_val.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       ├── y_val.csv
│       └── y_test.csv
│
├── notebooks/                         💻 Notebooks das Etapas
│   ├── 01_EDA.ipynb                  ⭐ Etapa 1
│   ├── 02_Preprocessamento.ipynb     ⭐ Etapa 2
│   ├── 03_Modelagem.ipynb            ⭐ Etapa 3
│   └── 04_Otimizacao.ipynb           ⭐ Etapa 4
│
├── models/                            🤖 Modelos Treinados
│   ├── modelo_final.joblib           (ou .pkl)
│   └── modelo_info.json              (opcional - metadados)
│
└── docs/                              📄 Documentação
    └── RELATORIO_FINAL.md            ⭐ OBRIGATÓRIO (ver Parte 3)
```

### 📋 Checklist da Estrutura:

- [ ] ✅ Pasta `data/` existe
- [ ] ✅ Pasta `notebooks/` existe com 4 notebooks nomeados corretamente
- [ ] ✅ Pasta `models/` existe com modelo final salvo
- [ ] ✅ Pasta `docs/` existe com `RELATORIO_FINAL.md`
- [ ] ✅ `README.md` na raiz do repositório
- [ ] ✅ `requirements.txt` com todas as dependências
- [ ] ✅ `.gitignore` configurado (ignorar `.venv/`, `__pycache__/`, etc.)

### ⚠️ Erros Comuns a Evitar:

❌ Notebooks com nomes genéricos (`Untitled.ipynb`, `Notebook1.ipynb`)  
❌ Arquivos soltos na raiz sem organização  
❌ Dados gigantes commitados (> 100MB)  
❌ Ambiente virtual (`.venv/`) commitado  
❌ Paths absolutos nos notebooks (`/home/usuario/...`)  

✅ Use paths relativos: `'../data/dataset.csv'`  
✅ Use `.gitignore` para excluir arquivos grandes  
✅ Nomes descritivos e consistentes

---

## 📝 PARTE 2: README.md Profissional (25% - 0.625 pontos)

O `README.md` é a **porta de entrada** do seu projeto. Deve ser claro, informativo e profissional.

### ✅ Seções Obrigatórias:

#### 1. Cabeçalho com Título e Badges

```markdown
# 🎓 [Título do Projeto]
## Predição de [Variável Alvo] usando Machine Learning

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3.0-orange.svg)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Disciplina:** Introdução à Machine Learning - 2025.2  
**Professor:** Professor Durval  
**Grupo:** [Nomes dos membros]
```

#### 2. Sobre o Projeto (2-3 parágrafos)

Responda:
- Qual o problema resolvido?
- Por que é importante?
- Qual a abordagem utilizada?

Exemplo:
```markdown
## 🎯 Sobre o Projeto

Este projeto desenvolveu um modelo de Machine Learning para prever [X]
com base em [Y]. O objetivo é [Z].

Utilizamos técnicas de análise exploratória, pré-processamento, feature
engineering e otimização de hiperparâmetros para alcançar [resultado].

O modelo final alcançou MAE de X.XX e R² de 0.XX, demonstrando [interpretação].
```

#### 3. Resultados Principais (Destaque)

```markdown
## 🏆 Resultados Principais

- **MAE:** X.XX pontos
- **RMSE:** X.XX pontos
- **R²:** 0.XX (explica XX% da variância)
- **Modelo Final:** [Nome do modelo + configuração]
- **Melhoria vs Baseline:** XX%
```

#### 4. Estrutura do Repositório

```markdown
## 📊 Estrutura do Repositório

[Cole a árvore de pastas aqui]
```

#### 5. Como Reproduzir (Passo a Passo)

```markdown
## 🚀 Como Reproduzir

### 1. Clonar o Repositório
\`\`\`bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
\`\`\`

### 2. Criar Ambiente Virtual
\`\`\`bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows
\`\`\`

### 3. Instalar Dependências
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Executar Notebooks
\`\`\`bash
jupyter notebook notebooks/01_EDA.ipynb
# Execute em ordem: 01 → 02 → 03 → 04
\`\`\`
```

#### 6. Tecnologias Utilizadas

```markdown
## 🛠️ Tecnologias Utilizadas

- **Python:** 3.10+
- **Pandas:** Manipulação de dados
- **NumPy:** Computação numérica
- **Scikit-learn:** Machine Learning
- **Matplotlib/Seaborn:** Visualizações
- **Jupyter:** Ambiente interativo
```

#### 7. Resultados Detalhados (Tabela)

```markdown
## 📈 Resultados Detalhados

| Modelo | MAE | RMSE | R² | Tempo |
|--------|-----|------|-----|-------|
| Random Forest | X.XX | X.XX | 0.XX | Xs |
| Ridge | X.XX | X.XX | 0.XX | Xs |
| ... | ... | ... | ... | ... |
```

#### 8. Membros do Grupo

```markdown
## 👥 Membros do Grupo

- **[Nome 1]** - Matrícula: XXXXX
  - Responsável: EDA e visualizações
- **[Nome 2]** - Matrícula: XXXXX
  - Responsável: Pré-processamento
- **[Nome 3]** - Matrícula: XXXXX
  - Responsável: Modelagem e otimização
```

#### 9. Licença

```markdown
## 📄 Licença

Este projeto é disponibilizado sob a licença MIT.
```

### 📋 Checklist do README.md:

- [ ] ✅ Título claro e descritivo
- [ ] ✅ Badges de tecnologias
- [ ] ✅ Seção "Sobre o Projeto" (2-3 parágrafos)
- [ ] ✅ Resultados principais em destaque
- [ ] ✅ Estrutura do repositório visualizada
- [ ] ✅ Instruções de reprodução passo-a-passo
- [ ] ✅ Lista de tecnologias
- [ ] ✅ Tabela de resultados comparativos
- [ ] ✅ Nomes dos membros do grupo
- [ ] ✅ Licença
- [ ] ✅ Sem erros de português
- [ ] ✅ Markdown formatado corretamente

---

## 📄 PARTE 3: Relatório Final (20% - 0.5 pontos)

**Arquivo:** `docs/RELATORIO_FINAL.md`

O relatório final é uma **consolidação técnica** de todo o trabalho realizado nas 4 etapas.

### ✅ Estrutura do Relatório:

#### 1. Sumário Executivo (½ página)
- Resumo do projeto
- Principal resultado
- Conclusão

#### 2. Introdução (1 página)
- Contexto do problema
- Objetivos
- Dataset utilizado

#### 3. Análise Exploratória - Etapa 1 (2-3 páginas)
- Estatísticas descritivas
- Visualizações principais
- Insights e descobertas

#### 4. Pré-processamento - Etapa 2 (2-3 páginas)
- Tratamento de missing values
- Tratamento de outliers
- Feature engineering
- Normalização/encoding

#### 5. Modelagem - Etapa 3 (2-3 páginas)
- Modelos testados
- Métricas utilizadas
- Comparação de performance
- Seleção do modelo

#### 6. Otimização - Etapa 4 (1-2 páginas)
- Hiperparâmetros otimizados
- Processo de tuning (Grid Search/Random Search)
- Resultados finais

#### 7. Conclusões (1-2 páginas)
- Resultados alcançados
- Limitações
- Trabalhos futuros
- Lições aprendidas

#### 8. Referências
- Artigos, documentações, tutoriais

### 📋 Checklist do Relatório:

- [ ] ✅ Todas as 8 seções presentes
- [ ] ✅ 10-15 páginas no total
- [ ] ✅ Visualizações incluídas e referenciadas
- [ ] ✅ Tabelas formatadas
- [ ] ✅ Justificativas para decisões técnicas
- [ ] ✅ Linguagem técnica mas clara
- [ ] ✅ Sem erros de português
- [ ] ✅ Markdown formatado corretamente

**Template disponível:** `etapas/etapa5/GABARITO_RELATORIO_FINAL_students.md`

---

## 🔄 PARTE 4: Reprodutibilidade (15% - 0.375 pontos)

Seu projeto deve ser **facilmente reproduzível** por outra pessoa.

### ✅ Checklist de Reprodutibilidade:

#### 1. requirements.txt

- [ ] ✅ Arquivo existe na raiz
- [ ] ✅ Contém TODAS as dependências
- [ ] ✅ Versões especificadas

Gerar automaticamente:
```bash
pip freeze > requirements.txt
```

Ou criar manualmente:
```txt
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
matplotlib==3.7.2
seaborn==0.12.2
jupyter==1.0.0
```

#### 2. Notebooks Executam Sem Erros

- [ ] ✅ "Restart Kernel & Run All Cells" funciona em TODOS os notebooks
- [ ] ✅ Sem erros de FileNotFoundError (paths corretos)
- [ ] ✅ Sem erros de ModuleNotFoundError (dependências no requirements.txt)
- [ ] ✅ Outputs salvos nos notebooks

**Como testar:**
1. Abra cada notebook
2. Menu: Kernel → Restart & Run All
3. Aguarde execução completa
4. Verifique se há erros

#### 3. Paths Relativos

❌ **ERRADO (path absoluto):**
```python
df = pd.read_csv('/home/durval/projeto/data/dataset.csv')
```

✅ **CORRETO (path relativo):**
```python
df = pd.read_csv('../data/dataset.csv')
```

#### 4. Dados Disponíveis

- [ ] ✅ Dataset original em `data/raw/` (se < 100MB)
- [ ] ✅ OU instruções de download no README
- [ ] ✅ Dados processados em `data/processed/` (se necessário)

#### 5. Modelo Salvo

- [ ] ✅ Modelo final em `models/modelo_final.joblib`
- [ ] ✅ Pode ser carregado sem erros

Testar:
```python
import joblib
model = joblib.load('models/modelo_final.joblib')
```

---

## 📤 COMO ENTREGAR

### 1. Preparar o Repositório

```bash
# 1. Verificar status
git status

# 2. Adicionar todos os arquivos
git add .

# 3. Commit final
git commit -m "feat: Entrega final - Etapa 5"

# 4. Push para GitHub
git push origin main
```

### 2. Verificar no GitHub

Acesse seu repositório no navegador e confirme:
- [ ] ✅ Todos os arquivos estão lá
- [ ] ✅ README.md renderiza corretamente
- [ ] ✅ Estrutura de pastas está correta
- [ ] ✅ Não há arquivos gigantes (> 100MB)

### 3. Entregar o Link

**Entregar via:** [Plataforma indicada pelo professor]

**Formato da entrega:**
```
Repositório: https://github.com/seu-usuario/seu-repositorio
Membros: [Nome 1], [Nome 2], [Nome 3]
Dataset: [Nome do dataset escolhido]
```

---

## ✅ CHECKLIST FINAL ANTES DE ENTREGAR

### Repositório
- [ ] ✅ Estrutura de pastas correta
- [ ] ✅ 4 notebooks nomeados e organizados
- [ ] ✅ Modelo final salvo
- [ ] ✅ `.gitignore` configurado
- [ ] ✅ Sem arquivos desnecessários (.DS_Store, __pycache__, etc.)

### README.md
- [ ] ✅ Todas as seções obrigatórias presentes
- [ ] ✅ Resultados em destaque
- [ ] ✅ Instruções de reprodução claras
- [ ] ✅ Nomes dos membros do grupo
- [ ] ✅ Sem erros de português

### Relatório Final
- [ ] ✅ Arquivo em `docs/RELATORIO_FINAL.md`
- [ ] ✅ 10-15 páginas
- [ ] ✅ Todas as 8 seções presentes
- [ ] ✅ Visualizações incluídas

### Reprodutibilidade
- [ ] ✅ `requirements.txt` completo
- [ ] ✅ Notebooks executam sem erros ("Restart & Run All")
- [ ] ✅ Paths relativos (não absolutos)
- [ ] ✅ Dados disponíveis ou instruções de download

### GitHub
- [ ] ✅ Repositório público
- [ ] ✅ Commit final feito
- [ ] ✅ Push realizado
- [ ] ✅ README renderiza corretamente no GitHub

### Entrega
- [ ] ✅ Link do repositório copiado
- [ ] ✅ Entregue na plataforma correta
- [ ] ✅ Nomes dos membros informados

---

## 🚨 ERROS COMUNS A EVITAR

### ❌ Erro 1: Repositório Desorganizado
**Problema:** Arquivos soltos, sem estrutura  
**Solução:** Seguir estrutura obrigatória de pastas

### ❌ Erro 2: README Incompleto ou Genérico
**Problema:** Falta informações, copia/cola de template  
**Solução:** Preencher todas as seções com informações reais do projeto

### ❌ Erro 3: Notebooks Não Executam
**Problema:** Paths errados, dependências faltando  
**Solução:** Testar "Restart & Run All" antes de entregar

### ❌ Erro 4: Dados Gigantes no GitHub
**Problema:** Arquivo > 100MB não sobe  
**Solução:** Usar `.gitignore` ou Git LFS, ou fornecer link de download

### ❌ Erro 5: Paths Absolutos
**Problema:** `/home/seu-usuario/...` não funciona em outro PC  
**Solução:** Sempre usar paths relativos: `../data/arquivo.csv`

### ❌ Erro 6: Relatório Copiado de Outro Grupo
**Problema:** Plágio detectado = nota zero  
**Solução:** Escrever com suas próprias palavras sobre SEU projeto

### ❌ Erro 7: requirements.txt Faltando
**Problema:** Pessoa clona mas não consegue rodar  
**Solução:** Gerar com `pip freeze > requirements.txt`

### ❌ Erro 8: Modelo Não Salvo
**Problema:** Notebook otimiza mas não salva o modelo  
**Solução:** Usar `joblib.dump(model, 'models/modelo_final.joblib')`

---

## 💡 DICAS PARA UMA ENTREGA EXCELENTE

### ✨ Diferenciais que Impressionam:

1. **README.md com Badges**
   ```markdown
   [![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
   [![Stars](https://img.shields.io/github/stars/seu-usuario/seu-repo)]()
   ```

2. **Gráficos Profissionais**
   - Use cores consistentes
   - Títulos e labels claros
   - Tamanho adequado (não muito pequeno)

3. **Código Limpo e Comentado**
   ```python
   # Aplicar StandardScaler para normalização
   scaler = StandardScaler()
   X_train_scaled = scaler.fit_transform(X_train)
   ```

4. **Markdown Bem Formatado**
   - Use negrito para destaques
   - Use código inline: \`variavel\`
   - Use blocos de código com sintaxe: \`\`\`python
   - Use tabelas para comparações

5. **Git Commits Descritivos**
   ```bash
   ❌ git commit -m "update"
   ✅ git commit -m "feat: Adiciona Grid Search na Etapa 4"
   ```

6. **Análise Crítica**
   - Não apenas "o modelo funcionou"
   - "O Random Forest superou a Regressão Linear em 15% no MAE
     porque captura relações não-lineares entre X e Y"

---

## 📞 PRECISA DE AJUDA?

### Problemas Comuns e Soluções:

**1. "Git não reconhece arquivos grandes"**
→ Adicione ao `.gitignore` ou use Git LFS

**2. "Notebook não encontra arquivo"**
→ Verifique o path relativo: `../data/arquivo.csv`

**3. "pip install dá erro"**
→ Atualize pip: `pip install --upgrade pip`

**4. "Não sei fazer README bonito"**
→ Use o template fornecido e adapte

**5. "Meu modelo demora muito para treinar"**
→ Salve o modelo treinado e só carregue depois

---

## 🎯 RESUMO: O QUE REALMENTE IMPORTA

### Para tirar nota máxima na Etapa 5:

1. ✅ **Organização** → Estrutura de pastas correta
2. ✅ **README.md** → Profissional, completo, informativo
3. ✅ **Relatório** → Técnico, bem escrito, 10-15 páginas
4. ✅ **Funcionalidade** → Notebooks executam sem erros
5. ✅ **Documentação** → Tudo explicado e justificado

**Não precisa ser perfeito, precisa ser completo e bem organizado!**

---

## 📊 Matriz de Avaliação Detalhada

| Item | Excelente (100%) | Bom (75%) | Satisfatório (50%) | Insatisfatório (25%) |
|------|-----------------|-----------|-------------------|---------------------|
| **Estrutura** | Perfeita, organizada | Pequenos desvios | Desorganizada | Caótica |
| **README** | Completo, profissional | Falta 1-2 seções | Genérico | Incompleto |
| **Relatório** | Técnico, detalhado | Falta profundidade | Superficial | Muito básico |
| **Reprodutibilidade** | Roda perfeitamente | Pequenos erros | Vários erros | Não roda |

---

**Boa entrega! 🚀**

*Checklist criado para a Etapa 5 - Entrega Final*  
*Disciplina: Introdução à Machine Learning - 2025.2*  
*Professor: Professor Durval*
