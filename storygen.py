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

# Generate a story using the model
def generate_story(model, characters, setting, theme, genre):
    try:
        # Construct the prompt for generating a story
        prompt = (f"Create a {genre} story with the following details:\n"
                  f"Characters: {characters}\n"
                  f"Setting: {setting}\n"
                  f"Theme: {theme}\n"
                  "Make the story engaging, imaginative, and unique.")
        response = model.generate_content(prompt)
        return response.text  # Return the generated story
    except Exception as e:
        st.error(f"Error generating story: {e}")
        return "Error generating story."

# Streamlit UI
def main():
    # Set the title and description of the page
    st.title("✨ Story Generator: Unlock the Magic of Automated Storytelling! ✨")
    st.markdown("""
    **Transform your ideas into engaging stories with AI.**  
    Input characters, settings, themes, and let AI bring your imagination to life!
    """)

    # Add some visuals for an engaging UI
    st.image("https://via.placeholder.com/800x200.png?text=Unlock+Your+Story's+Potential", use_column_width=True)

    # Input for characters
    characters = st.text_area(
        "Characters:",
        placeholder="Describe your characters (e.g., 'Alice, a brave knight; Bob, a curious wizard')."
    )

    # Input for setting
    setting = st.text_area(
        "Setting:",
        placeholder="Describe the setting (e.g., 'a mysterious forest at the edge of the kingdom')."
    )

    # Input for theme
    theme = st.text_input(
        "Theme:",
        placeholder="What's the theme? (e.g., 'friendship', 'overcoming fear', 'self-discovery')."
    )

    # Input for genre
    genre = st.selectbox(
        "Genre:",
        ["Fantasy", "Adventure", "Mystery", "Sci-Fi", "Romance", "Horror", "Comedy"]
    )

    # Button to generate the story
    if st.button("Generate Story"):
        if not characters or not setting or not theme:
            st.error("Please provide all the required inputs: Characters, Setting, and Theme.")
        else:
            with st.spinner("Crafting your story..."):
                model = init_model()
                if model:
                    story = generate_story(model, characters, setting, theme, genre)
                    st.success("Your story is ready!")
                    st.text_area("Generated Story:", value=story, height=400)

                    # Option to regenerate the story
                    if st.button("Regenerate Story"):
                        story = generate_story(model, characters, setting, theme, genre)
                        st.text_area("Generated Story:", value=story, height=400)

                    # Option to copy the story
                    st.markdown(
                        f'<a href="javascript:void(0)" onclick="navigator.clipboard.writeText(`{story}`)">Click to copy the story</a>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.error("Model initialization failed.")

    # Add a footer
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
    **Enjoy your storytelling journey! ✨**  
    Powered by AI, crafted with imagination.
    """)

if __name__ == "__main__":
    main()
