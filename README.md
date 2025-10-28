# 🎓 Projeto: Machine Learning - Previsão de Desempenho Acadêmico

**Disciplina:** Introdução à Machine Learning
**Professor:** Professor Durval
**Formato:** Trabalho em Grupo (até 5 pessoas)
**Duração:** 4 semanas (1 etapa por semana)

---

## 👋 Bem-vindo ao Projeto!

Você acaba de aceitar o convite para o projeto final da disciplina! Este é um repositório **privado** do seu grupo, criado automaticamente pelo GitHub Classroom.

### 🎯 O Que Você Vai Fazer

Desenvolver um modelo de **Machine Learning** para prever o desempenho acadêmico final de estudantes universitários, identificando aqueles em risco de baixo desempenho para permitir intervenções preventivas.

### Exemplo de tipo de dataset

**Tipo de problema:** Regressão (prever valores contínuos de 0-100)
**Dataset:** 2.510 estudantes com 13 variáveis (hábitos de estudo, condições socioeconômicas, saúde)

---

## 📅 Como Funciona o Projeto (Importante!)

### 🔄 Projeto Semanal e Progressivo

**⚠️ ATENÇÃO:** Este projeto **NÃO** entrega tudo de uma vez!

Você receberá **instruções semanais** do professor. Cada semana terá:
- 📋 Objetivos específicos da etapa
- 📚 Material de apoio necessário
- ✅ Critérios de avaliação da semana
- 🎯 Entregáveis esperados

**Não tente fazer tudo agora!** Siga o cronograma semanal do professor.

### 📆 Visão Geral das Etapas

| Semana | Etapa | O Que Você Vai Fazer |
|:------:|-------|----------------------|
| **1** | Análise Exploratória (EDA) | Conhecer e entender os dados |
| **2** | Pré-processamento | Limpar e preparar os dados |
| **3** | Modelagem | Treinar e comparar modelos |
| **4** | Otimização e Relatório | Ajustar modelo e documentar |

📖 **Instruções detalhadas de cada etapa serão fornecidas pelo professor no início de cada semana.**

---

## 👥 Trabalho em Grupo no GitHub Classroom

### Como Funciona

Vocês estão trabalhando em um **repositório compartilhado do grupo**. Todos os membros têm acesso ao mesmo repositório.

#### Se você foi o PRIMEIRO a aceitar:
✅ Você criou o grupo
✅ Este é o repositório do seu grupo
✅ Aguarde seus colegas se juntarem

#### Se você NÃO foi o primeiro:
✅ Você se juntou ao grupo criado por um colega
✅ Este é o repositório compartilhado de todos
✅ Você tem acesso total para colaborar

### 🤝 Boas Práticas de Colaboração

#### 1. Comuniquem-se Sempre
- Decidam juntos quem fará o quê
- Não trabalhem no mesmo arquivo ao mesmo tempo
- Usem Issues do GitHub para organizar tarefas

#### 2. Façam Commits Frequentes
```bash
# Antes de começar a trabalhar
git pull origin main

# Depois de fazer mudanças
git add .
git commit -m "Descrição clara do que fez"
git push origin main
```

#### 3. Dividam as Tarefas
**Sugestão de papéis:**
- 📊 **Analista de Dados:** EDA e visualizações
- 🔧 **Engenheiro de Dados:** Limpeza e pré-processamento
- 🤖 **Cientista ML:** Modelagem e otimização
- 📝 **Documentador:** Relatórios e apresentação
- 🧪 **Testador:** Validação e testes

*Nota: Em grupos menores, membros acumulam funções.*

#### 4. Revisem o Trabalho uns dos Outros
- Antes de fazer push, peça a um colega para revisar
- Use comentários no código para explicar decisões
- Documentem TUDO em células markdown nos notebooks

---

## 🚀 Primeiros Passos (Faça Isso AGORA)

### 1️⃣ Clone o Repositório

Cada membro do grupo deve clonar:

```bash
# Substituir [URL-DO-SEU-REPOSITORIO] pela URL real
git clone [URL-DO-SEU-REPOSITORIO]
cd [nome-do-repositorio]
```

💡 **Onde encontrar a URL:** Clique no botão verde "Code" aqui no GitHub

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

# Verificar instalação
python -c "import pandas, numpy, sklearn; print('✅ Ambiente pronto!')"
```

### 3️⃣ Explore o Repositório

```bash
# Listar arquivos
ls -la

# Ver estrutura
tree -L 2  # ou usar explorador de arquivos
```

### 4️⃣ Iniciar Jupyter Notebook

```bash
jupyter notebook
```

O navegador abrirá automaticamente. Navegue até `data/raw/` para ver o dataset.

---

## 📊 Sobre o Dataset

### Informações Básicas

- **Arquivo:** `data/raw/students_performance.csv`
- **Registros:** 2.510 estudantes universitários
- **Features:** 13 variáveis
- **Variável Alvo:** `final_grade` (nota final, 0-100 pontos)

### Categorias de Variáveis

- 👤 **Demográficas:** idade, gênero, educação dos pais
- 📚 **Acadêmicas:** notas anteriores, frequência, horas de estudo, tutoria
- 💻 **Infraestrutura:** qualidade da internet, atividades extracurriculares
- 🏥 **Bem-estar:** horas de sono, estado de saúde
- 💰 **Socioeconômicas:** renda familiar

### ⚠️ Desafios do Dataset

O dataset contém **problemas intencionais** (dados do mundo real):
- Valores faltantes (~8% dos dados)
- Outliers e valores impossíveis
- Inconsistências e erros de formatação

**Você precisará identificar e tratar esses problemas!**

📖 **Documentação completa:** `data/raw/README.md`

---

## 📁 Estrutura do Repositório

```
.
├── README.md                      # ⭐ Este arquivo (leia primeiro!)
│
├── data/
│   ├── raw/                       # Dados originais (NÃO MODIFICAR!)
│   │   ├── students_performance.csv
│   │   └── README.md             # Documentação do dataset
│   └── processed/                 # Dados limpos (vocês criam)
│
├── notebooks/                     # Notebooks Jupyter (seu trabalho)
│   ├── 00_EXEMPLO_STARTER.py     # Código de exemplo (ponto de partida)
│   └── README.md                 # Guia dos notebooks
│
├── src/                          # Scripts Python (opcional)
│
├── docs/                         # Documentação adicional
│   ├── BOAS_PRATICAS.md         # ⭐ Leia! Guia de boas práticas
│   └── TEMPLATE_RELATORIO_FINAL.md  # Template para relatório final
│
├── requirements.txt              # Dependências do projeto
└── .gitignore                   # Arquivos ignorados pelo Git
```

### 🗂️ Onde Criar Seus Arquivos

Durante o projeto, vocês criarão:

- **Semana 1:** `notebooks/01_EDA.ipynb`
- **Semana 2:** `notebooks/02_Preprocessamento_Baseline.ipynb` + `data/processed/dataset_clean.csv`
- **Semana 3:** `notebooks/03_Modelos_Avancados.ipynb`
- **Semana 4:** `notebooks/04_Otimizacao_Final.ipynb` + `docs/RELATORIO_FINAL.md`

---

## 📚 Recursos Disponíveis

### Documentação Incluída no Projeto

| Arquivo | Para Que Serve |
|---------|----------------|
| **`data/raw/README.md`** | Descrição completa de cada variável do dataset |
| **`notebooks/README.md`** | Como organizar seus notebooks, boas práticas |
| **`notebooks/00_EXEMPLO_STARTER.py`** | Código exemplo de EDA (~300 linhas comentadas) |
| **`docs/BOAS_PRATICAS.md`** | Guia de código limpo, visualizações, modelagem |
| **`docs/TEMPLATE_RELATORIO_FINAL.md`** | Estrutura completa para relatório final |

### Bibliotecas Principais

- **pandas** - Manipulação de dados
- **numpy** - Operações numéricas
- **matplotlib / seaborn** - Visualizações
- **scikit-learn** - Machine Learning
- **xgboost / lightgbm** - Modelos avançados

### Links Úteis

- 📖 [Pandas Documentation](https://pandas.pydata.org/docs/)
- 🤖 [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- 📊 [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- 🎨 [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)

---

## ⚠️ Regras Importantes

### ✅ O Que Você DEVE Fazer

- ✅ Criar notebooks na pasta `notebooks/`
- ✅ Fazer commits frequentes com mensagens descritivas
- ✅ Documentar TUDO em células markdown
- ✅ Salvar dados processados em `data/processed/`
- ✅ Consultar `docs/BOAS_PRATICAS.md` antes de começar
- ✅ Trabalhar em colaboração (todos contribuem!)
- ✅ Executar "Restart & Run All" antes de cada entrega
- ✅ Seguir o cronograma semanal do professor

### ❌ O Que Você NÃO DEVE Fazer

- ❌ Modificar arquivos em `data/raw/` (dados originais)
- ❌ Fazer commit de arquivos grandes (modelos `.pkl` > 100MB)
- ❌ Copiar código de outros grupos (= plágio)
- ❌ Deixar todo o trabalho para uma pessoa só
- ❌ Fazer commit sem testar o código antes
- ❌ Trabalhar no mesmo arquivo simultaneamente (use branches!)
- ❌ Tentar fazer todas as 4 semanas de uma vez

---

## 🆘 Precisa de Ajuda?

### Dúvidas Técnicas

1. **Sobre o dataset:** Leia `data/raw/README.md`
2. **Como começar:** Veja `notebooks/00_EXEMPLO_STARTER.py`
3. **Boas práticas:** Leia `docs/BOAS_PRATICAS.md`
4. **Erros no código:** Consulte a documentação das bibliotecas
5. **Git/GitHub:** Pergunte ao professor ou colegas

### Dúvidas sobre o Projeto

- 📧 **E-mail do professor:** [email do professor]
- 💬 **Horário de atendimento:** [horário]
- 📌 **Fórum da disciplina:** [link se houver]

### Problemas com Git

**Erro comum: "Updates were rejected"**
```bash
# Sempre puxe antes de fazer push
git pull origin main
git push origin main
```

**Conflitos de merge:**
```bash
# Peça ajuda ao professor ou use:
git status  # Ver arquivos em conflito
# Edite os arquivos, resolva os conflitos
git add .
git commit -m "Resolve conflitos"
git push origin main
```

---

## 🎯 Checklist da Primeira Semana

Antes de começar a trabalhar, certifique-se de que:

- [ ] Todos os membros do grupo aceitaram o convite
- [ ] Todos clonaram o repositório
- [ ] Todos configuraram o ambiente virtual
- [ ] Todos instalaram as dependências (`requirements.txt`)
- [ ] Vocês leram `data/raw/README.md` (documentação do dataset)
- [ ] Vocês leram `docs/BOAS_PRATICAS.md`
- [ ] Vocês dividiram as tarefas entre os membros
- [ ] Vocês testaram fazer commit e push

---

## 💡 Dicas de Sucesso

### Para o Grupo

- 🤝 **Comuniquem-se constantemente** (WhatsApp, Discord, etc.)
- 📅 **Marquem reuniões semanais** para alinhar o trabalho
- 🎯 **Definam metas claras** para cada semana
- 🔄 **Revisem o código uns dos outros** antes de fazer push
- 📊 **Mantenham um registro** de quem fez o quê (para o relatório final)

### Para o Código

- 💬 **Comentem TUDO** - você vai esquecer o que fez daqui 1 semana
- 📝 **Usem markdown** - expliquem descobertas, decisões, raciocínio
- 🎨 **Caprichem nas visualizações** - títulos, labels, legendas
- 🧪 **Testem antes de commitar** - execute "Restart & Run All"
- 🔍 **Sejam curiosos** - explore os dados além do mínimo exigido

### Para Git/GitHub

- ✍️ **Commits descritivos:** `"feat: Adiciona análise de correlação"` em vez de `"update"`
- 🔄 **Pull antes de Push:** Sempre `git pull` antes de `git push`
- 🌿 **Branches (opcional):** Para trabalhar em paralelo sem conflitos
- 💾 **Commits frequentes:** Pequenos commits > 1 commit gigante

---

## 📖 Como Usar Este README

**1. Leia este README completo primeiro** (você está aqui!)

**2. Configure seu ambiente** (seção "Primeiros Passos")

**3. Explore a documentação:**
   - `data/raw/README.md` - Entenda o dataset
   - `docs/BOAS_PRATICAS.md` - Aprenda boas práticas
   - `notebooks/README.md` - Veja como organizar notebooks

**4. Aguarde instruções do professor** para a Semana 1

**5. Comece a trabalhar!** 🚀

---

## ❓ Perguntas Frequentes

**P: Posso começar a fazer tudo agora?**
R: Não! Aguarde as instruções semanais do professor. Cada semana tem objetivos específicos.

**P: Como sei qual parte do trabalho devo fazer?**
R: Dividam as tarefas em reunião de grupo. Todos devem contribuir!

**P: Posso usar código da internet?**
R: Sim, mas você deve ENTENDER e ADAPTAR. Copiar sem entender = plágio.

**P: E se eu não souber fazer algo?**
R: Consulte a documentação, peça ajuda aos colegas, procure o professor.

**P: Preciso saber Git muito bem?**
R: Não. Você aprenderá no processo. Use os comandos básicos (pull, add, commit, push).

**P: O que acontece se meu grupo não colaborar?**
R: Documente sua contribuição nos commits. Procure o professor se houver problemas sérios.

---

## 🎉 Pronto para Começar!

Você tem tudo que precisa para iniciar o projeto. Siga o cronograma semanal, trabalhe em equipe e consulte a documentação quando necessário.

**Boa sorte e bom código!** 🚀

---

**📌 Próximo Passo:** Aguarde as instruções da **Semana 1** do professor.

*Última atualização: Outubro 2027*
