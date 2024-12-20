# Install necessary libraries (only required in Colab or first-time setup)
# !pip install google-generative-ai
# !pip install streamlit

import google.generativeai as genai
import streamlit as st

# Configuration: Hardcoded API Key and Model Name
API_KEY = "AIzaSyBbZJDUN6T9I9moSs71Sc1Bql1t6rtPQEc"  # Replace with your Gemini Flash 1.5 API key
MODEL_NAME = "gemini-1.5-flash"  # The model name you want to use

# Initialize the Gemini Flash 1.5 model
def init_model():
    try:
        # Configure the API key to be used by the model
        genai.configure(api_key=API_KEY)
        # Initialize the model by name
        model = genai.GenerativeModel(MODEL_NAME)
        return model
    except Exception as e:
        st.error(f"Error initializing Gemini Flash model: {e}")
        return None

# Generate LinkedIn post using the model
def generate_post(model, prompt, tone, length):
    try:
        # Use the model to generate content based on the user input
        response = model.generate_content(f"Write a LinkedIn post about {prompt}. Tone: {tone}. Length: {length}.")
        return response.text  # Return the generated text from the response
    except Exception as e:
        st.error(f"Error generating LinkedIn post: {e}")
        return "Error generating post."

# Streamlit UI
def main():
    # Set page title and description
    st.title("LinkedIn Post Generator with AI")
    st.write("Generate engaging LinkedIn posts effortlessly using AI. Customize the tone and length to fit your style.")

    # Get user inputs for LinkedIn post generation
    prompt = st.text_area(
        "What is your post about? (e.g., got a promotion, grateful to my colleagues, looking for new challenges):",
        placeholder="Describe your post in a sentence..."
    )
   
    tone = st.selectbox(
        "Tone of Voice:",
        ["Professional", "Energetic", "Funny", "Inspirational", "Casual"]
    )

    length = st.selectbox(
        "Output Length:",
        ["Short", "Medium", "Long"]
    )

    # Button to generate the LinkedIn post
    if st.button("Generate LinkedIn Post"):
        if not prompt:
            st.error("Please provide a description for your post.")
        elif not tone:
            st.error("Please select a tone of voice.")
        else:
            with st.spinner("Generating LinkedIn post..."):
                model = init_model()
                if model:
                    post = generate_post(model, prompt, tone, length)  # Pass the initialized model here
                    st.success("Post generated successfully!")
                    st.text_area("Generated LinkedIn Post:", value=post, height=300)
                else:
                    st.error("Model initialization failed.")

if __name__ == "__main__":
    main()
