import database as db
import requests
import pandas as pd  
import streamlit as st
import streamlit_lottie as st_lottie
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
from PIL import Image


#Webtab editing
st.set_page_config(page_title="Akshaya Patra", page_icon=":olive:", layout="wide")
img_contact_form = Image.open("/media/harinandan/RAGAVANS'S/Green_Leaf/Home Page/potato.png")
img_lottie_animation = Image.open("/media/harinandan/RAGAVANS'S/Green_Leaf/Home Page/potato.png")

selected = option_menu(menu_title=None, default_index=0,
            options=["Home", "About Us", "Login", "Feedback"],
            #FOR ICONS WEBISTE https://icons.getbootstrap.com/
            icons=["grid-fill","layout-text-window","fingerprint","envelope-paper-fill"],
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#7DB0DF"},
                "icon": {"color":"#ffffff", "font-size": "20px"},
                "nav-link": {
                    "font-size": "20px",
                    "text-align": "center",
                    "margin": "0px",
                    "--hover-color": "#cfe2f3 ",
                    },
                "nav-link-selected": {"background-color": "#135999 "},
                    },)

if selected == "Home":
    # ---- HEADER SECTION ----
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Freshness of farm on your table!")
            st.title("Akshaya Patra")
            st.write("Discover a vibrant array of fresh vegetables and fruits on our online marketplace. Enjoy farm-fresh goodness delivered to your doorstep, ensuring quality and convenience for your daily needs.")
if selected == "About Us":
    st.title(f"You have selected {selected}")
if selected == "Feedback":
    # ---- CONTACT ----
    with st.container():
        st.write("---")
        st.header("Give us ur feedback!!")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/harinandan.k007@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

def login_button():
    # --- USER AUTHENTICATION ---
    users = db.fetch_all_users()

    if st.button('Trial User') is True:
        st.write('Jeet file')

    if st.button('Register') is True:
        st.write('add pg to add new user to database')

    register_button = st.button("Register")

    usernames = [user["key"] for user in users]
    names = [user["name"] for user in users]
    hashed_passwords = [user["password"] for user in users]

    credentials = {"usernames":{}}

    for un, name, pw in zip(usernames, names, hashed_passwords):
        user_dict = {"name":name,"password":pw}
        credentials["usernames"].update({un:user_dict})

    authenticator = stauth.Authenticate(credentials, "app_home", "auth", cookie_expiry_days=30)

    name, authentication_status, username = authenticator.login("Login", "main")



    if authentication_status == False:
        st.error("Username/password is incorrect")

    if authentication_status == None:
        st.warning("Please enter your username and password")

    if authentication_status:
        # ---- PROJECTS ----
        with st.container():
            st.write('Welcome')
            st.write("---")
            st.header("Today's Specials!!")
            st.write("##")
            image_column, text_column = st.columns((1, 2))
            with image_column:
                st.image(img_lottie_animation)
            with text_column:
                st.subheader("White Potato")
                st.write("Seller : Arjun Sharma")
                st.write("Location : Tamil Nadu")

                st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                st.image(img_contact_form)
            with text_column:
                st.subheader("How To Add A Contact Form To Your Streamlit App")
                st.write(
                    """
                    Want to add a contact form to your Streamlit website?
                    In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
                    """
                )
                st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")



if selected == "Login":
    login_button()