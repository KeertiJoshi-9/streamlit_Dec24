import streamlit as st

st.title("Streamlit Introduction")

st.header("This is a test header")

st.write("I want to write something about streamlit.io")

checktest = st.checkbox("Check this box if you already know about streamlit.io")

if checktest:
    st.write("Wow, that is great news !")

genre = st.radio("Select the Machine Learning concept that you are familiar with the most:", 
                 ['Decision Trees', 'Regression and Classification', 'Recommendation Systems', 'Supervised Algorithms'])

if genre == 'Decision Trees':
    st.write("You must be familiar with boostig and bagging techniques.")
elif genre == 'Recommendation Systems':
    st.write("You must really love Netflix and Amazon!")

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)