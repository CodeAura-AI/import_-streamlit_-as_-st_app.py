import streamlit as st
import random

# Streamlit page configuration
st.set_page_config(
    page_title="FinanceMentor",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for warm, calming design
st.markdown("""
    <style>
    .stApp {
        background-color: #f5f7fa;
    }
    .sidebar .sidebar-content {
        background-color: #e6f0fa;
    }
    .stButton>button {
        background-color: #4a90e2;
        color: white;
        border-radius: 8px;
    }
    .stTextInput>div>input {
        border-radius: 8px;
        border: 1px solid #4a90e2;
    }
    h1, h2, h3 {
        color: #2e5a88;
    }
    .module-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Mock data for modules (to be replaced with book content)
MODULES = [
    {"id": 1, "title": "Financial Foundations", "topics": ["What is money?", "Budgeting basics", "Needs vs wants"], "progress": 0},
    {"id": 2, "title": "Building a Budget", "topics": ["Zero-based budgeting", "50/30/20 rule"], "progress": 0},
    {"id": 3, "title": "Smart Spending", "topics": ["Frugality", "Conscious consumerism", "Debt traps"], "progress": 0},
]

# Mock responses for "Ask Me Anything" (to be replaced with AI-trained responses)
MOCK_RESPONSES = [
    "Great question! Money is a tool for trading value. Start by separating needs from wants. Want to learn budgeting?",
    "Budgeting is like a roadmap for your money. Try the 50/30/20 rule: 50% needs, 30% wants, 20% savings. More details?",
    "Debt can be like a heavy backpack. The debt snowball method pays off smaller debts first. Need a plan?",
]

# Initialize session state
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "progress" not in st.session_state:
    st.session_state.progress = {mod["id"]: 0 for mod in MODULES}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar navigation
st.sidebar.title("FinanceMentor 💸")
page = st.sidebar.radio("Navigate", ["Learn", "Ask Me Anything", "My Progress"])

# Helper function to display a module card
def display_module(module):
    st.markdown(f"<div class='module-card'>", unsafe_allow_html=True)
    st.subheader(module["title"])
    st.write(f"**Topics**: {', '.join(module['topics'])}")
    progress = st.session_state.progress[module["id"]]
    st.progress(progress / 100)
    if st.button(f"Start Module {module['id']}", key=f"module_{module['id']}"):
        st.session_state.progress[module["id"]] = min(progress + 25, 100)
        st.session_state.xp += 10
        st.success(f"Completed a lesson in {module['title']}! +10 XP")
    st.markdown("</div>", unsafe_allow_html=True)

# Learn page
if page == "Learn":
    st.title("Learn with FinanceMentor")
    st.write("Welcome! Let’s build your financial wisdom step by step.")
    for module in MODULES:
        display_module(module)

# Ask Me Anything page
elif page == "Ask Me Anything":
    st.title("Ask FinanceMentor Anything")
    st.write("I’m your wise mentor. Ask any money question, and I’ll explain it simply!")
    user_input = st.text_input("Your question:", key="chat_input")
    if st.button("Ask"):
        if user_input:
            st.session_state.chat_history.append({"role": "user", "message": user_input})
            response = random.choice(MOCK_RESPONSES)
            st.session_state.chat_history.append({"role": "bot", "message": response})
            st.session_state.xp += 5
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(f"**You**: {chat['message']}")
        else:
            st.markdown(f"**FinanceMentor**: {chat['message']}")

# My Progress page
elif page == "My Progress":
    st.title("My Progress")
    st.write("Track your journey to financial freedom!")
    st.metric("Your XP", st.session_state.xp)
    badges = st.session_state.xp // 50
    st.write(f"**Badges Earned**: {badges} 🏅")
    st.subheader("Module Progress")
    for module in MODULES:
        progress = st.session_state.progress[module["id"]]
        st.write(f"**{module['title']}**: {progress}%")
        st.progress(progress / 100)