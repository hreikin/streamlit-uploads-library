import streamlit as st
from pathlib import Path

class Library():
    """Create a simple library out of streamlit widgets.

    Using the library is simple, import `streamlit_uploads_library` and then instantiate the class with the 
    required `directory` variable. Other options can be configured by passing in different variables 
    when instantiating the class.

    Example Usage:
        python
        import streamlit as st
        from streamlit_uploads_library.library import Library

        st.set_page_config(page_title="Streamlit Uploads Library", layout="wide")
        default_library = Library(directory="assets")
   
    Args:
        directory (str): A str() of the path to the folder containing the library images, for example, "assets".
        file_extensions (tuple): A tuple() containing strings of the file extensions to include in the library, default is (".png", ".jpg", ".jpeg").
        number_of_columns (int): An int() defining the number of required columns, default is 5.
        show_details (bool): A bool() to show or hide the file and edit details, False hides them, default is True to show them.
    """
    def __init__(self, directory, file_extensions=(".png", ".jpg", ".jpeg"), number_of_columns=5, show_details=True):
        self.directory = Path(directory).resolve()
        self.file_extensions = file_extensions
        self.number_of_columns = number_of_columns
        self.show_details = show_details
        self.library = self.create_library()

    def fetch_files(self):
        """Returns a list of all files and filenames.

        Returns a list of files and a list of filenames to be used by create_library().
        
        Returns:
            all_files (list): A list of files.
            all_filenames (list): A list of filenames.
        """
        self.all_files = list()
        self.all_filenames = list()
        for item in self.directory.rglob("*"):
            if item.is_file() and item.name.endswith(self.file_extensions):
                self.all_files.append(str(item.resolve()))
                self.all_filenames.append(str(item.name))
        return self.all_files, self.all_filenames

    @st.cache_resource(show_spinner="Refreshing library...")
    def create_library(_self):
        """Creates a simple library with columns.

        Creates a library using columns out of streamlit widgets.
        
        Returns:
            library_container (st.container or st.expander): A streamlit widget containing the library.
        """
        _self.library_container = st.container()
        with _self.library_container:
            _self.col_idx = 0
            _self.filename_idx = 0
            _self.max_idx = _self.number_of_columns-1
            _self.library_files, _self.library_filenames = _self.fetch_files()
            _self.all_columns = list(st.columns(_self.number_of_columns))
            for img in _self.library_files:
                with _self.all_columns[_self.col_idx]:
                    st.image(img, use_column_width=True)
                    if _self.col_idx < _self.max_idx:
                        _self.col_idx += 1
                    else:
                        _self.col_idx = 0
                    _self.filename_idx += 1
        return _self.library_container