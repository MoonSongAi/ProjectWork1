import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Korean language code
language_code = "ko-KR"

# Transcribe the audio file
# with sr.AudioFile(r"C:\ProjectWork1\WorkRoot\tests\yoon_test\변환파일\mono2.wav") as source:
with sr.AudioFile(r"C:\ProjectWork1\WorkRoot\tests\yoon_test\원본파일\녹취파일2.wav") as source:
# with sr.AudioFile(r"C:\ProjectWork1\WorkRoot\tests\yoon_test\원본파일\소음테스트2.wav") as source:
# with sr.AudioFile(r"C:\ProjectWork1\WorkRoot\tests\오디오변환\녹취파일1.m4a") as source:
    audio_data = r.record(source)
    try:
        # Recognizing the speech in the audio file
        text = r.recognize_google(audio_data, language=language_code)
    except sr.UnknownValueError:
        # If the speech is unintelligible
        text = "음성을 인식할 수 없습니다."
    except sr.RequestError:
        # If there's a problem with the request
        text = "요청 중 오류가 발생했습니다."

print(text)
