# perceptron.py
# -------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

# Perceptron implementation
import util
import random
PRINT = True


class PerceptronClassifier:
  """
  Perceptron classifier.
  
  Note that the variable 'datum' in this code refers to a counter of features
  (not to a raw samples.Datum).
  """
  WIDTH = 0
  HEIGHT = 0

  def __init__( self, legalLabels, max_iterations, size):
    self.legalLabels = legalLabels
    self.size = size
    if len(legalLabels) == 10:
      self.WIDTH = 28
      self.HEIGHT = 28
    else:
      self.WIDTH = 60
      self.HEIGHT = 70
    self.type = "perceptron"
    self.max_iterations = max_iterations
    self.weights = {}
    for label in legalLabels:
      self.weights[label] = util.Counter() # this is the data-structure you should use

  def setWeights(self, weights):
    assert len(weights) == len(self.legalLabels);
    self.weights == weights;


  def calcOutput(self, data):
    
    array = []

    for i in range(len(self.legalLabels)):
      value = 0
      for j in range(self.WIDTH):
        for k in range(self.HEIGHT):
          value  = value + data[(j,k)] * self.weights[i][(j,k)]
      #print str(i) + " " + str(value)
      array.append(value)

    return array.index(max(array))

  def shiftWeights(self, wrongVal, correctVal, data):
    
  
    for j in range(self.WIDTH):
        for k in range(self.HEIGHT):
          key = (j,k)
          self.weights[wrongVal][key] -= data[(j,k)] 
          self.weights[correctVal][key] += data[(j,k)] 
    
    
      
  def train( self, trainingData, trainingLabels, validationData, validationLabels ):
    """
    The training loop for the perceptron passes through the training data several
    times and updates the weight vector for each label based on classification errors.
    See the project description for details. 
    
    Use the provided self.weights[label] data structure so that 
    the classify method works correctly. Also, recall that a
    datum is a counter from features to values for those features
    (and thus represents a vector a values).
    """


    '''initialize the weights'''

    for i in range(len(self.legalLabels)):
      for j in range(self.WIDTH):
        for k in range(self.HEIGHT):
          key = (j,k)
          self.weights[i][key] = 0


    #randomized subset of data
    rand_data = []
    rand_labels = []

    for i in sorted(random.sample(xrange(len(trainingLabels)), self.size)):
      rand_data.append(trainingData[i])
      rand_labels.append(trainingLabels[i])



    self.features = trainingData[0].keys() # could be useful later
    # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING, OR
    # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.

    for iteration in range(self.max_iterations):
      print "Starting iteration ", iteration, "..."
      for i in range(len(rand_data)):
          "*** YOUR CODE HERE ***"
          '''
          if (len(self.legalLabels) == 10):
            print "Set number Weights"   
          '''
          val =  self.calcOutput(rand_data[i])
          #print "Predicted value " + str(val)
          #print "Actual Value " + str(trainingLabels[i])

          if(val != rand_labels[i]):
            self.shiftWeights(val, rand_labels[i], rand_data[i]);
            #self.shiftWeights()

          #util.raiseNotDefined()

  def classify(self, data ):
    """
    Classifies each datum as the label that most closely matches the prototype vector
    for that label.  See the project description for details.
    
    Recall that a datum is a util.counter... 
    """
    guesses = []
    for datum in data:
      vectors = util.Counter()
      for l in self.legalLabels:
        vectors[l] = self.weights[l] * datum
      guesses.append(vectors.argMax())
    return guesses

  
  def findHighWeightFeatures(self, label):
    """
    Returns a list of the 100 features with the greatest weight for some label
    """
    featuresWeights = []

    "*** YOUR CODE HERE ***"
    return featuresWeights.most_common(100)

'''
  def caclulateOutput(theta, weights):
    sum = 0
    for i in range(len(weights)):
      sum += weights[i]

    return 1 if (sum >= theta) else 0
'''


