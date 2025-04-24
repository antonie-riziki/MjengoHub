
# from __future__ import annotations

import streamlit as st 
import sys
# import google.generativeai as genai 
# import time, random, socket, os
# import numpy as np
# import pyvista as pv
# import streamlit as st
# import panel as pn

# from pyvista import examples


sys.path.insert(1, './models')
print(sys.path.insert(1, '../models/'))


# from func import send_sms, generate_otp, check_email, generate_captcha_text, generate_captcha_image, phishing_score, analyze_email_address, analyze_url, check_and_encrypt_password

from dotenv import load_dotenv

load_dotenv()





page_bg_img = '''
<style>
body {
background-image: url("https://wallpapers.com/images/hd/construction-background-qf7iizvernadg5jw.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h1 style="text-align: center; padding: 5px; color: #3EA99F;">Mjengo Hub🏗️</h1>
            <p style="text-align: center;">Your Digital Partner on Every Site.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.image('https://t3.ftcdn.net/jpg/01/88/67/32/360_F_188673280_69cCvYgLg03JsTWTEuKq1duuNHn3amWW.jpg', width=900)




# backend = st.sidebar.radio("Select backend", ["panel", "trame_html", "trame"], index=2)
# st.sidebar.divider()

# if backend == "panel":
#     from stpyvista.panel_backend import stpyvista
# elif backend == "trame_html":
#     from stpyvista.trame_backend import _as_html as stpyvista
# elif backend == "trame":
#     from stpyvista.trame_backend import stpyvista



# # Activate the VTK rendering backend in Panel
# pn.extension('vtk')

# # Create your mesh or load STL
# # Example: structure = pv.Sphere() or use: structure = pv.read("yourfile.stl")
# structure = pv.Sphere()  # Replace this with your actual structure

# # Create the plotter and add the mesh
# plotter = pv.Plotter(off_screen=True)
# plotter.enable_ssao(radius=0.01)
# plotter.add_mesh(
#     structure,
#     smooth_shading=True,
#     split_sharp_edges=True,
#     cmap='reds',
#     ambient=0.2,
# )

# plotter.enable_anti_aliasing('fxaa')

# # Export the scene to a VTKJS file
# vtkjs_path = "mesh_scene.vtkjs"
# plotter.export_vtkjs(vtkjs_path)

# # Display using Panel's VTK pane
# vtk_pane = pn.pane.VTK(vtkjs_path, sizing_mode="stretch_width", height=500)

# # Render inside Streamlit using st.components
# st.write("# 🏗️ MjengoHub 3D Viewer")
# st.write("Visualize your structure below:")
# st.components.v1.html(vtk_pane._repr_html_(), height=500, scrolling=False)



# import streamlit as st
# import pyvista as pv
# import tempfile
# import os

# # st.set_page_config(layout="wide")

# st.title("🏗️ MjengoHub 3D Viewer")
# st.write("Upload an `.stl` file to visualize your 3D construction model.")

# uploaded_file = st.file_uploader("Upload STL File", type=["stl"])

# if uploaded_file is not None:
#     # Save uploaded file temporarily
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".stl") as tmp_file:
#         tmp_file.write(uploaded_file.getvalue())
#         stl_path = tmp_file.name

#     # Read STL and plot
#     mesh = pv.read(stl_path)
#     mesh["z"] = mesh.points[:, 2]  # Add simple scalar for coloring

#     plotter = pv.Plotter(off_screen=True)
#     plotter.add_mesh(mesh, scalars="z", cmap="viridis", smooth_shading=True)
#     plotter.set_background("white")

#     # Export as static image
#     screenshot_path = os.path.join(tempfile.gettempdir(), "stl_preview.png")
#     plotter.show(screenshot=screenshot_path, auto_close=True)

#     # Display screenshot in Streamlit
#     st.image(screenshot_path, caption="3D Mesh Preview", use_column_width=True)
# else:
#     st.info("Please upload an STL file to get started.")



##################################################################################################

# import streamlit as st
# import pyvista as pv
# import tempfile
# import os
# import imageio

# st.title("🏗️ MjengoHub 3D Viewer (Animated Rotation)")
# st.write("Upload an STL file to generate a 360° rotating animation.")

# uploaded_file = st.file_uploader("Upload STL file", type=["stl"])

# if uploaded_file is not None:
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".stl") as tmp:
#         tmp.write(uploaded_file.getvalue())
#         stl_path = tmp.name

#     # Load mesh
#     mesh = pv.read(stl_path)
#     mesh["z"] = mesh.points[:, 2]

#     # Create plotter
#     plotter = pv.Plotter(off_screen=True)
#     plotter.add_mesh(mesh, scalars="z", cmap="coolwarm", smooth_shading=True)
#     plotter.set_background("white")

#     # Generate rotating frames
#     gif_path = os.path.join(tempfile.gettempdir(), "rotating_mesh.gif")
#     frames = []

#     n_frames = 36  # 10° per frame = 360° rotation
#     for i in range(n_frames):
#         plotter.camera_position = 'yz'
#         plotter.camera.azimuth(10)
#         img = plotter.screenshot(transparent_background=True)
#         frames.append(img)

#     # Save animation as gif
#     imageio.mimsave(gif_path, frames, fps=12)

#     # Show in Streamlit
#     st.image(gif_path, caption="Rotating 3D Mesh", use_column_width=True)
# else:
#     st.info("Please upload an STL file to generate the animation.")


