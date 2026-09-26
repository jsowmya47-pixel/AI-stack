
import streamlit as st
import ollama

# -----------------------------------
# 🎨 PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="My AI ChatBot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------
# 🎨 CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

    /* Main Background */
    .stApp {
        background: linear-gradient(
            135deg,
            #0f0c29,
            #302b63,
            #24243e
        );
        color: white;
    }

    /* Main Title */
    h1 {
        color: #00f5ff;
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        text-shadow: 0 0 15px #00f5ff;
    }

    /* Headings */
    h2, h3 {
        color: #00f5ff;
    }

    /* Text */
    p {
        color: #e0e0ff;
    }

    /* Chat Messages */
    [data-testid="stChatMessage"] {
        border-radius: 18px;
        padding: 12px;
        margin: 10px 0;
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(0, 245, 255, 0.2);
    }

    /* Chat Input */
    [data-testid="stChatInput"] {
        border: 1px solid #00f5ff;
        border-radius: 15px;
    }

    /* Buttons */
    .stButton button {
        background: linear-gradient(
            90deg,
            #00f5ff,
            #7b2ff7
        );
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: bold;
        transition: 0.3s;
    }

    .stButton button:hover {
        box-shadow: 0 0 15px #00f5ff;
        transform: scale(1.03);
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #11102b,
            #1b1742
        );
        border-right: 1px solid #7b2ff7;
    }

    /* Welcome Card */
    .welcome-card {
        background: linear-gradient(
            135deg,
            rgba(0,245,255,0.15),
            rgba(123,47,247,0.15)
        );
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        border: 1px solid rgba(0,245,255,0.4);
        margin-bottom: 20px;
    }

    /* Online Status */
    .status-card {
        background: rgba(0,255,170,0.1);
        border: 1px solid #00ffaa;
        border-radius: 12px;
        padding: 12px;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 20px;
        color: #aaaaff;
    }

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# 🤖 SIDEBAR
# -----------------------------------

with st.sidebar:

    st.markdown("## ⚙️ Settings")

    st.markdown("### 🤖 AI Model")

    st.info("Llama 3.2:3b")

    st.markdown("### 🌟 Features")

    st.write("✅ AI Conversations")
    st.write("✅ Local AI Processing")
    st.write("✅ Chat History")
    st.write("✅ Fast Responses")
    st.write("✅ Modern UI")

    st.markdown("---")

    st.markdown("### 💡 About")

    st.write(
        "This chatbot is powered by "
        "Ollama and Llama 3.2."
    )

    st.markdown("---")

    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = []

        st.rerun()

    st.markdown("---")

    st.caption(
        "Made with ❤️ using "
        "Python & Streamlit"
    )

# -----------------------------------
# 🌟 TITLE
# -----------------------------------

st.title("🤖 My AI ChatBot")

st.write(
    "Welcome to my AI ChatBot! "
    "Ask me anything and explore the world of AI. ✨"
)

# -----------------------------------
# 🟢 AI STATUS
# -----------------------------------

st.markdown("""
<div class="status-card">

    <span style="color:#00ffaa;
    font-weight:bold;">

        🟢 AI Online

    </span>

    <br>

    <span style="color:#cccccc;">

        Powered by Llama 3.2 • Local AI

    </span>

</div>
""", unsafe_allow_html=True)

# -----------------------------------
# 💬 SESSION STATE
# -----------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []

# -----------------------------------
# 🌟 WELCOME CARD
# -----------------------------------

if len(st.session_state.messages) == 0:

    st.markdown("""
    <div class="welcome-card">

        <h2 style="color:#00f5ff;">

            👋 Hello, AI Explorer!

        </h2>

        <p>

            Ask me anything and let's explore
            the world of AI together. ✨

        </p>

        <p style="color:#bcbcff;">

            💡 Try asking:
            Explain Python in simple words.

        </p>

    </div>
    """, unsafe_allow_html=True)

# -----------------------------------
# 💡 SUGGESTED QUESTIONS
# -----------------------------------

st.markdown("### 💡 Try asking")

col1, col2, col3 = st.columns(3)

with col1:

    python_btn = st.button(
        "🐍 Python",
        use_container_width=True
    )

with col2:

    ai_btn = st.button(
        "🤖 AI",
        use_container_width=True
    )

with col3:

    coding_btn = st.button(
        "💻 Coding",
        use_container_width=True
    )

# Suggested question selection

suggested_question = None

if python_btn:

    suggested_question = (
        "Explain Python in simple words."
    )

elif ai_btn:

    suggested_question = (
        "What is Artificial Intelligence?"
    )

elif coding_btn:

    suggested_question = (
        "Give me a beginner coding project."
    )

# -----------------------------------
# 💬 DISPLAY CHAT HISTORY
# -----------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])

# -----------------------------------
# 💬 CHAT INPUT
# -----------------------------------

question = st.chat_input(
    "Type your message here...."
)

# Use suggested question if selected

if suggested_question:

    question = suggested_question

# -----------------------------------
# 🤖 CHATBOT RESPONSE
# -----------------------------------

if question:

    # Add user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Display user message

    with st.chat_message("user"):

        st.write(question)

    # Display AI response

    with st.chat_message("assistant"):

        with st.spinner("🤔 AI is thinking..."):

            response = ollama.chat(

                model="llama3.2:3b",

                messages=st.session_state.messages

            )

            answer = response["message"]["content"]

            st.write(answer)

    # Save AI response

    st.session_state.messages.append(

        {
            "role": "assistant",
            "content": answer
        }

    )

# -----------------------------------
# 💜 FOOTER
# -----------------------------------

st.markdown("""
<br><br>

<div class="footer">

    <p>✨ My AI ChatBot ✨</p>

    <p style="font-size:13px;">

        Built with Python • Streamlit • Ollama

    </p>

</div>

""", unsafe_allow_html=True)