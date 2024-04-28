import streamlit as st
# from streamlit_option_menu import option_menu

import time
import util

st.set_page_config(page_title="Home")

# ---- HIDE STREAMLIT STYLE ----
st.markdown(util.load_css("style/streamlit_header.css"), unsafe_allow_html=True)

# Can add nav-bar in the standard way too, it doesn't create new pages
# with st.sidebar:
#     selected = option_menu(
#         menu_title=None,
#         options=["Home", "Projects", "Contact"],
#         icons=["house", "book", "envelope"],
#         styles={
#             "container": {"padding": "0!important", "background-color": "#fafafa"},
#             "icon": {"color": "orange", "font-size": "25px"}, 
#             "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#         }
#     )


tab1, tab2, tab3 = st.tabs([":house: Home", ":book: Projects", ":envelope: Contact"])

col1, col2, col3, col4 = tab1.columns(4)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
# col4.metric(label="Temperature", value="60 °C", delta="- 3 °C")

progress_text = "Operation in progress. Please wait."
if tab1.button('Rerun'):
    bar = tab1.progress(0, text=progress_text)
    for comp in range(100):
        time.sleep(0.02)
        bar.progress(comp+1, text=progress_text)
    time.sleep(1)
    bar.empty()
    st.toast('Your task was processed successfully!')

with tab1:
    with st.spinner("Loading..."):
        time.sleep(3)
    st.success("Done!")

# echo, write ---> this is basically an all-in function 
# container, sidebar, empty, columns, expander, tabs
# title, header, subheader, markdown
# metric, success, progress
# file_uploader, camera_input, image
# st.multiselect, st.selectbox
# pages/contact.py, pages/about.py --> for mulit-page webapp
# st.dataframe --> shows pandas dataframe
# streamlit session_state and callback functions
# st.secrets when deploying on share.streamlit.io / heroku

# streamlit-option-menu --> for navigation bar
# st-aggrid --> for dynamic dataframe table on page
# st-lottie  ---> for lottie animations
# streamlit-elements  ---- woooooaaaaah
# streamlit-echarts ------ wooooaaaah
# st_on_hover_tabs  ------ sidebar/nav-bar tabs on hover --- saves a lot of time
# Deta / Firebase / Google Sheets
