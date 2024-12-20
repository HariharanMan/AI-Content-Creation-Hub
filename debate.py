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

# Generate debate arguments using the model
def generate_argument(model, topic, perspective, tone):
    try:
        # Create a prompt for generating arguments
        prompt = (f"Generate a {tone} {perspective.lower()} argument for the following debate topic: "
                  f"'{topic}'. Provide a strong and well-structured argument.")
        response = model.generate_content(prompt)
        return response.text  # Return the generated argument
    except Exception as e:
        st.error(f"Error generating argument: {e}")
        return "Error generating argument."

# Streamlit UI
def main():
    # Set the title of the page
    st.title("Debate Argument Generator")
    st.write("Generate compelling arguments for any debate topic. Choose a perspective, tone, and get started!")

    # Input for debate topic
    topic = st.text_area(
        "Debate Topic:",
        placeholder="Enter the debate topic you want arguments for...",
    )

    # Input for perspective
    perspective = st.selectbox(
        "Choose Perspective:",
        ["Pro (For the topic)", "Con (Against the topic)"],
    )

    # Input for tone/style of argument
    tone = st.selectbox(
        "Argument Tone:",
        ["Formal", "Passionate", "Logical", "Persuasive"],
    )

    # Button to generate the argument
    if st.button("Generate Debate Argument"):
        if not topic:
            st.error("Please provide a debate topic.")
        else:
            with st.spinner("Generating debate argument..."):
                model = init_model()
                if model:
                    argument = generate_argument(model, topic, perspective, tone)
                    st.success("Debate argument generated successfully!")
                    st.text_area("Generated Argument:", value=argument, height=300)

                    # Option to regenerate the argument
                    if st.button("Regenerate Argument"):
                        argument = generate_argument(model, topic, perspective, tone)
                        st.text_area("Generated Argument:", value=argument, height=300)

                    # Option to copy the argument
                    st.markdown(
                        f'<a href="javascript:void(0)" onclick="navigator.clipboard.writeText(`{argument}`)">Click to copy the argument</a>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.error("Model initialization failed.")

if __name__ == "__main__":
    main()
