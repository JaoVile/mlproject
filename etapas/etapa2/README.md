# 🔧 Etapa 2: Pré-processamento de Dados

**Prazo de Entrega:** [Data será informada pelo professor]
**Peso:** 20% da nota do projeto (2.0 pontos)
- 17% Notebook e arquivos (1.7 pontos)
- 3% Apresentação (0.3 pontos)

**Tempo estimado:** 6-8 horas

**Entregáveis:**
- `notebooks/02_Preprocessamento.ipynb` (ou `.py`)
- `data/students_clean.csv`
- `models/scaler.pkl`
- **🎤 Apresentação de 5 minutos**

---

## 🎯 Objetivo Simples

Limpar e preparar os dados para a modelagem (Etapa 3).

**Você vai:**

💡 **Como fazer?** No arquivo [`INSTRUCOES_ALUNOS.md`](INSTRUCOES_ALUNOS.md) cada etapa traz:
- o objetivo da tarefa,
- exemplos de código prontos (copie, adapte e execute),
- explicações simples sobre quando usar média ou mediana, como ler um boxplot, a diferença entre One-Hot e LabelEncoder, e por que salvar o scaler.

---

## 📋 O Que Você Vai Entregar

### 1. Notebook: `notebooks/02_Preprocessamento.ipynb`
- 12 questões respondidas
- 4 visualizações criadas (antes/depois)

### 2. Dataset limpo: `data/students_clean.csv`
- Pronto para usar na Etapa 3

### 3. Scaler salvo: `models/scaler.pkl`
- Para reutilizar na Etapa 3

### 4. Apresentação: 5 minutos 🎤

**O que apresentar:**
- **Slide 1:** Problemas corrigidos
  - Quantos missing, outliers, duplicatas removidos
- **Slide 2:** Transformações de distribuição (skewness)
  - Quais colunas transformou e por quê
  - Mostrar 1 gráfico antes/depois
- **Slide 3:** Features criadas
  - Liste as 2 features e suas correlações com target
- **Slide 4:** Resultado final
  - Dataset antes: X linhas, Y colunas
  - Dataset depois: X linhas, Z colunas
  - Pronto para modelagem ✅

**Formato:**
- 4 slides (PowerPoint, Google Slides, ou PDF)
- Máximo 5 minutos
- Todos os membros devem participar (~1 min cada)

---

## 📖 Instruções Detalhadas

👉 **Abra o arquivo:** [`INSTRUCOES_ALUNOS.md`](INSTRUCOES_ALUNOS.md)

Lá você vai encontrar:
- **12 questões** divididas em 7 partes
- Código de exemplo pronto para copiar
- Links para documentação oficial
- Estrutura completa da apresentação

---

## ✅ Critérios de Avaliação

### Notebook e Arquivos (17% = 1.7 pontos)

| Critério | Peso | O Que Avaliamos |
|----------|:----:|-----------------|
| **12 Questões respondidas** | 60% | Código funciona + respostas corretas |
| **4 Visualizações** | 20% | Gráficos antes/depois (missing, outliers, skewness, normalização) |
| **Dataset limpo** | 15% | `students_clean.csv` salvo corretamente |
| **Scaler salvo** | 5% | `scaler.pkl` salvo |

### Apresentação (3% = 0.3 pontos)

| Critério | Peso | O Que Avaliamos |
|----------|:----:|-----------------|
| **Conteúdo** | 50% | Mostrou resultados relevantes (problemas corrigidos, transformações, features) |
| **Clareza** | 30% | Explicação clara e objetiva |
| **Participação** | 20% | Todos os membros apresentaram |

---

## 🚀 Como Começar

### Passo 1: Copiar Template
```bash
cd notebooks
cp 02_Preprocessamento_TEMPLATE.py 02_Preprocessamento.py
```

### Passo 2: Abrir no Jupyter/VS Code
```bash
# Opção 1: Jupyter Notebook
jupyter notebook 02_Preprocessamento.py

# Opção 2: VS Code
code 02_Preprocessamento.py
```

### Passo 3: Seguir os TODOs
- O template tem comentários `# TODO:` onde você deve completar
- Siga a ordem das questões em `INSTRUCOES_ALUNOS.md`

---

## 📦 Como Entregar

```bash
# 1. Adicionar arquivos
git add notebooks/02_Preprocessamento.py
git add data/students_clean.csv
git add models/scaler.pkl

# 2. Commit
git commit -m "feat: Completa Etapa 2 - Pré-processamento"

# 3. Push
git push origin main
```

---

## ✅ Checklist Antes de Entregar

### Código
- [ ] 12 questões respondidas
- [ ] 4 visualizações criadas (missing, outliers, skewness, normalização)
- [ ] Dataset salvo em `data/students_clean.csv`
- [ ] Scaler salvo em `models/scaler.pkl`
- [ ] Notebook executa sem erros ("Run All")
- [ ] Código está no GitHub

### Apresentação
- [ ] 4 slides preparados
- [ ] Apresentação ensaiada (máximo 5 min)
- [ ] Todos os membros sabem sua parte
- [ ] Slides salvos em `docs/apresentacao_etapa2.pdf`

---

## 💡 Dicas

✅ **Siga o template** - Não precisa começar do zero
✅ **Use os exemplos** - Código de exemplo está nos comentários
✅ **Execute célula por célula** - Não tente fazer tudo de uma vez
✅ **Consulte os links** - Documentação do scikit-learn ajuda

❌ **Não copie sem entender** - Você vai precisar explicar
❌ **Não pule questões** - Todas são obrigatórias
❌ **Não esqueça de salvar** - Dataset e scaler são entregáveis

---

## 🆘 Precisa de Ajuda?

1. Leia `INSTRUCOES_ALUNOS.md` com atenção
2. Veja o código de exemplo no template
3. Consulte os links de documentação
4. Pergunte ao professor no horário de atendimento

---

**Boa sorte!** 🚀

*Última atualização: Novembro 2025*
