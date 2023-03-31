import streamlit as st
from streamlit_uploads_library.gallery import Gallery

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

source_code = '''
import streamlit as st
from streamlit_uploads_library.library import Library

class Gallery(Library):
    """Create a simple gallery out of streamlit widgets.

    A wrapper around the `Library` class to create a gallery. Using the gallery is simple, import 
    `streamlit_uploads_library` and then instantiate the class with the required `directory` 
    variable. Other options can be configured by passing in different variables when instantiating 
    the class.

    Example Usage:
        python
        import streamlit as st
        from streamlit_uploads_library.gallery import Gallery

        st.set_page_config(page_title="Streamlit Uploads Library", layout="wide")
        default_gallery = Gallery(directory="assets")
   
    Args:
        directory (str): A str() of the path to the folder containing the gallery images, for example, "assets".
        file_extensions (tuple): A tuple() containing strings of the file extensions to include in the gallery, default is (".png", ".jpg", ".jpeg").
        image_alignment (str): A str() with the CSS keyword used to align the images and details columns.
        number_of_columns (int): An int() defining the number of required columns, default is 5.
        show_details (bool): A bool() to show or hide the file and edit details, True shows them, default is False to hide them and create a gallery.
        uid (str): A str() containing a unique identifier allowing you to create multiple galleries on the same page containing the same images.
    """
    def __init__(self, directory, file_extensions=(".png", ".jpg", ".jpeg"), image_alignment="center", number_of_columns=5, show_details=False, uid="gallery"):
        self.directory = directory
        self.file_extensions = file_extensions
        self.image_alignment = image_alignment
        self.number_of_columns = number_of_columns
        self.show_details = show_details
        self.uid = uid
        super(Gallery, self).__init__(self.directory, self.file_extensions, self.image_alignment, self.number_of_columns, self.show_details, self.uid)
'''

with st.sidebar:
    st.info("Welcome to the `streamlit-uploads-library` example app.")

st.header("Gallery")
st.markdown(
"""
A simple gallery for use in Streamlit projects. Using the gallery is simple, import the `Gallery` 
class from `streamlit_uploads_library.gallery` and then instantiate the class with the required 
`directory` variable. Other options can be configured by passing in different variables when 
instantiating the class.

- `directory` (required): A str() of the path to the folder containing the gallery images, for example, "assets".
- `file_extensions` (optional): A tuple() containing strings of the file extensions to include in the gallery, default is (".png", ".jpg", ".jpeg").
- `image_alignment` (optional): A str() with the CSS keyword used to align the images and details columns.
- `number_of_columns` (optional): An int() defining the number of required columns, default is 5.
- `show_details` (optional): A bool() to show or hide the file and edit details, True shows them, default is False to hide them and create a gallery.
- `uid` (optional): A str() containing a unique identifier allowing you to create multiple galleries on the same page containing the same images.
"""
)
st.code(
"""
import streamlit as st
from streamlit_uploads_library.gallery import Gallery

st.set_page_config(page_title="Streamlit Uploads Library")
default_gallery = Gallery(directory="assets/landscape/")
columns_gallery = Gallery(directory="assets/portrait/", number_of_columns=4, uid="gallery-columns")
mixed_gallery = Gallery(directory="assets/mixed/", uid="mixed-gallery")
"""
)
default_gallery = Gallery(directory="assets/landscape/")
columns_gallery = Gallery(directory="assets/portrait/", number_of_columns=4, uid="gallery-columns")
mixed_gallery = Gallery(directory="assets/mixed/", uid="mixed-gallery")

with st.expander(label="**Source Code**", expanded=True):
    st.code(body=source_code)