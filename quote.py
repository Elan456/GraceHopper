import streamlit as st
import csv
import random

with open("quotes.csv", "r") as file:
    quotes = list(csv.reader(file))[1:]
    # print("quotes loaded:", quotes)


def page():
    st.title("Quotes from Grace Hopper")

    st.markdown("Click the button below to get a random quote from Grace Hopper.")
    if st.button("Get a Quote"):
        quote = random.choice(quotes)
        st.markdown(f"""
        > *"{quote[0]}"*
        > 
        >
        """)

    st.header("Where the quotes are from")
    st.markdown("""
    - https://www.inhersight.com/blog/insight-commentary/grace-hopper-quotes
    - https://www.azquotes.com/author/6894-Grace_Hopper
    """)

    if st.button("Go back"):
        st.session_state["page"] = "landing"
        st.rerun()
