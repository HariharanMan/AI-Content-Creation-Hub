# Import necessary libraries
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

# Generate a story plot using the model
def generate_story_plot(model, genre, character_trait, conflict, setting):
    try:
        # Construct the prompt for generating a story plot
        prompt = (f"Generate an intriguing story plot for a {genre} genre with the following details:\n"
                  f"Main Character Traits: {character_trait}\n"
                  f"Conflict: {conflict}\n"
                  f"Setting: {setting}\n"
                  "Make the plot engaging, unique, and suitable for a full story development.")
        response = model.generate_content(prompt)
        return response.text  # Return the generated plot
    except Exception as e:
        st.error(f"Error generating story plot: {e}")
        return "Error generating story plot."

# Streamlit UI
def main():
    # Set the title and description of the page
    st.title("🎥 Story Plot Generator: Create Intriguing Storylines with AI 🎬")
    st.markdown("""
    **Bring your ideas to life with unique story plots.**  
    Input key details about the story, and let AI craft a compelling plot for you.
    """)

    # Add a visually appealing image
    st.image("https://via.placeholder.com/800x200.png?text=Create+Your+Next+Big+Plot+Now", use_column_width=True)

    # Input for genre
    genre = st.selectbox(
        "Choose the Genre:",
        ["Fantasy", "Adventure", "Mystery", "Sci-Fi", "Romance", "Horror", "Drama", "Comedy"]
    )

    # Input for main character traits
    character_trait = st.text_area(
        "Main Character Traits:",
        placeholder="Describe your main character(s) (e.g., 'a shy detective with a mysterious past')."
    )

    # Input for conflict
    conflict = st.text_area(
        "Main Conflict:",
        placeholder="What is the central conflict? (e.g., 'a race against time to stop a deadly virus')."
    )

    # Input for setting
    setting = st.text_area(
        "Story Setting:",
        placeholder="Where does the story take place? (e.g., 'a crumbling city in a post-apocalyptic world')."
    )

    # Button to generate the plot
    if st.button("Generate Story Plot"):
        if not character_trait or not conflict or not setting:
            st.error("Please provide all the required inputs: Character Traits, Conflict, and Setting.")
        else:
            with st.spinner("Crafting your story plot..."):
                model = init_model()
                if model:
                    story_plot = generate_story_plot(model, genre, character_trait, conflict, setting)
                    st.success("Your story plot is ready!")
                    st.text_area("Generated Story Plot:", value=story_plot, height=400)

                    # Option to regenerate the plot
                    if st.button("Regenerate Plot"):
                        story_plot = generate_story_plot(model, genre, character_trait, conflict, setting)
                        st.text_area("Generated Story Plot:", value=story_plot, height=400)

                    # Option to copy the plot
                    st.markdown(
                        f'<a href="javascript:void(0)" onclick="navigator.clipboard.writeText(`{story_plot}`)">Click to copy the plot</a>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.error("Model initialization failed.")

    # Add a footer
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
    **Happy Plotting! 🎥**  
    Powered by AI, inspired by imagination.
    """)

if __name__ == "__main__":
    main()
