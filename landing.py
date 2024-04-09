import streamlit as st


def page():
    st.title("Grace Hopper - A Pioneer in Computer Science")
    st.markdown("---------")

    image_1_address = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Commodore_Grace_M._Hopper%2C_USN_%28covered%29.jpg/360px-Commodore_Grace_M._Hopper%2C_USN_%28covered%29.jpg"
    image_2_address = "https://news.yale.edu/sites/default/files/styles/horizontal_image/public/d6_files/YaleNews_hopper-grace.UNIVAC.102635875-CC_0.jpg?itok=4HL3ETlO"

    columns = st.columns(2)
    with columns[0]:
        st.header("About Grace Hopper")
        st.markdown("""
            Grace Brewster Murray Hopper was a trailblazing computer scientist, and naval officer.
            Her work towards the development of the first compiler enabled the creation of the first high-level programming languages.
            This immensely simplified the process of writing code, and made programming more accessible to a wider audience.
            """)

        st.header("More")

        columns_2 = st.columns(2)
        with columns_2[0]:
            if st.button("Get a Quote"):
                st.session_state["page"] = "quote"
                st.rerun()
            if st.button("Code Demonstration"):
                st.session_state["page"] = "coding"
                st.rerun()
            if st.button("Have a discussion"):
                st.session_state["page"] = "discussion"
                st.rerun()

    with columns[1]:
        st.image(image_1_address, caption="Grace Hopper", use_column_width=True)
        st.image(image_2_address, caption="Grace Hopper with UNIVAC", use_column_width=True)


