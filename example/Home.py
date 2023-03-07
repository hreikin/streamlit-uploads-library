from numpy import exp
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
example_usage = """
Using the gallery is simple, import `streamlit_simple_gallery` and then instantiate the class with the 
required `directory` variable. Other options can be configured by passing in different variables 
when instantiating the class.
"""
example_usage_code = """
import streamlit as st
from streamlit_simple_gallery import ImageGallery

st.set_page_config(page_title="Streamlit Gallery", layout="wide")
default_gallery = ImageGallery(directory="assets")
gallery_with_columns = ImageGallery(directory="assets", label="**Gallery - Columns**", number_of_columns=3)
expander_gallery = ImageGallery(directory="assets", expanded=True, gallery_type="expander", label="**Gallery - Expander**")
multiple_options_gallery = ImageGallery(directory="assets", gallery_type="expander", label="**Gallery - Multiple Options**", number_of_columns=3, show_filename=False)
"""
configuration = """
- `directory` (required): A `str()` of the path to the folder containing the gallery images, for example `"assets"`.
- `expanded` (optional): A `bool()`, passing `False` starts the expander type gallery closed, default is open and `True`.
- `file_extensions` (optional): A `tuple()` containing strings of the file extensions to include in the gallery, default is `(".png", ".jpg", ".jpeg")`.
- `gallery_type` (optional): A `str()` with either "container" or "expander" used as the keyword, default is `"container"`.
- `label` (optional): A `str()` containing the name of the gallery, passing `None` disables the label. Default value is `"Gallery"`.
- `number_of_columns` (optional): An `int()` defining the number of required columns, default is `5`.
- `show_filenames` (optional): A `bool()`, passing `True` displays the filenames, default is `False` which hides them.
"""

with st.sidebar:
    st.info("Welcome to the `streamlit-simple-gallery` example app.")

st.header("Streamlit Simple Gallery")
st.markdown(body=example_usage)
st.markdown(body=configuration)
st.code(body=example_usage_code)
default_gallery = ImageGallery(directory="assets")
gallery_with_columns = ImageGallery(directory="assets", label="**Gallery - Columns**", number_of_columns=3)
expander_gallery = ImageGallery(directory="assets", expanded=True, gallery_type="expander", label="**Gallery - Expander**")
multiple_options_gallery = ImageGallery(directory="assets", gallery_type="expander", label="**Gallery - Multiple Options**", number_of_columns=3, show_filename=False)

with st.expander(label="**Source Code**", expanded=True):
    st.code(body=source_code)