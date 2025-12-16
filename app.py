import streamlit as st
import random
import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Cronos: O Enigma Histórico", page_icon="⏳")

# --- ESTILOS CSS ---
st.markdown("""
<style>
    .stButton>button { width: 100%; }
    .guess-box { padding: 10px; border-radius: 5px; margin-bottom: 5px; color: white; text-align: center; font-weight: bold;}
    .correct { background-color: #6aaa64; } /* Verde */
    .partial { background-color: #c9b458; } /* Amarelo - Opcional, dependendo da regra */
    .wrong { background-color: #787c7e; } /* Cinza */
    .higher { background-color: #787c7e; } /* Cinza com seta pra cima (implementado no texto) */
    .lower { background-color: #787c7e; } /* Cinza com seta pra baixo */
</style>
""", unsafe_allow_html=True)

# --- BASE DE DADOS EXPANDIDA (Exemplo com 50 - Adicione mais seguindo o padrão) ---
# Dica: Para 365 figuras, recomendo mover isso para um arquivo 'figures.json' e carregar com json.load()
database = {
    "Napoleão Bonaparte": {"Era": "Moderna", "Continente": "Europa", "Função": "Líder Militar/Político", "Morte": 1821},
    "Júlio César": {"Era": "Antiga", "Continente": "Europa", "Função": "Líder Militar/Político", "Morte": -44},
    "Dom Pedro II": {"Era": "Moderna", "Continente": "América do Sul", "Função": "Monarca", "Morte": 1891},
    "Cleópatra": {"Era": "Antiga", "Continente": "África", "Função": "Monarca", "Morte": -30},
    "Genghis Khan": {"Era": "Medieval", "Continente": "Ásia", "Função": "Líder Militar", "Morte": 1227},
    "Beethoven": {"Era": "Moderna", "Continente": "Europa", "Função": "Artista/Músico", "Morte": 1827},
    "Joana d'Arc": {"Era": "Medieval", "Continente": "Europa", "Função": "Líder Militar/Religiosa", "Morte": 1431},
    "Tupac Shakur": {"Era": "Contemporânea", "Continente": "América do Norte", "Função": "Artista/Músico", "Morte": 1996},
    "Marco Aurélio": {"Era": "Antiga", "Continente": "Europa", "Função": "Monarca/Filósofo", "Morte": 180},
    "Alexandre, o Grande": {"Era": "Antiga", "Continente": "Europa", "Função": "Líder Militar/Monarca", "Morte": -323},
    "Getúlio Vargas": {"Era": "Contemporânea", "Continente": "América do Sul", "Função": "Político", "Morte": 1954},
    "Miyamoto Musashi": {"Era": "Moderna", "Continente": "Ásia", "Função": "Guerreiro/Filósofo", "Morte": 1645},
    "Jesus Cristo": {"Era": "Antiga", "Continente": "Ásia", "Função": "Líder Religioso", "Morte": 33},
    "Albert Einstein": {"Era": "Contemporânea", "Continente": "Europa", "Função": "Cientista", "Morte": 1955},
    "Leonardo da Vinci": {"Era": "Moderna", "Continente": "Europa", "Função": "Polímata/Artista", "Morte": 1519},
    "Nelson Mandela": {"Era": "Contemporânea", "Continente": "África", "Função": "Político/Ativista", "Morte": 2013},
    "Santos Dumont": {"Era": "Contemporânea", "Continente": "América do Sul", "Função": "Inventor", "Morte": 1932},
    "Joaquim José da Silva Xavier (Tiradentes)": {"Era": "Moderna", "Continente": "América do Sul", "Função": "Ativista", "Morte": 1792},
    "Rainha Vitória": {"Era": "Moderna", "Continente": "Europa", "Função": "Monarca", "Morte": 1901},
    "Mahatma Gandhi": {"Era": "Contemporânea", "Continente": "Ásia", "Função": "Líder Político/Religioso", "Morte": 1948},
    "Abraham Lincoln": {"Era": "Moderna", "Continente": "América do Norte", "Função": "Político", "Morte": 1865},
    "Elvis Presley": {"Era": "Contemporânea", "Continente": "América do Norte", "Função": "Artista/Músico", "Morte": 1977},
    "Frida Kahlo": {"Era": "Contemporânea", "Continente": "América do Norte", "Função": "Artista", "Morte": 1954},
    "Sócrates": {"Era": "Antiga", "Continente": "Europa", "Função": "Filósofo", "Morte": -399},
    "Darwin": {"Era": "Moderna", "Continente": "Europa", "Função": "Cientista", "Morte": 1882},
    "Marilyn Monroe": {"Era": "Contemporânea", "Continente": "América do Norte", "Função": "Artista", "Morte": 1962},
    "Pelé": {"Era": "Contemporânea", "Continente": "América do Sul", "Função": "Atleta", "Morte": 2022},
    "Ayrton Senna": {"Era": "Contemporânea", "Continente": "América do Sul", "Função": "Atleta", "Morte": 1994},
    "Machado de Assis": {"Era": "Moderna", "Continente": "América do Sul", "Função": "Escritor", "Morte": 1908},
    "Dante Alighieri": {"Era": "Medieval", "Continente": "Europa", "Função": "Escritor", "Morte": 1321},
    "Simón Bolívar": {"Era": "Moderna", "Continente": "América do Sul", "Função": "Líder Militar", "Morte": 1830},
    "Che Guevara": {"Era": "Contemporânea", "Continente": "América do Sul", "Função": "Revolucionário", "Morte": 1967},
    "Maria Antonieta": {"Era": "Moderna", "Continente": "Europa", "Função": "Monarca", "Morte": 1793},
    "Van Gogh": {"Era": "Moderna", "Continente": "Europa", "Função": "Artista", "Morte": 1890},
    "Pablo Picasso": {"Era": "Contemporânea", "Continente": "Europa", "Função": "Artista", "Morte": 1973},
    "Isaac Newton": {"Era": "Moderna", "Continente": "Europa", "Função": "Cientista", "Morte": 1727},
    "Galileu Galilei": {"Era": "Moderna", "Continente": "Europa", "Função": "Cientista", "Morte": 1642},
    "Nicolau Maquiavel": {"Era": "Moderna", "Continente": "Europa", "Função": "Filósofo/Político", "Morte": 1527},
    "Sigmund Freud": {"Era": "Contemporânea", "Continente": "Europa", "Função": "Cientista", "Morte": 1939},
    "Karl Marx": {"Era": "Moderna", "Continente": "Europa", "Função": "Filósofo/Sociólogo", "Morte": 1883},
    "Martin Luther King Jr.": {"Era": "Contemporânea", "Continente": "América do Norte", "Função": "Ativista", "Morte": 1968},
    "Bruce Lee": {"Era": "Contemporânea", "Continente": "América do Norte", "Função": "Artista Marcial", "Morte": 1973},
    "Bob Marley": {"Era": "Contemporânea", "Continente": "América do Norte", "Função": "Músico", "Morte": 1981},
    "Freddie Mercury": {"Era": "Contemporânea", "Continente": "Europa", "Função": "Músico", "Morte": 1991},
    "Michael Jackson": {"Era": "Contemporânea", "Continente": "América do Norte", "Função": "Músico", "Morte": 2009},
    "Princesa Diana": {"Era": "Contemporânea", "Continente": "Europa", "Função": "Nobreza/Ativista", "Morte": 1997},
    "Steve Jobs": {"Era": "Contemporânea", "Continente": "América do Norte", "Função": "Empresário", "Morte": 2011},
    "Winston Churchill": {"Era": "Contemporânea", "Continente": "Europa", "Função": "Político", "Morte": 1965},
    "Saladino": {"Era": "Medieval", "Continente": "Ásia", "Função": "Líder Militar", "Morte": 1193},
    "Buda (Siddhartha Gautama)": {"Era": "Antiga", "Continente": "Ásia", "Função": "Líder Religioso", "Morte": -483}
}

figures_list = list(database.keys())

# --- FUNÇÕES AUXILIARES ---

def get_daily_figure():
    """Seleciona uma figura baseada no dia atual (seed)."""
    today = datetime.date.today()
    # Usa a data ordinal como seed para garantir que todos tenham o mesmo desafio no dia
    random.seed(today.toordinal())
    return random.choice(figures_list)

def check_guess(target_name, guess_name):
    """Compara o palpite com o alvo e retorna o feedback."""
    target = database[target_name]
    guess = database[guess_name]
    
    feedback = {}
    
    # Compara Era, Continente, Função (Igual ou Não)
    for attr in ["Era", "Continente", "Função"]:
        if guess[attr] == target[attr]:
            feedback[attr] = ("correct", guess[attr])
        else:
            feedback[attr] = ("wrong", guess[attr])
            
    # Compara Morte (Ano) - Verifica se é maior, menor ou igual
    if guess["Morte"] == target["Morte"]:
        feedback["Morte"] = ("correct", str(guess["Morte"]))
    elif guess["Morte"] < target["Morte"]:
        feedback["Morte"] = ("higher", f"{guess['Morte']} (▲)") # Seta para cima (alvo é maior)
    else:
        feedback["Morte"] = ("lower", f"{guess['Morte']} (▼)") # Seta para baixo (alvo é menor)
        
    return feedback

def render_row(feedback, name):
    """Renderiza uma linha de palpite na interface."""
    cols = st.columns(5)
    attrs = ["Nome", "Era", "Continente", "Função", "Morte"]
    
    # Nome
    if feedback == "WIN":
        cols[0].markdown(f"<div class='guess-box correct'>{name}</div>", unsafe_allow_html=True)
        for i in range(1, 5):
             cols[i].markdown(f"<div class='guess-box correct'>✅</div>", unsafe_allow_html=True)
        return

    # Atributos
    cols[0].markdown(f"<div class='guess-box wrong'>{name}</div>", unsafe_allow_html=True)
    
    keys = ["Era", "Continente", "Função", "Morte"]
    for i, key in enumerate(keys):
        status, text = feedback[key]
        cols[i+1].markdown(f"<div class='guess-box {status}'>{text}</div>", unsafe_allow_html=True)

# --- INTERFACE PRINCIPAL ---

st.title("Cronos: O Enigma Histórico ⏳")
st.write("Adivinhe a figura histórica!")

# Abas para os modos de jogo
tab1, tab2 = st.tabs(["📅 Desafio Diário", "🏋️ Modo Treino"])

# --- ABA 1: DESAFIO DIÁRIO ---
with tab1:
    st.header("Desafio do Dia")
    
    target_daily = get_daily_figure()
    
    # Inicializa estado do dia
    if 'daily_guesses' not in st.session_state:
        st.session_state.daily_guesses = []
    if 'daily_game_over' not in st.session_state:
        st.session_state.daily_game_over = False

    # Input do usuário
    daily_guess = st.selectbox("Escolha uma figura (Diário):", [""] + sorted(figures_list), key="daily_input")

    if st.button("Chutar (Diário)"):
        if daily_guess and daily_guess in database and not st.session_state.daily_game_over:
            if daily_guess == target_daily:
                st.session_state.daily_game_over = True
                st.session_state.daily_guesses.append(("WIN", daily_guess))
                st.balloons()
            else:
                feedback = check_guess(target_daily, daily_guess)
                st.session_state.daily_guesses.append((feedback, daily_guess))
        elif st.session_state.daily_game_over:
            st.warning("Você já venceu o desafio de hoje! Volte amanhã ou jogue o Modo Treino.")

    # Exibir tentativas anteriores
    st.markdown("### Tentativas:")
    # Cabeçalho da tabela
    hcols = st.columns(5)
    headers = ["Nome", "Era", "Continente", "Função", "Morte"]
    for i, h in enumerate(headers):
        hcols[i].markdown(f"**{h}**")
        
    for feedback, name in st.session_state.daily_guesses:
        render_row(feedback, name)

# --- ABA 2: MODO TREINO ---
with tab2:
    st.header("Treino Infinito")
    st.info("Jogue quantas vezes quiser. A figura muda ao clicar em 'Nova Partida'.")

    # Inicializa estado do treino
    if 'training_target' not in st.session_state:
        # Seed aleatória baseada no tempo do sistema (padrão do python)
        random.seed(None) 
        st.session_state.training_target = random.choice(figures_list)
        st.session_state.training_guesses = []
        st.session_state.training_game_over = False

    # Botão de Reset
    if st.button("🔄 Nova Partida de Treino"):
        random.seed(None)
        st.session_state.training_target = random.choice(figures_list)
        st.session_state.training_guesses = []
        st.session_state.training_game_over = False
        st.experimental_rerun()

    # Input do usuário (Treino)
    train_guess = st.selectbox("Escolha uma figura (Treino):", [""] + sorted(figures_list), key="train_input")

    if st.button("Chutar (Treino)"):
        if train_guess and train_guess in database and not st.session_state.training_game_over:
            target = st.session_state.training_target
            if train_guess == target:
                st.session_state.training_game_over = True
                st.session_state.training_guesses.append(("WIN", train_guess))
                st.success(f"Parabéns! A figura era **{target}**.")
            else:
                feedback = check_guess(target, train_guess)
                st.session_state.training_guesses.append((feedback, train_guess))

    # Exibir tentativas anteriores (Treino)
    st.markdown("### Tentativas (Treino):")
    t_hcols = st.columns(5)
    for i, h in enumerate(headers):
        t_hcols[i].markdown(f"**{h}**")

    for feedback, name in st.session_state.training_guesses:
        render_row(feedback, name)
