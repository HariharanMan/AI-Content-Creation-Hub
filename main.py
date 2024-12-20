import streamlit as st
import contentidea  # Content Idea Generator module
import linkedinpost  # LinkedIn Post Generator module
import passionproject  # Passion Project Generator module
import review  # Review Generator module
import debate  # Debate Argument Generator module
import storygen  # Story Generator module
import storyplotgenerator  # Story Plot Generator module
import fanfictionmaker  # Fanfiction Maker module
import manuscriptwriter
# App Title and Sidebar Navigation
def main():
    st.set_page_config(page_title="AI Content Creation Hub", layout="wide")
    st.sidebar.title("🚀 AI Content Creation Hub")
    st.sidebar.markdown("Choose a tool to generate content with AI.")

    # Page navigation options
    page = st.sidebar.radio(
        "Select a Tool:",
        [
            "Content Idea Generator",
            "LinkedIn Post Generator",
            "Passion Project Generator",
            "Review Generator",
            "Debate Argument Generator",
            "Story Generator",
            "Story Plot Generator",
            "Fanfiction Maker",
        ]
    )

    # Conditional rendering of selected tool
    if page == "Content Idea Generator":
        contentidea.main()
    elif page == "LinkedIn Post Generator":
        linkedinpost.main()
    elif page == "Passion Project Generator":
        passionproject.main()
    elif page == "Review Generator":
        review.main()
    elif page == "Debate Argument Generator":
        debate.main()
    elif page == "Story Generator":
        storygen.main()
    elif page == "Story Plot Generator":
        storyplotgenerator.main()
    elif page == "Fanfiction Maker":
        fanfictionmaker.main()
    elif page == "ManuScript Writer":
        manuscriptwriter.main()

# Run the app
if __name__ == "__main__":
    main()
