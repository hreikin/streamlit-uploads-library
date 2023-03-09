import streamlit as st
from src.streamlit_uploads_library.gallery import Gallery

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
gallery_with_columns = Gallery(directory="assets", number_of_columns=3)