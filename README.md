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

```python
import streamlit as st
from streamlit_gallery import ImageGallery

st.set_page_config(page_title="Streamlit Gallery", layout="wide")
gallery = ImageGallery(directory="assets")
```

To run the example application provided in the repository:

```bash
git clone https://github.com/hreikin/streamlit-simple-gallery
cd streamlit-gallery/example/
python -m venv .venv
source .venv/bin/activate
pip install streamlit-gallery
streamlit run Home.py
```