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
            background-color: rgba(0, 0, 0, 0);
            color: white;
            text-align: center;
            width: 500px; /* Adjusted width */
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
        .query-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 10vh; /* Adjusted height */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Configure page
st.set_page_config(page_title="DeepSeek Assistant", layout="wide")

# Add background
add_bg_from_path("Screenshot 2025-01-31 023542.png")

# Small title on the left
st.markdown("<div class='title'>AJ</div>", unsafe_allow_html=True)

# Center the query input box with a container
st.markdown("<div class='query-container'>", unsafe_allow_html=True)
user_input = st.text_input("Enter your query:", key="query_input", help="Type your query here", label_visibility="hidden")
st.markdown("</div>", unsafe_allow_html=True)

# Center the button and response container
if st.button("Submit") and user_input:
    response = ollama.chat(model="deepseek-r1:7b", messages=[{"role": "user", "content": user_input}])
    # Modify the response to start with "Darling"
    modified_response = "Darling, " + response["message"]["content"]
    st.markdown(f"""
        <div style='background-color: rgba(0, 0, 0, 0.9); 
                    color: white; 
                    padding: 20px; 
                    border-radius: 10px; 
                    margin-top: 20px; 
                    text-align: left;'>
            {modified_response}
        </div>
    """, unsafe_allow_html=True)
