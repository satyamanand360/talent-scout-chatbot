# TalentScout - AI Hiring Assistant (Project by Satyam Anand)
## Project Overview
TalentScout is an intelligent chatbot designed to conduct initial screenings of candidates for a technology recruitment agency. It automates the first steps of the hiring process by gathering essential candidate information and generating relevant technical questions based on their declared tech stack. The application is built with Python and Streamlit and is powered by the Llama 3.1 LLM via the Groq API for real-time, responsive interactions.

How to run ?

git clone [Your GitHub Repository Link Here]
cd [your-repo-folder]

## For Windows
python -m venv venv
venv\Scripts\activate

## For macOS/Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
streamlit run app.py

### Usage Guide:
Once the application is running, open the provided local URL in your browser. The chatbot will greet you and guide you through the screening process. Simply follow its prompts to provide your details and answer the generated technical questions. You can end the conversation at any time.

### Technical Details:
- Frontend: The user interface is built with Streamlit, chosen for its simplicity and speed in creating interactive web applications.
- Language Model: The project uses the Llama 3.1 model (llama-3.1-8b-instant) for its strong conversational and instruction-following abilities.
- API Provider: The Groq API is used to serve the LLM. It was selected for its exceptionally low latency, ensuring a smooth and responsive user experience.
- Architecture: The application uses Streamlit's session_state to manage the conversation history and all collected data. This is a lightweight, serverless approach that respects data privacy by not storing user information persistently.

### Prompt Design:
The core logic of the chatbot is driven by a powerful system prompt. This initial instruction, which is invisible to the user, defines the chatbot's complete persona ("TalentScout"), its precise tasks (e.g., asking for information one piece at a time), conversational rules, and fallback behavior. This method ensures the chatbot remains focused on its primary goal and handles all interactions consistently, leading to a reliable and predictable user experience.

### Challenges & Solutions:
During development, several challenges were encountered and addressed:
- The LLM API provider (Groq) rapidly updated its model names, causing the initially selected models to become decommissioned and return errors.
  Solution: The code was updated to use the latest, officially supported model ID (llama-3.1-8b-instant). This highlights the importance of keeping up with API documentation in a fast-evolving field.
- Challenge: Custom UI styling for the chat bubbles resulted in invisible text when users enabled dark mode in their browser.
  Solution: A more specific CSS rule was added to explicitly set a dark text color within the chat message component, ensuring readability across both light and dark themes.
- Challenge: Ensuring candidate data is handled securely and in compliance with privacy best practices.
  Solution: Instead of using a database or files, all candidate information is stored exclusively in Streamlit's temporary session_state. This data is automatically erased when the user closes the browser tab, ensuring no sensitive information is stored.
