#### How Does It Work?
#### The Multi-Language Invoice Extractor allows users to:
- Upload an invoice image via a clean, intuitive interface.
- Analyze the invoice using the Gemini 1.5 Flash AI model.
- Extract key financial details automatically, displayed in a user-friendly format.
- This tool automates data extraction, eliminating manual input and overcoming language barriers, saving businesses time and effort.

### Set Up Python Environment
```bash
  conda create -n invoice-extractor python=3.8 -y
  conda activate invoice-extractor
```

### Install Required Libraries
```bash
  pip install -r requirements.txt
```
### Set Up Environment Variables
```bash
  Create a .env file in the root directory and add your Google API credentials for Gemini:
  GOOGLE_API_KEY=your-google-api-key
```
### Run the Application
```bash
  streamlit run app.py
```

### Tech Stack-
-Frontend: Streamlit
-Generative AI Model: Gemini 1.5 Flash
-Programming Language: Python

