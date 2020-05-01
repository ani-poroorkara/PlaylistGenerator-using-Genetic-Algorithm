"""
# Unzip the file containing music files
# !unzip "/content/drive/My Drive/Colab Notebooks/Music.zip" -d MusicFile

"""

"""
Loop through the entire dataset and store the music file name along with path in a list. 
This is needed to find the songs and extract their features.
"""
import os

datacount = 0
songs = []
for file in os.listdir('MusicFiles'):
  if file == "2018":
    for file in os.listdir('MusicFiles/2018'):
      songs.append('2018/' + file)
      datacount +=1
  else :
    for file in os.listdir('MusicFiles/2019'):
      songs.append('2019/'+file)
      datacount +=1
print(str(datacount) + " files found and loaded")

"""
Feature extraction from the music files.
All the features are extracted into a dictionary and returned.
This dictionary is then added into another dictionary indexed with the name of the file/song.
data should look like :
{'2018/song1.mp3': {'bpm': 89.94617462158203,
  'dissonance': 0.4526239037513733,
  'loudness': -8.428863525390625,
  'loudness_range': 8.834383010864258,
  'tonal_key': 'A',
  'tonal_scale': 'minor'},
'2019/song2': {'bpm': 144.7926788330078,
  'dissonance': 0.452959269285202,
  'loudness': -6.793518543243408,
  'loudness_range': 3.4764232635498047,
  'tonal_key': 'F',
  'tonal_scale': 'major'}
}
"""
from essentia.standard import *

def feature_Extraction(song):
  try:
    song = "/content/MusicFiles/" + song
    #song = "/content/MusicFiles/2018/01 - Lost In The Echo.mp3"
    features,features_frames = MusicExtractor(lowlevelStats =['mean','stdev'],
                              rhythmStats =['mean','stdev'],
                              tonalStats =  ['mean','stdev'])(song)
    stat = {
      'loudness' :  features['lowlevel.loudness_ebu128.integrated'],
      'loudness_range' : features['lowlevel.loudness_ebu128.loudness_range'],
      'bpm' : features['rhythm.bpm'],
      'tonal_key' : features['tonal.key_edma.key'],
      'tonal_scale' : features['tonal.key_edma.scale'],
      'dissonance' : features['lowlevel.dissonance.mean']
    }

  except:
      stat = {}
  return stat

data = {}
count = 0
for song in songs:
  data[song] = feature_Extraction(song)
  print("#"*10, end = '')
  count +=1
  print(count)


"""
Save the dictionary as a pickle file.
Before saving the dictionary, do check if all feature values are present in the file.
If not present, remove those cells. 
"""

# Save the data in a pickle file as a dictionary 
import pickle

pickle.dump(data, open("data_music.pkl", "wb"))

print("End of processing :)")
