import streamlit as st
from streamlit_uploads_library.gallery import Gallery
from streamlit_uploads_library.library import Library

# Configure page title, layout, menu items and links.
st.set_page_config(
    page_title="Streamlit Uploads Library",
    menu_items={
        "Get Help": "https://github.com/hreikin/streamlit-uploads-library",
        "Report a bug": "https://github.com/hreikin/streamlit-uploads-library/issues",
        "About": """
        Streamlit Uploads Library is created and maintained by [@hreikin](https://hreikin.co.uk). The source code is available on [GitHub](https://github.com/hreikin/streamlit-uploads-library), community contributions are always welcome.
        
        MIT licensed: [MIT](https://opensource.org/license/mit/)
        """
    },
)

with st.sidebar:
    st.info("Welcome to the `streamlit-uploads-library` example app.")

st.header("Custom File Details")
st.markdown(
"""
A default set of basic file details is provided for each image within the library. Using class 
inheritance this can be overridden to create your own file details section if you wish to include 
more information or different options.
"""
)
st.code(
"""
import streamlit as st
from streamlit_uploads_library.library import Library

class CustomLibrary(Library):
    def __init__(self, directory, file_extensions=(".png", ".jpg", ".jpeg"), image_alignment="center", number_of_columns=5, show_details=True, uid="custom"):
        self.directory = directory
        self.file_extensions = file_extensions
        self.image_alignment = image_alignment
        self.number_of_columns = number_of_columns
        self.show_details = show_details
        self.uid = uid
        super(CustomLibrary, self).__init__(self.directory, self.file_extensions, self.image_alignment, self.number_of_columns, self.show_details, self.uid)

    def create_details(_self, img, filename_idx, uid):
        # Your details section code here
"""
)

st.header("Caching")
st.markdown(
"""
Streamlit Uploads Library makes use of the `st.cache_resource` decorator so the library and gallery 
on this page will load from the cache instead of reloading the images each time the app is run. You 
will probably want to clear your cache after uploading new files to your app, to do this you can use 
the `st.cache_resource.clear()` function provided by Streamlit.
"""
)
default_library = Library(directory="assets/landscape/")
default_gallery = Gallery(directory="assets/portrait/")