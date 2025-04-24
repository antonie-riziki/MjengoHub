import pandas as pd 
import soccerdata as sd
import streamlit as st 
import matplotlib.pyplot as plt 
import seaborn as sb 
import numpy as np  
import csv
import warnings

reg_page = st.Page("./pgs/registration.py", title="register", icon=":material/person_add:")
signin_page = st.Page("./pgs/signin.py", title="sign in", icon=":material/login:")
home_page = st.Page("./pgs/main.py", title="home page", icon=":material/home:")
attendance_page = st.Page("./pgs/attendance.py", title="attendance", icon=":material/check_in_out:")
team_page = st.Page("./pgs/team.py", title="team building", icon=":material/group_search:")
resources_page = st.Page("./pgs/resources.py", title="resources", icon=":material/apps:")
assets_page = st.Page("./pgs/assets_tracking.py", title="asset tracking", icon=":material/speed:")
value_page = st.Page("./pgs/value.py", title="market value", icon=":material/finance_chip:")
td_page = st.Page("./pgs/technical_drawing.py", title="techical drawing", icon=":material/architecture:")
three_d_page = st.Page("./pgs/three-dee.py", title="three d's", icon=":material/deployed_code:")
damage_page = st.Page("./pgs/damage.py", title="damage assessment", icon=":material/flood:")
chatbot_page = st.Page("./pgs/chatbot.py", title="chatbot", icon=":material/chat:")



pg = st.navigation([reg_page, signin_page, home_page, attendance_page, team_page, resources_page, assets_page, value_page, td_page, three_d_page, damage_page, chatbot_page])

st.set_page_config(
    page_title="MjengoHub",
    page_icon="👷",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.echominds.africa',
        'Report a bug': "https://www.echominds.africa",
        'About': "# We are a leading ConTech application company, Try *MjengoHub* and experience reality!"
    }
)

pg.run()



