import streamlit as st
from streamlit_uploads_library.gallery import Gallery
from streamlit_uploads_library.uploads import UploadFiles
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
    default_uploader = UploadFiles(save_location="assets")

st.header("Streamlit Uploads Library")
st.markdown(
"""
This package provides library and gallery views for use in Streamlit projects and also provides a 
simple wrapper around `st.file_uploader` with a save method included. Installation is available 
via pip:

```
pip install streamlit-uploads-library
```

The default file uploader can be seen in the sidebar and the library and gallery views are shown 
down below. Using any of the provided views is easy, just import the class and then instantiate 
it. Multiple options are able to be configured with more info available on the relevant pages. Here 
is a code example that shows how to create the default library, gallery and file uploader views. 
"""
)
st.code(
"""
from streamlit_uploads_library.gallery import Gallery
from streamlit_uploads_library.uploads import UploadFiles
from streamlit_uploads_library.library import Library

default_library = Library(directory="assets")               # Displays a library view with details in a grid
default_gallery = Gallery(directory="assets")               # Displays a simple gallery to show images in a grid
default_uploader = UploadFiles(save_location="assets")      # Wraps st.file_uploader and provides save functionality
"""
)
default_library = Library(directory="assets/landscape/")
default_gallery = Gallery(directory="assets/portrait/")