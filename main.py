from pydub import AudioSegment
import speech_recognition as sr
import pandas as pd
import numpy as np


def calculate_pitch(audio):
    dominant_frequency = audio.dBFS
    return dominant_frequency


def calculate_loudness(audio):
    loudness = audio.dBFS
    return loudness


def recognize_emotion(pitch, loudness):
    if pitch > 0 and loudness < -20:
        return "Happy"
    elif pitch < 0 and loudness < -25:
        return "Sad"
    else:
        return "Neutral"


def predict_speech_volume(loudness):
    # Simple threshold for loudness
    if loudness > -15:
        return "Loud"
    else:
        return "Soft"


# Record audio using the SpeechRecognition library
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Please speak something...")
    audio_data = recognizer.listen(source)

# Convert audio data to AudioSegment
audio_data = AudioSegment(
    data=audio_data.frame_data,
    sample_width=audio_data.sample_width,
    frame_rate=audio_data.sample_rate,
    channels=1  # Set channels to 1 for mono audio
)

# Calculate pitch and loudness
pitch = calculate_pitch(audio_data)
loudness = calculate_loudness(audio_data)

# Recognize emotion
emotion = recognize_emotion(pitch, loudness)

# Predict speech volume
speech_volume = predict_speech_volume(loudness)

print(f'Pitch: {pitch} Hz')
print(f'Loudness: {loudness} dBFS')
print(f'Emotion: {emotion}')
print(f'Speech Volume: {speech_volume}')

data = {'Pitch': [pitch], 'Loudness': [loudness],
        'Emotion': [emotion], 'Speech Volume': [speech_volume]}
df = pd.DataFrame(data)

df['Pitch'] = df['Pitch'].apply(np.sqrt)
df['Loudness'] = df['Loudness'].apply(np.sqrt)
df['Emotion'] = df['Emotion'].apply(np.sqrt)
df['Speech Volume'] = df['Speech Volume'].apply(np.sqrt)

def calculate_energy(audio):
    energy = sum(abs(audio.get_array_of_samples())) / len(audio.get_array_of_samples())
    return energy

def calculate_duration(audio):
    duration = len(audio) / 1000
    return duration

def recognize_language(audio):
    recognizer = sr.Recognizer()
    language = 'Unknown'
    try:
        language = recognizer.recognize_google(audio, language='en-US')
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return language

def recognize_speaker(audio):
    recognizer = sr.Recognizer()
    speaker = 'Unknown'
    try:
        speaker = recognizer.recognize_google(audio, show_all=True)['alternative'][0]['transcript']
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return speaker

def recognize_text(audio):
    recognizer = sr.Recognizer()
    text = 'Unknown'
    try:
        text = recognizer.recognize_google(audio, show_all=True)['alternative'][0]['transcript']
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return text

def recognize_speech(audio):
    recognizer = sr.Recognizer()
    speech = 'Unknown'
    try:
        speech = recognizer.recognize_google(audio, show_all=True)['alternative'][0]['transcript']
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return speech

energy = calculate_energy(audio_data)
duration = calculate_duration(audio_data)
language = recognize_language(audio_data)
speaker = recognize_speaker(audio_data)
text = recognize_text(audio_data)
speech = recognize_speech(audio_data)

print(f'Energy: {energy}')
print(f'Duration: {duration}')
print(f'Language: {language}')
print(f'Speaker: {speaker}')
print(f'Text: {text}')
print(f'Speech: {speech}')

