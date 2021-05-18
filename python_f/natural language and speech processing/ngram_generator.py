#Daniel Gallab
#assignment7
#n-grams
#applies concepts of relative probability for text generation


import random

def text_to_lst(s):
    s=open("101-0.txt","r")
    s=s.read()
    s=s.lower()
    #s=s.replace('\n'," </s> <s> ") #can be removed if we want word sequences within lines
    s=s.replace('.',"")
    s=s.replace(',',"")
    wrd_lst=s.split()
    return (wrd_lst)

def create_ngrams(wrd_lst,n):
    gram_lst = []
    for x in range(len(wrd_lst)-n+1):
        gram_lst = gram_lst + [ wrd_lst[x:x+n] ]
    gram_tupl=[]
    for e in (gram_lst):
        gram_tupl=gram_tupl + [tuple(e)]
    return (gram_tupl)

def create_dict(gram_tupl):
    gram_dict = {}
    for e in (gram_tupl):
        if e in gram_dict:
            gram_dict[e] = gram_dict[e] + 1
        else:
            gram_dict[e]= 1
    return (gram_dict)


# when n is 1, the chart can be understood linearly
def prob_chart(gram_dict, gram_dict_2):
    mat = [0]*(len(gram_dict)+1)
    gram_keys = list(gram_dict)
    gram_keys_2=list(gram_dict_2)
    
    for i in range(len(mat)):
        mat[i] = [0]*(len(gram_dict_2)+1)

    for i in range(1,len(mat)):
        mat[i][0] = gram_keys[i-1]

    for i in range(1,len(mat[0])):
        mat[0][i] = gram_keys_2[i-1]

    return (mat)

def calc_rel_prob(mat,gram_dict,gram_dict_2,n):
    for x in range(1,len(mat)):
        for y in range(1,len(mat[0])):
            if mat[x][0][0:n-1] == mat[0][y]:
                num=gram_dict[mat[x][0]]
                den=gram_dict_2[mat[0][y]]
                mat[x][y]=float(num)/float(den)
    print(mat)
    return (mat)
            
            
def construct_sen(mat,n):
    v = 20 #sentence length (in individual words)
    j= random.randint(1,len(mat)-1)
    sen=[mat[j][0]]
    nxt= mat[j][0][1:n]
    p=1
    while(v !=0) :
        n_ind=mat[0].index(nxt)
        cand=[]
        for i in range(1,len(mat)):
            if mat[i][n_ind]>0 : #2nd part can be removed
                cand=cand+[i]                                       
        r=random.choice(cand)
        p=p*mat[r][n_ind] #multiply each n-gram prob with each other to get total prob for sen
        nxt=mat[r][0][1:n]
        sen=sen+[mat[r][0][n-1:n]]
        v=v-1  
    sen_f=""+ " ".join(sen[0])+" "
    for e in sen[1:len(sen)]:
        sen_f=sen_f+ e[0] + " "
        
    print(p)
    print(sen_f)
    
    
    return (p,sen_f)


def normalize(sen):
    n_sen=""
    for gram in sen:
        n_sen = n_sen + ' ' +(gram[0])
    return (n_sen)

def main():
    #test string
    s = "a great great warrior never slays a slays a warrior you feel me great sunshine slays a sunshine"
    
    n = 4 #1->unigrams, 2->bigrams, 3->trigrams, 4->quadgrams
    wrd_lst=text_to_lst(s)
    
    gram_tupl = create_ngrams(wrd_lst,n)
    gram_tupl_2 = create_ngrams(wrd_lst,n-1)

    gram_dict = create_dict(gram_tupl)
    gram_dict_2 = create_dict(gram_tupl_2)
    mat=prob_chart(gram_dict,gram_dict_2)
    
    mat=calc_rel_prob(mat,gram_dict,gram_dict_2,n)
    
    p,sen_f=construct_sen(mat,n)
    
    

    

main()
