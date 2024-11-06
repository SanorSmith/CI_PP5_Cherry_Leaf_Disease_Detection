import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_cells_visualizer import page_cells_visualizer_body
from app_pages.page_cherry_leaf_disease_detector import page_cherry_leaf_disease_detector_body

app = MultiPage(app_name="Leaf Disease Detector")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Cells Visualiser", page_cells_visualizer_body)
app.add_page("Disease Detector", page_cherry_leaf_disease_detector_body)

app.run()  # Run the app