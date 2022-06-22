from xlcrf.CRF import CRF
import tempfile
import streamlit as st

# Uploader file
xlsx = st.file_uploader(
    label = "Fai l'upload del file struttura qui.",
    type = ["xlsx"],
    accept_multiple_files = False
)

if xlsx is not None:
    struc = tempfile.NamedTemporaryFile(suffix = '.xlsx')
    out = tempfile.NamedTemporaryFile(suffix = '.xlsx')
    strucfile = struc.name
    outfile = out.name
    # salvo per comodità il file in un file
    with open(strucfile, "wb") as f:
        f.write(xlsx.getbuffer())
    crf = CRF()
    crf.read_structure(strucfile)
    crf.create(outfile)
    with open(outfile, "rb") as f:
        btn = st.download_button(
            label = "Download CRF",
            data = f,
            file_name = "crf.xlsx")
    

with open('README.md', 'r') as r:
    readme = r.read()
st.markdown(readme)
        
