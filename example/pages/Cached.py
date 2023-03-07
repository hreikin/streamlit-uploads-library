import streamlit as st
from streamlit_simple_gallery import ImageGallery

# Configure page title, layout, menu items and links.
st.set_page_config(
    page_title="Streamlit Gallery",
    initial_sidebar_state="expanded",
    layout="wide",
    menu_items={
        "Get Help": "https://github.com/hreikin/streamlit-simple-gallery",
        "Report a bug": "https://github.com/hreikin/streamlit-simple-gallery/issues",
        "About": """
        Streamlit Gallery is created and maintained by [@hreikin](https://hreikin.co.uk). The source code is available on [GitHub](https://github.com/hreikin/streamlit-simple-gallery), community contributions are always welcome.
        
        MIT licensed: [MIT](https://opensource.org/license/mit/)
        """
    },
)

source_code = """
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
"""
cache_usage = """
Streamlit Simple Gallery makes use of the `st.cache_resource` decorator so the galleries on this 
page will load from the cache instead of reloading the images each time the app is run. You will 
probably want to clear your cache after uploading new files to your app, to do this you can use the 
`st.cache_resource.clear()` function provided by Streamlit.
"""

with st.sidebar:
    st.info("Welcome to the `streamlit-simple-gallery` example app.")

st.header("Caching")
st.markdown(body=cache_usage)
default_gallery = ImageGallery(directory="assets")
gallery_with_columns = ImageGallery(directory="assets", label="**Gallery - Columns**", number_of_columns=3)
expander_gallery = ImageGallery(directory="assets", expanded=True, gallery_type="expander", label="**Gallery - Expander**")
multiple_options_gallery = ImageGallery(directory="assets", gallery_type="expander", label="**Gallery - Multiple Options**", number_of_columns=3, show_filename=False)

with st.expander(label="**Source Code**", expanded=True):
    st.code(body=source_code)