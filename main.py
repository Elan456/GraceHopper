import streamlit as st
import landing
import quote
import code
import discussion
if "page" not in st.session_state:
    st.session_state["page"] = "landing"

st.set_page_config(page_title="Grace Hopper", page_icon=":computer:",
                    initial_sidebar_state="auto")


def page_handler():
    if st.session_state["page"] == "landing":
        landing.page()
    elif st.session_state["page"] == "quote":
        quote.page()
    elif st.session_state["page"] == "coding":
        code.page()
    elif st.session_state["page"] == "discussion":
        discussion.page()

    else:
        st.error("Invalid page, you shouldn't be here")
        if st.button("Go back"):
            st.session_state["page"] = "landing"
            st.rerun()


page_handler()