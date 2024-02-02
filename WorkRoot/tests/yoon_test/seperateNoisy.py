import librosa
import numpy as np
import soundfile as sf

def separate_audio(audio_path, voice_output_path, noise_output_path, background_output_path, thresholds=(0.05, 0.1)):
    # Load audio file
    y, sr = librosa.load(audio_path, sr=None)

    # Perform STFT
    stft = librosa.stft(y)

    # Extract magnitude and phase of the spectrogram
    magnitude, phase = librosa.magphase(stft)

    # Calculate threshold values for voice, noise, and background
    threshold_voice = np.max(magnitude) * thresholds[0]
    threshold_noise = np.max(magnitude) * thresholds[1]

    # Extract voice, noise, and background spectrograms based on thresholds
    voice_mag = np.where(magnitude > threshold_voice, magnitude, 0)
    noise_mag = np.where((magnitude <= threshold_voice) & (magnitude > threshold_noise), magnitude, 0)
    background_mag = np.where(magnitude <= threshold_noise, magnitude, 0)

    # Reconstruct signals using inverse STFT
    voice_signal = librosa.istft(voice_mag * phase)
    noise_signal = librosa.istft(noise_mag * phase)
    background_signal = librosa.istft(background_mag * phase)

    # Write separated audio signals to files
    sf.write(voice_output_path, voice_signal, sr, format='wav')
    sf.write(noise_output_path, noise_signal, sr, format='wav')
    sf.write(background_output_path, background_signal, sr, format='wav')

if __name__ == "__main__":
    input_audio_path = r"C:\ProjectWork1\WorkRoot\tests\yoon_test\원본파일\소음테스트2.wav" # 입력 오디오 파일 경로
    voice_output_path = r"C:\ProjectWork1\WorkRoot\tests\yoon_test\변환파일\소음테스트2_voice.wav"  # 분리된 음성 파일 경로
    noise_output_path = r"C:\ProjectWork1\WorkRoot\tests\yoon_test\변환파일\소음테스트2_noisy.wav" # 분리된 소음 파일 경로
    background_output_path = r"C:\ProjectWork1\WorkRoot\tests\yoon_test\변환파일\소음테스트2_back.wav"  # Output background noise file path

    # Thresholds for separating voice, noise, and background
    thresholds = (0.05, 0.1)

    # Separate audio into voice, noise, and background
    separate_audio(input_audio_path, voice_output_path, noise_output_path, background_output_path, thresholds)

    print("Audio separation completed.")
