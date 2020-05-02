# Load the data as a dictionary

print("Loading data....")
import pickle
data = pickle.load(open("dataSave.pkl", "rb")) 
print("Done!")


"""
Import the required libraries.
Load the song names from the loaded dictionary.
Define the basis of the fitness function and what parameters need to be minimized or maximized for creating the playlist.
Here entropy of tone, average beats per minute of the entire playlist, difference in loudness and difference in dissonance are taken as parameters and all of the parameters are to be minimized.
"""

import pandas as pd
import numpy as np
import random as rand
from scipy.stats import entropy
from math import log, e

songs = []
for i in data:
  songs.append(i)

def entropyCalc(labels):
  value,counts = np.unique(labels, return_counts=True)
  return entropy(counts)

def information_evaluation(individual):

  sum_bpm = 0
  for i in range(1,len(individual)):
    sum_bpm += abs(data[individual[i-1]]['bpm'] - data[individual[i]]['bpm'])
  avg_bpm = sum_bpm/len(individual)

  loudness = []
  dissonance = []
  tone = []
  for i in individual:
    loudness.append(data[i]['loudness'])
    dissonance.append(data[i]['dissonance'])
    tone.append(data[i]['tonal_key'])
  
  entropy_tone = entropyCalc(tone)
  max_loudness = max(loudness)
  min_loudness = min(loudness)
  max_dissonance = max(dissonance)
  min_dissonance = min(dissonance)
  diff_loudness = max_loudness - min_loudness
  diff_dissonance = max_dissonance - min_dissonance
  
  return (entropy_tone, avg_bpm, diff_loudness, diff_dissonance)


"""
The fitness function should be first defined. 
Associate the fitness function to the individual (i.e. playlist) 
Create the toolbox function.
"""

from deap import base
from deap import creator
from deap import tools
from deap import algorithms
import random

creator.create("FitnessMulti", base.Fitness, weights =(-1,-1,-1,-1))
creator.create("Individual", list, fitness=creator.FitnessMulti)

# Number of songs in each playlist when created.
size = 30
toolbox = base.Toolbox()
toolbox.register("songs", random.sample, songs, size)
toolbox.register("playlist", tools.initIterate, creator.Individual,toolbox.songs)
toolbox.register("population", tools.initRepeat, list, toolbox.playlist)
toolbox.register("evaluate", information_evaluation)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("select", tools.selNSGA2)


"""
Check working of the toolbox.
# individual = toolbox.playlist()
# result = information_evaluation(individual)
# print(individual)
# print(result)
"""


"""
Run the generation
deap.algorithms.eaMuPlusLambda(population, 
                                toolbox, 
                                selected individuals for next generation, 
                                children at each generation , 
                                probability of crossover, 
                                probability of mutation, 
                                num of generations, 
                                halloffame)
"""

print("Starting Generation....")
pop = toolbox.population(n = 20)
hof = tools.ParetoFront()
algorithms.eaMuPlusLambda(pop, toolbox, 20, 20, 0.5, 0, 20, halloffame = hof, verbose = False)
print("Populations Generated.")


"""
The best population can be accessed the first list in hall of fame. 
Here, you can generate
  1. A text file containing the playlist names.  
  2. Create a record with all the music files merged.
"""

bestlist = hof[0]

print("Creating playlist.txt file .... ")
playlist_file = open("playlist.txt","w+")
for s in bestlist:
  playlist_file.write(s + "\n")
playlist_file.close()
print("File saved.")

from pydub import AudioSegment
print("Generating RECORD.mp3 with best population....")
num = 1
for s in bestlist:
  m = 'MusicFiles/' + s
  ms = AudioSegment.from_mp3(m)
  if num == 1:
    record = AudioSegment.from_mp3(m)
  else:
    record = record + ms
  num += 1
  print("#", end='')
print("DONE!")
print("Exporting record...(will take time depending on number of songs)")
record.export("Record.mp3", format="mp3")
print("Record Exported.")
