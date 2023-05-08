import streamlit as st

import numpy as np

from streamlit_option_menu import option_menu

#welcome
with st.sidebar :
    
    from PIL import Image
    
    image = Image.open("MASBRO.jpg")
    
    st.image(image, caption="")
    
    selected = option_menu("Aplikasi Analisis Kuantitatif Gravimetri",
    ["Identitas Kelompok",
     "Perhitungan Kadar Air Sampel",
     "Perhitungan Kadar Abu",
     "Kalkulator Faktor Gravimetri"],
    default_index=0)
    
if (selected == "Identitas Kelompok") :
    st.title("Identitas Anggota Kelompok")
    
    st.write ('''Daftar Anggota \n
    Alma Lubna Kamilia (2219032) \n
    Diyana Iffah (2219065)\n
    Lathifah Hasna (2219096)\n
    Luthfi Muhammad Fikri (2219101)\n
    Muh. Irham Asya'bani (2219110)
    ''')
    
                        
if (selected == "Perhitungan Kadar Air Sampel") :
    st.title("Perhitungan mencari Kadar Air Sampel")

    st.write("Perhitungan Kadar Air Sampel") 

    massa_sebelum = st.number_input('Masukkan massa bahan sebelum dioven (g) :', format='%.4f')
    massa_setelah = st.number_input('Masukkan massa bahan setelah dioven (g) :', format='%.4f')
    massa_sampel = st.number_input('Masukkan massa sampel (g);',format='%.4f')

    if st.button('Hitung') :
         kadar_air = (massa_sebelum - massa_setelah) / (massa_sampel* 100)
         st.success(f'Hasil kadar air adalah {kadar_air}')
         st.balloons()
        
    
if (selected == "Perhitungan Kadar Abu") :
    st.title ("Aplikasi Menghitung Kadar Abu")

    massa_sebelum = st.number_input('Masukkan massa bahan sebelum dibakar (g) :', format='%.4f')
    massa_setelah = st.number_input('Masukkan massa abu setelah dibakar (g) :', format='%.4f')
    massa_sampel  = st.number_input ('Masukkan massa sampel (g) :',format='%.4f') 
                                     
    if st.button('Hitung') :
        kadar_abu = (massa_sebelum - massa_setelah) / (massa_sampel * 100)
        st.success(f'Hasil kadar abu adalah {kadar_abu}')
        
        st.balloons()
        
if (selected == "Kalkulator Faktor Gravimetri") :
    st.title("Kalkulator Faktor Gravimetri")

    berat = st.number_input('Masukkan berat sampel dalam gram (g)', value=0.0)
    volume = st.number_input('Masukkan volume pelarut dalam mililiter (mL)', value=0.0)
    densitas = st.number_input('Masukkan densitas pelarut dalam g/mL', value=0.0)

    if st.button ('Hitung') :
        faktor_gravimetri =  berat / (volume * densitas)
        st.success(f'Hasil Faktor Gravimetri adalah {faktor_gravimetri}')
        
        st.balloons()

