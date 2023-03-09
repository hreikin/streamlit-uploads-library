import streamlit as st
from src.streamlit_uploads_library.gallery import Gallery
from src.streamlit_uploads_library.uploads import UploadFiles

# Configure page title, layout, menu items and links.
st.set_page_config(
    page_title="Streamlit Uploads Library",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com/hreikin/streamlit-uploads-library",
        "Report a bug": "https://github.com/hreikin/streamlit-uploads-library/issues",
        "About": """
        Streamlit Uploads Library is created and maintained by [@hreikin](https://hreikin.co.uk). The source code is available on [GitHub](https://github.com/hreikin/streamlit-uploads-library), community contributions are always welcome.
        
        MIT licensed: [MIT](https://opensource.org/license/mit/)
        """
    },
)
install_instructions = """
A wrapper around `st.file_uploader` providing library and gallery views for use in Streamlit projects. Installation is available via pip:

```
pip install streamlit-uploads-library
```
"""
example_usage_code = """
EXAMPLE USAGE CODE
"""

with st.sidebar:
    st.info("Welcome to the `streamlit-uploads-library` example app.")
    default_uploader = UploadFiles(save_location="assets")

st.header("Streamlit Uploads Library")
st.markdown(body=install_instructions)
st.code(body=example_usage_code)
default_gallery = Gallery(directory="assets")
gallery_with_columns = Gallery(directory="assets", number_of_columns=3)