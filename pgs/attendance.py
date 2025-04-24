import streamlit as st
import pandas as pd 
import sys
import africastalking

sys.path.insert(1, './modules')
print(sys.path.insert(1, '../modules/')) 

from func import welcome_message, generate_otp




st.title('Attendance')

st.image('https://www.xamax.co.uk/wp/wp-content/uploads/2019/01/safety-checklist.jpg', width=900)


@st.dialog("Work Permit")
def work_badge(fname, lname, phone_number, address, face_id, site_id):
	personal_details, profile_pic = st.columns(2)

	with personal_details:
		st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>👷 Name {str.upper(fname) + ' ' + str.upper(lname)}</h5>", unsafe_allow_html=True)
		st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>📬 P.O. Box 00200 </h5>", unsafe_allow_html=True)
		st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>📌 {address}, Kenya</h5>", unsafe_allow_html=True)
		st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>📞 Tel: +254 {phone_number}</h5>", unsafe_allow_html=True)
		st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>#️⃣ Site ID: MJ#{site_id}</h5>", unsafe_allow_html=True)
		st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>📧 Email: info@mjengohub.com</h5>", unsafe_allow_html=True)

	with profile_pic:
		
		if face_id is not None:
			st.image(face_id, width=600)

		else:
	 		st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdvltpjF8BWal0iwevlrM8ccNwRJDGFxVS6g&s')

	st.write(f"<h5 style='text-align: center; margin-bottom: 1px;'>Any damage to the Institute property will be made good at individual risk \nContractor shall obtain prior permission for carrying out work on Sundays & holidays</h5>", unsafe_allow_html=True)
	st.write(f"<h5 style='text-align: center; margin-bottom: 1px;'>📑 Terms and Conditions apply</h5>", unsafe_allow_html=True)

	welcome_message(fname, phone_number, site_id)



reg, clock_in, clock_out = st.tabs(['👷 Fundi Registration', '✅ Check In', '⛔ Check Out'])

with reg:
	with st.form(key="User Registration"):
	
		blank, logo, head_text = st.columns([2, 1, 3])
		
		with logo:
			logo_img = st.image('./assets/logo2.png', width=100)

		with head_text:
			title_text = st.write("<h3 style='text-align: left; color: #3EA99F;'>Registration </h3>", unsafe_allow_html=True)

		details_1, details_2 = st.columns(2)

		with details_1:
			fname = st.text_input('First Name')

			dob = st.date_input('D.O.B')

			residence = st.text_input('Residence')

			id_number = st.number_input('ID number', value=None, min_value=0, max_value=int(10e10))

		with details_2:
			lname = st.text_input('Last Name')

			phone_number = st.number_input('Phone number', value=None, min_value=0, max_value=int(10e10))

			insurances_options = ['None', 'Jubilee Health Ins', 'AAR Ins', 'Old Mutual Ins', 'CIC Ins', 'Britam Ins', 'APA Ins', 'MUA Ins', 'ICEA Lion Ins']

			health_ins = st.selectbox(label='Health Insuarnce (optional)', options=insurances_options)

			# face_id = st.file_uploader('Face ID')

			face_id = st.camera_input("Face ID", key='Registration Pic')


		submitted = st.form_submit_button("⏳ Register", use_container_width=True)

		if submitted:

			if fname != None and phone_number != None:
				
				site_id = generate_otp()
				work_badge(fname, lname, phone_number, residence, face_id, site_id)


				st.toast(f"Account Created Successfully")

			else:
				st.toast(f"Must fill all fields")



with clock_in:
	col1, col2 = st.columns(2)

	with col1:
		get_site_id = st.text_input('Site ID:')

		work_selection = ['Foreman', 'Mason', 'Plumber', 'Tiler', 'Electrician', 'Welder', 'Painter', 'Machine operator', 'Surveyor', 'Driver']
		assignment = st.selectbox(label='Assignment', options=work_selection)

		section_options = ['Overall', 'Excavation', 'Basement', 'Foundation', 'Ground Flr', 'Typical Floors', 'Penthouse / Top Floor']
		work_section = st.multiselect('Service Station', section_options)

		protective_equips = ['🪖 Helmet', '🥽 Goggles', '😷 Dust Mask']

		cols = st.columns(len(protective_equips))

		for i, equip in enumerate(protective_equips):
		    with cols[i]:
		        ppe = st.checkbox(equip, key=f'clock_in_1-{i}')

		more_protective_equips = [ '🧤 Gloves', '🦺 Reflector', '🎧 Ear Plugs']

		cols = st.columns(len(more_protective_equips))

		for i, equip in enumerate(more_protective_equips):
		    with cols[i]:
		        ppe = st.checkbox(equip, key=f'clock_in_2-{i}')

	with col2:
		get_pic = st.camera_input("Face ID")


	check_in_btn = st.button('🏗️ Check In', use_container_width=True)

	new_user = [get_site_id, assignment, work_section, ppe, get_pic]

	# st.dataframe(pd.DataFrame(new_user))
	# st.table(new_user)



with clock_out:
	col1, col2 = st.columns(2)

	with col1:
		check_out_site_id = st.text_input('Site ID:', key='check_out_id')

		protective_equips = ['🪖 Helmet', '🥽 Goggles', '😷 Dust Mask']

		cols = st.columns(len(protective_equips))

		for i, equip in enumerate(protective_equips):
		    with cols[i]:
		        check_out_ppe1 = st.checkbox(equip, key=f'clock_out_1-{i}')

		more_protective_equips = [ '🧤 Gloves', '🦺 Reflector', '🎧 Ear Plugs']

		cols = st.columns(len(more_protective_equips))

		for i, equip in enumerate(more_protective_equips):
		    with cols[i]:
		        check_out_ppe2 = st.checkbox(equip, key=f'clock_out_2-{i}')

	with col2:
		check_out_text = st.text_area(label="Remarks", value="", height=350)


	check_out_btn = st.button('🚷 Check Out', use_container_width=True)

	# new_user = [check_out_site_id, check_out_ppe, check_out_get_pic]
