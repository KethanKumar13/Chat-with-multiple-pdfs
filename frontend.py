import streamlit as st



def frontend():
    # Streamlit UI
    st.set_page_config(page_title="Chat with multiple pdf files", layout="wide")
    st.title("Chat with Multiple :red[PDF Files]!")
    question = st.text_input("Ask Question Below: ")

    with st.sidebar:
        st.image("chatPDF.png")
        api_key = st.text_input("Enter apikey", placeholder="Enter OpenAI Key", type="password")

        st.subheader("Upload PDFs here")
        pdfs = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)
        st.button('Process')

    


if __name__ == "__main__":
    frontend()