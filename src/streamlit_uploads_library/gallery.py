import streamlit as st
from pathlib import Path
from src.streamlit_uploads_library.library import Library

class Gallery(Library):
    def __init__(self, directory, file_extensions=(".png", ".jpg", ".jpeg"), number_of_columns=5, show_details=False):
        super(Gallery, self).__init__(directory, file_extensions, number_of_columns, show_details)

    def fetch_files(self):
        return super().fetch_files()

    def create_gallery(_self):
        return super().create_library()
