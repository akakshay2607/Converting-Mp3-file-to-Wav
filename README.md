# Converting-Mp3-file-to-Wav

 Here we will take the set of Mp3 files from a perticular folder and will convert them into the Wav files.

 We will be using the Librosa library for this purpose.

 first we will import the necessary libraries:

`import librosa`

`import soundfile as sf`

`import os`

Soundfile library will be used to write the output

first we will read all the audio files ending with .mp3 in a folder.

Then we will load that audio file in lobrosa.

`y, sr = librosa.load(mp3)`

sr - is the sampling rate of the audio

y- is the waveform array

Then we will create a output path to save the Wav file in the folder

`wav_file = os.path.splitext(audio)[0] + ".wav"`

`wav_path = os.path.join(output_folder, wav_file)`

Now we will write the wave file using the soundfile library

`sf.write(wav_path, y, sr)`

it takes the output path name, waveform array, sampling rate as arguments and creates a Wav file.
