import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="University Statistics",
    page_icon="👋",
)
st.title("Statistics")


# load dataframe
filename = 'final_annotation_clean.xlsx'
df = pd.read_excel(filename, header=0)

# list
ranking_lst = df['Ranking'].unique().tolist()
uni_lst = df['University Name'].unique().tolist()
citysize_lst = df['City Size'].unique().tolist()


#selection
citysize_selection = st.multiselect('City Size:',
                                    citysize_lst,
                                    default=citysize_lst)