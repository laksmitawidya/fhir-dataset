#!/usr/bin/env python

from operator import itemgetter 
import sys

# keep a map of the sum of conditions of each symptoms
observationmap = {}
symptommap = {}

current_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    symptom, count, totalsymptom = line.split('\t')
    try:
        count = float(count)
        totalsymptom = int(count)
        observationmap[symptom] = observationmap.get(symptom, 0) + count
        
        if current_word == symptom:
            symptommap[symptom] = symptommap.get(symptom,0) + totalsymptom
            current_count += totalsymptom
        else:
            current_count = totalsymptom
            current_word = symptom

    except ValueError:
        # ignore lines where the count is not a number
        pass

# sort the symptoms alphabetically;
alphabetic_observationmap = sorted(observationmap.items(), key=itemgetter(0))
alphabetic_symptommap = sorted(symptommap.items(), key=itemgetter(0))

print("\n\n============= TOTAL OBSERVATION ================ \n\n")
# output to STDOUT
for symptom, countsymptom in alphabetic_observationmap:
    print('%s\t%s'% (symptom, countsymptom))

print("\n\n============= TOTAL SYMPTOM ================ \n\n")

for symptom, countsymptom in alphabetic_symptommap:
    print('%s\t%s'% (symptom, countsymptom))