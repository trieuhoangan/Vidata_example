from utils import Dataload
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.model_selection import GridSearchCV
from sklearn import svm, datasets
# ANT = 0
# SYM = 1

class Dataset:
    def __init__(self,test_link):
        self.x_train = []
        self.y_train = []
        self.x_test = []
        self.y_test = []
        
        link_w2v_file = '../ViData/W2V_150.txt'
        model150 = Dataload(link_w2v_file,0)
        self.w2v = model150.w2v
        # self.add_test_set(test_link)
        # self.get_w2v_model(link_w2v_file)
    # def get_w2v_model(self,link_file):
    #     self.w2v = 
def add_test_set(dataset,link_file):
    with open(link_file,'r',encoding='utf-8') as reader:
        data = reader.readlines()
    count = 0
    for row in data:
        if count ==0:
            count= count+1
        else:
            row = row.replace('\n','')
            words = row.split('\t')
            pair =[]
            if words[0] in dataset.w2v:
                v1 = dataset.w2v[words[0]]
                
            else:
                continue
            if words[1] in dataset.w2v:
                v2 = dataset.w2v[words[1]]
            else:
                continue
            pair.append(v1)
            pair.append(v2)
            dataset.x_test.append(np.convolve(v1,v2))
            if words[2]=="ANT":
                dataset.y_test.append(0)
            else:
                dataset.y_test.append(1)

# check cosin only            
def get_train_set(dataset,link_file,mode):
    with open(link_file,'r',encoding='utf-8') as reader:
        data = reader.readlines()
    for row in data:
        row = row.replace('\n','')
        words = row.split(' ')
        pair=[]
        for word in words:
            pair.append(word)
        if pair[0] in dataset.w2v and pair[1] in dataset.w2v:
            pair[0] = dataset.w2v[pair[0]]
            pair[1] = dataset.w2v[pair[1]]
            vector = np.convolve(pair[0],pair[1])    
            dataset.x_train.append(vector)
            dataset.y_train.append(mode)
        
if __name__ == "__main__":
    test_link_n = '../ViData/ViCon/400_noun_pairs.txt'
    test_link_a = '../ViData/ViCon/600_adj_pairs.txt'
    test_link_v = '../ViData/ViCon/400_verb_pairs.txt'
    link_ant = '../ViData/antonym-synonym set/Antonym_vietnamese.txt'
    link_sym = '../ViData/antonym-synonym set/Synonym_vietnamese.txt'
    data = Dataset(test_link_n)
    get_train_set(data,link_ant,0)
    get_train_set(data,link_sym,1)
    add_test_set(data,test_link_n)
    add_test_set(data,test_link_a)
    add_test_set(data,test_link_v)


    # parameters = [{'penalty':['l1'],'solver':['saga'],'multi_class':['multinomial','ovr']},{'penalty':['l1'],'solver':['liblinear'],'multi_class':['ovr']}]

    # LR = LogisticRegression(random_state=0,max_iter=500)
    # clf = GridSearchCV(LR, parameters,cv=5,scoring='precision')
    # clf.fit(data.x_train,data.y_train)
    # print(clf.best_params_)
    model = LogisticRegression(multi_class='ovr',penalty='l1',solver='saga',random_state=0,max_iter=800)
    model.fit(data.x_train,data.y_train)
    result = model.predict(data.x_test)
   
    print(accuracy_score(data.y_test,result))
    model2 = MLPClassifier(alpha=1, max_iter=500)
    model2.fit(data.x_train,data.y_train)
    result = model2.predict(data.x_test)

    print(accuracy_score(data.y_test,result))
    print(precision_score(data.y_test,result))
    # w1 = input()
    # if w1 in data.w2v:
    #     v1 = data.w2v[w1]
    # w2 = input()
    # if w2 in data.w2v:
    #     v2 = data.w2v[w2]
    # vec = np.convolve(v1,v2)
    # print(model2.predict([vec,vec]))


                