import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "ecoli2.data"
names = ['SeqName', 'MCG', 'GVH', 'LIP', 'CHG', 'AAC', 'ALM1', 'ALM2', 'Class']
dataset = pandas.read_csv(url, names=names)

print dataset.shape
print dataset.head(10)
print dataset.describe()
print dataset.groupby('Class').size()
########################################################
dataset.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
plt.show()
dataset.hist()
plt.show()
# this graph doesnt work unless the above four lines are commented out.
#scatter_matrix(dataset)
#plt.show()
