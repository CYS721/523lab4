import streamlit as st
st.set_page_config(
    page_title="Search by Filter",
    page_icon="👋",
)
st.title("Search by Filter")


# load dataframe
filename = 'final_annotation.xlsx'
df = pd.read_excel(filename, header=0)

# list
ranking_lst = df['Ranking'].unique().tolist()
uni_lst = df['University Name'].unique().tolist()
citysize_lst = df['City Size'].unique().tolist()


#selection
citysize_selection = st.multiselect('City Size:',
                                    citysize_lst,
                                    default=citysize_lst)