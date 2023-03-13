import streamlit as st
import logging
from pathlib import Path
from PIL import Image

logger = logging.getLogger(__name__)

class UploadFiles():
    """A file uploader with save functionality.

    The file uploader comes with multiple options able to be configured including 2 different view 
    types. It is not required to use this and you can easily replace it with your own, it is provided 
    as a convenience so you dont need to create the code yourself or replicate it across multiple 
    projects.

    Example usage:
        import streamlit as st
        from streamlit_uploads_library.uploads import UploadFiles

        st.set_page_config(page_title="Streamlit Uploads Library")
        default_uploader = UploadFiles(save_location="assets")

    Args:
        save_location (str): A str() of the path to the folder you wish to save images to, for example, "assets".
        expander (bool): A bool() used to set the initial state of the expander, only used when using the "expander" widget_type.
        file_extensions (list): A list() containing strings of the file extensions to include in the library, default is (".png", ".jpg", ".jpeg").
        info_msg (str): A str() used to set an info message above the uploader, default is "Upload new files here.".
        label (str): A str() used to set the label of the "expander" or the header in the "container" type widget, default is "Upload Files", can be set to None to not display it.
        upload_label (str): A str() used to set the label of the file uploader widget, default is "Upload Files".
        widget_type (str): A str() defining the type of widget to use to display the file uploader, options are "container" or "expander", default is "container".
    """
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
        """Creates the file uploader widget layout.
        
        Creates a file uploader widget using either a container or expander.

        Returns:
            upload_options (st.container or st.expander): The root widget for the file uploader layout.
        """
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
        """Saves the uploaded files.
        
        Saves the files selected using the file uploader to the directory provided.

        Args:
            files_to_upload (list): A list() of files retuned by the st.file_uploader widget.
            destination (str): A str() pointing to the directory to save the uploaded files.
        """
        for file in files_to_upload:
            self.full_path = Path(f"{destination}/{file.name}")
            with Image.open(file) as f:
                f.save(self.full_path)
        st.cache_resource.clear()
