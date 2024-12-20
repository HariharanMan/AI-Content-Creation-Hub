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

# Generate review or testimonial using the model
def generate_review(model, product_name, feedback, rating, tone):
    try:
        # Create prompt for generating testimonial or review
        prompt = f"Write a {tone} testimonial for the product '{product_name}' based on the following feedback: '{feedback}'. The customer rated it {rating}/5 stars."
        response = model.generate_content(prompt)
        return response.text  # Return the generated review or testimonial
    except Exception as e:
        st.error(f"Error generating review: {e}")
        return "Error generating review."

# Streamlit UI
def main():
    # Set the title of the page
    st.title("Review Generator: Generate Testimonials & Reviews in Seconds!")

    # Explanation of the app
    st.write("Generate professional, casual, or enthusiastic testimonials and reviews in seconds for your products or services.")

    # Input for product/service name
    product_name = st.text_input("Product/Service Name:", placeholder="Enter the name of the product or service...")

    # Input for customer feedback
    feedback = st.text_area("Customer Feedback:", placeholder="Describe the feedback here...")

    # Input for rating (1-5)
    rating = st.slider("Customer Rating (1-5):", min_value=1, max_value=5, value=5)

    # Input for tone
    tone = st.selectbox("Tone of Review:", ["Professional", "Enthusiastic", "Casual"])

    # Button to generate the review
    if st.button("Generate Review"):
        if not product_name or not feedback:
            st.error("Please provide both the product name and customer feedback.")
        else:
            with st.spinner("Generating review..."):
                model = init_model()
                if model:
                    review = generate_review(model, product_name, feedback, rating, tone)
                    st.success("Review generated successfully!")
                    st.text_area("Generated Review/Testimonial:", value=review, height=300)

                    # Option to regenerate the review
                    if st.button("Regenerate Review"):
                        review = generate_review(model, product_name, feedback, rating, tone)
                        st.text_area("Generated Review/Testimonial:", value=review, height=300)
                    
                    # Option to copy the review
                    st.markdown(f'<a href="javascript:void(0)" onclick="navigator.clipboard.writeText(`{review}`)">Click to copy the review</a>', unsafe_allow_html=True)
                else:
                    st.error("Model initialization failed.")

if __name__ == "__main__":
    main()
