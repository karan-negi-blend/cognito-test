import streamlit as st
import time 
import components.authenticate as authenticate

if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'expanded'
st.set_page_config(page_title="HGV",initial_sidebar_state=st.session_state.sidebar_state)

# Check authentication when user lands on the home page.
st.markdown("""
        <div style="background-color: #464e5f; padding: 10px; border-radius: 10px;">
            <h1 style="color:white;text-align:center;">Welcome to HGV CCA TOOL</h1>
        </div>
    """, unsafe_allow_html=True)

authenticate.set_st_state_vars()

# Add login/logout buttons
if st.session_state["authenticated"]:
    authenticate.button_logout()
    if st.session_state.sidebar_state == 'collapsed':
        st.session_state.sidebar_state = 'expanded'
    # st.session_state.sidebar_state = 'expanded' if st.session_state.sidebar_state == 'collapsed' else 'expanded'
else:
    st.write("Please Login to use the app")
    authenticate.button_login()
