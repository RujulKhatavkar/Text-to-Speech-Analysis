from audio_to_text import AudioTranscription 
from sentiment_analysis import SentimentAnalysis
from speaker_identification import SpeakerNameMapper

def process_audio(audio_file_path):
    transcriber = AudioTranscription()
    result = transcriber.transcribe_audio(audio_file_path)
    df = transcriber.convert_to_df(result)
    analyzer = SentimentAnalysis(df)
    analyzer.add_sentiment_analysis()
    analyzer.add_sentiment_category()
    df = analyzer.save_to_csv('user_sentiment.csv')
    mapper = SpeakerNameMapper(df)
    final_df = mapper.map_speakers()
    return final_df

if __name__ == "__main__":
    audio_file_path = "/Users/rujul/Documents/Projects/Speech-To-Text-Project/Speech-To-Text-Project-main/audio_file/AI Advancement.wav"
    process_audio(audio_file_path)
