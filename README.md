# Streamlit Uploads Library

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://hreikin-streamlit-uploads-library-home-ar6h9h.streamlit.app/)

A simple uploads library and gallery for use in Streamlit projects. Check out the demo using the 
Streamlit Cloud button above. This package provides a simple wrapper around `st.file_uploader` 
with a save function included and also provides library and gallery views for use in Streamlit 
projects.

## Installation

Installation is available via pip:

```
pip install streamlit-uploads-library
```

## Usage

Using any of the provided views is easy, import `streamlit_uploads_library` and then instantiate the class 
with the required `directory` variable. Other options can be configured by passing in different variables 
when instantiating the class.

### Library View

- `directory` (str): A str() of the path to the folder containing the library images, for example, "assets".
- `file_extensions` (tuple): A tuple() containing strings of the file extensions to include in the library, default is (".png", ".jpg", ".jpeg").
- `image_alignment` (str): A str() with the CSS keyword that is used to align the images and details columns.
- `number_of_columns` (int): An int() defining the number of required columns, default is 5.
- `show_details` (bool): A bool() to show or hide the file and edit details, False hides them, default is True to show them.
- `uid` (str): A str() containing a unique identifier allowing you to create multiple libraries on the same page containing the same images.

```python
import streamlit as st
from streamlit_uploads_library.library import Library

st.set_page_config(page_title="Streamlit Uploads Library", layout="wide")
library = Library(directory="assets/landscape/")
library_columns = Library(directory="assets/portrait/", number_of_columns=4, uid="library-columns")
library_mixed = Library(directory="assets/mixed/", uid="mixed-library")
```

### Gallery View

- `directory` (str): A str() of the path to the folder containing the gallery images, for example, "assets".
- `file_extensions` (tuple): A tuple() containing strings of the file extensions to include in the gallery, default is (".png", ".jpg", ".jpeg").
- `image_alignment` (str): A str() with the CSS keyword that is used to align the images and details columns.
- `number_of_columns` (int): An int() defining the number of required columns, default is 5.
- `show_details` (bool): A bool() to show or hide the file and edit details, True shows them, default is False to hide them and create a gallery.
- `uid` (str): A str() containing a unique identifier allowing you to create multiple galleries on the same page containing the same images.

```python
import streamlit as st
from streamlit_uploads_library.gallery import Gallery

st.set_page_config(page_title="Streamlit Uploads Library", layout="wide")
default_gallery = Gallery(directory="assets/landscape/")
columns_gallery = Gallery(directory="assets/portrait/", number_of_columns=4, uid="gallery-columns")
mixed_gallery = Gallery(directory="assets/mixed/", uid="mixed-gallery")
```

### Upload View

The file uploader comes with multiple options able to be configured including 2 different view 
types. It is not required to use this and you can easily replace it with your own, it is provided 
as a convenience so you don't need to create the code yourself or replicate it across multiple 
projects.

- `save_location` (str): A str() of the path to the folder you wish to save images to, for example, "assets".
- `expander` (bool): A bool() used to set the initial state of the expander, only used when using the "expander" widget_type.
- `file_extensions` (list): A list() containing strings of the file extensions to include in the library, default is (".png", ".jpg", ".jpeg").
- `info_msg` (str): A str() that is used to set an info message above the uploader, default is "Upload new files here.".
- `label` (str): A str() used to set the label of the "expander" or the header in the "container" type widget, default is "Upload Files", can be set to None to not display it.
- `upload_label` (str): A str() that is used to set the label of the file uploader widget, default is "Upload Files".
- `widget_type` (str): A str() defining the type of widget to use to display the file uploader, options are "container" or "expander", default is "container".

```python
import streamlit as st
from streamlit_uploads_library.uploads import UploadFiles

st.set_page_config(page_title="Streamlit Uploads Library", layout="wide")
default_uploader = UploadFiles(save_location="assets")
expander_uploader = UploadFiles(save_location="assets", widget_type="expander")
```

## Caching

Streamlit Uploads Library makes use of the `st.cache_resource` decorator so the library and gallery 
on this page will load from the cache instead of reloading the images each time the app is run. You 
will probably want to clear your cache after uploading new files to your app, the file uploader view 
provided by this package takes care of that for you but if you use your own file uploader and save 
function then to clear the cache you can use the `st.cache_resource.clear()` function provided by 
Streamlit.

## Example App (Demo)

To run the example application provided in the repository:

```bash
git clone https://github.com/hreikin/streamlit-uploads-library
cd streamlit-uploads-library/
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run Home.py
```