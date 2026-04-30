import streamlit as st
import pandas as pd
import joblib
import os

# Configuração da página para um visual mais premium
st.set_page_config(
    page_title="London Houses | Smart Real Estate",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização customizada (CSS)
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        border: none;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    .prediction-box {
        background-color: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        text-align: center;
        border-top: 5px solid #4CAF50;
    }
    .price-text {
        font-size: 2.5rem;
        color: #2c3e50;
        font-weight: 800;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Cache para carregar o modelo apenas uma vez
@st.cache_resource
def load_model():
    # Caminho absoluto baseado na localização deste script (src/app/app.py)
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    model_path = os.path.join(base_dir, "models", "trained_models", "xgboost_model.pkl")
    preprocessor_path = os.path.join(base_dir, "models", "trained_models", "preprocessor.pkl")
    
    if os.path.exists(model_path) and os.path.exists(preprocessor_path):
        model = joblib.load(model_path)
        preprocessor = joblib.load(preprocessor_path)
        return model, preprocessor
    return None, None

model, preprocessor = load_model()

# Header
st.title("🏠 London Houses AI Predictor")
st.markdown("### Previsão inteligente de valores imobiliários usando Machine Learning")
st.markdown("---")

# Layout principal
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📍 Características do Imóvel")
    with st.form("prediction_form"):
        longitude = st.slider("Longitude", -124.35, -114.31, -122.23, step=0.01)
        latitude = st.slider("Latitude", 32.54, 41.95, 37.88, step=0.01)
        housing_median_age = st.slider("Idade Média das Casas", 1.0, 52.0, 41.0, step=1.0)
        total_rooms = st.number_input("Total de Quartos (Bloco)", value=880.0, step=10.0)
        total_bedrooms = st.number_input("Total de Quartos de Dormir", value=129.0, step=1.0)
        population = st.number_input("População do Bloco", value=322.0, step=10.0)
        households = st.number_input("Número de Famílias", value=126.0, step=1.0)
        median_income = st.slider("Renda Média (x$10.000)", 0.4999, 15.0001, 8.3252, step=0.1)
        ocean_proximity = st.selectbox("Proximidade do Oceano", 
                                      ['NEAR BAY', '<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND'])
        
        submit_button = st.form_submit_button(label="🔮 Estimar Valor do Imóvel")

with col2:
    st.subheader("💡 Resultado da Avaliação")
    
    if submit_button:
        if model is None:
            st.error("⚠️ Modelo não encontrado! Por favor, treine o modelo primeiro executando o script `trainer.py`.")
        else:
            with st.spinner("Analisando dados do mercado..."):
                # Criar DataFrame com o input
                input_data = pd.DataFrame({
                    "longitude": [longitude],
                    "latitude": [latitude],
                    "housing_median_age": [housing_median_age],
                    "total_rooms": [total_rooms],
                    "total_bedrooms": [total_bedrooms],
                    "population": [population],
                    "households": [households],
                    "median_income": [median_income],
                    "ocean_proximity": [ocean_proximity]
                })
                
                try:
                    # Pré-processar e prever
                    processed_data = preprocessor.transform(input_data)
                    prediction = model.predict(processed_data)[0]
                    
                    # Exibir resultado com estilo premium
                    st.markdown(f"""
                    <div class="prediction-box">
                        <p style="color: #7f8c8d; font-size: 1.1rem; text-transform: uppercase; letter-spacing: 1px;">Valor Estimado</p>
                        <h1 class="price-text">$ {prediction:,.2f}</h1>
                        <p style="color: #95a5a6; font-size: 0.9rem;">Baseado no algoritmo XGBoost com 81% de R² Score</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Seção futura para GenAI (Chatbot)
                    st.markdown("---")
                    st.subheader("🤖 Assistente de IA Corretor (Em breve)")
                    st.info("Aqui podemos integrar um chat usando LangChain/OpenAI para que o usuário faça perguntas sobre o imóvel ou peça sugestões de como valorizar a casa antes de vender.")
                
                except Exception as e:
                    st.error(f"Erro durante a previsão: {e}")
    else:
        st.info("👈 Preencha as características do imóvel no painel ao lado e clique em **Estimar Valor do Imóvel** para ver a previsão da IA.")
