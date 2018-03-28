from sklearn import tree #importing decision tree

clf = tree.DecisionTreeClassifier()

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

clf = clf.fit(X, Y)

lst = []

x = 0
v = " height(cm) "
while x<3:
    a = input("Enter" + v)
    lst.append(a)
    x = x+1
    if x  == 1:
        v = " weight(kg) "
    if x == 2:
        v = " shoe size "

prediction = clf.predict([lst])

print(prediction)
