from PIL import Image
import streamlit as st


st.set_page_config(page_title="My Portfolio", layout="wide")


st.subheader("Welcome to my portfolio!")
st.title("This portfolio contains information about what me and my friend can do via game dev'ing in roblox studio!")
st.write("This website is currently in development (im coding it myself)")



with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What i script:")
        st.write("##")
        st.write("Inside of roblox (lua) i can make movement systems, script guis, weapons, learning combat, abilities, and more.")

    with right_column:
        st.header("What pug makes:")
        st.write("##")
        st.write("Pug can make basic GUI's")

        image_coding_form = Image.open("Images/Image1.png")
        image2_coding_form = Image.open("Images/LeaderstatsRank.png")


    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, image2_column = st.columns(2)

        with image_column:
            st.image(image_coding_form, "Examples:")
            st.write("---")
            st.image(image2_coding_form, "Examples:")




            with st.container():
                st.write("---")
                st.header("Contact Me")
                st.write("##")


            contact_form = """
            <form action="https://discord.gg/qF4DfXZA" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="Discord Username" name="User" placeholder="Your User" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
            </form>
            """


            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
                with right_column:
                    st.empty()

                  


