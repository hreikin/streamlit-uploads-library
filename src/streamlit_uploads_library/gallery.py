import streamlit as st
from src.streamlit_uploads_library.library import Library

class Gallery(Library):
    def __init__(self, directory, file_extensions=(".png", ".jpg", ".jpeg"), number_of_columns=5, uid="gallery"):
        image_alignment = "center"
        show_details=False
        super(Gallery, self).__init__(directory, file_extensions, image_alignment, number_of_columns, show_details, uid)

    def fetch_files(self):
        return super().fetch_files()

    @st.cache_resource(experimental_allow_widgets=True, show_spinner="Refreshing gallery...")
    def create_gallery(_self):
        return super().create_library(_self.number_of_columns, _self.show_details)
