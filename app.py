from transformers import pipeline 
import streamlit as st
from PIL import Image 

#tab name and favicon
st.set_page_config(page_title='Text Summarizer', page_icon='📖', layout='centered')

#import pipeline
summarizer=pipeline('summarization')



st.write("""
# Text Summarizer  
Using Hugging Face Transformers 🤗
""")

with st.form(key='my_form'):

    input=st.text_area('Enter your Text',height=300)

    left_column, right_column=st.columns(2)

    min=left_column.number_input('Minimum words',value=30)
    max=right_column.number_input('Maximum words',value=130)

    summarize=st.form_submit_button('Summarize!')


if summarize:
    summary=summarizer(input,max_length=max, min_length=min, do_sample=False)
    st.subheader('Result 🎉')
    st.info(summary[0]['summary_text'])
    st.write('**Length:** '+str(len(summary[0]['summary_text'].split(' ')))+' words')




