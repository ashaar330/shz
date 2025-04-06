import streamlit as st
st.set_page_config(page_title="puntland" , page_icon=":tada:" , layout="wide")
with st.container():
 st.subheader("""asc , manta waxaan soo bandhigi dona magaloyinka 
                ugu quruxda badan ee puntland. """)
 st.title("magaloyinka : ")
with st.container():
 st.write("---")
 left_column, right_column=st.columns(2)
 with left_column:
  st.write("#")
  st.write("""
            - kalinta kobaad waxaa ku jira Eyl.
            - Kalinta labaad waxaa ku jira Caluula. 
            - kalinta sadexaad waxaa ku jira Qandala.
           """)