import streamlit as st 
import sys
import os
import pandas as pd 
import folium
import openrouteservice



from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
from openrouteservice import convert

import plotly.graph_objects as go




sys.path.insert(1, './assets')
sys.path.insert(1, './modules')

from func import generate_otp, send_sms

from dotenv import load_dotenv

load_dotenv()

geolocator = Nominatim(user_agent="mjengo_hub")
client = openrouteservice.Client(key=os.getenv("ORS_API_KEY"))

df = pd.read_csv('./src/construction_materials.csv')



st.image('https://www.scnsoft.com/blog-pictures/internet-of-things/iiot-and-rfid-industrial-asset-tracking-cover.png', width=700)


tab1, tab2 = st.tabs(['📑Stock Control', '🚛Fleet Control'])


with tab1:
	# st.write('Site Inventory')
	st.dataframe(df.head())

	col1, col2 = st.columns(2, border=True)

	with col1:
		st.write('🛠️Material Details')

		col1_1, col1_2 = st.columns(2)

		with col1_1:
			sign_out_date = st.date_input('Date')
			qty = st.number_input('Quantity')
			

		with col1_2:
			prod_id = st.text_input('Product ID')
			unit = st.selectbox('Unit', ['Kgs', 'Grams', 'Tonnes', 'Pcs', 'Ltrs' 'Per meter', 'Bags'])

	with col2:
		st.write('👷Signee Details')

		col2_1, col2_2 = st.columns(2)

		with col2_1:
			signee_name = st.text_input('Names:')
			signee_site_id = st.text_input('Site ID')

		with col2_2:
			signee_phone = st.number_input('Phone number:', value=None, min_value=0, max_value=int(10e10))
		
		confirmation_btn = st.button('Confirmation Code')

		if confirmation_btn:
			if not signee_phone:
				st.toast('Enter Phone number')
				

			else:
				generate_otp_code = generate_otp()
				send_sms(signee_phone, generate_otp_code)

				with col2_2:
					otp_code = st.text_input('OTP')


				

	sign_out_btn = st.button('📑Update Stock', use_container_width=True)

	if sign_out_btn:
		# data = pd.DataFrame(columns={'Date': sign_out_date, 'Material': prod_id, 'Quantity': qty, 'Unit': unit, 'Site ID': signee_site_id, 'Signee': signee_name, 'Phone': signee_phone})
		# st.dataframe(data)

		materials = ["Cement", "Sand", "Steel", "Bricks", "Paint"]
		qty_in_stock = [100, 200, 150, 300, 80]
		qty_used = [40, 120, 90, 180, 60]
		remaining_qty = [in_stock - used for in_stock, used in zip(qty_in_stock, qty_used)]

		# Create Bar Chart
		fig = go.Figure()

		# In Stock
		fig.add_trace(go.Bar(
		    name='Qty In Stock',
		    x=materials,
		    y=qty_in_stock,
		    marker_color='green',
		    offsetgroup=0
		))

		# Used
		fig.add_trace(go.Bar(
		    name='Qty Used',
		    x=materials,
		    y=qty_used,
		    marker_color='orange',
		    offsetgroup=1
		))

		# Remaining
		fig.add_trace(go.Bar(
		    name='Remaining Qty',
		    x=materials,
		    y=remaining_qty,
		    marker_color='red',
		    offsetgroup=2
		))

		# Layout & Styling
		fig.update_layout(
		    title="Construction Materials Stock Control",
		    barmode='group',
		    xaxis_title="Material",
		    yaxis_title="Quantity",
		    legend_title="Stock Status",
		    template="plotly_white"
		)

		st.plotly_chart(fig, use_container_width=True)



with tab2:
	with st.form(key="user_registration"):
		st.write('Delivery Note:')

		col1, col2 = st.columns(2, border=True)

		with col1:

			st.write('🛠️Material Details')

			col1_1, col1_2 = st.columns(2)

			with col1_1:
				item_name = st.text_input('Item')
				item_description = st.text_area('Description', height=150)


			with col1_2:
				item_qty = st.number_input('Item Qty')
				item_units = st.selectbox('Unit', ['Kgs', 'Grams', 'Tonnes', 'Pcs', 'Ltrs' 'Per meter', 'Bags'], key='delivery_unit')

				item_price = st.number_input('Unit Price (Ksh)')

				# add_item = st.button('✅Add Item')

				total = item_price * item_qty

			# item_total = st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>Grand Total \tKsh. {total}</h5>", unsafe_allow_html=True)

			item_total = st.text_input(label="Grand Total", value=f'Ksh. {total}', disabled=True)


		with col2:
			st.write('🏢Company Details')

			company = st.text_input('Company')

			col2_1, col2_2 = st.columns(2)

			with col2_1:
				location = st.text_input('Location')
				address = st.text_input('Address')
				fax = st.number_input('Tel / Fax')

			with col2_2:
				city = st.text_input('City')
				state = st.text_input('State')
				country = st.selectbox('Country', ['Kenya', 'Uganda', 'Tanzania', 'South Africa', 'Ghana', 'Rwanda', 'Mauritius'])



		col1, col2 = st.columns(2, border=True)

		with col1:
			st.write('🚛Vehicle Details')

			col1_1, col1_2 = st.columns(2)

			with col1_1:
				reg_num = st.text_input('Reg number')
				make = st.selectbox('Make', ['Toyota', 'Nissan', 'Honda', 'Ford', 'Benz'])
				v_model = st.text_input('Model')

			with col1_2:
				v_type = st.selectbox('Type', ['Lorry', 'Double Cabin', 'Pickup', 'Container', 'Tanker'])
				gross_weight = st.number_input('Gross Weight')
				tare_weight = st.number_input('Tare Weight')

			total_capacity = st.number_input('Total Capacity', disabled=True)


		with col2:
			st.write('🧑‍🦼Driver Details')

			col2_1, col2_2 = st.columns(2)

			with col2_1:
				driver_name = st.text_input('Driver Name:')
				driver_address = st.text_input('Address', key='driver_address')
				driver_id = st.number_input('ID number', value=None, min_value=0, max_value=int(10e10))

			with col2_2:
				driver_phone = st.number_input('Phone number', value=None, min_value=0, max_value=int(10e10))
				driver_pic = st.file_uploader('Face ID')

		col1, col2 = st.columns(2, border=True)

		with col1:
			st.write('🏗️Site Details')

			col1_1, col1_2 = st.columns(2)

			with col1_1:
				site_loc = st.text_input('Site Location')
				site_address = st.text_input('Site address')

			with col1_2:
				incharge = st.text_input('Recieving Person (Name)')
				incharge_phone = st.number_input('Incharge Phone number', value=None, min_value=0, max_value=int(10e10))


		with col2:
			st.write('')
			st.write('')
			st.write('')

			ticket_btn = st.form_submit_button('🎯Generate Vehicle Ticket', use_container_width=True)


			# track_btn = st.button('🌍Track Vehicle', use_container_width=True)

		if ticket_btn:

			try:

				start = geolocator.geocode(location)
				end = geolocator.geocode(site_loc)

				start_coords = (start.latitude, start.longitude)
				end_coords = (end.latitude, end.longitude)

				route = client.directions(
					coordinates=[(start.longitude, start.latitude), (end.longitude, end.latitude)],
					profile='driving-car',
					format='geojson'
					)

				summary = route['features'][0]['properties']['summary']
				distance_km = round(summary['distance'] / 1000, 2)
				duration_min = round(summary['duration'] / 60, 2)

				st.success(f"🛣️ Distance: {distance_km} km | ⏱️ Estimated Time: {duration_min} min | the time varies based on traffic")


				m = folium.Map(location=start_coords, zoom_start=10)
				folium.Marker(start_coords, popup=f"Company: {company} \nLocation: {location}", tooltip=f"from", icon=folium.Icon(color="green", icon="truck", prefix="fa")).add_to(m)
				folium.Marker(end_coords, popup=f"Site: {site_loc} \nAddress: {site_address}", tooltip=f"to", icon=folium.Icon(color="red", icon="truck", prefix="fa")).add_to(m)
				folium.GeoJson(route, name='route').add_to(m)

				live_loc = st_folium(m, width=920, height=500)

				google_maps_url = f"https://www.google.com/maps/dir/{start.latitude},{start.longitude}/{end.latitude},{end.longitude}"
				st.markdown(f"[🗺️ View on Google Maps]({google_maps_url})", unsafe_allow_html=True)


			except Exception as e:
				st.error(f"An error occurred: {e}")



################################################################################################






###############################################################################################

# Get OpenRouteService API Key (free on openrouteservice.org)
  # Replace this with your actual key

# Initialize geolocator and ORS client


# st.title("🗺️ MjengoHub Route & Distance Finder")

# start_location = st.text_input("Enter Starting Point (e.g., Nairobi)")
# end_location = st.text_input("Enter Destination (e.g., Thika)")

# if track_btn:
    # Geocode both locations
    # start = geolocator.geocode(start_location)
    # end = geolocator.geocode(end_location)

    # if start and end:
    #     start_coords = (start.latitude, start.longitude)
    #     end_coords = (end.latitude, end.longitude)

    #     # Get route
    #     route = client.directions(
    #         coordinates=[(start.longitude, start.latitude), (end.longitude, end.latitude)],
    #         profile='driving-car',
    #         format='geojson'
    #     )

    #     # Distance and duration
    #     summary = route['features'][0]['properties']['summary']
    #     distance_km = round(summary['distance'] / 1000, 2)
    #     duration_min = round(summary['duration'] / 60, 2)

    #     st.success(f"🛣️ Distance: {distance_km} km | ⏱️ Estimated Time: {duration_min} min")

    # # Draw Map
    # m = folium.Map(location=start_coords, zoom_start=10)
    # folium.Marker(start_coords, tooltip="Start", icon=folium.Icon(color="green")).add_to(m)
    # folium.Marker(end_coords, tooltip="End", icon=folium.Icon(color="red")).add_to(m)
    # folium.GeoJson(route, name='route').add_to(m)

    # st_folium(m, width=700, height=500)

    # # Optional: Link to Google Maps
    # google_maps_url = f"https://www.google.com/maps/dir/{start.latitude},{start.longitude}/{end.latitude},{end.longitude}"
    # st.markdown(f"[🗺️ View on Google Maps]({google_maps_url})", unsafe_allow_html=True)

    # else:
    #     st.error("One of the locations could not be found. Please check your spelling.")







