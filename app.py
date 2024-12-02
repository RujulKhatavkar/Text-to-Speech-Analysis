import streamlit as st
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from main import process_audio
from feedback_generation import ConversationReviewer

img_path = "uploaded_files/ff620854b85ca2824e8e3b6b3e5d079e.gif"

# Set up page configuration
st.set_page_config(page_title="Speech To Text Analysis", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    .stApp {
        background-color: black;
        color: white;
    }
    h1,h2 {
        color: lightgrey; /* Title text color */
    }
    .css-18e3th9 {
        background-color: black; /* Main background for Streamlit container */
    }
    [data-testid='stWidgetLabel'] {
        color:aqua;
    }
    .css-1d391kg {
        background-color: #2b2d2f /* Dark grey background for sidebar */
    }
    .css-hxt7ib {
        color: white; /* Text color for sidebar */
    }
    </style>
    """,
    unsafe_allow_html=True
)

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join("uploaded_files", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        return os.path.join("uploaded_files", uploaded_file.name)
    except Exception as e:
        st.error(f"Error saving file: {e}")
        return None

def get_conversation(df):
    conversation = ""
    for index, row in df.iterrows():
        conversation += f"{row['speaker']}: {row['text']} "
    return conversation

def display_data(df):
    # Display the dataframe with specified columns
    st.write("Speech to Text Results with Speaker Identification")

    transcript = ""
    previous_speaker = None
    combined_text = ""

    for _, row in df.iterrows():
        if row['speaker'] == previous_speaker:
            # Continue the same speaker's conversation
            combined_text += f" {row['text']}"
        else:
            # Append the previous speaker's complete text to the transcript
            if previous_speaker is not None:
                transcript += f"**{previous_speaker} [{start_time} - {end_time}]:** {combined_text}\n\n"
            
            # Update speaker and text details for the new segment
            previous_speaker = row['speaker']
            combined_text = row['text']
            start_time = row['start']
        
        # Always update the end time for each row
        end_time = row['end']
    
    # Add the last speaker's text to the transcript
    if previous_speaker is not None:
        transcript += f"**{previous_speaker} [{start_time} - {end_time}]:** {combined_text}\n\n"
    # Display the generated transcript
    st.write("Transcript")
    st.markdown(transcript)

    # Check if sentiment_category column is present and display it
    if 'sentiment_category' in df.columns:
        st.write("Sentiment Analysis Results")
        st.dataframe(df[['speaker', 'text', 'sentiment_category']])
    else:
        st.error("Column 'sentiment_category' not found in the data.")


    st.write("Sentiment Category by Speaker")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(data=df, x='speaker', hue='sentiment_category', ax=ax)
    st.pyplot(fig)

    # Analyze conversation
    conversation_reviewer = ConversationReviewer()
    conversation = get_conversation(df)
    review_output = conversation_reviewer.review_conversation(conversation)

    st.write("Conversation Review")
    st.write(review_output)
col1, col2 = st.columns([2, 3])
with col1:
    st.image(img_path)
    
with col2:
    st.markdown("""<div style=" padding-top : 100px">
        <h2>Get insights into your conversations quickly and easily.</h2>
    </div>""", unsafe_allow_html=True)

    
# File Uploader and Processing Section
st.write("## Upload Your Audio File")
uploaded_file = st.file_uploader("Select an audio file (wav, mp3)", type=["wav", "mp3"], label_visibility='visible')


if uploaded_file is not None:
    file_path = save_uploaded_file(uploaded_file)
    if file_path:
        st.success("File uploaded successfully!")
        df = process_audio(file_path)

        # Display Results Section
        st.write("## Analysis Results")
        display_data(df)
else:
    st.info("Please upload an audio file to proceed with the analysis.")
    
# Title and Image


st.write("""
    This application allows you to upload an audio file, transcribe it, and analyze the sentiment of each speaker. 
    Get insights into your conversations quickly and easily.
    """)








