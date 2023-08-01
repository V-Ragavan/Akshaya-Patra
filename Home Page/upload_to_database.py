import streamlit_authenticator as stauth

import database as db

usernames = ["demo_user"]
names = ["Trail"]
passwords = ["ap@2023"]
hashed_passwords = stauth.Hasher(passwords).generate()


for (username, name, hash_password) in zip(usernames, names, hashed_passwords):
    db.insert_user(username, name, hash_password)