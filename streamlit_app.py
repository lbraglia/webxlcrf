from xlcrf.CRF import CRF
import tempfile
import streamlit as st

# Uploader file
xlsx = st.file_uploader(
    label = st.markdown("Fai l'upload del file struttura qui. Puoi compilarlo a partire dal [template](https://github.com/lbraglia/xlcrf/raw/main/examples/blank_template.xlsx) seguendo le istruzioni di sotto. Puoi fare prove con gli esempi: [esempio1](https://github.com/lbraglia/xlcrf/raw/main/examples/esempio1.xlsx), [esempio2](https://github.com/lbraglia/xlcrf/raw/main/examples/esempio2.xlsx)."),
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
        
