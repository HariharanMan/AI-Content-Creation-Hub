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

# Generate fanfiction using the model
def generate_fanfiction(model, fandom, character_details, relationships, plot_preference):
    try:
        # Construct the prompt for generating a fanfiction story
        prompt = (f"Write a fanfiction story for the fandom '{fandom}'.\n"
                  f"Character Details: {character_details}\n"
                  f"Relationships: {relationships}\n"
                  f"Plot Preference: {plot_preference}\n"
                  "Create an engaging and imaginative story while staying true to the fandom.")
        response = model.generate_content(prompt)
        return response.text  # Return the generated story
    except Exception as e:
        st.error(f"Error generating fanfiction: {e}")
        return "Error generating fanfiction."

# Streamlit UI
def main():
    # Set the title and description of the page
    st.title("📚 Fanfiction Maker: Create Your Own Stories with AI 🌟")
    st.markdown("""
    **Unleash your creativity with AI-powered fanfiction!**  
    Input your favorite fandom, characters, and plot ideas to create unique fanfiction stories.
    """)

    # Add an eye-catching header image
    st.image("https://via.placeholder.com/800x200.png?text=Create+Your+Ultimate+Fanfiction", use_column_width=True)

    # Input for fandom
    fandom = st.text_input(
        "Fandom (e.g., Harry Potter, Marvel, Naruto):",
        placeholder="Enter the name of the fandom..."
    )

    # Input for character details
    character_details = st.text_area(
        "Character Details:",
        placeholder="Describe the characters you want in the story (e.g., Hermione Granger, a brilliant witch who loves reading)."
    )

    # Input for relationships
    relationships = st.text_area(
        "Relationships (optional):",
        placeholder="Mention any specific relationships you'd like to explore (e.g., Harry and Hermione friendship)."
    )

    # Input for plot preference
    plot_preference = st.text_area(
        "Plot Preferences:",
        placeholder="Describe the type of plot you'd like (e.g., an epic battle, a romantic journey, or a mysterious adventure)."
    )

    # Button to generate the fanfiction story
    if st.button("Generate Fanfiction"):
        if not fandom or not character_details or not plot_preference:
            st.error("Please provide at least the fandom, character details, and a plot preference.")
        else:
            with st.spinner("Crafting your fanfiction story..."):
                model = init_model()
                if model:
                    fanfiction_story = generate_fanfiction(model, fandom, character_details, relationships, plot_preference)
                    st.success("Your fanfiction story is ready!")
                    st.text_area("Generated Fanfiction Story:", value=fanfiction_story, height=400)

                    # Option to regenerate the story
                    if st.button("Regenerate Story"):
                        fanfiction_story = generate_fanfiction(model, fandom, character_details, relationships, plot_preference)
                        st.text_area("Generated Fanfiction Story:", value=fanfiction_story, height=400)

                    # Option to copy the story
                    st.markdown(
                        f'<a href="javascript:void(0)" onclick="navigator.clipboard.writeText(`{fanfiction_story}`)">Click to copy the story</a>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.error("Model initialization failed.")

    # Footer for additional inspiration
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
    **Let your imagination run wild! 🚀**  
    Powered by AI, inspired by your favorite fandoms.
    """)

if __name__ == "__main__":
    main()
