import streamlit as st
from src.streamlit_uploads_library.gallery import Gallery

# Configure page title, layout, menu items and links.
st.set_page_config(
    page_title="Streamlit Uploads Library",
    layout="wide",
    menu_items={
        "Get Help": "https://github.com/hreikin/streamlit-uploads-library",
        "Report a bug": "https://github.com/hreikin/streamlit-uploads-library/issues",
        "About": """
        Streamlit Uploads Library is created and maintained by [@hreikin](https://hreikin.co.uk). The source code is available on [GitHub](https://github.com/hreikin/streamlit-uploads-library), community contributions are always welcome.
        
        MIT licensed: [MIT](https://opensource.org/license/mit/)
        """
    },
)

source_code = """
import streamlit as st
from pathlib import Path

@st.cache_resource(show_spinner="Refreshing gallery...")
class Gallery():
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
"""
cache_usage = """
Streamlit Uploads Library makes use of the `st.cache_resource` decorator so the galleries on this 
page will load from the cache instead of reloading the images each time the app is run. You will 
probably want to clear your cache after uploading new files to your app, to do this you can use the 
`st.cache_resource.clear()` function provided by Streamlit.
"""

with st.sidebar:
    st.info("Welcome to the `streamlit-uploads-library` example app.")

st.header("Caching")
st.markdown(body=cache_usage)
default_gallery = Gallery(directory="assets")
gallery_with_columns = Gallery(directory="assets", label="**Gallery - Columns**", number_of_columns=3)
expander_gallery = Gallery(directory="assets", expanded=True, gallery_type="expander", label="**Gallery - Expander**")
multiple_options_gallery = Gallery(directory="assets", gallery_type="expander", label="**Gallery - Multiple Options**", number_of_columns=3, show_filename=False)

with st.expander(label="**Source Code**", expanded=True):
    st.code(body=source_code)