from moviepy.editor import AudioFileClip
import os

def convert_to_wav(input_path, output_path):
    # m4a 파일을 로드하여 AudioFileClip 객체 생성
    audio_clip = AudioFileClip(input_path)

    # wav 파일로 저장
    audio_clip.write_audiofile(output_path, codec='pcm_s16le', ffmpeg_params=['-ac', '2'])

if __name__ == "__main__":
    input_directory = "C:\\ProjectWork1\\WorkRoot\\tests\\yoon_test"       # m4a 파일이 있는 입력 디렉토리
    output_directory = 'C:\\ProjectWork1\\WorkRoot\\tests\\yoon_test\\변환파일\\'  # 변환된 wav 파일을 저장할 출력 디렉토리

    # 출력 디렉토리가 없으면 생성cd
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 입력 디렉토리의 파일들을 순회
    for filename in os.listdir(input_directory):
        if filename.endswith(".m4a"):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, os.path.splitext(filename)[0] + ".wav")

            # m4a를 wav로 변환
            print(output_path)
            convert_to_wav(input_path, output_path)

    print("변환 완료.")