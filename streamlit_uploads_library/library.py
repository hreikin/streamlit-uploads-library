import streamlit as st
import get_image_size
import logging
from pathlib import Path
from math import ceil

logger = logging.getLogger(__name__)

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
        image_alignment (str): A str() with the CSS keyword used to align the images and details columns.
        number_of_columns (int): An int() defining the number of required columns, default is 5.
        show_details (bool): A bool() to show or hide the file and edit details, False hides them, default is True to show them.
        uid (str): A str() containing a unique identifier allowing you to create multiple libraries on the same page containing the same images.
    """
    def __init__(self, directory, file_extensions=(".png", ".jpg", ".jpeg"), image_alignment="end", number_of_columns=5, show_details=True, uid="library"):
        self.directory = Path(directory).resolve()
        self.file_extensions = file_extensions
        self.image_alignment = image_alignment
        self.number_of_columns = number_of_columns
        self.show_details = show_details
        self.uid = uid
        self.root_container = self.create(directory=self.directory, file_extensions=self.file_extensions, image_alignment=self.image_alignment, number_of_columns=self.number_of_columns, show_details=self.show_details, uid=self.uid)

    def fetch_files(self, directory, file_extensions):
        """Returns a list of all files.

        Returns a list of files to be used by create_library().

        Args:
            directory (str): A str() of the path to the folder containing the library images, for example, "assets".
            file_extensions (tuple): A tuple() containing strings of the file extensions to include in the library, default is (".png", ".jpg", ".jpeg").
        
        Returns:
            all_files (list): A list of files.
            all_filenames (list): A list of filenames.
        """
        all_files = list()
        for item in directory.rglob("*"):
            if item.is_file() and item.name.endswith(file_extensions):
                all_files.append(str(item.resolve()))
        return all_files

    def update_file(self, old_file, new_file, del_check=False):
        """Update or delete the file.
        
        Updates or deletes the file depending on the supplied options.

        Args:
            old_file (Path): A Path() object pointing to the file to be changed.
            new_file (str): A str() containing the desired name of the new file.
            del_check (bool): A bool() used to set the mode (update/delete) of the method.
        """
        if del_check == False:
            try:
                old_file.rename(old_file.with_stem(new_file))
            except FileExistsError as e:
                logger.warning(e)
        else:
            try:
                old_file.unlink()
            except FileNotFoundError as e:
                logger.warning(e)
        st.cache_resource.clear()
        st.experimental_rerun()

    def create_details(self, img, filename_idx, uid):
        """Create the details section for each displayed image.

        Creates a default details section for each image it is used on, can be overridden to create 
        a custom details section with more information or other options available.

        Args:
            img (file): An image file object to create the details from.
            filename_idx (int): An int() of the current "filename_idx" used to create a unique key for fields within the details section.
            uid (str): A str() containing a unique identifier allowing you to create multiple libraries on the same page containing the same images.
        """
        try:
            img_meta = get_image_size.get_image_metadata(img)
            img_path = Path(img).resolve()
            new_name = st.text_input(label="Name:", key=f"{img_path.stem}_{uid}_name_{filename_idx}", value=f"{img_path.stem}")
            st.text_input(label="Type:", key=f"{img_path.stem}_{uid}_type_{filename_idx}", value=f"{img_path.suffix.strip('.').upper()}", disabled=True)
            details_col1, details_col2 = st.columns(2)
            del_check = st.checkbox(label="Delete ?", key=f"{img_path.stem}_{uid}_del_check_{filename_idx}", help="Permanently delete a file from the library.")
            if del_check:
                st.button(label="Delete", key=f"{img_path.stem}_{uid}_delete_button_{filename_idx}", type="secondary", use_container_width=True, on_click=self.update_file, args=(img_path, new_name, del_check))
            else:
                st.button(label="Update", key=f"{img_path.stem}_{uid}_submit_button_{filename_idx}", type="primary", use_container_width=True, on_click=self.update_file, args=(img_path, new_name, del_check))
            with details_col1:
                st.text_input(label="Width:", key=f"{img_path.stem}_{uid}_width_{filename_idx}", value=f"{img_meta.width}", disabled=True)
            with details_col2:
                st.text_input(label="Height:", key=f"{img_path.stem}_{uid}_height_{filename_idx}", value=f"{img_meta.height}", disabled=True)
        except get_image_size.UnknownImageFormat:
            width, height = -1, -1

    @st.cache_resource(experimental_allow_widgets=True, show_spinner="Loading...")
    def create(_self, directory, file_extensions, image_alignment, number_of_columns, show_details, uid):
        """Creates a simple library or gallery with columns.

        Creates a library or gallery using columns out of streamlit widgets.

        Args:
            directory (str): A str() of the path to the folder containing the library images, for example, "assets".
            file_extensions (tuple): A tuple() containing strings of the file extensions to include in the library, default is (".png", ".jpg", ".jpeg").
            image_alignment (str): A str() with the CSS keyword used to align the images and details columns.
            number_of_columns (int): An int() defining the number of required columns, default is 5.
            show_details (bool): A bool() to show or hide the file and edit details, False hides them, default is True to show them.
            uid (str): A str() containing a unique identifier allowing you to create multiple libraries on the same page containing the same images.
        
        Returns:
            root_container (st.container): A streamlit widget containing the library.
        """
        root_container = st.container()
        with root_container:
            # To be able to display the images, details and buttons all in one row and aligned 
            # correctly so that images of different sizes don't affect the alignment of the details 
            # and buttons we need do some minor maths and keep track of multiple index values. 
            # First we instantiate some defaults.
            col_idx = 0
            filename_idx = 0
            max_idx = number_of_columns-1
            # Get the file list and filename list, work out the total number of files from the 
            # length of the file list.
            library_files = _self.fetch_files(directory, file_extensions)
            num_of_files = len(library_files)
            # Work out the number of rows required by dividing the number of files by the number of 
            # columns and rounding up using `math.ceil`.
            num_of_rows_req = ceil(num_of_files / number_of_columns)
            # Create the required number of rows (st.container).
            library_rows = list()
            library_rows_idx = 0
            for i in range(num_of_rows_req):
                library_rows.append(st.container())
            # For each library row we need to create separate rows (st.container) for images, 
            # and rows (st.expander) for details and buttons to keep them in the correct columns.
            for idx in range(num_of_rows_req):
                with library_rows[library_rows_idx]:
                    imgs_columns = list(st.columns(number_of_columns))
                # Since we are keeping track of the column and filename indexes we can use 
                # those to slice the `library_files` list at the correct points for each row 
                # and then increase or reset the indexes as required.
                for img in library_files[filename_idx:(filename_idx + number_of_columns)]:
                    with imgs_columns[col_idx]:
                        st.image(img, use_column_width="auto")
                        st.write(
                                f"""<style>
                                [data-testid="stHorizontalBlock"] {{
                                    align-items: {image_alignment};
                                }}
                                </style>
                                """,
                                unsafe_allow_html=True
                            )
                        if show_details == True:
                            _self.create_details(img, filename_idx, uid)
                    # Keeps track of the current column, if we reach the `max_idx` we reset it 
                    # to 0 and increase the row index. This combined with the slicing should 
                    # ensure all images, details and buttons are in the correct columns.
                    if col_idx < max_idx:
                        col_idx += 1
                    else:
                        col_idx = 0
                        library_rows_idx += 1
                    filename_idx += 1
        return root_container

# Below is an example of using class inheritance to override the default file details section.
#
# import streamlit as st
# from streamlit_uploads_library.library import Library
#
# class CustomLibrary(Library):
#     def __init__(self, directory, file_extensions=(".png", ".jpg", ".jpeg"), image_alignment="center", number_of_columns=5, show_details=True, uid="custom"):
#         self.directory = directory
#         self.file_extensions = file_extensions
#         self.image_alignment = image_alignment
#         self.number_of_columns = number_of_columns
#         self.show_details = show_details
#         self.uid = uid
#         super(CustomLibrary, self).__init__(self.directory, self.file_extensions, self.image_alignment, self.number_of_columns, self.show_details, self.uid)

#     def create_details(_self, img, filename_idx, uid):
#         # Your details section code here