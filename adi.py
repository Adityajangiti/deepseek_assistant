# import streamlit as st
# from ollama import Ollama

# st.title("DeepSeek-R1:1.5b Assistant")
# st.subheader("Powered by Ollama")

# # Initialize Ollama with DeepSeek-R1:1.5b model
# ollama = Ollama(model="deepseek-r1:1.5b")

# # Create a text input box
# user_input = st.text_input("Enter your query:")

# # Display the response
# if st.button("Submit"):
#     response = ollama.generate(user_input)
#     st.write(response)



# import streamlit as st
# import ollama

# st.title("DeepSeek-R1:1.5B Assistant")
# st.subheader("Powered by Ollama")

# # Create a text input box
# user_input = st.text_input("Enter your query:")

# # Display the response
# if st.button("Submit") and user_input:
#     response = ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": user_input}])
#     st.write(response["message"]["content"])






import streamlit as st
import ollama
import base64
from pathlib import Path

# Function to add background image
def add_bg_from_path(image_path):
    img_data = Path(image_path).read_bytes()
    encoded_img = base64.b64encode(img_data).decode("utf-8")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_img}");
            background-attachment: fixed;
            background-size: cover;
        }}
        /* Custom styles for better visibility */
        .stTextInput {{
            background-color: rgba(0, 0, 0, 0.8);
            color: white;
        }}
        .stMarkdown {{
            background-color: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 10px;
            border-radius: 5px;
        }}
        .title {{
            position: absolute;
            top: 20px;
            left: 20px;
            color: white;
            padding: 5px 10px;
            background-color: rgba(0, 0, 0, 0.9);
            border-radius: 5px;
        }}
        .response-container {{
            background-color: rgba(0, 0, 0, 0.9);
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Configure page
st.set_page_config(page_title="AJ'S DeepSeek Assistant", layout="wide")

# Add background
add_bg_from_path("Screenshot 2025-01-31 023542.png")

# Small title on the left
st.markdown("<div class='title'>AJ</div>", unsafe_allow_html=True)

# Create a text input box
user_input = st.text_input("Enter your query:")

# Display the response
if st.button("Submit") and user_input:
    response = ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": user_input}])
    # Modify the response to start with "Darling"
    modified_response = "Darling, " + response["message"]["content"]
    st.markdown(f"""
        <div class='response-container'>
            {modified_response}
        </div>
    """, unsafe_allow_html=True)


