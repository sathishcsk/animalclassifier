Project Objective

This project is designed to validate a reusable local AI application workflow rather than implement only a simple classification use case. The current animal classifier demonstrates how a Streamlit user interface can send requests through FastAPI to a locally hosted LLM using Ollama. The classification function can be replaced with other business or domain-specific functions without changing the overall application architecture. Similarly, Qwen2.5 can be replaced with another compatible local model based on performance, accuracy, or hardware requirements. The primary objective is to build, understand, and test a modular AI workflow that can later support more practical and advanced use cases.
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
