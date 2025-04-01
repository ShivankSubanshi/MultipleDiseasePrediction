# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 19:45:37 2025

@author: shiva
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabetes_model = pickle.load(open("saved_models/diabetes_model.sav", "rb"))
heart_model = pickle.load(open("saved_models/heart_disease_model.sav","rb"))
parkinson_model = pickle.load(open("saved_models/parkinson_model.sav","rb"))

#creating the sidebar for options menu
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction Menu',['Diabetes Prediction','Heart Disease Prediction','Parkinson Disease'],icons=['activity','heart','person'],default_index=0)
    
#Diabetes Prediction Page
if(selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    #getting the input data from the user
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness Level')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree function')
    
    with col2:
        Age = st.text_input('Age of the Person')
        
    #code for the prediction
    diab_diagnosis = ''
# =============================================================================
#     Pregnancies = st.text_input('Number of Pregnancies')
#     Glucose = st.text_input('Glucose Level')
#     BloodPressure = st.text_input('Blood Pressure value')
#     SkinThickness = st.text_input('Skin Thickness Level')
#     Insulin = st.text_input('Insulin Level')
#     BMI = st.text_input('BMI value')
#     DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree function')
#     Age = st.text_input('Age of the Person')
      
# =============================================================================
    
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        try:
            input_data = [[
                int(Pregnancies) if Pregnancies else 0,
                float(Glucose) if Glucose else 0,
                float(BloodPressure) if BloodPressure else 0,
                float(SkinThickness) if SkinThickness else 0,
                float(Insulin) if Insulin else 0,
                float(BMI) if BMI else 0,
                float(DiabetesPedigreeFunction) if DiabetesPedigreeFunction else 0,
                int(Age) if Age else 0
                ]]
            
            diab_prediction = diabetes_model.predict(input_data)
            
            if diab_prediction[0] == 0:
                diab_diagnosis = 'The person is not diabetic'
            else:
                diab_diagnosis = 'The Person is diabetic'
                
                    
            st.success(diab_diagnosis)
                    
        except ValueError:
            st.error("Please enter valid numeric values in all fields.")

    
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Input fields for heart disease prediction
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        trestbps = st.text_input('Resting Blood Pressure (mm Hg)')
        restecg = st.text_input('Resting ECG Results (0, 1, 2)')
        oldpeak = st.text_input('ST Depression Induced by Exercise')

    with col2:
        sex = st.text_input('Sex (1 = Male, 0 = Female)')
        chol = st.text_input('Serum Cholesterol (mg/dl)')
        thalach = st.text_input('Maximum Heart Rate Achieved')
        slope = st.text_input('Slope of Peak Exercise ST Segment')

    with col3:
        cp = st.text_input('Chest Pain Type (0, 1, 2, 3)')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = Yes, 0 = No)')
        exang = st.text_input('Exercise Induced Angina (1 = Yes, 0 = No)')
        ca = st.text_input('Number of Major Vessels (0-3)')

    thal = st.text_input('Thalassemia (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            input_data = [[
                int(age) if age else 0,
                int(sex) if sex else 0,
                int(cp) if cp else 0,
                float(trestbps) if trestbps else 0,
                float(chol) if chol else 0,
                int(fbs) if fbs else 0,
                int(restecg) if restecg else 0,
                float(thalach) if thalach else 0,
                int(exang) if exang else 0,
                float(oldpeak) if oldpeak else 0,
                int(slope) if slope else 0,
                int(ca) if ca else 0,
                int(thal) if thal else 0
            ]]

            heart_prediction = heart_model.predict(input_data)

            if heart_prediction[0] == 0:
                heart_diagnosis = 'The person is not at risk of heart disease'
            else:
                heart_diagnosis = 'The Person is at risk of heart disease'

            st.success(heart_diagnosis)

        except ValueError:
            st.error("Please enter valid numeric values in all fields.")
    
#Parkinson's prediction Page
if selected == 'Parkinson Disease':
    st.title("Parkinson's Disease Prediction using ML")

    # Input fields for Parkinson's prediction
    col1, col2, col3, col4, col5 = st.columns(5)  

    with col1:
        fo = st.text_input('MDVP:Fo(Hz) - Average vocal fundamental frequency')
        fhi = st.text_input('MDVP:Fhi(Hz) - Maximum vocal fundamental frequency')
        flo = st.text_input('MDVP:Flo(Hz) - Minimum vocal fundamental frequency')

    with col2:
        jitter_percent = st.text_input('MDVP:Jitter(%) - Measures of variation in fundamental frequency')
        jitter_abs = st.text_input('MDVP:Jitter(Abs) - Absolute jitter')
        rap = st.text_input('MDVP:RAP - Relative amplitude perturbation')

    with col3:
        ppq = st.text_input('MDVP:PPQ - Five-point period perturbation quotient')
        ddp = st.text_input('Jitter:DDP - Average absolute difference of differences between jitter cycles')
        shimmer = st.text_input('MDVP:Shimmer - Measures of variation in amplitude')

    with col4:
        shimmer_db = st.text_input('MDVP:Shimmer(dB) - Shimmer in decibels')
        apq3 = st.text_input('Shimmer:APQ3 - Three-point amplitude perturbation quotient')
        apq5 = st.text_input('Shimmer:APQ5 - Five-point amplitude perturbation quotient')

    with col5:
        apq = st.text_input('MDVP:APQ - Amplitude perturbation quotient')
        dda = st.text_input('Shimmer:DDA - Average absolute difference between consecutive differences')
        nhr = st.text_input('NHR - Noise-to-harmonics ratio')

    # Second row of inputs
    col1, col2, col3, col4, col5 = st.columns(5)  

    with col1:
        hnr = st.text_input('HNR - Harmonics-to-noise ratio')
    with col2:
        rpde = st.text_input('RPDE - Nonlinear dynamical complexity measure')
    with col3:
        dfa = st.text_input('DFA - Signal fractal scaling exponent')
    with col4:
        spread1 = st.text_input('spread1 - Nonlinear measure of fundamental frequency variation')
    with col5:
        spread2 = st.text_input('spread2 - Nonlinear measure of fundamental frequency variation')

    # Third row of inputs
    col1, col2, col3 = st.columns(3)  
    with col1:
        d2 = st.text_input('D2 - Correlation dimension')
    with col2:
        ppe = st.text_input('PPE - Pitch period entropy')

    parkinsons_diagnosis = ''

    if st.button("Parkinson's Test Result"):
        try:
            input_data = [[
                float(fo) if fo else 0,
                float(fhi) if fhi else 0,
                float(flo) if flo else 0,
                float(jitter_percent) if jitter_percent else 0,
                float(jitter_abs) if jitter_abs else 0,
                float(rap) if rap else 0,
                float(ppq) if ppq else 0,
                float(ddp) if ddp else 0,
                float(shimmer) if shimmer else 0,
                float(shimmer_db) if shimmer_db else 0,
                float(apq3) if apq3 else 0,
                float(apq5) if apq5 else 0,
                float(apq) if apq else 0,
                float(dda) if dda else 0,
                float(nhr) if nhr else 0,
                float(hnr) if hnr else 0,
                float(rpde) if rpde else 0,
                float(dfa) if dfa else 0,
                float(spread1) if spread1 else 0,
                float(spread2) if spread2 else 0,
                float(d2) if d2 else 0,
                float(ppe) if ppe else 0
            ]]

            parkinsons_prediction = parkinson_model.predict(input_data)

            if parkinsons_prediction[0] == 0:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person has Parkinson's disease"

            st.success(parkinsons_diagnosis)

        except ValueError:
            st.error("Please enter valid numeric values in all fields.")

# Add footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 10px;
        width: 100%;
        text-align: center;
        font-size: 14px;
        color: gray;
        left: 50%;
        transform: translateX(-50%);
    }
    </style>
    <div class="footer">Developed by <b>Shivank Subanshi</b></div>
    """,
    unsafe_allow_html=True
)   


