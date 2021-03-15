import numpy as np
import random

mchain={}
mchain['start']={}

def markovchain(words):
    words_set=set(words)
    words_set.add('start')
    words_set.add('end')
    j=1
    for i in range(len(words)-1):
        if i==0:
            if words[i] in mchain['start'].keys():
                mchain['start'][words[i]]=mchain['start'][words[i]]+1
            else:
                mchain['start'][words[i]]=1
        
        if words[i] in mchain.keys():
            if  words[j] in mchain[words[i]].keys():
               mchain[words[i]][words[j]]=mchain[words[i]][words[j]]+1
            else:
                mchain[words[i]][words[j]]=1
        
        else:
            mchain[words[i]]={}
            mchain[words[i]][words[j]]=1
        
        if j==len(words)-1:
            if words[j] in mchain.keys():
                if  'end' in mchain[words[j]].keys():
                    mchain[words[j]]['end']=mchain[words[j]]['end']+1
                else:
                    mchain[words[j]]['end']=1
        
            else:
                mchain[words[j]]={}
                mchain[words[j]]['end']=1

        if j<len(words)-1:
            j=j+1

    calculateProbs(mchain)


        

def calculateProbs(inp_dict):
    for i in inp_dict:
        sum=0
        for j in inp_dict[i]:
            sum=sum+inp_dict[i][j]
        for j in inp_dict[i]:
            inp_dict[i][j]=inp_dict[i][j]/sum
    
#no indicates number of words in a line
#line indicates number of lines
def generate_words(inp_dict,no,lines):
    
    prev_word=''
    for i in range(lines):
        line=[]
        for j in range(no):
            if j==0 and i==0:
                possibilites=inp_dict['start']
            else:
                possibilites=inp_dict[prev_word]

            next_wor=''
            if len(possibilites)>1:
                probs=[]
                
                for k in possibilites:
                    probs.append(possibilites[k])
            
                for k in range(len(probs)):
                    ran=random.randint(1,100)        
                    probs[k]=probs[k]*ran

                pos=probs.index(max(probs))
                count=0
                
                if next_wor=='end':
                    possibilites=inp_dict['start']
                    for k in possibilites:
                        probs.append(possibilites[k])
                    for k in range(len(probs)):
                        ran=random.randint(1,100)        
                        probs[k]=probs[k]*ran

                    pos=probs.index(max(probs))

                for i in possibilites:
                    if count==pos:
                        next_wor=i
                        break
                    count+=1
                line.append(next_wor)
                prev_word=next_wor

            else:
                temp=(possibilites.keys())
                for i in temp:
                    next_wor=i
                if next_wor!='end':
                    line.append(next_wor)
                    prev_word=next_wor
                else:
                    probs=[]
                    possibilites=inp_dict['start']
                    for k in possibilites:
                        probs.append(possibilites[k])
                    for k in range(len(probs)):
                        ran=random.randint(1,100)        
                        probs[k]=probs[k]*ran
                    pos=probs.index(max(probs))
                    count=0
                    for i in possibilites:
                        if count==pos:
                            next_wor=i
                            break
                        count+=1
                    line.append(next_wor)
                    prev_word=next_wor
        print(line)



#Following is for testing
sentence=input()
words=sentence.split()
markovchain(words)
print(mchain)
generate_words(mchain,20,10)