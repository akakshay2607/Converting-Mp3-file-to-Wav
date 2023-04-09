# importing necessary libraries
import librosa
import soundfile as sf
import os

input_folder = "C://Users/akaks/Downloads/MP3/"      # path to input folder
output_folder = "C://Users/akaks/Downloads/Wav/"     # path to output folder

# Looping through files
for audio in os.listdir(input_folder):
    if audio.endswith(".mp3"):
        # Load MP3 file
        mp3 = os.path.join(input_folder, audio)
        y, sr = librosa.load(mp3)
        
        wav_file = os.path.splitext(audio)[0] + ".wav"
        wav_path = os.path.join(output_folder, wav_file)
        
        # Saving the Wav file
        sf.write(wav_path, y, sr)
        print('Converted',audio,'into Wav')
