import pickle
import streamlit as st
import numpy as np

def load_file():
    with open ("saved_exoplanets_pipe_only_model.pkl", "rb") as file:
        read_data = pickle.load(file)
    return read_data

data = load_file()

model = data

def predict_func():
    st.title("Exoplanets Habitability Prediction")

    s_temperature_error_max = st.text_input("Enter the value of temperature error max")
    p_distance = st.text_input("Enter the planet distance")
    p_periastron = st.text_input("Enter the planet periastron")
    p_apastron = st.text_input("Enter the planet apastron")
    p_distance_eff = st.text_input("Enter the planet distance EFF")
    p_flux = st.text_input("Enter the planet mean stellar flux (Earth units)")
    p_flux_min = st.text_input("Enter the planet minimun orbital stellar flux (earth units)")
    p_flux_max = st.text_input("Enter the planet maximum orbital stellar flux (earth units)")
    p_temp_equil = st.text_input("Enter the planet equilibrium temperature assuming bond albedo 0.3 (K)")
    s_hz_con1_max = st.text_input("Enter the stellar hz con1 max")
    s_tidal_lock = st.text_input("Enter the star tidal lock zone outer edge (AU)")
    p_habzone_opt = st.text_input("Enter the planet habitable zone opt")
    p_habzone_con = st.text_input("Enter the planet habitable zone con")

    submit = st.button("Submit")

    if submit:
        selected = np.array([[s_temperature_error_max, p_distance, p_periastron, p_apastron, p_distance_eff, p_flux, p_flux_min, 
                              p_flux_max, p_temp_equil, s_hz_con1_max, s_tidal_lock, p_habzone_opt, p_habzone_con]])
        
        selected = selected.astype(float)

        habitable_response = model.predict(selected)

        if habitable_response == 0:
            st.subheader(f"This planet is probably not habitable.")
            st.subheader(f"Habitability Index = {habitable_response}")
        elif habitable_response == 1:
            st.subheader(f"This planet have some chances to be habitable! Give him a chance.")
            st.subheader(f"Habitability Index = {habitable_response}")
        else:
            st.subheader(f"This planet have a great chances to be habitable! Give him attention.")
            st.subheader(f"Habitability Index = {habitable_response}")



# saved_exoplanets_pipe_only_model.pkl: 'S_TEMPERATURE_ERROR_MAX', 'P_DISTANCE', 'P_PERIASTRON', 'P_APASTRON', 'P_DISTANCE_EFF', 'P_FLUX', 
#  'P_FLUX_MIN', 'P_FLUX_MAX', 'P_TEMP_EQUIL', 'S_HZ_CON1_MAX', 'S_TIDAL_LOCK', 'P_HABZONE_OPT', 'P_HABZONE_CON'