import streamlit as st
from pathlib import Path
from src.streamlit_uploads_library.library import Library

class Gallery(Library):
    def __init__(self, directory, expanded=True, file_extensions=(".png", ".jpg", ".jpeg"), gallery_type="container", label="**Gallery**" or None, number_of_columns=5, show_filename=False):
        super(Gallery, self).__init__(directory, expanded, file_extensions, gallery_type, label, number_of_columns, show_filename)

    def fetch_files(self):
        return super().fetch_files()

    def create_gallery(_self):
        return super().create_library()
