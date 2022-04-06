# importing library
import streamlit as st
# import streamlit.components.v1 as components
# Giving a title 
st.title('Feedback Form')
# creating a form
my_form=st.form(key='form-1')
# creating input fields
fname=my_form.text_input('First Name:')
lname=my_form.text_input('Last Name:')
email=my_form.text_input('Email:')
# creating radio button 
gender=my_form.radio('Gender',('Male','Female'))
# creating slider 
age=my_form.slider('Age:',1,120)
# creating date picker
# bday=my_form.date_input('Enter Birthdate:')
# creating a text area
feedback=my_form.text_area('Enter feedback:')
# creating a submit button
submit=my_form.form_submit_button('Submit')
# the following gets updated after clicking on submit, printing the details of the fields that are submitted in the form
st.write('Name is '+fname+' '+lname)
st.write('Email is '+email)
st.write('Gender is '+gender)
st.write('Age is '+str(age))
# st.write('Birthday is '+str(bday))
st.write('Address is '+feedback)
# HtmlFile = open("test.html", 'r', encoding='utf-8')
# source_code = HtmlFile.read() 
# print(source_code)
# components.html(source_code)