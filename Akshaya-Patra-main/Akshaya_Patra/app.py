import pickle
import os.path
import requests
from subprocess import run
import streamlit as st
from streamlit_lottie import st_lottie
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu


#run(['pip','install','-r','Requirment'])

#---- Page Design ----
st.set_page_config(page_title="Akshaya Patra", page_icon=":olive:", layout="wide")

selected = option_menu(menu_title=None, default_index=0,
            options=["Home", "About Us", "Login","Register","Feedback"],
            # --- ICONS WEBISTE https://icons.getbootstrap.com/ ---font
            icons=["grid-fill","layout-text-window","fingerprint","person-plus-fill","envelope-paper-fill"],
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


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")


# --- Home Page ---
if selected == "Home":
    # ---- HEADER SECTION ----
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Freshness of farm on your table!")
            st.title("Akshaya Patra")
            st.subheader("Discover a vibrant array of fresh vegetables and fruits on our online marketplace. Enjoy farm-fresh goodness delivered to your doorstep, ensuring quality and convenience for your daily needs.")
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")


# --- About Us Page ---
elif selected == "About Us":
    st.header ("What is Akshaya Patra?")
    st.write("Akshaya Patra is an open source food and grocery store where you will find everything you are loking for, right from Fruits and Vegetable,Rice and Dals,Spices and Seasonings to packaged products, Beverages and many more-we have it all.We are fresh that stands out.Choosefrom a wide range of options in every category, exclusively handpicked to help you find the best quality available at the lowest prices. Select a time slot for delivery and your order will be delivered right to your doorstep, anywhere in Bangalore.We guarantee on time delivery, and the best quality!\nDid you know the average person makes 221 food related decisions every day? As a grocer, we believe that everyone deserves to have access to fresh, affordable and delicious food, no matter who you are, how you shop or what you like to eat.At the heart of it, food can and SHOULD be fresh, so our new brand has been designed to stand out by being optimistic, bright, welcoming and above all fresh.")
    st.subheader("\nWhy should I use Akshaya Patra?")
    st.write("\nAkshaya Patra allows you to walk away from the drudgery of grocery shopping and welcome an easy relaxed way of browsing and shopping for groceries. Discover new products and shop for all your food and grocery needs from the comfort of your home or office. No more getting stuck in traffic jams, paying for parking , standing in long queues and carrying heavy bags – get everything you need, when you need, right at your doorstep. Food shopping online is now easy as every product on your monthly shopping list.")
    st.subheader("\n\nWhere do we operate?")
    st.write("\nWe currently offer our services in Bangalore")





# --- Seller Page ---
def seller_pg():
    sec = option_menu(menu_title=None, default_index=0,
                      options=["My Page", "My Products", "Add New Product"],
                      # --- ICONS WEBISTE https://icons.getbootstrap.com/ ---font
                      icons=["collection", "box-seam-fill", "cart-plus-fill"],
                      orientation="horizontal",
                      styles={
                          "container": {"padding": "0!important", "background-color": "#0A2F51"},
                          "icon": {"color": "#ffffff", "font-size": "20px"},
                          "nav-link": {
                              "font-size": "20px",
                              "text-align": "center",
                              "margin": "0px",
                              "--hover-color": "#224362 ",
                          },
                          "nav-link-selected": {"background-color": "#1977CC"},
                      }, )

    if sec == "Add New Product":
        col1, col2, = st.columns(2)

        # --- For Trail User ---
        with col1:
            uploaded_file = st.file_uploader("Upload your file here", type=['png', 'jpeg', 'jpg'])

            if uploaded_file is not None:
                st.image(uploaded_file)

        with col2:
            product_name = st.text_input("Product Name", value="", max_chars=None, key=str)
            product_price = st.text_input("Product Price", value="", max_chars=None, key=int)
            st.warning("Please enter Numbers")
            location = st.text_input("Location", value="", max_chars=None)

            


# --- Registering Page ---
if selected == "Register":
    st.title("Registration Page")
    st.subheader("Tell us about your self!")
    user_name = st.text_input("User Name", max_chars=None)
    user_password = st.text_input("Password", max_chars=None)
    user_type = st.radio("What are you?" , ('Customer', 'Seller'))


    if user_type == "Seller":
        col1, col2, = st.columns(2)
        with col1:
            seller_location = st.text_input("From Where do you Export?", max_chars=None)
            print("\n\n\nLocation:",seller_location,"\n\n\n")
        with col2:
            seller_location_pin = st.text_input("Enter Your City PIN", max_chars=None)
        seller_options = st.multiselect("What would like to sell?",['Fruits', 'Vegitables', 'Animal Products'])
        txt = st.text_area("Give A Small Introduction About yourslef!")
        option = st.selectbox('Uplad a user picture!',("Upload Image","Camera"))
        if option == "Upload Image":
            seller_img = st.file_uploader("Choose a Picture file", accept_multiple_files=False)
        elif option == "Camera":
            seller_picture = st.camera_input("Take a picture")
        
        submit = st.button("Submit")

        if submit == True:
                #---- Saving User Data----
                file_name = "seller_data.dat"
                save_path = os.path.abspath(file_name)
                with open (file_name,"ab+") as datafile:
                    register = {}
                    register[user_name]={}
                    register[user_name]["password"]=user_password
                    register[user_name]["user_type"]=user_type
                    register[user_name]["City"]=seller_location
                    register[user_name]["PIN"]=seller_location_pin
                    register[user_name]["Food_type"]=seller_options
                    register[user_name]["Info"]= txt

                    pickle.dump(register,datafile)

                st.warning("Your Data Has Be Submitted")


    if user_type == "Customer":
        col1, col2, = st.columns(2)
        with col1:
            custo_location = st.text_input("Which City Are you in?", value="", max_chars=None)
        with col2:
            custo_location_pin = st.text_input("Enter Your City PIN", value="", max_chars=None)
        custo_options = st.multiselect("What is your die style?",['Vegetarian','Vegan','Non-Vegetarian'])
        option = st.selectbox('Uplad a user picture!',("Upload Image","Camera"))
        if option == "Upload Image":
            custo_img = st.file_uploader("Choose a Picture file", accept_multiple_files=False)
        elif option == "Camera":
            custo_picture = st.camera_input("Take a picture")
        submit = st.button("Submit")
        if submit == True:
                #---- Saving User Data----
                file_name = "consumer_data.dat"
                save_path = os.path.abspath(file_name)
                with open (file_name,"ab+") as datafile:
                    register = {}
                    register[user_name]={}
                    register[user_name]["password"]=user_password
                    register[user_name]["user_type"]=user_type
                    register[user_name]["City"]=custo_location
                    register[user_name]["PIN"]=custo_location_pin
                    register[user_name]["Food_type"]=custo_options

                    pickle.dump(register,datafile)

                st.warning("Your Data Has Be Submitted")





if selected == "Login":
    # --- USER AUTHENTICATION ---
    file_name = "consumer_data.dat"
    save_path = os.path.abspath(file_name)

    with open (file_name,"rb") as loginfile:
        data = pickle.load(loginfile)
        for i in data:
            usernames = data[i[0]]
            hashed_passwords = data[i]["password"]
            names = data[i]["user_type"]
    
        
        credentials = {"usernames":{}}

        for username, name, pw in zip(usernames, names, hashed_passwords):
            user_dict = {"name":name,"password":pw}
            credentials["usernames"].update({username:user_dict})

        authenticator = stauth.Authenticate(credentials, "app_home", "auth", cookie_expiry_days=30)

        name, authentication_status, username = authenticator.login("Login", "main")

        if authentication_status == False:
            st.error("Username/password is incorrect")

        if authentication_status == None:
            st.warning("Please enter your username and password")

        if authentication_status:
            seller_pg()








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
