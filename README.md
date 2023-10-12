# Ziomara ZIONE Shop Chatbot

## Overview

Welcome to the Ziomara ZIONE Shop Chatbot repository! This Streamlit-based web application serves as a chatbot interface designed to assist users with various queries related to ZIONE Shop's online selling platform. Powered by a fine-tuned LLaMa 2 70B language model and leveraging the Replicate API for model inference, Ziomara offers personalized responses based on different tones or personas that users can select from the sidebar.

## Table of Contents

- [Imports](#imports)
- [Streamlit Configuration](#streamlit-configuration)
- [Sidebar](#sidebar)
- [Session State](#session-state)
- [Message Handling](#message-handling)
- [Predefined System Prompts](#predefined-system-prompts)
- [Chatbot Logic](#chatbot-logic)

## Imports

- `streamlit` for the web app interface
- `replicate` for model inference
- `os` for environment variable handling

## Streamlit Configuration

- The page title and custom CSS styles are set to provide a user-friendly interface.

## Sidebar

- The sidebar features an image, a title, and a dropdown for selecting the chatbot's persona.
- It also fetches the Replicate API token from `st.secrets` and sets it as an environment variable.

## Session State

- The application utilizes Streamlit's session state to maintain a conversation history.

## Message Handling

- Messages are displayed in a chat interface where the user can interact with the chatbot. The chat history can also be cleared.

## Predefined System Prompts

- The code includes predefined system prompts designed to generate responses in different tones (professional, enthusiastic, commercial).

## Chatbot Logic

- The `generate_ziomara_response()` function interacts with the LLaMa 2 70B language model via the Replicate API. It takes user input and generates a response based on the selected persona.

## Conclusion

Overall, the application is well-structured and serves as a comprehensive customer service solution. Advanced fine-tuning and prompt engineering techniques have been applied to make Ziomara more responsive and accurate.

---

## Author Information

Developed by Juan Jaramillo | Prompt Engineer & AI Expert specialized in Generative AI, Machine Learning Engineering and PEFT and RLHF optimizations.

- 🌐 Website: [juanjaramillo.tech](https://juanjaramillo.tech/)
- 📧 Email: [info@juanjaramillo.tech](mailto:info@juanjaramillo.tech)
- 💼 LinkedIn: [Juan Jaramillo](https://www.linkedin.com/in/juan-jaramillo-ai/)
