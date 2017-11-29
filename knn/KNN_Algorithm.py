
# coding: utf-8

# In[2]:


def loadData():
    fileTest = open('TestData.txt', 'r')
    testData = []
    for line in fileTest:
        linePoints = line.split(',')
        points = []
        for i in range(len(linePoints) - 1):
            points.append(float(linePoints[i]))
        lastPoint = linePoints[-1]
        if lastPoint != '\n':
            points.append(lastPoint[0:3])
            testData.append(points)
    #print(testData)
    fileTest.close()
    
    fileTrain = open('TrainData.txt', 'r')
    trainData = []
    for line in fileTrain:
        linePoints = line.split(',')
        points = []
        for i in range(len(linePoints) - 1):
            points.append(float(linePoints[i]))
        lastPoint = linePoints[-1]
        if lastPoint != '\n':
            points.append(lastPoint[0:3])
            trainData.append(points)
    #print(trainData)
    fileTrain.close()
    return trainData , testData

#trainingData , testingData = loadData()
#print (len(trainingData), len(testingData))


# In[3]:


import math
def eclideanDistance(x, xi):
    d = 0.0
    for i in range(len(x) - 1):
        d += pow(x[i] - xi[i], 2)
    math.sqrt(d)
    return d


# In[4]:


def getAccuracy(predictions, test):
    correct = 0
    for x in range(len(test)):
        if predictions[x] == test[x][-1]:
            correct += 1
    result = (correct/(float(len(test)))) * 100.0
    return correct, result


# In[5]:


import operator
def knnPredict(train, test, k):
    predictions = []
    print('K Value: ', k)
    for iTest in test:
        distances = []
        for iTrain in train:
            dist = eclideanDistance(iTest, iTrain)
            distances.append((iTrain, dist))
        distances.sort(key = operator.itemgetter(1))
        iTestKNN = distances[0:k]
        classCounter = {}
        for iDist in iTestKNN:
            if iDist[0][-1] in classCounter:
                classCounter[iDist[0][-1]] += 1
            else:
                classCounter[iDist[0][-1]] = 1
        #print(classCounter)
        #print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        classCounterSorted = sorted(classCounter.items(), key=operator.itemgetter(1), reverse=True)
        #print(classCounterSorted)
        print('Predicted Class: ', classCounterSorted[0][0], 'Actual Class: ', iTest[-1])
        predictions.append(classCounterSorted[0][0])
    correct, accuracy = getAccuracy(predictions, test)
    print('Number of correctly classified instances : ', correct)
    print('Total number of instances : ', len(test))
    print('Accuracy: ', accuracy)
    


# In[6]:


trainingData , testingData = loadData()
for k in range(1,10):
    knnPredict(trainingData, testingData, k)
    print('##########################################################')

