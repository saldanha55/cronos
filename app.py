import streamlit as st
import random
import datetime
from dados import database # Importando do arquivo separado

# --- CONFIGURAÇÃO DA PÁGINA (WIDE PARA OCUPAR TELA TODA) ---
st.set_page_config(page_title="Cronos", page_icon="⏳", layout="wide")

# --- ESTILOS CSS (DESIGN MODERNO E RESPONSIVO) ---
st.markdown("""
<style>
    /* Fonte e Layout Geral */
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    
    /* Estilo das Caixas de Palpite */
    .guess-box { 
        padding: 12px 5px; 
        border-radius: 8px; 
        margin-bottom: 8px; 
        color: white; 
        text-align: center; 
        font-weight: 600;
        font-size: 0.9rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        height: 100%;
        display: flex;
        align-items: center;
        justify_content: center;
    }
    
    /* Cores de Feedback */
    .correct { background-color: #538d4e; border: 1px solid #538d4e; } /* Verde Wordle */
    .wrong { background-color: #3a3a3c; border: 1px solid #3a3a3c; }   /* Cinza Escuro */
    .higher { background-color: #3a3a3c; border-bottom: 4px solid #b59f3b; } /* Cinza com indicação amarela */
    .lower { background-color: #3a3a3c; border-top: 4px solid #b59f3b; }   /* Cinza com indicação amarela */
    
    /* Ajuste para Mobile - Texto menor se necessário */
    @media (max-width: 600px) {
        .guess-box { font-size: 0.75rem; padding: 8px 2px; }
    }

    /* Estilização da Selectbox e Botão */
    .stSelectbox > div > div { background-color: #f0f2f6; color: black; }
    .stButton>button { 
        width: 100%; 
        background-color: #538d4e; 
        color: white; 
        font-weight: bold;
        border: none;
        padding: 0.5rem;
    }
    .stButton>button:hover { background-color: #406e3b; color: white; }
</style>
""", unsafe_allow_html=True)

figures_list = sorted(list(database.keys()))

# --- FUNÇÕES ---

def get_daily_figure():
    today = datetime.date.today()
    random.seed(today.toordinal())
    return random.choice(figures_list)

def check_guess(target_name, guess_name):
    target = database[target_name]
    guess = database[guess_name]
    feedback = {}
    
    # Atributos simples
    for attr in ["Era", "Continente", "Função"]:
        if guess[attr] == target[attr]:
            feedback[attr] = ("correct", guess[attr])
        else:
            feedback[attr] = ("wrong", guess[attr])
            
    # Ano de Morte (Lógica de dicas visuais)
    target_death = target["Morte"]
    guess_death = guess["Morte"]
    
    if guess_death == target_death:
        feedback["Morte"] = ("correct", str(guess_death))
    elif guess_death < target_death:
        # Chute foi menor que o alvo (o alvo é maior/mais recente)
        feedback["Morte"] = ("higher", f"{guess_death} ▲") 
    else:
        # Chute foi maior que o alvo (o alvo é menor/mais antigo)
        feedback["Morte"] = ("lower", f"{guess_death} ▼")
        
    return feedback

def render_header():
    cols = st.columns(5)
    headers = ["FIGURA", "ERA", "CONTINENTE", "FUNÇÃO", "MORTE"]
    for i, h in enumerate(headers):
        cols[i].markdown(f"<div style='text-align:center; color:#888; font-size:0.8rem; margin-bottom:5px;'>{h}</div>", unsafe_allow_html=True)

def render_row(feedback, name):
    cols = st.columns(5)
    
    # Se ganhou
    if feedback == "WIN":
        cols[0].markdown(f"<div class='guess-box correct'>{name}</div>", unsafe_allow_html=True)
        for i in range(1, 5):
             cols[i].markdown(f"<div class='guess-box correct'>Correto</div>", unsafe_allow_html=True)
        return

    # Se errou (renderiza cada atributo)
    # Coluna 1: Nome (sempre errado se chegou aqui)
    cols[0].markdown(f"<div class='guess-box wrong'>{name}</div>", unsafe_allow_html=True)
    
    keys = ["Era", "Continente", "Função", "Morte"]
    for i, key in enumerate(keys):
        status, text = feedback[key]
        cols[i+1].markdown(f"<div class='guess-box {status}'>{text}</div>", unsafe_allow_html=True)

# --- APP ---

st.title("CRONOS")
st.markdown("**Enigma Histórico Diário**")

# Abas limpas
tab_game, tab_train, tab_about = st.tabs(["JOGO DIÁRIO", "TREINO LIVRE", "SOBRE"])

# === MODO DIÁRIO ===
with tab_game:
    target_daily = get_daily_figure()
    
    if 'daily_guesses' not in st.session_state:
        st.session_state.daily_guesses = []
    if 'daily_game_over' not in st.session_state:
        st.session_state.daily_game_over = False

    # Filtra lista para não permitir repetir chute
    guessed_names = [g[1] for g in st.session_state.daily_guesses]
    available_options = [f for f in figures_list if f not in guessed_names]

    # Área de Input (Centralizada e limpa)
    if not st.session_state.daily_game_over:
        c1, c2 = st.columns([3, 1])
        with c1:
            # O selectbox permite digitar para filtrar automaticamente
            daily_guess = st.selectbox(
                "Pesquise a figura histórica:", 
                options=[""] + available_options, 
                key="daily_input",
                label_visibility="collapsed",
                placeholder="Digite para buscar..."
            )
        with c2:
            btn_chute = st.button("CONFIRMAR", key="btn_daily")

        if btn_chute and daily_guess:
            if daily_guess == target_daily:
                st.session_state.daily_game_over = True
                st.session_state.daily_guesses.insert(0, ("WIN", daily_guess)) # Insere no topo
                st.balloons()
            else:
                feedback = check_guess(target_daily, daily_guess)
                st.session_state.daily_guesses.insert(0, (feedback, daily_guess)) # Insere no topo
                st.experimental_rerun()

    # Feedback de Vitória
    if st.session_state.daily_game_over:
        st.success(f"Parabéns! A figura era **{target_daily}**.")

    st.divider()
    
    # Renderiza tabela de tentativas
    if st.session_state.daily_guesses:
        render_header()
        for feedback, name in st.session_state.daily_guesses:
            render_row(feedback, name)

# === MODO TREINO ===
with tab_train:
    if 'training_target' not in st.session_state:
        random.seed(None)
        st.session_state.training_target = random.choice(figures_list)
        st.session_state.training_guesses = []
        st.session_state.training_game_over = False

    # Botão de Reset no topo
    if st.button("NOVA PARTIDA", type="secondary"):
        st.session_state.training_target = random.choice(figures_list)
        st.session_state.training_guesses = []
        st.session_state.training_game_over = False
        st.experimental_rerun()

    # Filtra lista
    train_guessed_names = [g[1] for g in st.session_state.training_guesses]
    train_available = [f for f in figures_list if f not in train_guessed_names]

    if not st.session_state.training_game_over:
        c1, c2 = st.columns([3, 1])
        with c1:
            train_guess = st.selectbox(
                "Pesquise:", 
                options=[""] + train_available, 
                key="train_input",
                label_visibility="collapsed"
            )
        with c2:
            btn_train = st.button("CONFIRMAR", key="btn_train")

        if btn_train and train_guess:
            target = st.session_state.training_target
            if train_guess == target:
                st.session_state.training_game_over = True
                st.session_state.training_guesses.insert(0, ("WIN", train_guess))
            else:
                feedback = check_guess(target, train_guess)
                st.session_state.training_guesses.insert(0, (feedback, train_guess))
                st.experimental_rerun()

    if st.session_state.training_game_over:
        st.success(f"Acertou! Era **{st.session_state.training_target}**.")

    st.divider()
    
    if st.session_state.training_guesses:
        render_header()
        for feedback, name in st.session_state.training_guesses:
            render_row(feedback, name)

# === SOBRE ===
with tab_about:
    st.markdown("### Criador")
    col_a, col_b = st.columns([1, 4])
    
    with col_a:
        try:
            st.image("perfil.jpg", use_column_width=True)
        except:
            st.warning("Sem foto")
            
    with col_b:
        st.markdown("**Nic Saldanha**")
        st.caption("Estudante de Informática | Músico | Dev")
        st.markdown("Obrigado por jogar Cronos! Este projeto é feito com carinho para amantes de história.")
        
        st.markdown("---")
        st.markdown("**Apoie o projeto:**")
        st.code("119.978.036-74", language="text")
        st.markdown("[Instagram @nicsaldanha](https://instagram.com/nicsaldanha)")
