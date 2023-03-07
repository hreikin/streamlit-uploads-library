import streamlit as st
from pathlib import Path

@st.cache_resource(show_spinner="Refreshing gallery...")
class ImageGallery():
    """Create a simple gallery out of streamlit widgets.

    Using the gallery is simple, import `streamlit_simple_gallery` and then instantiate the class with the 
    required `directory` variable. Other options can be configured by passing in different variables 
    when instantiating the class.

    Example Usage:
        python
        import streamlit as st
        from streamlit_simple_gallery import ImageGallery

        st.set_page_config(page_title="Streamlit Gallery", layout="wide")
        default_gallery = ImageGallery(directory="assets")
        gallery_with_columns = ImageGallery(directory="assets", label="**Gallery - Columns**", number_of_columns=3)
        expander_gallery = ImageGallery(directory="assets", expanded=True, gallery_type="expander", label="**Gallery - Expander**")
        multiple_options_gallery = ImageGallery(directory="assets", gallery_type="expander", label="**Gallery - Multiple Options**", number_of_columns=3, show_filename=False)
   
    Args:
        directory (str): A str() of the path to the folder containing the gallery images, for example, "assets".
        expanded (bool): A bool(), passing False starts the expander type gallery closed, default is open and True.
        file_extensions (tuple): A tuple() containing strings of the file extensions to include in the gallery, default is (".png", ".jpg", ".jpeg").
        gallery_type (str): A str() with either "container" or "expander" used as the keyword, the default is "container".
        label (str or None): A str() containing the name of the gallery, passing None disables the label. The default value is "Gallery".
        number_of_columns (int): An int() defining the number of required columns, default is 5.
        show_filenames (bool): A bool(), passing True displays the filenames, the default is False which hides them.
    """
    def __init__(self, directory, expanded=True, file_extensions=(".png", ".jpg", ".jpeg"), gallery_type="container", label="**Gallery**" or None, number_of_columns=5, show_filename=False):
        self.directory = Path(directory).resolve()
        self.expanded = expanded
        self.file_extensions = file_extensions
        self.gallery_type = gallery_type
        self.label = label
        self.number_of_columns = number_of_columns
        self.show_filename = show_filename
        self.gallery = self.create_gallery()

    def fetch_files(self):
        """Returns a list of all files and filenames.

        Returns a list of files and a list of filenames to be used by create_gallery().
        
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

    def create_gallery(self):
        """Creates a simple gallery with columns.

        Creates a gallery using columns out of streamlit widgets.
        
        Returns:
            container_or_expander (st.container or st.expander): A streamlit widget containing the gallery.
        """
        if self.gallery_type == "expander":
            if self.label == None:
                self.label = ""
                self.container_or_expander = st.expander(label=self.label, expanded=self.expanded)
            else:
                self.container_or_expander = st.expander(label=self.label, expanded=self.expanded)
        else:
            self.container_or_expander = st.container()
            with self.container_or_expander:
                if self.label == None:
                    pass
                else:
                    self.gallery_label = st.markdown(f"**{self.label}**")
        with self.container_or_expander:
            self.col_idx = 0
            self.filename_idx = 0
            self.max_idx = self.number_of_columns-1
            self.gallery_files, self.gallery_filenames = self.fetch_files()
            self.all_columns = list(st.columns(self.number_of_columns))
            for img in self.gallery_files:
                with self.all_columns[self.col_idx]:
                    if self.show_filename == True:
                        st.image(img, caption=self.gallery_filenames[self.filename_idx], use_column_width=True)
                    else:
                        st.image(img, use_column_width=True)
                    if self.col_idx < self.max_idx:
                        self.col_idx += 1
                    else:
                        self.col_idx = 0
                    self.filename_idx += 1
        return self.container_or_expander