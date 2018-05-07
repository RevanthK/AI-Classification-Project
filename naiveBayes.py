# naiveBayes.py
# -------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import util
import classificationMethod
import math
import time
import numpy as np
import random

class NaiveBayesClassifier(classificationMethod.ClassificationMethod):
  """
  See the project description for the specifications of the Naive Bayes classifier.
  
  Note that the variable 'datum' in this code refers to a counter of features
  (not to a raw samples.Datum).
  """
  WIDTH = 0
  HEIGHT = 0


  def __init__(self, legalLabels, size):
    self.legalLabels = legalLabels
    self.type = "naivebayes"
    self.k = 1 # this is the smoothing parameter, ** use it in your train method **
    self.automaticTuning = False # Look at this flag to decide whether to choose k automatically ** use this in your train method **    
    self.priors = {}
    self.featureProb = []
    self.size = size

    #self.featureProb = util.Counter()
    if len(legalLabels) == 10:
      self.WIDTH = 28
      self.HEIGHT = 28
    else:
      self.WIDTH = 60
      self.HEIGHT = 70

  def setSmoothing(self, k):
    """
    This is used by the main method to change the smoothing parameter before training.
    Do not modify this method.
    """
    self.k = k

  def train(self, trainingData, trainingLabels, validationData, validationLabels):
    """
    Outside shell to call your method. Do not modify this method.
    """  
      
    # might be useful in your code later...
    # this is a list of all features in the training set.
    self.features = list(set([ f for datum in trainingData for f in datum.keys() ]));
    
    if (self.automaticTuning):
        kgrid = [0.001, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 20, 50]
    else:
        kgrid = [self.k]
        
    self.trainAndTune(trainingData, trainingLabels, validationData, validationLabels, kgrid)
      
  def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, kgrid):
    """
    Trains the classifier by collecting counts over the training data, and
    stores the Laplace smoothed estimates so that they can be used to classify.
    Evaluate each value of k in kgrid to choose the smoothing parameter 
    that gives the best accuracy on the held-out validationData.
    
    trainingData and validationData are lists of feature Counters.  The corresponding
    label lists contain the correct label for each datum.
    
    To get the list of all possible features or labels, use self.features and 
    self.legalLabels.
    """

    "*** YOUR CODE HERE ***"


    #self.features = trainingData[0].keys() # could be useful later
    # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING, OR
    # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.
    rand_data = []
    rand_labels = []

    for i in sorted(random.sample(xrange(len(trainingLabels)), self.size)):
      rand_data.append(trainingData[i])
      rand_labels.append(trainingLabels[i])

    self.priors = {}
    self.featureProb = []

    for i in range(len(self.legalLabels)):
        self.priors[i] = 0;
        dictn = {}
        for j in range(self.WIDTH):
          for k in range(self.HEIGHT):
            #to solving zero frequency problem we used 1 instead of 0
            dictn[(j,k)] = self.k
        self.featureProb.append(dictn)

    total = 0;



    for i in range(len(rand_labels)):
        total += 1
        self.priors[rand_labels[i]] = self.priors[rand_labels[i]] + 1;  
        for j in range(self.WIDTH):
          for k in range(self.HEIGHT):
            if rand_data[i][(j,k)] == 1:
              self.featureProb[rand_labels[i]][(j,k)] += 1

    for i in range(len(self.legalLabels)):
        #print str(self.priors[legalLabels[i]])

        for j in range(self.WIDTH):
          for k in range(self.HEIGHT):
            self.featureProb[i][(j,k)] = float(self.featureProb[i][(j,k)])/float(self.priors[self.legalLabels[i]])

        self.priors[i] = float(self.priors[i])/float(total)
        #print self.featureProb[i]
        #print self.featureProb[i]

    
    #print self.priors



        
  def classify(self, testData):
    """
    Classify the data based on the posterior distribution over labels.
    
    You shouldn't modify this method.
    """
  

    guesses = []
    self.posteriors = [] # Log posteriors are stored for later data analysis (autograder).
    for datum in testData:
      posterior = self.calculateLogJointProbabilities(datum)
      guesses.append(posterior.argMax())
      self.posteriors.append(posterior)
    return guesses
      
  def calculateLogJointProbabilities(self, datum):
    """
    Returns the log-joint distribution over legal labels and the datum.
    Each log-probability should be stored in the log-joint counter, e.g.    
    logJoint[3] = <Estimate of log( P(Label = 3, datum) )>
    
    To get the list of all possible features or labels, use self.features and 
    self.legalLabels.
    """
    logJoint = util.Counter()

    for i in range(len(self.legalLabels)):
      logJoint[i] = np.log(self.priors[i])

    for j in range(self.WIDTH):
      for k in range(self.HEIGHT):
        if(datum[(j,k)] == 1):
          for i in range(len(self.legalLabels)):
            logJoint[i] += np.log(self.featureProb[i][(j,k)]);
        

    return logJoint
  
  def findHighOddsFeatures(self, label1, label2):
    """
    Returns the 100 best features for the odds ratio:
            P(feature=1 | label1)/P(feature=1 | label2) 
    
    Note: you may find 'self.features' a useful way to loop through all possible features
    """
    featuresOdds = []
       
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

    return featuresOdds
    

    
      
