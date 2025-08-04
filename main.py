import numpy as np
import pickle
import streamlit as st
from PIL import Image

# Load the model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# Function for prediction
def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

# Main function for the app
def main():
    # Load and display the icon image
    icon = Image.open('icon124.png') 
    st.sidebar.image(icon, width=260)

    # Set the app title and description
    st.title('WELCOME TO SUGARSENSE')
    st.write("""
        ## Introduction
        This application predicts whether a person has diabetes based on medical parameters.
        Please enter the details in the sidebar, and click on 'Diabetes Test Result' to see the prediction.
    """)

    # Sidebar for input details
    st.sidebar.header('Input Details')
    st.sidebar.write("Provide the following information:")

    Pregnancies = st.sidebar.number_input('Number of Pregnancies', help="Number of times the patient has been pregnant.")
    Glucose = st.sidebar.number_input('Glucose Level', help="Blood glucose concentration (mg/dL).")
    BloodPressure = st.sidebar.number_input('Blood Pressure value', help="Diastolic blood pressure (mm Hg).")
    SkinThickness = st.sidebar.number_input('Skin Thickness value', help="Triceps skinfold thickness (mm).")
    Insulin = st.sidebar.number_input('Insulin Level', help="2-Hour serum insulin (mu U/ml).")
    BMI = st.sidebar.number_input('BMI value', help="Body Mass Index (weight in kg/(height in m)^2).")
    DiabetesPedigreeFunction = st.sidebar.number_input('Diabetes Pedigree Function', help="Function that scores likelihood of diabetes based on family history.")
    Age = st.sidebar.number_input('Age of the Person', help="Age in years.")

    # Prediction
    diagnosis = ''
    if st.button('Diabetes Test Result'):
        input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        diagnosis = diabetes_prediction(input_data)

    st.success(diagnosis)

    # Description of the parameters
    st.write("""
        ## About the Parameters
        - **Pregnancies:** Number of pregnancies the patient has had.
        - **Glucose:** Plasma glucose concentration a 2 hours in an oral glucose tolerance test.
        - **Blood Pressure:** Diastolic blood pressure.
        - **Skin Thickness:** Thickness of the skin fold on the triceps muscle.
        - **Insulin:** 2-hour serum insulin concentration.
        - **BMI:** Body Mass Index.
        - **Diabetes Pedigree Function:** Diabetes risk based on family history.
        - **Age:** Age in years.
    """)

    # Educational section about diabetes
    st.write("""
        ## Understanding Diabetes
        Diabetes is a chronic health condition that affects how your body turns food into energy. When you eat, your body breaks down carbohydrates into glucose (sugar), which enters your bloodstream. In response, the pancreas releases insulin, a hormone that helps glucose enter your cells to be used for energy. With diabetes, this process doesn’t work correctly, leading to high levels of glucose in the blood.

        ### Types of Diabetes
        - **Type 1 Diabetes:** An autoimmune condition where the body attacks insulin-producing cells in the pancreas. People with Type 1 diabetes must take insulin injections to survive. It’s typically diagnosed in children and young adults.
        - **Type 2 Diabetes:** The most common form, occurring when the body becomes resistant to insulin or doesn’t produce enough. Type 2 diabetes is often linked to lifestyle factors like poor diet, inactivity, and obesity, but genetics can also play a role. It can often be managed with diet, exercise, and medication.
    """)

    # Symptoms of Diabetes
    st.write("""
        ## Symptoms of Diabetes
        Common symptoms of diabetes include:
        - Increased thirst and frequent urination
        - Unexplained weight loss
        - Fatigue and irritability
        - Blurred vision
        - Slow-healing sores or frequent infections
    """)

# Run the app
if __name__ == '__main__':
    main()
