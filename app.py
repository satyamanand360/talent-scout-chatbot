import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Groq API Configuration ---
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("GROQ_API_KEY not found. Please set it in your .env file.")
    st.stop()

client = Groq(api_key=api_key)

# --- System Prompt ---
system_prompt = {
    "role": "system",
    "content": """
You are "TalentScout," a friendly, professional, and efficient AI hiring assistant. 
Your primary purpose is to conduct an initial screening of job candidates.

Your tasks are:
1. Greet the candidate and briefly explain your purpose.
2. Collect the following details in order: Full Name, Email Address, Phone Number, Years of Experience, Desired Position(s), Current Location, and Tech Stack. Do not ask for them all at once. Ask for one piece of information at a time.
3. Once the tech stack is provided, generate 3-5 relevant technical questions tailored to the listed technologies.
4. Maintain a polite and conversational tone.
5. If the user's input is unclear or unexpected, politely ask for clarification without deviating from your purpose.
6. Gracefully conclude the conversation by thanking the candidate and explaining the next steps after you have provided the technical questions.
"""
}

# --- UI Enhancements --- 🎨
st.set_page_config(page_title="TalentScout AI", page_icon="🤖")

# This is the new, more advanced CSS block for styling
st.markdown("""
    <style>
        /* General body styling */
        .st-emotion-cache-16txtl3 {
            padding-top: 2rem;
        }

        /* Container for each chat message */
        div[data-testid="stChatMessage"] {
            display: flex;
            align-items: flex-start;
            margin-bottom: 1rem;
        }

        /* Style for the Assistant's message bubble */
        div[data-testid="stChatMessage"]:has(div[data-testid="stAvatarIcon-assistant"]) {
            justify-content: flex-start;
        }
        
        div[data-testid="stChatMessage"]:has(div[data-testid="stAvatarIcon-assistant"]) div[data-testid="stMarkdownContainer"] {
            background-color: #f0f2f6;
            color: #333;
            border-radius: 20px 20px 20px 5px;
            padding: 10px 15px;
            margin-left: 10px;
            max-width: 80%;
        }

        /* Style for the User's message bubble */
        div[data-testid="stChatMessage"]:has(div[data-testid="stAvatarIcon-user"]) {
            justify-content: flex-end; /* This aligns the whole container to the right */
        }

        div[data-testid="stChatMessage"]:has(div[data-testid="stAvatarIcon-user"]) div[data-testid="stMarkdownContainer"] {
            background-color: #0084ff; /* A nice blue for the user */
            color: white;
            border-radius: 20px 20px 5px 20px;
            padding: 10px 15px;
            margin-right: 10px;
            max-width: 80%;
        }
        
        /* Ensure text inside user bubble is white */
        div[data-testid="stChatMessage"]:has(div[data-testid="stAvatarIcon-user"]) p,
        div[data-testid="stChatMessage"]:has(div[data-testid="stAvatarIcon-user"]) li {
            color: white;
        }

        /* Ensure text inside assistant bubble is dark */
        div[data-testid="stChatMessage"]:has(div[data-testid="stAvatarIcon-assistant"]) p,
        div[data-testid="stChatMessage"]:has(div[data-testid="stAvatarIcon-assistant"]) li {
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)


# --- "About Me" Sidebar ---
with st.sidebar:
    st.header("About Me")
    st.info(
        """
        **Satyam Anand**

        I am a data and machine learning enthusiast with a passion for 
        Natural Language Processing (NLP) and Large Language Models (LLMs).

        Currently, I am a dual degree student at the Indian Institute of 
        Technology, Kharagpur, specializing in Signal Processing and Machine Learning.
        """
    )

# App Header
st.title("TalentScout AI 🤖")
st.caption("Your intelligent hiring assistant powered by Llama 3.1")
st.divider()

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        system_prompt,
        {"role": "assistant", "content": "Hello! I'm TalentScout, an AI assistant from the TalentScout recruitment agency. My goal is to gather some initial information about your skills and experience. Shall we begin?"}
    ]

# Display past messages (skipping the system prompt)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# --- Chat Input and Response Logic ---
if prompt := st.chat_input("Your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        chat_completion = client.chat.completions.create(
            messages=st.session_state.messages,
            model="llama-3.1-8b-instant",
        )
        response_content = chat_completion.choices[0].message.content

        st.session_state.messages.append({"role": "assistant", "content": response_content})
        with st.chat_message("assistant"):
            st.markdown(response_content)

    except Exception as e:
        st.error(f"An error occurred: {e}")