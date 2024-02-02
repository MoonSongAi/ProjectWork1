from google.cloud import speech
# from google.cloud.speech import enums
# from google.cloud.speech import types
import io

def transcribe_file(speech_file):
    """Transcribes the given audio file."""
    client = speech.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,  # WAV 파일의 실제 샘플 레이트로 수정
        language_code="ko-KR"  # 한국어로 설정
        )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
        print("="*40)

def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,  # WAV 파일의 실제 샘플 레이트로 수정
        language_code="ko-KR"    # 한국어로 설정
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))


transcribe_file(r"C:\ProjectWork1\WorkRoot\tests\yoon_test\변환파일\mono1.wav")
#transcribe_file(r"C:\ProjectWork1\WorkRoot\tests\yoon_test\변환파일\소음테스트2_voice.wav")

# Google Cloud Storage의 오디오 파일 URI 예시: "gs://your-bucket-name/your-audio-file.wav"
#transcribe_gcs(r"C:\ProjectWork1\WorkRoot\tests\yoon_test\변환파일\mono1.wav")
