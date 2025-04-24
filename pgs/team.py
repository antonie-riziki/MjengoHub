import streamlit as st 
import sys
import pandas as pd 


sys.path.insert(1, './assets')
sys.path.insert(1, './src')







st.image('https://www.bls.gov/spotlight/2022/the-construction-industry-labor-force-2003-to-2020/images/cover-image.jpg', width=900)

certifications = [
    "NCA Certified", "AutoCAD Pro", "Diploma in Civil Eng.", "Electrical License", "Plumbing Cert.",
    "BSc. Architecture", "Safety Compliance Cert.", "Certified Quantity Surveyor", "OSHA Trained", "Masonry Grade I"
]

skills_list = [
    "Blueprint Reading", "Concrete Mixing", "Electrical Wiring", "Project Supervision",
    "AutoCAD", "3D Modeling", "Safety Management", "Site Surveying", "Steel Fixing", "Plumbing & Drainage"
]

@st.dialog('Refer someone')
def refferal():
	names = st.text_input('Names:')
	role = st.text_input('Roles')
	yox = st.slider("Years of Experience", 0, 10, 3)

	col1, col2 = st.columns(2)
	with col1:
		certs = st.multiselect('Certification', certifications)
	with col2:
		skills = st.multiselect('Skills', skills_list)
	projects = st.text_input('Top Projects')

	submit_referal = st.button('Submit', use_container_width=True)

	if submit_referal:
		st.toast('Verification Process started')
		st.toast(f'{names} will be contacted')


@st.dialog('Report Fraud')
def report():
	names = st.text_input('Names:')

	fraud_options = ["Material theft",
				    "Ghost workers",
				    "Inflated labor hours",
				    "False invoicing",
				    "Substandard work",
				    "Kickbacks and bribery",
				    "Material substitution",
				    "Tool misuse or loss",
				    "Site vandalism",
				    "Overbilling / scope creep"]

	fraud_type = st.selectbox('Fraud type', fraud_options)

	incident = st.text_area('Explain how it happend...', height=100)
	measures = st.text_input('Measures taken')

	submit_fraud = st.button('📢Report Fraud',use_container_width=True)

	if submit_fraud:
		st.toast('Case Processed')


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("./assets/style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

# icon("search")
col1, col2, col3 = st.columns(3)

with col1:
	col1_1, col1_2 = st.columns([3, 1])
	with col1_1:
		selected = st.text_input("", "Search...")
	with col1_2:
		st.write('')
		st.write('')
		button_clicked = st.button("OK")


with col2:
	st.write('')
	st.write('')
	refer_btn = st.button('🎯Refer someone')

	if refer_btn:
		refferal()


with col3:
	st.write('')
	st.write('')
	report_fraud = st.button('📢Report Fraud')

	if report_fraud:
		report()

pro_df = pd.read_csv('./src/construction_professionals.csv')

st.dataframe(pro_df.head())

st.divider()

st.write("<h3 style='text-align: left; margin-bottom: 1px;'>Top Features</h6>", unsafe_allow_html=True)

col1, col2 = st.columns(2, border=True)

with col1:
	personal_details, profile_pic = st.columns(2)

	with personal_details:
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>👷 Name: Evans Mwendwa</h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>📬 P.O. Box 00200 </h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>📌 Machakos, Kenya</h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>📞 Tel: +254 71234 5678</h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>#️⃣ Proffesion: Surveyor</h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>📧 Email: evansmwendwa2015@gmaiil.com</h6>", unsafe_allow_html=True)

	with profile_pic:
		
		if True:
			st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSf_w5OJlq5D0igPoBtSGudZk5xi0CNLq1xPw&s', width=400)

		else:
	 		st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdvltpjF8BWal0iwevlrM8ccNwRJDGFxVS6g&s')


with col2:
	personal_details, profile_pic = st.columns(2)

	with personal_details:
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>👷 Name: Sharon Njeri</h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>📬 P.O. Box 00200 </h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>📌 Nairobi, Kenya</h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>📞 Tel: +254 71234 5678</h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>#️⃣ Profession: Architect</h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>📧 Email: shanjeri2001@gmaiil.com</h6>", unsafe_allow_html=True)
		# sms_btn = st.button('Message')
		# call_btn = st.button('📞Call')

	with profile_pic:
		
		if True:
			st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQn9zilY2Yu2hc19pDZFxgWDTUDy5DId7ITqA&s', width=180)

		else:
	 		st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdvltpjF8BWal0iwevlrM8ccNwRJDGFxVS6g&s')
