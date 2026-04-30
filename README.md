# London Houses - Regression Analysis With Sells Agent

<details>
  <summary> File tree</summary>

```
London-houses-agents/
│
│
├── data/                       # Dados e armazenamento
│   ├── raw/
│   │   └── Californian_housing.csv
│   ├── processed/
│   │   ├── features_train.pkl
│   │   ├── features_test.pkl
│   │   └── processed_data.pkl
│   ├── external/               # Dados externos para enriquecimento
│   │   ├── Californian_geo.json
│   │   └── demographic_data.csv
│   ├── vector_store/           # Armazenamento vetorial para agentes
│   │   ├── property_embeddings/
│   │   └── sales_knowledge/
│   └── agent_memory/           # Memória de conversas dos agentes
│       ├── conversations.db
│       └── session_store/
│
├── notebooks/                  # Notebooks de exploração
│   ├── 01_data_exploration.ipynb
│   ├── 02_statistical_analysis.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_experiments.ipynb
│   ├── 05_agent_prototyping.ipynb
│   └── 06_dashboard_design.ipynb
│
├── src/                        # Código fonte principal
│   ├── __init__.py
│   ├── main.py                 # Ponto de entrada
│   │
│   ├── data/                   # Pipeline de dados
│   │   ├── __init__.py
│   │   ├── data_loader.py      # Carregamento de dados
│   │   ├── data_processor.py   # Processamento
│   │   ├── feature_engineer.py # Engenharia de features
│   │   └── data_validator.py   # Validação de dados
│   │
│   ├── ml/                     # Modelos de machine learning
│   │   ├── __init__.py
│   │   ├── models/             # Implementações de modelos
│   │   │   ├── base_model.py
│   │   │   ├── linear_regression.py
│   │   │   ├── random_forest.py
│   │   │   ├── xgboost_model.py
│   │   │   └── ensemble.py
│   │   ├── training/           # Treinamento
│   │   │   ├── trainer.py
│   │   │   ├── cross_validation.py
│   │   │   └── hyperparameter_tuning.py
│   │   ├── evaluation/         # Avaliação
│   │   │   ├── evaluator.py
│   │   │   ├── metrics.py
│   │   │   └── explainability.py  # SHAP, LIME
│   │   └── pipeline/           # Pipeline completo
│   │       ├── ml_pipeline.py
│   │       └── inference.py
│   │
│   ├── agents/                 # Sistema de agentes
│   │   ├── __init__.py
│   │   ├── core/               # Núcleo do sistema de agentes
│   │   │   ├── agent_base.py
│   │   │   ├── orchestrator.py
│   │   │   ├── memory_manager.py
│   │   │   └── agent_registry.py
│   │   ├── specialist_agents/  # Agentes especializados
│   │   │   ├── statistical_agent.py
│   │   │   ├── valuation_agent.py
│   │   │   ├── sales_agent.py
│   │   │   ├── market_agent.py
│   │   │   └── visualization_agent.py
│   │   ├── tools/              # Ferramentas dos agentes
│   │   │   ├── data_tools.py
│   │   │   ├── ml_tools.py
│   │   │   ├── visualization_tools.py
│   │   │   └── sales_tools.py
│   │   └── prompts/            # Templates de prompts
│   │       ├── statistical_prompts.yaml
│   │       ├── sales_prompts.yaml
│   │       ├── valuation_prompts.yaml
│   │       └── system_prompts.yaml
│   │
│   ├── dashboard/              # Interface Streamlit
│   │   ├── __init__.py
│   │   ├── app.py              # App principal
│   │   ├── pages/              # Páginas do dashboard
│   │   │   ├── home.py
│   │   │   ├── exploratory_analysis.py
│   │   │   ├── model_comparison.py
│   │   │   ├── property_valuation.py
│   │   │   ├── agent_chat.py
│   │   │   └── market_insights.py
│   │   ├── components/         # Componentes reutilizáveis
│   │   │   ├── charts.py
│   │   │   ├── data_tables.py
│   │   │   ├── property_card.py
│   │   │   └── chat_interface.py
│   │   └── utils/              # Utilitários do dashboard
│   │       ├── theme.py
│   │       ├── session_state.py
│   │       └── formatters.py
│   │
│   ├── api/                    # API REST
│   │   ├── __init__.py
│   │   ├── main.py             # FastAPI app
│   │   ├── routes/             # Rotas da API
│   │   │   ├── predictions.py
│   │   │   ├── agents.py
│   │   │   └── data.py
│   │   ├── schemas/            # Schemas Pydantic
│   │   │   ├── prediction.py
│   │   │   ├── property.py
│   │   │   └── agent.py
│   │   └── dependencies/       # Dependências da API
│   │       ├── auth.py
│   │       └── models.py
│   │
│   └── utils/                  # Utilitários gerais
│       ├── __init__.py
│       ├── config_loader.py
│       ├── logger.py
│       ├── decorators.py
│       └── helpers.py
│
├── models/                     # Modelos treinados
│   ├── trained_models/         # Modelos serializados
│   │   ├── linear_regression.pkl
│   │   ├── random_forest.pkl
│   │   ├── xgboost.pkl
│   │   ├── lightgbm.pkl
│   │   ├── knn.pkl
│   │   └── ensemble.pkl
│   ├── model_artifacts/        # Artefatos dos modelos
│   │   ├── feature_importance/
│   │   ├── shap_values/
│   │   └── training_curves/
│   └── model_registry/         # Registro de modelos (MLflow)
│       ├── models/
│       └── experiments/
│
├── reports/                    # Relatórios e documentação
│   ├── figures/                # Figuras e gráficos
│   │   ├── eda/
│   │   │   ├── distributions.png
│   │   │   ├── correlations.png
│   │   │   └── geographical.png
│   │   ├── models/
│   │   │   ├── performance_comparison.png
│   │   │   ├── feature_importance.png
│   │   │   └── residual_analysis.png
│   │   └── agents/
│   │       ├── agent_interactions.png
│   │       └── sales_pitch_examples.png
│   ├── statistical_reports/    # Relatórios estatísticos
│   │   ├── hypothesis_tests.md
│   │   ├── correlation_analysis.md
│   │   └── assumptions_check.md
│   ├── business_insights/      # Insights de negócio
│   │   ├── market_analysis.md
│   │   ├── investment_opportunities.md
│   │   └── risk_assessment.md
├── docs/                       # Documentação do projeto
│   └── architecture/          # Diagramas e especificações
│       ├── architecture.txt
│       ├── architecture.drawio
│       └── architecture_agent.drawio
│
├── tests/                      # Testes
│   ├── __init__.py
│   ├── unit/                   # Testes unitários
│   │   ├── test_data_processing.py
│   │   ├── test_models.py
│   │   ├── test_agents.py
│   │   └── test_utils.py
│   ├── integration/            # Testes de integração
│   │   ├── test_ml_pipeline.py
│   │   ├── test_agent_system.py
│   │   └── test_api.py
│   └── fixtures/               # Fixtures para testes
│       ├── test_data.py
│       └── test_models.py
│
├── config/                     # Configurações
│   ├── config.yaml             # Configuração principal
│   ├── model_config.yaml       # Configuração de modelos
│   ├── agent_config.yaml       # Configuração de agentes
│   ├── api_config.yaml         # Configuração da API
│   └── dashboard_config.yaml   # Configuração do dashboard
│
├── docker/                     # Configurações Docker
│   ├── Dockerfile.app
│   ├── Dockerfile.api
│   ├── docker-compose.yml
│   └── nginx/
│       └── nginx.conf
│
├── scripts/                    # Scripts utilitários
│   ├── setup_environment.sh
│   ├── run_training.py
│   ├── deploy_model.py
│   ├── start_dashboard.py
│   └── start_api.py
│
├── .env.example                # Variáveis de ambiente exemplo
├── .gitignore
├── pyproject.toml              # Configuração do projeto
├── setup.py                    # Instalação como pacote
├── Makefile                    # Comandos automatizados
├── README.md                   # Documentação principal
├── CONTRIBUTING.md
└── LICENSE
´´´

</details>
