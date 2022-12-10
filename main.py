import streamlit as st
from datetime import date
from fpdf import FPDF
import base64
from PIL import Image

# date du jour
today = date.today()


st.set_page_config(layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("style.css")



# --- THERAPEUTE ---
#Title
t_col1, t_col2, t_col3 = st.columns([1,2,1])
t_col2.markdown("<p style='padding: 20; border: 2px solid white;text-align: center;font-size: 50;'> Thérapeute </p>", unsafe_allow_html=True)
therapeute_choice = st.columns(3)[1].selectbox("Thérapeute :",["Magali Citro","Autre"],index=0, key=1)

# NOM / PRENOM
therapeute_cols = st.columns(4)

# Nom
with therapeute_cols[1]:
    nom_the_temp = st.empty()
    nom_the = nom_the_temp.text_input('Nom',key="nom_the1")
    if therapeute_choice=="Magali Citro":
        nom_the = nom_the_temp.text_input('Nom', value='Citro', key="nom_the2")
    else: 
        nom_the = nom_the_temp.text_input('Nom',value = "",key="nom_the3")

# Prénom
with therapeute_cols[2]:
    prenom_the_temp = st.empty()
    prenom_the = prenom_the_temp.text_input('Prenom',key="prenom_the1")
    if therapeute_choice=="Magali Citro":
        prenom_the = prenom_the_temp.text_input('Prenom', value='Magali', key="prenom_the2")
    else: 
        prenom_the = prenom_the_temp.text_input('Prenom',value = "",key="prenom_the3")

# -- MAIL / TELEPHONE
therapeute_cols2 = st.columns(4)

# Mail
with therapeute_cols2[1]:
    mail_the_temp = st.empty()
    mail_the = mail_the_temp.text_input('Mail',key="mail_the1")
    if therapeute_choice=="Magali Citro":
        mail_the = mail_the_temp.text_input('Mail', value='mcitro.sophrologue@gmail.com', key="mail_the2")
    else: 
        mail_the = mail_the_temp.text_input('Mail',value = "",key="mail_the3")
# Téléphone
with therapeute_cols2[2]:
    num_the_temp = st.empty()
    num_the = num_the_temp.text_input('Telephone',key="num_the1")
    if therapeute_choice=="Magali Citro":
        num_the = num_the_temp.text_input('Telephone', value='06 18 24 61 58', key="num_the2")
    else: 
        num_the = num_the_temp.text_input('Telephone',value = "",key="num_the3")



# ADRESSE / SIRET
therapeute_cols3 = st.columns(4)

# Adresse
with therapeute_cols3[1]:
    adresse_the_temp = st.empty()
    adresse_the = adresse_the_temp.text_input('Adresse',key="add_the1")
    if therapeute_choice=="Magali Citro":
        adresse_the = adresse_the_temp.text_input('Adresse', value='50 RUE DE LA SOURCE, 74890 LULLY', key="add_the2")
    else: 
        adresse_the = adresse_the_temp.text_input('Adresse',value = "",key="add_the3")
# Siret
with therapeute_cols3[2]:
    siret__the_temp = st.empty()
    siret_the = siret__the_temp.text_input('SIRET',key="siret_the1")
    if therapeute_choice=="Magali Citro":
        siret_the = siret__the_temp.text_input('SIRET', value='500 824 016 000 33', key="siret_the2")
    else: 
        siret_the = siret__the_temp.text_input('SIRET',value = "",key="siret_the3")


# --- PATIENT ---
p_col1, p_col2, p_col3 = st.columns([2,9,2])
p_col2.write("")
p_col2.markdown("<p style='padding: 20; border: 2px solid white;text-align: center;font-size: 50;'> Patient </p>", unsafe_allow_html=True)

pat_cols1, pat_cols2, pat_cols3, pat_cols4, pat_cols5, pat_cols6 = st.columns([2,1,2,2,4,2])

gender = pat_cols2.radio(label="gender",options=["M.","Mme."],label_visibility="hidden")
# -- NOM / PRENOM

nom_patient = pat_cols3.text_input("Nom",key="nom_pat")
prenom_patient = pat_cols4.text_input("Prenom",key="prenom_pat")
presta_choice = pat_cols5.selectbox("Prestation",["Autre","Sophro-coaching","Sophrologie","Accompagnement pédagogique et sophrologique"])

# --- PRESTATION --- 
pat1_cols1, pat1_cols2, pat1_cols3, pat1_cols4, pat1_cols5 = st.columns([2,1,6,2,2])

# Date prestation 
with pat1_cols2:
    date_presta = st.date_input("test",label_visibility="hidden")

# Réécriture date

today_day = str(today)[-2:]
today_month = str(today)[-5:-3]
today_year = str(today)[:4]

day = str(date_presta)[-2:]
month = str(date_presta)[-5:-3]
year = str(date_presta)[:4]

# Choix de prestation
with pat1_cols3:
    presta_temp = st.empty()
    presta = presta_temp.text_input('Prestation',key="presta1")
    if presta_choice=="Autre":
        presta = presta_temp.text_input('Prestation', value="", key="presta2")
    else : 
        presta = presta_temp.text_input('Prestation',value =presta_choice,key="presta3")

# Prix presta
with pat1_cols4:
    prix_temp = st.empty()
    prix = prix_temp.text_input("Prix",key="prix1")
    if presta_choice=="Autre":
        prix = prix_temp.text_input('Prix',value="",key="prix2")
    else:
        prix = prix_temp.text_input('Prix',value="60",key="prix3")


st.columns(3)[1].markdown("<p style='padding: 20; border: 2px solid white;text-align: center;font-size: 50;'> Téléchargement </p>", unsafe_allow_html=True)

# --- PDF ---

dl_col1,dl_col2,dl_col3 = st.columns([6,3,6])
file_name = dl_col2.text_input("Numero de facture :")
def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Télécharger facture n°{file_name}</a>'


if file_name != "":
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', style='B', size=15)
    pdf.cell(0,10,f"Facture n°{file_name} du {today_day}/{today_month}/{today_year}",border=1,align="C",ln=2)
    pdf.cell(0,15,ln=2)
    pdf.set_font('Arial', style='', size=10)
    pdf.cell(50,7,f" {nom_the} {prenom_the}",border="L",ln=2)
    pdf.cell(50,7," Téléphone : "+num_the,border="L",ln=2)
    pdf.cell(50,7," Mail : "+mail_the,border="L",ln=2)
    pdf.cell(50,7," Adresse : "+adresse_the,border="L",ln=2)
    pdf.cell(50,7," SIRET : "+siret_the,border="L",ln=2)

    pdf.cell(0,15,ln=2)

    pdf.cell(0,7, f"Patient : {gender} {nom_patient.upper()} {prenom_patient} ",align="R",border="R",ln=2)
    
    pdf.cell(0,15,ln=2)

    pdf.set_font('Arial', style='B', size=15)
    pdf.cell(0,7, "Prestation", align="C",ln=2)
    
    pdf.cell(0,15,ln=2)

    pdf.set_font('Arial', style='', size=10)
    pdf.cell(100,10," Intitulé",border=1,align="L")
    pdf.cell(45,10,"Date de préstation",border=1,align="C")
    pdf.cell(45,10,"Prix",border=1,align="C")
    pdf.ln()
    pdf.cell(100,10,f" {presta}",align="L",border=1)
    pdf.cell(45,10,f"{day}/{month}/{year}",align="C",border=1)
    pdf.cell(45,10,f"{str(prix)} euros",align="C",border=1)
    pdf.ln()
    pdf.cell(0,15)
    pdf.ln()
    pdf.cell(0,10,"Exonération de TVA, 1° du 4 de l'art. 261 du Code général des impôts.")
    pdf.ln()
    pdf.cell(0,10,"Facture électronique émise avec l'accord du patient")
    pdf.ln()
    pdf.cell(0,40)
    pdf.ln()
    pdf.cell(0,10,"CITRO Magali  ",align="R")
    pdf.ln()
    pdf.image("logo.png",x=155,y=240,w=40,h=40)
    html = create_download_link(pdf.output(dest="S").encode('latin-1'), f"fact_{file_name}")
    dl_col2.markdown(html, unsafe_allow_html=True)