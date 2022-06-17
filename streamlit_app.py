from xlcrf.CRF import CRF
import tempfile
import streamlit as st

st.markdown("""# webxlcrf

Basically [xlcrf](https://pypi.org/project/xlcrf/), but repacked as an online
[streamlit](https://streamlit.io) app.

Structure file examples can be found [here](https://github.com/lbraglia/xlcrf/tree/main/examples).


""")

# Uploader file
xlsx = st.file_uploader(
    label = "Upload CRF structure below.",
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
    ex1 = CRF()
    ex1.read_structure(strucfile)
    ex1.create(outfile)
    with open(outfile, "rb") as f:
        btn = st.download_button(
            label = "Download CRF",
            data = f,
            file_name = "crf.xlsx")
    
