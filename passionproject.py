# Import necessary libraries
import google.generativeai as genai
import streamlit as st

# Configuration: Hardcoded API Key and Model Name
API_KEY = "Your API"  # Replace with your Gemini Flash 1.5 API key
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

# Generate passion project idea using the model
def generate_passion_project(model, interests, time_commitment, goals):
    try:
        # Use the model to generate a passion project idea based on user input
        prompt = f"Generate a unique and inspiring passion project idea based on the following interests: {interests}. The user can commit {time_commitment} hours per week. The project goal is: {goals}."
        response = model.generate_content(prompt)
        return response.text  # Return the generated project idea from the response
    except Exception as e:
        st.error(f"Error generating passion project idea: {e}")
        return "Error generating passion project idea."

# Streamlit UI
def main():
    # Set page title and description
    st.title("Passion Project Generator")
    st.write("Generate a unique and inspiring passion project idea based on your interests, time commitment, and goals!")

    # Input for Interests
    interests = st.text_area(
        "Your Interests (e.g., Photography, Coding, Cooking):",
        placeholder="Enter your interests here..."
    )

    # Input for Time Commitment
    time_commitment = st.selectbox(
        "Time Commitment (hours per week):",
        ["1-2 hours per week", "3-5 hours per week", "5+ hours per week"]
    )

    # Input for Project Goals
    goals = st.text_area(
        "Project Goals (e.g., Learn a new skill, Build a portfolio, Start a business, Improve academic performance):",
        placeholder="Describe the goals of your project..."
    )

    # Button to generate the passion project idea
    if st.button("Generate Passion Project Idea"):
        if not interests or not goals:
            st.error("Please provide both your interests and project goals.")
        else:
            with st.spinner("Generating passion project idea..."):
                model = init_model()
                if model:
                    project_idea = generate_passion_project(model, interests, time_commitment, goals)  # Pass the initialized model here
                    st.success("Passion project idea generated successfully!")
                    st.text_area("Generated Passion Project Idea:", value=project_idea, height=300)
                else:
                    st.error("Model initialization failed.")

if __name__ == "__main__":
    main()
