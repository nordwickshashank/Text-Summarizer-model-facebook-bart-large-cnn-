import streamlit as st
from transformers import pipeline

# Initialize the summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def get_user_input():
    """Function to get user input from text_area"""
    user_input = st.text_area("Enter your text here", value='', height=None, max_chars=None, key=None)
    return user_input

def main():
    """Main function to orchestrate the summarization process"""
    st.title("Text Summarizer")
    user_input = get_user_input()

    # Summarize text when the button is pressed
    if st.button("Summarize"):
        summary = summarizer(user_input, max_length=130, min_length=30, do_sample=False)
        st.write(summary[0]['summary_text'])

    # Add the signature
    st.markdown("---")
    st.markdown("With ❤️ from Shashank")

# Run the main function when the script is run
if __name__ == "__main__":
    main()
