from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Set page config
st.set_page_config(page_title="MultiLanguage Invoice Extractor", layout="wide")

# Load environment variables
load_dotenv()

# Google Gemini Configuration
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

# CSS for custom styling - fixed layout for the image and analysis result
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 20px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px 24px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .title {
            font-size: 2.5rem;
            color: #3a7ee4;
            text-align: center;
        }
        .subtitle {
            font-size: 1.2rem;
            color: #555;
            text-align: center;
        }
        /* Fix image and analysis in one view */
        .fixed-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 60%; /* Adjust the size */
            height: auto;
        }
        .result {
            text-align: center;
            font-size: 1.5rem;
            font-weight: bold;
            color: #222222;
            margin-top: 20px;
            padding: 10px;
            background-color: #f8f9fa;
            border: 2px solid #dee2e6;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 70%;
            margin-left: auto;
            margin-right: auto;
        }
        .caption {
            text-align: center;
            font-size: 1rem;
            color: #333;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Function to load and process invoice image
def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Main app layout
st.markdown('<h1 class="title">MultiLanguage Invoice Extractor</h1>', unsafe_allow_html=True)
st.markdown('<h4 class="subtitle">Upload an invoice and get detailed insights about it!</h4>', unsafe_allow_html=True)

# Sidebar for input fields
st.sidebar.header("Upload Invoice & Enter Prompt")
input = st.sidebar.text_input("Input Prompt: ", key="input")
uploaded_file = st.sidebar.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

# Display uploaded image (centered and non-scrollable)
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice Image", output_format="auto", width=600, clamp=True, use_column_width=True)
    st.markdown('<p class="caption">Uploaded Invoice Image</p>', unsafe_allow_html=True)

submit = st.sidebar.button("Analyze Invoice")

# Input prompt for the model
input_prompt = """
You are an expert in understanding invoices. We will upload an image of an invoice, and you will have to answer any questions
based on the uploaded invoice image.
"""

# If submit button is clicked
if submit:
    try:
        image_data = input_image_details(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, input)
        
        # Display the result in the center below the image
        st.markdown(f'<div class="result">{response}</div>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Please upload an image of the invoice before submitting.")
