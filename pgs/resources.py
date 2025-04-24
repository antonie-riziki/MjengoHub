import streamlit as st 
import sys
import pandas as pd


sys.path.insert(1, './assets')








st.image('https://cdn-aoadm.nitrocdn.com/KuVfinkzGFVaEOfMOIsLUKmwNnxwFguR/assets/images/optimized/rev-4863c6f/www.qtoestimating.com/wp-content/uploads/2020/01/Wholesale-Construction-Suppliers-650x325.png', width=900)


materials = ["Cement", "Steel Bars", "Sand", "Ballast", "Bricks", "Paint", "PVC Pipes",
             "Tiles", "Glass Panels", "Timber"]

quality_options = [
    "Premium", "Standard", "Medium", "Poor"
]

@st.dialog('Recommend Company')
def refferal():
	names = st.text_input('Company Name:')
	location = st.text_input('Address')
	rate = st.slider("Ratings", 0, 10, 3)

	col1, col2 = st.columns(2)
	with col1:
		products = st.multiselect('Products', materials)
	with col2:
		quality = st.multiselect('quality', quality_options)
	projects = st.text_input('Top Projects')

	submit_referal = st.button('Submit', use_container_width=True)

	if submit_referal:
		st.toast('Verification Process started')


@st.dialog('Report Fraud')
def report():
	names = st.text_input('Names:')

	fraud_options = [
					"Inflated project costs",
				    "Bribing officials for tenders",
				    "Use of substandard materials",
				    "Billing for uncompleted work",
				    "Kickbacks to procurement officers",
				    "Ghost projects",
				    "Falsified progress reports",
				    "Deliberate project delays for more funding",
				    "Double invoicing",
				    "Underpaying or exploiting workers",
				    "Environmental regulation violations",
				    "Non-compliance with safety standards",
				    "Overstatement of manpower and equipment",
				    "Fronting (using shell companies for contracts)",
				    "Concealing defects in construction"
				    ]

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
	refer_btn = st.button('🎯Recommend Company')

	if refer_btn:
		refferal()


with col3:
	st.write('')
	st.write('')
	report_fraud = st.button('📢Report Fraud')

	if report_fraud:
		report()

pro_df = pd.read_csv('./src/construction_materials.csv')

st.dataframe(pro_df.head())

st.divider()

st.write("<h3 style='text-align: left; margin-bottom: 1px;'>Top Features</h6>", unsafe_allow_html=True)

col1, col2 = st.columns(2, border=True)

with col1:
	personal_details, profile_pic = st.columns(2)

	with personal_details:
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>👷 JTL Co. Ltd</h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>📬 P.O. Box 00200 </h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>📌 Industrial area, Kenya</h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>📞 Tel: +254 71234 5678</h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>#️⃣ Proffesion: Surveyor</h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>🌐 www.jtlcompanies.ke</h6>", unsafe_allow_html=True)

	with profile_pic:
		
		if True:
			st.image('data:image/png;base64,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', width=400)

		else:
	 		st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdvltpjF8BWal0iwevlrM8ccNwRJDGFxVS6g&s')


with col2:
	personal_details, profile_pic = st.columns(2)

	with personal_details:
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>👷 XYZ Works Engineering.</h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>📬 P.O. Box 00200 </h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>📌 Mombasa rd, Kenya</h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>📞 Tel: +254 71234 5678</h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>#️⃣ Profession: Architect</h6>", unsafe_allow_html=True)
		st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>🌐 www.xyzengineers.com</h6>", unsafe_allow_html=True)
		# sms_btn = st.button('Message')
		# call_btn = st.button('📞Call')

	with profile_pic:
		
		if True:
			st.image('data:image/png;base64,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', width=180)

		else:
	 		st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdvltpjF8BWal0iwevlrM8ccNwRJDGFxVS6g&s')