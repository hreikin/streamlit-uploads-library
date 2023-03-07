# Streamlit Simple Gallery

A simple gallery for use in Streamlit projects.

## Installation

Installation is via pip:

```
pip install streamlit-simple-gallery
```

## Usage

Using the gallery is simple, import `streamlit_simple_gallery` and then instantiate the class with the 
required `directory` variable. Other options can be configured by passing in different variables 
when instantiating the class.

- `directory` (required): A `str()` of the path to the folder containing the gallery images, for example, `"assets"`.
- `expanded` (optional): A `bool()`, passing `False` starts the expander type gallery closed, default is open and `True`.
- `file_extensions` (optional): A `tuple()` containing strings of the file extensions to include in the gallery, default is `(".png", ".jpg", ".jpeg")`.
- `gallery_type` (optional): A `str()` with either "container" or "expander" used as the keyword, the default is `"`container"`.
- `label` (optional): A `str()` containing the name of the gallery, passing `None` disables the label. The default value is `"Gallery"`.
- `number_of_columns` (optional): An `int()` defining the number of required columns, default is `5`.
- `show_filenames` (optional): A `bool()`, passing `True` displays the filenames, the default is `False`` which hides them.

```python
import streamlit as st
from streamlit_simple_gallery import ImageGallery

st.set_page_config(page_title="Streamlit Gallery", layout="wide")
default_gallery = ImageGallery(directory="assets")
gallery_with_columns = ImageGallery(directory="assets", label="**Gallery - Columns**", number_of_columns=3)
expander_gallery = ImageGallery(directory="assets", expanded=True, gallery_type="expander", label="**Gallery - Expander**")
multiple_options_gallery = ImageGallery(directory="assets", gallery_type="expander", label="**Gallery - Multiple Options**", number_of_columns=3, show_filename=False)
```

To run the example application provided in the repository:

```bash
git clone https://github.com/hreikin/streamlit-simple-gallery
cd streamlit-simple-gallery/example/
python -m venv .venv
source .venv/bin/activate
pip install streamlit-simple-gallery
streamlit run Home.py
```