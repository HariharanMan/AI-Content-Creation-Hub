import google.generativeai as genai
import streamlit as st

# Configuration: Hardcoded API Key and Model Name
API_KEY = "Your API "  # Replace with your Gemini Flash 1.5 API key
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

# Generate content ideas using the model
def generate_content_ideas(model, topic, audience):
    try:
        # Use the model to generate content ideas based on the user input
        prompt = f"Generate a list of content ideas for a topic about '{topic}', aimed at '{audience}'."
        response = model.generate_content(prompt)
        return response.text  # Return the generated content ideas from the response
    except Exception as e:
        st.error(f"Error generating content ideas: {e}")
        return "Error generating content ideas."

# Streamlit UI
def main():
    # Set page title and description
    st.title("Content Idea Generator")
    st.write("Get inspiration for your next piece of content by generating a variety of content ideas based on your topic and target audience.")

    # Get user inputs for content idea generation
    topic = st.text_area(
        "What is your topic? (e.g., how to optimize your website for search engines):",
        placeholder="Describe the topic in detail..."
    )
    
    audience = st.text_input(
        "What is your target audience? (e.g., small business owners, marketers):",
        placeholder="Enter your target audience..."
    )

    # Button to generate the content ideas
    if st.button("Generate Content Ideas"):
        if not topic or not audience:
            st.error("Please provide both a topic and a target audience.")
        else:
            with st.spinner("Generating content ideas..."):
                model = init_model()
                if model:
                    content_ideas = generate_content_ideas(model, topic, audience)  # Pass the initialized model here
                    st.success("Content ideas generated successfully!")
                    st.text_area("Generated Content Ideas:", value=content_ideas, height=300)
                else:
                    st.error("Model initialization failed.")

if __name__ == "__main__":
    main()
