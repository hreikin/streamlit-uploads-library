import streamlit as st
from src.streamlit_uploads_library.gallery import Gallery
from src.streamlit_uploads_library.library import Library

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

with st.sidebar:
    st.info("Welcome to the `streamlit-uploads-library` example app.")

st.header("Caching")
st.markdown(
"""
Streamlit Uploads Library makes use of the `st.cache_resource` decorator so the library and gallery 
on this page will load from the cache instead of reloading the images each time the app is run. You 
will probably want to clear your cache after uploading new files to your app, to do this you can use 
the `st.cache_resource.clear()` function provided by Streamlit.
"""
)
default_library = Library(directory="assets")
default_gallery = Gallery(directory="assets")