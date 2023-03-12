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

source_code = '''
import streamlit as st
from streamlit_uploads_library.library import Library

class Gallery(Library):
    """Create a simple gallery out of streamlit widgets.

    Using the gallery is simple, import `streamlit_uploads_library` and then instantiate the class with the 
    required `directory` variable. Other options can be configured by passing in different variables 
    when instantiating the class.

    Example Usage:
        python
        import streamlit as st
        from streamlit_uploads_library.gallery import Gallery

        st.set_page_config(page_title="Streamlit Uploads Library", layout="wide")
        default_gallery = Gallery(directory="assets")
   
    Args:
        directory (str): A str() of the path to the folder containing the gallery images, for example, "assets".
        file_extensions (tuple): A tuple() containing strings of the file extensions to include in the gallery, default is (".png", ".jpg", ".jpeg").
        number_of_columns (int): An int() defining the number of required columns, default is 5.
        uid (str): A str() containing a unique identifier allowing you to create multiple galleries on the same page containing the same images.
    """
    def __init__(self, directory, file_extensions=(".png", ".jpg", ".jpeg"), number_of_columns=5, uid="gallery"):
        image_alignment = "center"
        show_details=False
        super(Gallery, self).__init__(directory, file_extensions, image_alignment, number_of_columns, show_details, uid)

    def fetch_files(self):
        """Returns a list of all files and filenames.

        Returns a list of files and a list of filenames to be used by create_gallery().
        
        Returns:
            all_files (list): A list of files.
            all_filenames (list): A list of filenames.
        """
        return super().fetch_files()

    @st.cache_resource(experimental_allow_widgets=True, show_spinner="Refreshing gallery...")
    def create_gallery(_self):
        """Creates a simple gallery with columns.

        Creates a gallery using columns out of streamlit widgets.

        Args:
            number_of_columns (int): An int() indicating the number of columns to create.
            show_details (bool): A bool() that when set to True allows the creation of libraries, default is False to create a gallery.
        
        Returns:
            library_container (st.container): A streamlit widget containing the library.
        """
        return super().create_library(_self.number_of_columns, _self.show_details)
'''

with st.sidebar:
    st.info("Welcome to the `streamlit-uploads-library` example app.")

st.header("Gallery")
st.markdown(
"""
A simple gallery for use in Streamlit projects. Using the gallery is simple, import `streamlit_uploads_library` and then instantiate the class with the 
required `directory` variable. Other options can be configured by passing in different variables 
when instantiating the class.

- `directory` (required): A `str()` of the path to the folder containing the gallery images, for example, `"assets"`.
- `file_extensions` (optional): A `tuple()` containing strings of the file extensions to include in the gallery, default is `(".png", ".jpg", ".jpeg")`.
- `number_of_columns` (optional): An `int()` defining the number of required columns, default is `5`.
"""
)
st.code(
"""
import streamlit as st
from streamlit_uploads_library.gallery import Gallery

st.set_page_config(page_title="Streamlit Uploads Library")
default_gallery = Gallery(directory="assets")
columns_gallery = Gallery(directory="assets", number_of_columns=4, uid="columns")
"""
)
default_gallery = Gallery(directory="assets")
columns_gallery = Gallery(directory="assets", number_of_columns=4, uid="columns")

with st.expander(label="**Source Code**", expanded=True):
    st.code(body=source_code)