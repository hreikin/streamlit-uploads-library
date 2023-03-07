import streamlit as st
from pathlib import Path

@st.cache_resource(show_spinner="Refreshing gallery...")
class ImageGallery():
    def __init__(self, directory, expanded=True, file_extensions=(".png", ".jpg", ".jpeg"), label="**Images**"):
        self.directory = Path(directory).resolve()
        self.expanded = expanded
        self.file_extensions = file_extensions
        self.label = label
        self.gallery = self.create_gallery()

    def fetch_files(self):
        self.all_files = list()
        self.all_filenames = list()
        for item in self.directory.rglob("*"):
            if item.is_file() and item.name.endswith(self.file_extensions):
                self.all_files.append(str(item.resolve()))
                self.all_filenames.append(str(item.name))
        return self.all_files, self.all_filenames

    def create_gallery(self):
        self.source_image_dropdown = st.expander(label=self.label, expanded=self.expanded)
        with self.source_image_dropdown:
            self.source_gallery = st.container()
        with self.source_gallery:
            self.col1, self.col2, self.col3, self.col4, self.col5 = st.columns(5)
            self.col_list = [self.col1, self.col2, self.col3, self.col4, self.col5]
            self.col_idx = 0
            self.filename_idx = 0
            self.gallery_files, self.gallery_filenames = self.fetch_files()
            for img in self.gallery_files:
                with self.col_list[self.col_idx]:
                    st.image(img, caption=self.gallery_filenames[self.filename_idx], use_column_width=True)
                    if self.col_idx < 4:
                        self.col_idx += 1
                    else:
                        self.col_idx = 0
                    self.filename_idx += 1
        return self.source_image_dropdown