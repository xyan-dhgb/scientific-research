from sklearn import tree

# Step 1: Collecting data
# Step 2: Processing data
# Step 3: Building model
# Step 4: Predicting result
# Step 5: Evaluating model

my_tree = tree.DecisionTreeClassifier()

dac_trung = [['1', '3', '3', '7'],
             ['5', '2', '4', '6'],
             ['1', '2', '4', '6'],
             ['5', '4', '4', '3'],
             ['1', '4', '4', '7'],
             ['3', '2', '3', '7'],
             ['3', '3', '3', '6'],
             ['5', '2', '2', '7']] 

nhan = [0,1,1,0,0,0,0,1] # Result

ket_qua = my_tree.fit(dac_trung, nhan)

ket_qua_final = ket_qua.predict([[1,4,3,6]])

print(ket_qua_final)