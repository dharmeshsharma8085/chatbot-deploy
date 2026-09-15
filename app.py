import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage

# -----------------------------
# Setup
# -----------------------------
load_dotenv()

st.set_page_config(
    page_title="Nova AI",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# Clean CSS
# -----------------------------
st.markdown("""
<style>

    .stApp {
        background-color: #0f1117;
    }

    .block-container {
        max-width: 850px;
        padding-top: 2rem;
        padding-bottom: 7rem;
    }

    section[data-testid="stSidebar"] {
        background-color: #151820;
    }

    .sidebar-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .sidebar-text {
        color: #8b8f98;
        font-size: 13px;
        margin-bottom: 25px;
    }

    .title {
        text-align: center;
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .subtitle {
        text-align: center;
        color: #8b8f98;
        font-size: 14px;
        margin-bottom: 35px;
    }

    .welcome {
        text-align: center;
        color: #8b8f98;
        margin-top: 100px;
        margin-bottom: 100px;
    }

    .welcome-icon {
        font-size: 45px;
        margin-bottom: 15px;
    }

    .welcome h2 {
        color: #ffffff;
        font-size: 24px;
        margin-bottom: 8px;
    }

    div[data-testid="stChatMessage"] {
        padding: 12px 16px;
        border-radius: 14px;
        margin-bottom: 8px;
    }

    div[data-testid="stChatMessage"]:has(
        div[data-testid="chatAvatarIcon-user"]
    ) {
        background-color: #1b2333;
    }

    div[data-testid="stChatMessage"]:has(
        div[data-testid="chatAvatarIcon-assistant"]
    ) {
        background-color: #151820;
    }

    div[data-testid="stChatInput"] {
        background-color: transparent;
    }

    div[data-testid="stChatInput"] textarea {
        background-color: #181b23 !important;
        border: 1px solid #2b2f39 !important;
        border-radius: 14px !important;
        color: white !important;
    }

    div[data-testid="stChatInput"] textarea:focus {
        border-color: #4b5563 !important;
        box-shadow: none !important;
    }

    .stButton button {
        border-radius: 10px;
        background-color: #1b1e26;
        border: 1px solid #2b2f39;
    }

    .stButton button:hover {
        border-color: #555b68;
    }

    hr {
        border-color: #252933;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 12px;
        margin-top: 35px;
        padding: 15px 0;
    }

    .footer b {
        color: #d1d5db;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# LLM
# -----------------------------
llm = ChatOpenAI(
    model="gpt-4.1-mini"
)


# -----------------------------
# Conversation Memory
# -----------------------------
if "messages" not in st.session_state:

    st.session_state.messages = [
        SystemMessage(
            content=(
                "You are Nova, a helpful and friendly AI assistant. "
                "Give clear, accurate and concise answers."
            )
        )
    ]


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🤖 Nova AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-text">Your personal AI assistant</div>',
        unsafe_allow_html=True
    )

    if st.button("＋ New Chat", use_container_width=True):

        st.session_state.messages = [
            SystemMessage(
                content=(
                    "You are Nova, a helpful and friendly AI assistant. "
                    "Give clear, accurate and concise answers."
                )
            )
        ]

        st.rerun()

    st.divider()

    st.caption("MODEL")
    st.write("GPT-4.1 Mini")

    st.caption("POWERED BY")
    st.write("LangChain + OpenAI")


# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="title">Nova AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">How can I help you today?</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Get visible messages
# -----------------------------
chat_messages = [
    message
    for message in st.session_state.messages
    if isinstance(message, (HumanMessage, AIMessage))
]


# -----------------------------
# Welcome Screen
# -----------------------------
if not chat_messages:

    st.markdown(
        """
        <div class="welcome">
            <div class="welcome-icon">🤖</div>
            <h2>Welcome to Nova</h2>
            <p>Ask me anything. I'm here to help.</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# Display Messages
# -----------------------------
for message in chat_messages:

    if isinstance(message, HumanMessage):

        with st.chat_message("user", avatar="🧑"):
            st.markdown(message.content)

    else:

        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(message.content)


# -----------------------------
# User Input
# -----------------------------
user_prompt = st.chat_input(
    "Message Nova..."
)


# -----------------------------
# Generate Response
# -----------------------------
if user_prompt:

    human_message = HumanMessage(
        content=user_prompt
    )

    st.session_state.messages.append(
        human_message
    )

    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_prompt)

    with st.chat_message("assistant", avatar="🤖"):

        with st.spinner("Thinking..."):

            response = llm.invoke(
                st.session_state.messages
            )

        st.markdown(response.content)

    st.session_state.messages.append(
        response
    )


# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <div class="footer">
        Developed by <b>Dharmesh Sharma</b>
        · Powered by LangChain & OpenAI
    </div>
    """,
    unsafe_allow_html=True)