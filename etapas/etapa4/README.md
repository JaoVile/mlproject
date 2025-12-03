    # ⚡ Etapa 4: Otimização e Tuning de Hiperparâmetros

    **Prazo de Entrega:** [Data será informada pelo professor]
    **Peso:** 25% da nota do projeto (2.5 pontos)
    **Entregáveis:**
    - `notebooks/04_Otimizacao.ipynb`
    - Modelo final salvo
    - Apresentação de 15 minutos

    ---

    ## 🎯 Objetivos da Etapa

    Ao final desta etapa, você deve:

    1. **Otimizar hiperparâmetros** - Tuning do melhor modelo da Etapa 3
    2. **Evitar overfitting** - Técnicas de regularização e validação
    3. **Avaliar no conjunto de teste** - Desempenho final do modelo
    4. **Salvar modelo final** - Modelo treinado pronto para produção

    ---

    ## 📋 O Que Você Vai Entregar

    ### 1. Notebook Principal
    **`notebooks/04_Otimizacao.ipynb`**

    Seções obrigatórias:
    1. Recapitulação dos Resultados da Etapa 3
    2. Seleção do Modelo para Otimização
    3. Grid Search ou Random Search
    4. Análise dos Melhores Hiperparâmetros
    5. Treinamento do Modelo Final
    6. Avaliação no Conjunto de Teste
    7. Análise de Erros Detalhada
    8. Salvamento do Modelo
    9. Conclusões Finais

    ### 2. Modelo Treinado
    **`models/modelo_final.pkl`** (ou `.joblib`)
    - Modelo otimizado e treinado
    - Pronto para fazer predições

    ### 3. Apresentação (15 minutos) 🎤

    **O que apresentar:**
    - Recapitulação: melhor modelo da Etapa 3
    - Processo de otimização de hiperparâmetros
    - Hiperparâmetros testados vs selecionados
    - Comparação: modelo antes vs depois da otimização
    - Desempenho final no conjunto de teste
    - Análise de erros e limitações
    - Possíveis melhorias futuras

    **Formato:**
    - 8-12 slides
    - Todos os membros do grupo devem participar
    - Inclua gráficos de comparação
    - Mostre exemplos de predições

    **Critérios de avaliação da apresentação:**
    - Profundidade técnica (35%)
    - Análise crítica do modelo (25%)
    - Visualizações e clareza (20%)
    - Participação de todos (20%)

    ---

    ## 🔍 Análises Obrigatórias

    ### 1. Otimização de Hiperparâmetros

    **Escolha uma técnica:**

    #### Opção A: Grid Search (Busca Exaustiva)
    Testa TODAS as combinações de hiperparâmetros definidas.

    **Pesquise:**
    - Documentação do `sklearn.model_selection.GridSearchCV`
    - Como definir um grid de hiperparâmetros
    - Quais hiperparâmetros são importantes para seu modelo
    - Como usar cross-validation durante o tuning
    - Como extrair os melhores parâmetros

    **Vantagens:** Garante encontrar a melhor combinação no grid
    **Desvantagens:** Pode ser muito lento

    #### Opção B: Random Search (Mais Rápido)
    Testa N combinações ALEATÓRIAS de hiperparâmetros.

    **Pesquise:**
    - Documentação do `sklearn.model_selection.RandomizedSearchCV`
    - Diferença entre Grid Search e Random Search
    - Como definir distribuições de hiperparâmetros
    - Quantas iterações (n_iter) usar
    - Quando usar Random Search vs Grid Search

    **Vantagens:** Muito mais rápido que Grid Search
    **Desvantagens:** Pode não encontrar a combinação ótima

    ### 2. Análise dos Resultados do Tuning

    **Objetivo:** Analisar os resultados do Grid/Random Search.

    **Pesquise:**
    - Atributo `.cv_results_` do GridSearchCV/RandomizedSearchCV
    - Como converter resultados em DataFrame
    - Como encontrar top N melhores combinações
    - Como visualizar comparação entre configurações
    - Como criar gráfico de erro com barras de desvio padrão

    ### 3. Treinamento do Modelo Final

    **Objetivo:** Treinar modelo final com melhores hiperparâmetros usando TREINO + VALIDAÇÃO.

    **Pesquise:**
    - Atributo `.best_estimator_` do GridSearchCV
    - Atributo `.best_params_` para ver os parâmetros escolhidos
    - Como combinar conjuntos de treino e validação (pd.concat)
    - Por que treinar no conjunto completo após tuning

    ### 4. Avaliação Final no Conjunto de Teste

    **⚠️ IMPORTANTE:** Só use o conjunto de teste UMA VEZ!

    **Objetivo:** Avaliar desempenho final do modelo otimizado.

    **Pesquise:**
    - Como fazer predições no conjunto de teste
    - Como calcular MAE, RMSE e R² (já viu na Etapa 3)
    - Por que só podemos usar o teste uma vez
    - Como formatar saída para apresentação clara

    ### 5. Comparação: Antes vs Depois da Otimização

    **Objetivo:** Mostrar o impacto da otimização.

    **Pesquise:**
    - Como criar DataFrame comparativo com pandas
    - Como calcular melhoria percentual
    - Como formatar tabela para apresentação
    - Como interpretar se houve melhoria significativa

    ### 6. Análise de Erros Detalhada

    **Gráficos obrigatórios:**

    #### Scatter: Predito vs Real
    **Pesquise:**
    - Como criar scatter plot com linha diagonal de referência
    - Interpretação: pontos perto da linha = boas predições

    #### Distribuição dos Resíduos
    **Pesquise:**
    - Como criar subplots (1 linha, 2 colunas)
    - Histograma de resíduos com linha vertical em x=0
    - Scatter de resíduos vs predições com linha horizontal em y=0
    - Como interpretar padrões nos resíduos

    #### Análise de Casos Extremos
    **Pesquise:**
    - Como calcular erro absoluto
    - Como encontrar N maiores valores (.nlargest)
    - Como criar tabela mostrando piores predições
    - Como interpretar por que o modelo errou nesses casos

    ### 7. Salvamento do Modelo

    **Objetivo:** Salvar modelo final para uso futuro.

    **Pesquise:**
    - Biblioteca `joblib` para salvar modelos
    - Como criar pasta se não existir (`os.makedirs`)
    - Diferença entre `.joblib` e `.pkl`
    - Como carregar modelo salvo
    - Como testar se o modelo carregado funciona corretamente

    ---

    ## ✅ Critérios de Avaliação

    | Critério | Peso | O Que Avaliamos |
    |----------|:----:|-----------------|
    | **Otimização de Hiperparâmetros** | 30% | Grid/Random Search executado, melhores params identificados |
    | **Avaliação Final** | 25% | Métricas no teste, comparação antes/depois |
    | **Análise de Erros** | 20% | Resíduos, casos extremos, interpretação |
    | **Documentação** | 10% | Markdown claro, decisões justificadas |
    | **Apresentação** | 15% | Clareza, participação, profundidade técnica |

    ---

    ## 📦 Como Entregar

    ### 1. Commit e Push
    ```bash
    # Criar pasta models
    mkdir -p models

    git add notebooks/04_Otimizacao.ipynb
    git add models/modelo_final.joblib
    git commit -m "feat: Completa Etapa 4 - Otimização e modelo final"
    git push origin main
    ```

    ### 2. Apresentação
    - Upload dos slides em `docs/apresentacao_etapa4.pdf`
    - Apresentar na aula marcada pelo professor

    ---

    ## 💡 Dicas Importantes

    **DO:**
    ✅ Documente TODOS os hiperparâmetros testados
    ✅ Use validação cruzada durante o tuning
    ✅ Analise POR QUE o modelo erra (não só QUANTO)
    ✅ Compare antes vs depois da otimização
    ✅ Teste o modelo salvo para garantir que funciona

    **DON'T:**
    ❌ Usar o conjunto de teste durante o tuning (data leakage!)
    ❌ Fazer tuning sem validação cruzada
    ❌ Testar hiperparâmetros aleatoriamente sem critério
    ❌ Esquecer de salvar o modelo final
    ❌ Ignorar análise de erros

    ---

    ## 🎯 Checklist Antes de Entregar

    - [ ] Grid Search ou Random Search executado
    - [ ] Melhores hiperparâmetros identificados
    - [ ] Modelo final treinado com TREINO + VALIDAÇÃO
    - [ ] Avaliação no conjunto de TESTE (uma única vez)
    - [ ] Comparação antes vs depois criada
    - [ ] Análise de resíduos completa
    - [ ] Casos extremos (piores erros) analisados
    - [ ] Modelo salvo em `models/modelo_final.joblib`
    - [ ] Notebook executa "Restart & Run All" sem erros
    - [ ] Apresentação preparada (8-12 slides)

    ---

    ## 🆘 Precisa de Ajuda?

    **Dúvidas comuns:**
    - Grid Search vs Random Search? → Grid = exaustivo mas lento; Random = mais rápido
    - Quantos hiperparâmetros testar? → Comece com 3-4 principais
    - Overfitting após tuning? → Verifique validação cruzada, pode precisar regularização

    **Consulte:**
    - Scikit-learn hyperparameter tuning: https://scikit-learn.org/stable/modules/grid_search.html
    - XGBoost tuning guide: https://xgboost.readthedocs.io/en/stable/tutorials/param_tuning.html
    - Material da aula de otimização

    ---

    **Ótima otimização!** ⚡

    *Última atualização: Outubro 2027*
