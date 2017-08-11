from sklearn import tree

#features [x,y] x means the weight of the fruit & y is it bumby (1) or smooth(0)
#labels [z] z means is it apple(0) or orange (1)
features = [[140,1],[130,1],[150,0],[170,0]]
labels = [0,0,1,1]

cls = tree.DecisionTreeClassifier()
cls = cls.fit(features,labels)

print(cls.predict([[200,1]]))
