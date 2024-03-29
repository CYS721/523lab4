import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Search by Filter",
    page_icon="👋",
)
st.title("Search by Filter")


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

mask = (df['City Size'].isin(citysize_selection))
df_filtered = df[mask]

df_filtered_lst = df_filtered.to_dict('records')

for d in df_filtered_lst:
    st.write('-------------------------')
    st.write(d['University Name'])
    st.write('Ranking: ', d['Ranking'])
    st.write(d['Corpus Text'])
