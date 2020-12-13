#!/usr/bin/python
# -*- coding: utf-8 -*-
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Sonder", page_icon="data/favicon/favicon.png")

'''
# Sonder
_An Open Knowledge Platform_

---
'''

# Main
st.sidebar.title('Sonder')
st.sidebar.markdown('_An Open Knowledge Platform_')

st.sidebar.markdown('---')

# Sidebar
navigate_sidebar = st.sidebar.radio(
    'Go to', ['Home', 'Polar', 'Spectrum', 'Balance'])

st.sidebar.markdown('---')

st.sidebar.markdown('**Contribute**')
st.sidebar.info('Sonder is an open source project enabling access to diverse knowledge. Please contribute any comments, questions, code changes, and resources as [issues](https://github.com/saurabh-khanna/sonder/issues) of or [pull requests](https://github.com/saurabh-khanna/sonder/pulls) to the [source code](https://github.com/saurabh-khanna/sonder).')

st.sidebar.markdown('**About me**')
st.sidebar.info("""I am a doctoral student at Stanford studying how knowledge flows through networks. You can learn more about me [here](https://saurabh-khanna.github.io).""")

# Home
if navigate_sidebar == 'Home':
    st.markdown(Path("markdown/home_top.md").read_text(), unsafe_allow_html=True)
    st.markdown(Path("markdown/home_bottom.md").read_text(), unsafe_allow_html=True)

if navigate_sidebar == 'Polar':
    exec(open('scripts/polar.py').read())

# Spectrum
if navigate_sidebar == 'Spectrum':
    exec(open('scripts/spectrum.py').read())

# Balance
if navigate_sidebar == 'Balance':
    st.write('This page is under development')


# hiding the footer
hide_footer_style = \
    """
    <style>
    .reportview-container .main footer {visibility: hidden;}    
    """
st.markdown(hide_footer_style, unsafe_allow_html=True)
