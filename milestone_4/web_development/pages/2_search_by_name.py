import streamlit as st
import pandas as pd

#page config
st.set_page_config(
    page_title="Search by Name",
    page_icon="👋",
)
st.title("Search by Name")

# load dataframe
filename = 'final_annotation_clean.xlsx'
df = pd.read_excel(filename, header=0)
uni_lst = df['University Name'].unique().tolist()

#input name
if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input the name of the university here", st.session_state["my_input"])
submit = st.button("Submit")

if submit:
    st.session_state["my_input"] = my_input
    mask = df['University Name'].str.contains(my_input)
    number_of_result = df[mask].shape[0]
    st.markdown(f'*Available Results: {number_of_result}*')
    
    df_filtered = df[mask]
    

    #st.dataframe(df_filtered)
    df_filtered_lst = df_filtered.to_dict('records')

    for d in df_filtered_lst:
        st.write('-------------------------')
        st.write(d['University Name'])
        st.write('Ranking: ', d['Ranking'])
        st.write(d['Corpus Text'])
        
