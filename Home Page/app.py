import database as db
import streamlit as st
import mysql.connector
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu


#Webtab editing
st.set_page_config(page_title="Akshaya Patra", page_icon=":olive:", layout="wide")

selected = option_menu(menu_title=None, default_index=0,
            options=["Home", "About Us", "Login", "Feedback"],
            # --- ICONS WEBISTE https://icons.getbootstrap.com/ ---font
            icons=["grid-fill","layout-text-window","fingerprint","envelope-paper-fill"],
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#0A2F51"},
                "icon": {"color":"#ffffff", "font-size": "20px"},
                "nav-link": {
                    "font-size": "20px",
                    "text-align": "center",
                    "margin": "0px",
                    "--hover-color": "#224362 ",
                    },
                "nav-link-selected": {"background-color": "#1977CC"},
                    },)





# --- Home Page ---
if selected == "Home":
    # ---- HEADER SECTION ----
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Freshness of farm on your table!")
            st.title("Akshaya Patra")
            st.write("Discover a vibrant array of fresh vegetables and fruits on our online marketplace. Enjoy farm-fresh goodness delivered to your doorstep, ensuring quality and convenience for your daily needs.")





# --- About Us Page ---
if selected == "About Us":
    st.title("About Us! text here!!")





# --- Seller Page ---
def seller_pg():
    st.write("Jeet U gota type ur codes here for seller gui!!!!")




# --- Registering Page ---
def register_pg():
    st.write("haro ur part")

if selected == "Login":

    col1, col2,= st.columns(2)
    
    # --- For Trail User ---
    with col1:
        trial_user = st.button('Trail User',                                
                               help='Click this button to get a free look at our website!',
                              )
        
        #if trial_user:
            #user_pg()

    


    # --- For Registering A New Users ---
    with col2:
        register = st.button('Register', 
                               help='Click this button to register with us!',
                              )
        
        if register:
            register_pg()




    # --- USER AUTHENTICATION ---
    users = db.fetch_all_users()

    usernames = [user["key"] for user in users]
    names = [user["name"] for user in users]
    hashed_passwords = [user["password"] for user in users]

    credentials = {"usernames":{}}

    for username, name, pw in zip(usernames, names, hashed_passwords):
        user_dict = {"name":name,"password":pw}
        credentials["usernames"].update({username:user_dict})

    authenticator = stauth.Authenticate(credentials, "app_home", "auth", cookie_expiry_days=30)

    name, authentication_status, username = authenticator.login("Login", "main")



    # --- If User Enter Wrong Details Ask To Re-Try---
    if authentication_status == False:
        wrong = 0
        st.error("Username or Password is incorrect")



    # --- User Not Enter Deatails Then Ask Them To Enter Details ---
    if authentication_status == None:
        st.warning("Please enter your username and password")



    if authentication_status:
        # --- User Page ---
        def seller_pg():
            con=mysql.connector.connect(host = 'sql6.freemysqlhosting.net',
                                        user = 'sql6636529',
                                        password = '4eKzvSdr1k',
                                        database = 'sql6636529' 
                                        )
            
            if con.is_connected():
                print("Server connected!!")
            else:
                ("krisha will take care dw!")




# --- Feedback Page ---
if selected == "Feedback":
    # ---- CONTACT ----
    with st.container():
        st.write("---")
        st.header("Give us ur feedback!!")
        st.write("##")

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

