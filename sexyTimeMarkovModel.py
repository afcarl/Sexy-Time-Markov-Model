'''
Copyright (c) 2014 Michael A. Alcorn (https://sites.google.com/site/michaelaalcorn/)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

#!/bin/python

# python sexyTimeMarkovModel.py "initialProbs.csv" "transitionProbs.csv" "arousalRates.csv" "timeParameters.csv"

from scipy import stats
import csv
import numpy
import sys

# Import the probabilities for starting in different sexual positions.
def getInitialProbs(filename):
    positions = []
    initialProbs = []
    
    reader = csv.DictReader(open(filename))
    
    for row in reader:
        positions.append(row["Position"])
        initialProbs.append(float(row["p"]))
    
    return positions, stats.rv_discrete(name = "initialProbs", values = (range(0, len(positions)), initialProbs))

# Import the probabilities for transitioning between different sexual positions.
def getTransitionProbs(filename):
    transitionProbs = {}
    
    reader = csv.DictReader(open(filename))
    
    for row in reader:
        currentPosition = row["Position"]
        probs = []
        for i in range(1, len(reader.fieldnames)):
            nextPosition = reader.fieldnames[i]
            probs.append(float(row[nextPosition]))
        transitionProbs[currentPosition] = stats.rv_discrete(name = "transitionProbs", values = (range(0, len(reader.fieldnames) - 1), probs))
    
    return transitionProbs

# Import the orgasm rate for each partner and sexual position.
def getArousalRates(filename):
    reader = csv.DictReader(open(filename))
    [position, partnerOne, partnerTwo] = reader.fieldnames
      
    arousalRates = {partnerOne: {}, partnerTwo: {}}
    
    for row in reader:
        position = row["Position"]
        arousalRates[partnerOne][position] = float(row[partnerOne])
        arousalRates[partnerTwo][position] = float(row[partnerTwo])
    
    return arousalRates

# Import the parameters used to determine the amount of time spent in each sexual position.
def getTimeParameters(filename):
    timeParameters = {}
    
    reader = csv.DictReader(open(filename))
    
    for row in reader:
        position = row["Position"]
        timeParameters[position] = {}
        timeParameters[position]["mean"] = float(row["Mean"])
        timeParameters[position]["std"] = float(row["Standard Deviation"])
    
    return timeParameters

positions, initialProbs = getInitialProbs(sys.argv[1])
transitionProbs = getTransitionProbs(sys.argv[2])
arousalRates = getArousalRates(sys.argv[3])
timeParameters = getTimeParameters(sys.argv[4])

while True:
    simulate = raw_input("Simulate sex (y/n)? ")
    # Simulate sex.
    if "y" in simulate.lower():
        totalTime = 0.0
        positionCount = 0
        partnerOneOrgasms = 0.0
        partnerTwoOrgasms = 0.0
        pos = positions[initialProbs.rvs()]
        # while partnerOneOrgasms < 1.0 or partnerTwoOrgasms < 1.0: # You know... if you're into being fair.
        while partnerTwoOrgasms < 1.0:
            mu = timeParameters[pos]["mean"]
            sigma = timeParameters[pos]["std"]
            time = numpy.random.normal(mu, sigma)
            totalTime += time
            partnerOneOrgasms += time * arousalRates["PartnerOne"][pos]
            partnerTwoOrgasms += time * arousalRates["PartnerTwo"][pos]
            # print("Position: " + pos + "\tTime: " + str(time) + " (s)/" + str(time / 60.0) + " (min)\tPartnerOne Orgasms: " + str(partnerOneOrgasms) + "\tPartnerTwo Orgasms: " + str(partnerTwoOrgasms))
            print("Position: {0}\tTime: {1:.2f} (s)/{2:.2f} (min)\tPartnerOne Orgasms: {3:.2f}\tPartnerTwo Orgasms: {4:.2f}".format(pos, time, time / 60.0, partnerOneOrgasms, partnerTwoOrgasms))
            pos = positions[transitionProbs[pos].rvs()]
            positionCount += 1
        
        # print("Total Time: " + str(totalTime) + "\tPosition Count: " + str(positionCount) + "\tPartnerOne Orgasms: " + str(partnerOneOrgasms) + "\tPartnerTwo Orgasms: " + str(partnerTwoOrgasms))
        print("Total Time: {0:.2f} (s)/{1:.2f} (min)\tPosition Count: {2}\tPartnerOne Orgasms: {3}\tPartnerTwo Orgasms: {4}".format(totalTime, totalTime / 60.0, positionCount, int(partnerOneOrgasms), int(partnerTwoOrgasms)))
    else:
        break
