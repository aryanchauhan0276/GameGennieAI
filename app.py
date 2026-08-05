import streamlit as st
from model import solution
from ui import set_background

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="🎮 GameGenie AI",
    page_icon="🎮",
    layout="wide"
)

# ---------------- LOAD CSS ---------------- #

def load_css():
    with open("style.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

set_background()
load_css()

# ---------------- HEADER ---------------- #

logo_col, title_col = st.columns([6, 8], vertical_alignment="center")

with logo_col:
    st.image("logo.png", width=220)

with title_col:

    st.markdown("""
    <div class="main-title">
        GAMEGENIE AI
    </div>

    <div class="sub-title">
        Discover • Explore • Play • Repeat
        <br>
        ✨ AI Powered Semantic Game Recommendation Engine
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------------- METRIC CARDS ---------------- #
col1, col2, col3 = st.columns(3)

metrics = [
    ("🎮", "20K+", "Games"),
    ("🤖", "AI", "Powered Search"),
    ("⚡", "Fast", "Semantic Search")
]

for col, (icon, title, sub) in zip([col1, col2, col3], metrics):

    with col:

        st.markdown(f"""
<div class="metric-card">

<div class="metric-icon">{icon}</div>

<div class="metric-number">{title}</div>

<div class="metric-text">{sub}</div>

</div>
""", unsafe_allow_html=True)

# ---------------- SEARCH BOX ---------------- #

st.markdown("## 🎯 Choose Your Gaming Mood")

if "prompt" not in st.session_state:
    st.session_state.prompt = ""

col1, col2, col3, col4 = st.columns(4)
# ---------------- GENRE BUTTONS ---------------- #

with col1:

    if st.button("🔥 Action"):
        st.session_state.prompt = "Action game"

    if st.button("👻 Horror"):
        st.session_state.prompt = "Horror game"


with col2:

    if st.button("🧩 Puzzle"):
        st.session_state.prompt = "Puzzle game"

    if st.button("🏎 Racing"):
        st.session_state.prompt = "Racing game"


with col3:

    if st.button("⚔ RPG"):
        st.session_state.prompt = "Role Playing Game"

    if st.button("😌 Relax"):
        st.session_state.prompt = "Relaxing casual game"


with col4:

    if st.button("👨‍👩‍👧 Multiplayer"):
        st.session_state.prompt = "Multiplayer game"

    if st.button("🧟 Survival"):
        st.session_state.prompt = "Survival game"


st.write("")

# ---------------- USER QUERY ---------------- #

query = st.text_area(

    "📝 Describe Your Dream Game",

    value=st.session_state.prompt,

    height=140,

    placeholder="Example: Multiplayer zombie shooting game with futuristic weapons..."
)

search = st.button("🚀 Find My Game")


# ---------------- AI SEARCH ---------------- #

if search:

    if query.strip() == "":
        st.warning("⚠ Please enter a game description.")

    else:

        with st.spinner("🤖 AI is finding the best games for you..."):
            games = solution(query)

        st.success(f"🎉 Found {len(games)} Recommended Games")

        st.markdown("## 🎯 AI Recommendations")

        for i, game in enumerate(games, start=1):

            with st.container(border=True):

                col1, col2 = st.columns([6, 1])

                with col1:
                    st.subheader(f"🎮 {game}")
                    st.caption("⭐ Best AI Match based on semantic similarity")

                with col2:
                    st.metric("Rank", i)

                st.success("🔥 AI Recommended")
st.divider()
st.caption("❤️ Made with Streamlit | Sentence Transformers | Scikit-Learn")