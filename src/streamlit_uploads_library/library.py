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
        library_with_columns = Library(directory="assets", label="**Library - Columns**", number_of_columns=3)
        expander_library = Library(directory="assets", expanded=True, library_type="expander", label="**Library - Expander**")
        multiple_options_library = Library(directory="assets", library_type="expander", label="**Library - Multiple Options**", number_of_columns=3, show_filename=False)
   
    Args:
        directory (str): A str() of the path to the folder containing the library images, for example, "assets".
        expanded (bool): A bool(), passing False starts the expander type library closed, default is open and True.
        file_extensions (tuple): A tuple() containing strings of the file extensions to include in the library, default is (".png", ".jpg", ".jpeg").
        library_type (str): A str() with either "container" or "expander" used as the keyword, the default is "container".
        label (str or None): A str() containing the name of the library, passing None disables the label. The default value is "Library".
        number_of_columns (int): An int() defining the number of required columns, default is 5.
        show_filenames (bool): A bool(), passing True displays the filenames, the default is False which hides them.
    """
    def __init__(self, directory, expanded=True, file_extensions=(".png", ".jpg", ".jpeg"), library_type="container", label="**Library**" or None, number_of_columns=5, show_filename=False):
        self.directory = Path(directory).resolve()
        self.expanded = expanded
        self.file_extensions = file_extensions
        self.library_type = library_type
        self.label = label
        self.number_of_columns = number_of_columns
        self.show_filename = show_filename
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
            container_or_expander (st.container or st.expander): A streamlit widget containing the library.
        """
        if _self.library_type == "expander":
            if _self.label == None:
                _self.label = ""
                _self.container_or_expander = st.expander(label=_self.label, expanded=_self.expanded)
            else:
                _self.container_or_expander = st.expander(label=_self.label, expanded=_self.expanded)
        else:
            _self.container_or_expander = st.container()
            with _self.container_or_expander:
                if _self.label == None:
                    pass
                else:
                    _self.library_label = st.markdown(f"**{_self.label}**")
        with _self.container_or_expander:
            _self.col_idx = 0
            _self.filename_idx = 0
            _self.max_idx = _self.number_of_columns-1
            _self.library_files, _self.library_filenames = _self.fetch_files()
            _self.all_columns = list(st.columns(_self.number_of_columns))
            for img in _self.library_files:
                with _self.all_columns[_self.col_idx]:
                    if _self.show_filename == True:
                        st.image(img, caption=_self.library_filenames[_self.filename_idx], use_column_width=True)
                    else:
                        st.image(img, use_column_width=True)
                    if _self.col_idx < _self.max_idx:
                        _self.col_idx += 1
                    else:
                        _self.col_idx = 0
                    _self.filename_idx += 1
        return _self.container_or_expander