import streamlit as st
from streamlit_ace import st_ace
import subprocess

with open("place_holder_code.py", "r") as file:
    place_holder_code = file.read()
with open("place_holder_assembly.txt", "r") as file:
    place_holder_assembly = file.read()


def page():
    st.header("High-Level vs Low-Level Programming")
    st.write("Grace Hopper's work helped to bridge the gap between high-level and low-level programming languages.")
    st.write("She developed the first compiler, which allowed programmers to write code in high-level languages, "
             "which are easier to read and write.")
    st.write("While she was working on the compiler, others scrutinized her work saying that computers can only be "
             "used for simple arithmetic.")
    st.write("Grace Hopper's work proved them wrong, and she showed that computers could be used for much more than "
                "simple arithmetic.")
    st.write("The demo below shows the difference between high-level and low-level programming languages.")


    # st.header("Try Coding")
    level = st.radio("Select the level of code you want to try", ["High-Level", "Low-Level"])
    st.markdown("**Both of these example programs add two numbers together**")
    if level == "High-Level":
        st.markdown("### Python")
        st.markdown("----")
        st.markdown("""This programming language is called Python.  
                        It's a high-level language that is easy to learn.  
                        It follows in the footsteps of Grace Hopper's work.  
                        Like COBOL, it benefits from separate algorithms to turn the code into machine code.   
""")
        user_code = st_ace(language="python", value=place_holder_code, height=300, key="ace")
        if st.button("Run Code"):
            with open("user_code.py", "w") as file:
                file.write(user_code)
            result = subprocess.run(["python", "user_code.py"], capture_output=True)
            print("output:", result.stdout.decode())
            st.markdown("### Output")
            st.markdown("----")
            st.text(result.stdout.decode())  # Doesn't not respect new lines
            st.markdown("----")

    if level == "Low-Level":
        st.markdown("### Assembly Language")
        st.markdown("----")
        st.markdown("""
                Assembly language is a low-level programming language.
                It's much closer to machine code than high-level languages like Python, and it's much harder to read and write.
                Below is an example that adds two numbers together. Notice how much more complex it is compared to the Python code.
                """)
        st_ace(language="assembly_x86", value=place_holder_assembly, height=300)
        st.markdown("----")
        if st.button("Can't run this code"):
            st.write("Sorry")

    if st.button("Go back"):
        st.session_state["page"] = "landing"
        st.rerun()
