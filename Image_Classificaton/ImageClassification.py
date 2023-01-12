from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import confusion_matrix
import seaborn as sn
sn.set(font_scale=1.4)
from sklearn.metrics import accuracy_score, precision_score,recall_score,f1_score
from Exploratory_Data_Analysis import train_images, train_labels,test_images,test_labels




#Linear Support Vector Classification

linear_svc = LinearSVC(max_iter=4000)
linear_svc.fit(train_images, train_labels)
Y_pred = linear_svc.predict(test_images)
accuracy_svc=round(accuracy_score(test_labels,Y_pred)* 100, 2)
acc_linear_svc = round(linear_svc.score(train_images, train_labels) * 100, 2)

cm = confusion_matrix(test_labels, Y_pred)
accuracy = accuracy_score(test_labels,Y_pred)
precision =precision_score(test_labels, Y_pred,average='micro')
recall =  recall_score(test_labels, Y_pred,average='micro')
f1 = f1_score(test_labels,Y_pred,average='micro')
print('Confusion matrix for SVC\n',cm)
print('accuracy_SVC: %.3f' %accuracy)
print('precision_SVC: %.3f' %precision)
print('recall_SVC: %.3f' %recall)
print('f1-score_SVC : %.3f' %f1)





# K-Nearest Neighbors Classification

knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(train_images, train_labels)
Y_pred = knn.predict(test_images) 
accuracy_knn = round(accuracy_score(test_labels, Y_pred) * 100, 2)
acc_knn = round(knn.score(train_images, train_labels) * 100, 2)

cm = confusion_matrix(test_labels, Y_pred)
accuracy = accuracy_score(test_labels,Y_pred)
precision =precision_score(test_labels, Y_pred,average='micro')
recall =  recall_score(test_labels, Y_pred,average='micro')
f1 = f1_score(test_labels, Y_pred, average='micro')
print('Confusion matrix for KNN\n',cm)
print('accuracy_KNN : %.3f' %accuracy)
print('precision_KNN : %.3f' %precision)
print('recall_KNN: %.3f' %recall)
print('f1-score_KNN : %.3f' %f1)





#Gaussian Naive Bayes Classification

gaussian = GaussianNB()
gaussian.fit(train_images, train_labels)
Y_pred = gaussian.predict(test_images) 
accuracy_nb=round(accuracy_score(test_labels,Y_pred)* 100, 2)
acc_gaussian = round(gaussian.score(train_images, train_labels) * 100, 2)

cm = confusion_matrix(test_labels, Y_pred)
accuracy = accuracy_score(test_labels,Y_pred)
precision =precision_score(test_labels, Y_pred,average='micro')
recall =  recall_score(test_labels, Y_pred,average='micro')
f1 = f1_score(test_labels,Y_pred,average='micro')
print('Confusion matrix for Naive Bayes\n',cm)
print('accuracy_Naive Bayes: %.3f' %accuracy)
print('precision_Naive Bayes: %.3f' %precision)
print('recall_Naive Bayes: %.3f' %recall)
print('f1-score_Naive Bayes : %.3f' %f1)





#Random Forest Classification

random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(train_images, train_labels)
Y_prediction = random_forest.predict(test_images)
accuracy_rf=round(accuracy_score(test_labels,Y_prediction)* 100, 2)
acc_random_forest = round(random_forest.score(train_images, train_labels) * 100, 2)


cm = confusion_matrix(test_labels, Y_prediction)
accuracy = accuracy_score(test_labels,Y_prediction)
precision = precision_score(test_labels, Y_prediction, average='micro')
recall =  recall_score(test_labels, Y_prediction,average='micro')
f1 = f1_score(test_labels, Y_prediction, average='micro')
print('Confusion matrix for Random Forest\n',cm)
print('accuracy_random_Forest : %.3f' %accuracy)
print('precision_random_Forest : %.3f' %precision)
print('recall_random_Forest : %.3f' %recall)
print('f1-score_random_Forest : %.3f' %f1)





#Decision Tree Classification

decision_tree = DecisionTreeClassifier() 
decision_tree.fit(train_images, train_labels)  
Y_pred = decision_tree.predict(test_images) 
accuracy_dt=round(accuracy_score(test_labels,Y_pred)* 100, 2)
acc_decision_tree = round(decision_tree.score(train_images, train_labels) * 100, 2)

cm = confusion_matrix(test_labels, Y_pred)
accuracy = accuracy_score(test_labels,Y_pred)
precision =precision_score(test_labels, Y_pred,average='micro')
recall =  recall_score(test_labels, Y_pred,average='micro')
f1 = f1_score(test_labels,Y_pred,average='micro')
print('Confusion matrix for DecisionTree\n',cm)
print('accuracy_DecisionTree: %.3f' %accuracy)
print('precision_DecisionTree: %.3f' %precision)
print('recall_DecisionTree: %.3f' %recall)
print('f1-score_DecisionTree : %.3f' %f1)


