import streamlit as st
import components.authenticate as authenticate

authenticate.set_st_state_vars()
st.set_page_config(page_title="Hotel Description", page_icon="")

st.markdown("Hotel Description")
if st.session_state["authenticated"]:
    st.write("Only logged in person can see this text")
    authenticate.button_logout()
else:
    st.write("Login to start using the Tool")
    authenticate.button_login()
