import google.generativeai as genai
import streamlit as st

# Configuration: Hardcoded API Key and Model Name
API_KEY = "Your API"  # Replace with your Gemini Flash 1.5 API key
MODEL_NAME = "gemini-1.5-flash"  # The model name you want to use

# Initialize the Gemini Flash 1.5 model
def init_model():
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel(MODEL_NAME)
        return model
    except Exception as e:
        st.error(f"Error initializing Gemini Flash model: {e}")
        return None

# Generate manuscript content using the model
def generate_manuscript(model, genre, word_count, chapters, tone, summary):
    try:
        prompt = (
            f"Write a manuscript outline in the {genre} genre. The manuscript should have {word_count} words, "
            f"divided into {chapters} chapters. Use a {tone} tone. Here is the summary or theme: {summary}."
        )
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating manuscript content: {e}")
        return "Error generating manuscript content."

# Streamlit UI
def main():
    st.title("📜 Manuscript Writer")
    st.subheader("AI-powered tool to assist in writing your manuscript.")
    st.markdown(
        """
        Write compelling manuscripts with AI. Define your genre, tone, and structure, and let AI provide a starting outline.
        """
    )

    # Input fields for manuscript details
    genre = st.selectbox("Choose your Genre:", ["Fiction", "Non-Fiction", "Fantasy", "Science Fiction", "Romance", "Mystery", "Biography"])
    word_count = st.slider("Word Count:", min_value=1000, max_value=100000, step=1000, value=5000)
    chapters = st.number_input("Number of Chapters:", min_value=1, max_value=100, value=5)
    tone = st.selectbox("Choose the Tone:", ["Formal", "Conversational", "Inspirational", "Suspenseful", "Romantic"])
    summary = st.text_area("Theme or Summary:", placeholder="Provide a short description of the manuscript's theme or idea.")

    # Generate button
    if st.button("Generate Manuscript Outline"):
        if not summary:
            st.error("Please provide a summary or theme.")
        else:
            with st.spinner("Generating manuscript outline..."):
                model = init_model()
                if model:
                    manuscript = generate_manuscript(model, genre, word_count, chapters, tone, summary)
                    st.success("Manuscript outline generated successfully!")
                    st.text_area("Generated Manuscript Outline:", value=manuscript, height=300)
                else:
                    st.error("Model initialization failed.")

    # Unique UI feature: Sectioned Preview with Chapter Display
    st.markdown("---")
    st.subheader("📖 Manuscript Preview")
    if st.button("Preview Manuscript by Chapters"):
        if not summary:
            st.error("Please provide manuscript details to preview.")
        else:
            with st.spinner("Generating chapter preview..."):
                model = init_model()
                if model:
                    for i in range(1, chapters + 1):
                        chapter_prompt = (
                            f"Write Chapter {i} for a manuscript in the {genre} genre. "
                            f"The tone is {tone}. The theme is: {summary}."
                        )
                        chapter_response = model.generate_content(chapter_prompt)
                        st.markdown(f"### Chapter {i}")
                        st.write(chapter_response.text)
                else:
                    st.error("Model initialization failed.")

if __name__ == "__main__":
    main()
