import streamlit as st
from src.streamlit_uploads_library.gallery import Gallery

# Configure page title, layout, menu items and links.
st.set_page_config(
    page_title="Streamlit Uploads Library",
    initial_sidebar_state="expanded",
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
from streamlit_uploads_library.library import Library

class Gallery(Library):
    def __init__(self, directory, file_extensions=(".png", ".jpg", ".jpeg"), number_of_columns=5):
        super(Gallery, self).__init__(directory, file_extensions, number_of_columns)

    def fetch_files(self):
        return super().fetch_files()

    @st.cache_resource(experimental_allow_widgets=True, show_spinner="Refreshing gallery...")
    def create_gallery(_self):
        return super().create_library(_self.number_of_columns, _self.show_details)
"""
example_usage = """
A simple gallery for use in Streamlit projects. Using the gallery is simple, import `streamlit_uploads_library` and then instantiate the class with the 
required `directory` variable. Other options can be configured by passing in different variables 
when instantiating the class.
"""
# Needs updating with latest changes
configuration = """
- `directory` (required): A `str()` of the path to the folder containing the gallery images, for example, `"assets"`.
- `file_extensions` (optional): A `tuple()` containing strings of the file extensions to include in the gallery, default is `(".png", ".jpg", ".jpeg")`.
- `number_of_columns` (optional): An `int()` defining the number of required columns, default is `5`.
"""
example_usage_code = """
import streamlit as st
from streamlit_uploads_library.gallery import Gallery

st.set_page_config(page_title="Streamlit Uploads Library")
default_gallery = Gallery(directory="assets")
gallery_with_columns = Gallery(directory="assets", label="**Gallery - Columns**", number_of_columns=3)
"""

with st.sidebar:
    st.info("Welcome to the `streamlit-uploads-library` example app.")

st.header("Gallery")
st.markdown(body=example_usage)
st.markdown(body=configuration)
st.code(body=example_usage_code)
default_gallery = Gallery(directory="assets")
gallery_with_columns = Gallery(directory="assets", number_of_columns=4)

with st.expander(label="**Source Code**", expanded=True):
    st.code(body=source_code)