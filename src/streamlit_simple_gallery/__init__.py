import streamlit as st
from pathlib import Path

@st.cache_resource(show_spinner="Refreshing gallery...")
class ImageGallery():
    def __init__(self, directory, expanded=True, file_extensions=(".png", ".jpg", ".jpeg"), gallery_type="container", label="**Gallery**" or None, number_of_columns=5, show_filename=False):
        self.directory = Path(directory).resolve()
        self.expanded = expanded
        self.file_extensions = file_extensions
        self.gallery_type = gallery_type
        self.label = label
        self.number_of_columns = number_of_columns
        self.show_filename = show_filename
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
        if self.gallery_type == "expander":
            if self.label == None:
                self.label = ""
                self.container_or_expander = st.expander(label=self.label, expanded=self.expanded)
            else:
                self.container_or_expander = st.expander(label=self.label, expanded=self.expanded)
        else:
            self.container_or_expander = st.container()
            with self.container_or_expander:
                if self.label == None:
                    pass
                else:
                    self.gallery_label = st.markdown(f"**{self.label}**")
        with self.container_or_expander:
            self.col_idx = 0
            self.filename_idx = 0
            self.max_idx = self.number_of_columns-1
            self.gallery_files, self.gallery_filenames = self.fetch_files()
            self.all_columns = list(st.columns(self.number_of_columns))
            for img in self.gallery_files:
                with self.all_columns[self.col_idx]:
                    if self.show_filename == True:
                        st.image(img, caption=self.gallery_filenames[self.filename_idx], use_column_width=True)
                    else:
                        st.image(img, use_column_width=True)
                    if self.col_idx < self.max_idx:
                        self.col_idx += 1
                    else:
                        self.col_idx = 0
                    self.filename_idx += 1
        return self.container_or_expander