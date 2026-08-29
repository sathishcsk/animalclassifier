Local AI Animal Classifier

Application Flow

Streamlit UI
    ↓
FastAPI
    ↓
Local Ollama
    ↓
Qwen2.5
    ↓
AI determines classification
    ↓
FastAPI returns JSON
    ↓
Streamlit displays result

Streamlit UI accepts the creature name from the user.

FastAPI receives the request from Streamlit.

Local Ollama runs the AI model on the local system.

Qwen2.5 processes the input.

AI determines the classification such as Land Animal, Bird, Sea Creature, or Unknown.

FastAPI returns JSON, and Streamlit displays the classification result.