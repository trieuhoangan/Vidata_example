import sklearn
from utils import Dataload
from loaddata import Dataset
import math  
import scipy
import numpy as np
from heapq import nlargest

link_visim_400 = '../ViData/ViSim-400/Visim-400.txt'
target = []
with open(link_visim_400,'r',encoding='utf-8') as reader:
    visim400 = reader.readlines()
def get_length_of_vector(vector):
    sum = 0
    for dimension in vector:
        sum = sum + dimension*dimension
    sum = math.sqrt(sum)
    return sum
def get_dot(vector_a, vector_b):
    limit = 0
    # print(vector_a)
    # print(vector_b)
    if len(vector_a) < len(vector_b):
        limit = len(vector_a)
    else:
        limit = len(vector_b)
    sum = 0
    for i in range(0,limit):
        sum = sum + vector_b[i]*vector_a[i]
    return sum
def get_cosine(w1,w2,model):
    single_cosine = get_dot(model[w1],model[w2])/(get_length_of_vector(model[w1])*get_length_of_vector(model[w2]))
    return single_cosine
def get_target():
    count = 0
    for line in visim400:
        if count == 0:
            count = count +1
        else:
            words = line.split('\t')
            # print(words)
            target.append(float(words[3])/6)
def get_cosin_of_visim(model):
    count = 0
    
    cosine = []
    for line in visim400:
        if count == 0:
            count = count +1
        else:
            words = line.split('\t')
            # print(words)

            if words[0] not in model or words[1] not in model:
                cosine.append(0)
            else:
                single_cosine = get_cosine(words[0],words[1],model)
                cosine.append(single_cosine)
    return cosine
def get_pearson_of_visim(cosin):
    return scipy.stats.pearsonr(cosin,target)
def get_spearman_of_visim(cosin):
    return scipy.stats.spearmanr(cosin,target)
def get_k_nearest_word(word,model,k):
    if word not in model:
        return None
    else:
        cosine_list = []
        for other in model:
            if other != word:
                cosine_list.append(get_cosine(word,other,model))
        k_nearest = nlargest(k,cosine_list)
        return k_nearest
if __name__ == "__main__":
    link_W2V_150 = '../ViData/W2V_150.txt'
    model150 = Dataload(link_W2V_150,0)
    get_target()
    cosin = get_cosin_of_visim(model150.w2v)
    print(get_pearson_of_visim(cosin))
    print(get_spearman_of_visim(cosin))
    


