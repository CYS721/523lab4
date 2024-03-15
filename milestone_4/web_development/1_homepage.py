import streamlit as st

st.set_page_config(
    page_title="Universities Information",
    page_icon="👋",
)

st.title("Main Page")
#st.sidebar.success("Select a page above.")

# Introduction to corpus
st.write("""
### Introduction to Corpus

Our project aims to annotate university information according to various parameters including city size, type of institution, year of institution's history, city economy, and country development level. The annotation plan includes the following criteria:
- **City Size (Population):** Large, middle, or small cities based on population size.
- **Type of Institution:** Public or private.
- **Year of Institution's History:** Long or short.
- **City Economy - GDP:** High, middle, or low based on GDP.
- **Country Development Level:** Developed or developing.

Annotators will be the 4 members in our team, ensuring inter-annotator agreement through cross-annotated records. Quality assurance steps include training sessions and pilot studies.

""")
