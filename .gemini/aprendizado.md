# Diário de Aprendizado do Murilo

## [2026-03-31] - Docker e Redes
- **O que aprendi:** A diferença entre redes `bridge` (padrão) e `host` (performance).
- **Desafio Socrático:** O Agente Docker me explicou por que o FastAPI precisa do `0.0.0.0` para ser acessível de fora do container.

## [2026-03-31] - Engenharia de Agentes
- **O que aprendi:** Como orquestrar o Antigravity usando um arquivo `.md` para separar responsabilidades de infra e QA.

## [2026-04-08] - Modelagem Preditiva Modular
- **O que aprendi:** Optar por uma "Abordagem Produtiva" estruturada em scripts modulares (em vez de Jupyter Notebooks avulsos) para treinar modelos preditivos garante que o código está pronto para deploy desde o começo. Decidimos usar a suíte do `scikit-learn` (`Pipeline`, `ColumnTransformer`, `OneHotEncoder` para variáveis categóricas como `ocean_proximity`) no `src/` no lugar de deixar tudo solto no notebook. Entendemos também que não devemos descartar as diferentes métricas (RMSE, MAE, R², MAPE) no projeto pessoal, pois explorá-las é benéfico para a interpretação dos resultados do negócio, gerando uma documentação mais aprofundada para o portfólio.