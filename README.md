# 🎙️ Speech-to-Text with Speaker Diarization and Sentiment Analysis 🎙️

## Here is the link to use this application hosted on Streamlit Cloud Community
https://speech-to-text-analysis-5lj8qzwt925q4qdfo48yxi.streamlit.app/

# Speech-To-Text Project

This repository contains a Speech-to-Text application that converts spoken words into text using machine learning techniques and cutting-edge NLP models. The project aims to provide a flexible and efficient solution for transforming audio files or real-time speech into text, making it suitable for a wide range of applications such as transcription services, accessibility tools, and voice-controlled interfaces.

## Features

- **High Accuracy Speech Recognition**: Utilizes state-of-the-art deep learning models to achieve high accuracy in speech recognition.
- **Support for Multiple Languages**: Capable of recognizing speech in different languages.
- **Customizable Vocabulary**: Fine-tune the model to recognize specific domain-specific words or phrases.
- **Real-time and Batch Processing**: Supports both real-time speech recognition and batch processing of audio files.
- **Noise Handling**: Pre-processing and noise reduction methods to handle noisy environments.

## Web Interface Overview

The application includes a user-friendly web interface that allows users to easily interact with the Speech-to-Text functionality. Below is an overview of the main pages and what they do:

### 1. Audio File Transcription Page

Here users can upload audio files (WAV or MP3 format) for transcription with additional features such as speaker diarization and sentiment analysis.

- **Screenshot**:
  ![image](https://github.com/user-attachments/assets/8e7d9e21-5f51-4c16-934c-fe5642449551)

- **Description**: Users can upload an audio file, and once successfully uploaded, they can view the transcript with each speaker clearly identified. Different speakers are labeled, and a script is generated where each new voice is distinguished accordingly. The transcription result, along with speaker diarization and sentiment analysis, is displayed on the page.

  - **Speech-to-Text Output**: The transcribed text is shown, with different speakers labeled if multiple voices are detected.
  - **Sentiment Analysis**: Displays the sentiment (e.g., positive, negative, neutral) for each speaker's segment to give a deeper understanding of the conversation.

![image](https://github.com/user-attachments/assets/a5ca2ffc-5163-4316-b81b-5b38dfaa0829)

![image](https://github.com/user-attachments/assets/6085f876-fc3a-44be-970e-ba15b96f5bc9)

![image](https://github.com/user-attachments/assets/842671c9-a3aa-4b9f-8f7a-498bead065f4)


## Installation

To get started, clone the repository and install the required dependencies:

```sh
# Clone the repository
git clone https://github.com/YourUsername/Speech-To-Text-Project.git
cd Speech-To-Text-Project

# Create and activate a virtual environment (recommended)
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Usage

### 1. Running the Web Interface

To start the web interface for the Speech-to-Text application, run the following command:

```sh
streamlit run app.py
```

Once the server is running, open your web browser and navigate to `http://127.0.0.1:5000/` to access the interface.

### 2. Running the Application via Command Line

To run the speech-to-text model on an audio file:

```sh
python transcribe.py --audio_path "path/to/audio/file.wav"
```

## Directory Structure

```
Speech-To-Text-Project/
|
|-- data/                  # Sample audio files for testing
|-- models/                # Pre-trained models and checkpoints
|-- scripts/               # Utility scripts for processing
|-- screenshots/           # Screenshots of the web interface
|-- transcribe.py          # Main script to convert audio to text
|-- real_time_transcription.py # Script for real-time transcription
|-- app.py                 # Script to run the web interface
|-- requirements.txt       # Python dependencies
|-- README.md              # Project documentation (this file)
```

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`
- Compatible microphone for real-time speech recognition

## Examples

1. **Transcribing an Audio File**

   ```sh
   python transcribe.py --audio_path "./data/sample.wav"
   ```

   Output:
   ```
   Transcription: "This is a sample speech converted to text."
   ```

## Troubleshooting

- Ensure that your audio files are in a supported format (e.g., WAV).
- If you face low accuracy, try fine-tuning the vocabulary or using a higher quality audio input.
- For real-time speech recognition, make sure that your microphone is properly configured.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## Acknowledgements

- The core model is built using [OpenAI's Whisper](https://github.com/openai/whisper).
- Thanks to https://github.com/m-bain/whisperX for inspiration.

## Contact

For questions or suggestions, feel free to contact Rujul Khatavkar rujulsk@gmail.com.

---

Happy Coding!
