import streamlit as st
import logging
from pathlib import Path
from PIL import Image

logger = logging.getLogger(__name__)

class UploadFiles():
    def __init__(self, save_location, expanded=True, file_extensions=["png", "jpg", "jpeg"], info_msg="Upload new files here.", label="Upload Files", upload_label="Upload Files", widget_type="container"):
        self.save_location = save_location
        self.expanded = expanded
        self.file_extenions = file_extensions
        self.info_msg = info_msg
        self.label = label
        self.widget_type = widget_type
        self.upload_label = upload_label
        self.uploader = self.create_layout()

        if self.uploaded_files is not None:
            self.save_uploaded_files(self.uploaded_files, self.save_location)

    def create_layout(self):
        if self.widget_type == "expander":
            if self.label == None:
                self.label = ""
                self.upload_options = st.expander(label=self.label, expanded=self.expanded)
            else:
                self.upload_options = st.expander(label=self.label, expanded=self.expanded)
        else:
            self.upload_options = st.container()
            with self.upload_options:
                if self.label == None:
                    pass
                else:
                    self.gallery_label = st.markdown(f"**{self.label}**")
        with self.upload_options:
            self.upload_options_msg = st.info(self.info_msg)
            self.uploaded_files = st.file_uploader(label=self.upload_label, accept_multiple_files=True, type=self.file_extenions, help="Upload a new file.")
        return self.upload_options

    def save_uploaded_files(self, files_to_upload, destination):
        for file in files_to_upload:
            self.full_path = Path(f"{destination}/{file.name}")
            with Image.open(file) as f:
                f.save(self.full_path)
        st.cache_resource.clear()
