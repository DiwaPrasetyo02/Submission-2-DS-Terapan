import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('best_model_employee.pkl')

# Define the input features
input_features = [
    'Marital_status', 'Application_mode', 'Application_order', 'Course',
    'Daytime_evening_attendance', 'Previous_qualification', 
    'Previous_qualification_grade', 'Nacionality', 'Mothers_qualification', 
    'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation', 
    'Admission_grade', 'Displaced', 'Educational_special_needs', 'Debtor', 
    'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder', 
    'Age_at_enrollment', 'International', 'Curricular_units_1st_sem_credited', 
    'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_evaluations', 
    'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade', 
    'Curricular_units_1st_sem_without_evaluations', 'Curricular_units_2nd_sem_credited', 
    'Curricular_units_2nd_sem_enrolled', 'Curricular_units_2nd_sem_evaluations', 
    'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade', 
    'Curricular_units_2nd_sem_without_evaluations', 'Unemployment_rate', 
    'Inflation_rate', 'GDP'
]

# Dictionaries for alias
marital_status = {1: 'single', 2: 'married', 3: 'widower', 4: 'divorced', 5: 'facto union', 6: 'legally separated'}
application_mode = {
    1: '1st phase - general contingent', 2: 'Ordinance No. 612/93', 5: '1st phase - special contingent (Azores Island)', 
    7: 'Holders of other higher courses', 10: 'Ordinance No. 854-B/99', 15: 'International student (bachelor)', 
    16: '1st phase - special contingent (Madeira Island)', 17: '2nd phase - general contingent', 
    18: '3rd phase - general contingent', 26: 'Ordinance No. 533-A/99, item b2) (Different Plan)', 
    27: 'Ordinance No. 533-A/99, item b3 (Other Institution)', 39: 'Over 23 years old', 42: 'Transfer', 
    43: 'Change of course', 44: 'Technological specialization diploma holders', 51: 'Change of institution/course', 
    53: 'Short cycle diploma holders', 57: 'Change of institution/course (International)'
}
course = {
    33: 'Biofuel Production Technologies', 171: 'Animation and Multimedia Design', 8014: 'Social Service (evening attendance)', 
    9003: 'Agronomy', 9070: 'Communication Design', 9085: 'Veterinary Nursing', 9119: 'Informatics Engineering', 
    9130: 'Equinculture', 9147: 'Management', 9238: 'Social Service', 9254: 'Tourism', 9500: 'Nursing', 9556: 'Oral Hygiene', 
    9670: 'Advertising and Marketing Management', 9773: 'Journalism and Communication', 9853: 'Basic Education', 
    9991: 'Management (evening attendance)'
}
yes_no = {1: 'yes', 0: 'no'}
gender = {1: 'male', 0: 'female'}

# Streamlit app
st.title('Student Dropout Prediction')

st.sidebar.header('Input Features')

def user_input_features():
    data = {}
    data['Marital_status'] = st.sidebar.selectbox('Marital status', list(marital_status.keys()), format_func=lambda x: marital_status[x])
    data['Application_mode'] = st.sidebar.selectbox('Application mode', list(application_mode.keys()), format_func=lambda x: application_mode[x])
    data['Application_order'] = st.sidebar.number_input('Application order', value=0, min_value=0, max_value=9)
    data['Course'] = st.sidebar.selectbox('Course', list(course.keys()), format_func=lambda x: course[x])
    data['Daytime_evening_attendance'] = st.sidebar.selectbox('Daytime/evening attendance', list(yes_no.keys()), format_func=lambda x: yes_no[x])
    data['Previous_qualification'] = st.sidebar.selectbox('Previous qualification', [1, 2, 3, 4, 5, 6, 9, 10, 12, 14, 15, 19, 38, 39, 40, 42, 43])
    data['Previous_qualification_grade'] = st.sidebar.number_input('Previous qualification grade', value=0, min_value=0, max_value=200)
    data['Nacionality'] = st.sidebar.selectbox('Nacionality', [1, 2, 6, 11, 13, 14, 17, 21, 22, 24, 25, 26, 32, 41, 62, 100, 101, 103, 105, 108, 109])
    data['Mothers_qualification'] = st.sidebar.selectbox('Mother\'s qualification', [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 14, 18, 19, 22, 26, 27, 29, 30, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44])
    data['Fathers_qualification'] = st.sidebar.selectbox('Father\'s qualification', [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 18, 19, 20, 22, 25, 26, 27, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44])
    data['Mothers_occupation'] = st.sidebar.selectbox('Mother\'s occupation', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 90, 99, 122, 123, 125, 131, 132, 134, 141, 143, 144, 151, 152, 153, 171, 173, 175, 191, 192, 193, 194])
    data['Fathers_occupation'] = st.sidebar.selectbox('Father\'s occupation', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 90, 99, 101, 102, 103, 112, 114, 121, 122, 123, 124, 131, 132, 134, 135, 141, 143, 144, 151, 152, 153, 154, 161, 163, 171, 172, 174, 175, 181, 182, 183, 192, 193, 194, 195])
    data['Admission_grade'] = st.sidebar.number_input('Admission grade', value=0, min_value=0, max_value=200)
    data['Displaced'] = st.sidebar.selectbox('Displaced', list(yes_no.keys()), format_func=lambda x: yes_no[x])
    data['Educational_special_needs'] = st.sidebar.selectbox('Educational special needs', list(yes_no.keys()), format_func=lambda x: yes_no[x])
    data['Debtor'] = st.sidebar.selectbox('Debtor', list(yes_no.keys()), format_func=lambda x: yes_no[x])
    data['Tuition_fees_up_to_date'] = st.sidebar.selectbox('Tuition fees up to date', list(yes_no.keys()), format_func=lambda x: yes_no[x])
    data['Gender'] = st.sidebar.selectbox('Gender', list(gender.keys()), format_func=lambda x: gender[x])
    data['Scholarship_holder'] = st.sidebar.selectbox('Scholarship holder', list(yes_no.keys()), format_func=lambda x: yes_no[x])
    data['Age_at_enrollment'] = st.sidebar.number_input('Age at enrollment', value=18, min_value=18, max_value=100)
    data['International'] = st.sidebar.selectbox('International', list(yes_no.keys()), format_func=lambda x: yes_no[x])
    data['Curricular_units_1st_sem_credited'] = st.sidebar.number_input('Curricular units 1st sem (credited)', value=0, min_value=0)
    data['Curricular_units_1st_sem_enrolled'] = st.sidebar.number_input('Curricular units 1st sem (enrolled)', value=0, min_value=0)
    data['Curricular_units_1st_sem_evaluations'] = st.sidebar.number_input('Curricular units 1st sem (evaluations)', value=0, min_value=0)
    data['Curricular_units_1st_sem_approved'] = st.sidebar.number_input('Curricular units 1st sem (approved)', value=0, min_value=0)
    data['Curricular_units_1st_sem_grade'] = st.sidebar.number_input('Curricular units 1st sem (grade)', value=0, min_value=0, max_value=20)
    data['Curricular_units_1st_sem_without_evaluations'] = st.sidebar.number_input('Curricular units 1st sem (without evaluations)', value=0, min_value=0)
    data['Curricular_units_2nd_sem_credited'] = st.sidebar.number_input('Curricular units 2nd sem (credited)', value=0, min_value=0)
    data['Curricular_units_2nd_sem_enrolled'] = st.sidebar.number_input('Curricular units 2nd sem (enrolled)', value=0, min_value=0)
    data['Curricular_units_2nd_sem_evaluations'] = st.sidebar.number_input('Curricular units 2nd sem (evaluations)', value=0, min_value=0)
    data['Curricular_units_2nd_sem_approved'] = st.sidebar.number_input('Curricular units 2nd sem (approved)', value=0, min_value=0)
    data['Curricular_units_2nd_sem_grade'] = st.sidebar.number_input('Curricular units 2nd sem (grade)', value=0, min_value=0, max_value=20)
    data['Curricular_units_2nd_sem_without_evaluations'] = st.sidebar.number_input('Curricular units 2nd sem (without evaluations)', value=0, min_value=0)
    data['Unemployment_rate'] = st.sidebar.number_input('Unemployment rate', value=0.0, min_value=0.0)
    data['Inflation_rate'] = st.sidebar.number_input('Inflation rate', value=0.0, min_value=0.0)
    data['GDP'] = st.sidebar.number_input('GDP', value=0.0, min_value=0.0)
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Predict using the model
prediction_proba = model.predict_proba(df)

st.subheader('Prediction')
if prediction_proba[0][0] > prediction_proba[0][1]:
    student_status = 'Dropout'
else:
    student_status = 'Graduate'

st.write(f'Student status: {student_status} (0 = Dropout, 1 = Graduate)')

st.subheader('Prediction Probability')
st.write(prediction_proba)
