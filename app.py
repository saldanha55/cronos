import streamlit as st
import random
import datetime
import csv
import os
import pandas as pd
from dados import database

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Cronos", page_icon="⏳", layout="wide")

# --- ARQUIVO DE LEADERBOARD ---
LEADERBOARD_FILE = "ranking.csv"

# --- ESTILOS CSS ---
st.markdown("""
<style>
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    
    .guess-box { 
        padding: 12px 5px; border-radius: 8px; margin-bottom: 8px; 
        color: white; text-align: center; font-weight: 600; font-size: 0.9rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .correct { background-color: #538d4e; border: 1px solid #538d4e; }
    .wrong { background-color: #3a3a3c; border: 1px solid #3a3a3c; }
    .higher { background-color: #3a3a3c; border-bottom: 4px solid #b59f3b; }
    .lower { background-color: #3a3a3c; border-top: 4px solid #b59f3b; }
    
    .hint-box {
        background-color: #262730; border-left: 5px solid #ff4b4b;
        padding: 15px; border-radius: 5px; margin-bottom: 10px;
        font-style: italic; color: #e0e0e0;
    }
    .hint-label { font-weight: bold; color: #ff4b4b; display: block; margin-bottom: 5px; }

    .stButton>button { width: 100%; font-weight: bold; }
    
    .score-highlight { font-size: 2rem; font-weight: bold; color: #538d4e; }
</style>
""", unsafe_allow_html=True)

figures_list = sorted(list(database.keys()))

# --- FUNÇÕES DE LÓGICA DO JOGO ---

def get_daily_figure():
    today = datetime.date.today()
    random.seed(today.toordinal())
    return random.choice(figures_list)

def check_guess(target_name, guess_name):
    target = database[target_name]
    guess = database[guess_name]
    feedback = {}
    
    for attr in ["Era", "Continente", "Função"]:
        if guess[attr] == target[attr]:
            feedback[attr] = ("correct", guess[attr])
        else:
            feedback[attr] = ("wrong", guess[attr])
            
    target_death = target["Morte"]
    guess_death = guess["Morte"]
    
    if guess_death == target_death:
        feedback["Morte"] = ("correct", str(guess_death))
    elif guess_death < target_death:
        feedback["Morte"] = ("higher", f"{guess_death} ▲") 
    else:
        feedback["Morte"] = ("lower", f"{guess_death} ▼")
        
    return feedback

def calculate_score(total_guesses, hints_opened):
    wrong_guesses = max(0, total_guesses - 1)
    extra_hints = max(0, hints_opened - 1)
    score = 1000 - (wrong_guesses * 50) - (extra_hints * 150)
    return max(0, score)

# --- FUNÇÕES DE LEADERBOARD ---

def save_score_to_csv(name, score):
    today = datetime.date.today().isoformat()
    file_exists = os.path.isfile(LEADERBOARD_FILE)
    
    with open(LEADERBOARD_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Data", "Nome", "Pontos"])
        writer.writerow([today, name, score])

def get_leaderboard_data():
    if not os.path.isfile(LEADERBOARD_FILE):
        return pd.DataFrame(columns=["Data", "Nome", "Pontos"])
    
    df = pd.read_csv(LEADERBOARD_FILE)
    today = datetime.date.today().isoformat()
    df_today = df[df["Data"] == today]
    df_today = df_today.sort_values(by="Pontos", ascending=False).reset_index(drop=True)
    return df_today

# --- FUNÇÕES DE RENDERIZAÇÃO ---

def render_header():
    cols = st.columns(5)
    headers = ["FIGURA", "ERA", "CONTINENTE", "FUNÇÃO", "MORTE"]
    for i, h in enumerate(headers):
        cols[i].markdown(f"<div style='text-align:center; color:#888; font-size:0.8rem;'>{h}</div>", unsafe_allow_html=True)

def render_row(feedback, name):
    cols = st.columns(5)
    if feedback == "WIN":
        cols[0].markdown(f"<div class='guess-box correct'>{name}</div>", unsafe_allow_html=True)
        for i in range(1, 5): cols[i].markdown(f"<div class='guess-box correct'>Correto</div>", unsafe_allow_html=True)
        return

    cols[0].markdown(f"<div class='guess-box wrong'>{name}</div>", unsafe_allow_html=True)
    keys = ["Era", "Continente", "Função", "Morte"]
    for i, key in enumerate(keys):
        status, text = feedback[key]
        cols[i+1].markdown(f"<div class='guess-box {status}'>{text}</div>", unsafe_allow_html=True)

def render_hints(target_name, context_key):
    target_data = database[target_name]
    if "Dicas" in target_data:
        hints_list = target_data["Dicas"]
    else:
        hints_list = [target_data.get("Dica", "Sem dica disponível.")]

    session_key = f"{context_key}_hints_count"
    if session_key not in st.session_state:
        st.session_state[session_key] = 1 

    current_count = st.session_state[session_key]
    total_hints = len(hints_list)

    for i in range(current_count):
        if i < total_hints:
            label = "🗣️ Monólogo Inicial" if i == 0 else f"🗣️ Dica {i+1} (-150 pts)"
            st.markdown(f"<div class='hint-box'><span class='hint-label'>{label}:</span>\"{hints_list[i]}\"</div>", unsafe_allow_html=True)

    if current_count < total_hints and not st.session_state.get(f"{context_key}_game_over", False):
        if st.button(f"🔍 Revelar Dica {current_count + 1} (Custa 150 pts)", key=f"btn_hint_{context_key}"):
            st.session_state[session_key] += 1
            st.rerun()

# --- APP ---

st.title("CRONOS")
st.markdown("**Enigma Histórico Diário**")

tab_game, tab_train, tab_about = st.tabs(["JOGO DIÁRIO", "TREINO LIVRE", "SOBRE"])

# === MODO DIÁRIO ===
with tab_game:
    target_daily = get_daily_figure()
    
    if 'daily_guesses' not in st.session_state: st.session_state.daily_guesses = []
    if 'daily_game_over' not in st.session_state: st.session_state.daily_game_over = False
    if 'daily_score_submitted' not in st.session_state: st.session_state.daily_score_submitted = False
    
    if not st.session_state.daily_game_over:
        st.markdown("### Quem sou eu?")
        render_hints(target_daily, "daily")
        
        st.divider()
        
        guessed_names = [g[1] for g in st.session_state.daily_guesses]
        available_options = [f for f in figures_list if f not in guessed_names]

        c1, c2 = st.columns([3, 1])
        with c1:
            daily_guess = st.selectbox("Palpite:", [""] + available_options, key="daily_input", label_visibility="collapsed")
        with c2:
            if st.button("CONFIRMAR", key="btn_daily") and daily_guess:
                if daily_guess == target_daily:
                    st.session_state.daily_game_over = True
                    st.session_state.daily_guesses.insert(0, ("WIN", daily_guess))
                    st.balloons()
                    st.rerun()
                else:
                    feedback = check_guess(target_daily, daily_guess)
                    st.session_state.daily_guesses.insert(0, (feedback, daily_guess))
                    st.rerun()
                    
        if st.session_state.daily_guesses:
            st.markdown("---")
            render_header()
            for feedback, name in st.session_state.daily_guesses:
                render_row(feedback, name)

    else:
        final_score = calculate_score(len(st.session_state.daily_guesses), st.session_state.daily_hints_count)
        
        st.success(f"Parabéns! A figura era **{target_daily}**.")
        
        col_score, col_blank = st.columns([1, 2])
        with col_score:
            st.metric(label="Sua Pontuação Final", value=f"{final_score} PTS")
        
        st.markdown("---")
        
        if not st.session_state.daily_score_submitted:
            st.markdown("### 🏆 Registre seu feito, Viajante do Tempo!")
            with st.form("score_form"):
                traveler_name = st.text_input("Seu Nome ou Apelido:")
                submitted = st.form_submit_button("Gravar no Leaderboard")
                
                if submitted and traveler_name:
                    save_score_to_csv(traveler_name, final_score)
                    st.session_state.daily_score_submitted = True
                    st.rerun()
                elif submitted and not traveler_name:
                    st.error("Por favor, digite um nome.")
        
        else:
            st.markdown("### 📊 Leaderboard do Dia")
            df_leaderboard = get_leaderboard_data()
            df_leaderboard.index = df_leaderboard.index + 1
            
            tab_top10, tab_geral = st.tabs(["Top 10", "Geral"])
            
            with tab_top10:
                if not df_leaderboard.empty:
                    # Voltamos para use_container_width=True (seguro)
                    st.dataframe(df_leaderboard.head(10), use_container_width=True) 
                else:
                    st.info("Ainda sem registros hoje.")
                    
            with tab_geral:
                if not df_leaderboard.empty:
                    st.dataframe(df_leaderboard, use_container_width=True)
                else:
                    st.info("Ainda sem registros hoje.")

# === MODO TREINO ===
with tab_train:
    if 'training_target' not in st.session_state:
        random.seed(None)
        st.session_state.training_target = random.choice(figures_list)
        st.session_state.training_guesses = []
        st.session_state.training_game_over = False
        st.session_state.training_hints_count = 1 

    if st.button("NOVA PARTIDA", type="secondary"):
        st.session_state.training_target = random.choice(figures_list)
        st.session_state.training_guesses = []
        st.session_state.training_game_over = False
        st.session_state.training_hints_count = 1 
        st.rerun()

    target_train = st.session_state.training_target
    
    st.markdown("### Quem sou eu?")
    render_hints(target_train, "training")
    
    st.divider()

    train_guessed = [g[1] for g in st.session_state.training_guesses]
    train_available = [f for f in figures_list if f not in train_guessed]

    if not st.session_state.training_game_over:
        c1, c2 = st.columns([3, 1])
        with c1:
            train_guess = st.selectbox("Palpite:", [""] + train_available, key="train_input", label_visibility="collapsed")
        with c2:
            if st.button("CONFIRMAR", key="btn_train") and train_guess:
                if train_guess == target_train:
                    st.session_state.training_game_over = True
                    st.session_state.training_guesses.insert(0, ("WIN", train_guess))
                    st.rerun()
                else:
                    feedback = check_guess(target_train, train_guess)
                    st.session_state.training_guesses.insert(0, (feedback, train_guess))
                    st.rerun()
    else:
        score_train = calculate_score(len(st.session_state.training_guesses), st.session_state.training_hints_count)
        st.success(f"Acertou! Era **{target_train}**. Pontuação simulada: {score_train}")

    if st.session_state.training_guesses:
        st.markdown("---")
        render_header()
        for feedback, name in st.session_state.training_guesses:
            render_row(feedback, name)

# === SOBRE ===
with tab_about:
    st.markdown("### Criador")
    col_a, col_b = st.columns([1, 4])
    with col_a:
        try: 
            st.image("perfil.jpg", width=200) 
        except: 
            st.warning("Sem foto")
    with col_b:
        st.markdown("**Nic Saldanha**")
        st.caption("Estudante de Informática | Músico | Dev")
        st.markdown("Obrigado por jogar Cronos!")
        st.markdown("---")
        st.code("119.978.036-74", language="text")
        st.markdown("[Instagram @nicsaldanha](https://instagram.com/nicsaldanha)")
