'''
Script Details:
        cript Generates frequent Itemset Needed for Apriori Rule Generation.

Git: 
'''
import csv
import time
import itertools


start_time = time.time()
# CSV to list format
def CSV_TO_LIST(csvfile):
    with open(csvfile) as f:
        reader = csv.reader(f)
        data = list(reader)
        return data
# creates candidateset as {'product' : frequency} dataset is in form [[T1], [T2]...]
def GenerateCandidateSet(Dataset):
    CandidateSet = {}
    for i in range(0,len(Dataset)):
        for j in range(0,len(Dataset[i])):
            if Dataset[i][j].lower() in CandidateSet:
                CandidateSet[Dataset[i][j].lower()][0] += 1
                CandidateSet[Dataset[i][j].lower()][1].append(i)
            else:
                CandidateSet[Dataset[i][j].lower()] = [1]
                CandidateSet[Dataset[i][j].lower()].append([i])
    return CandidateSet
    #return Format {'Unique Item' : [frequency, [rows in which it was found]]}

# Generates Support for each
def CreateFrequentSet(CandidateSet):
    SupportSet = {}
    Transactions = len(CandidateSet)
    for key in CandidateSet:
        SupportSet[key] =   int((CandidateSet[key][0]/Transactions)*10)
    return SupportSet

final_set = (GenerateCandidateSet(CSV_TO_LIST('testdata.csv')))
#print(final_set)

def SetGenerater(data_set, threshold):
    items = data_set.keys()
    transactions = len(CSV_TO_LIST('testdata.csv'))
    All_Com = []
    Final_Frequent_Sets = []
    for i in range (1,len(items)):
        comb = list(itertools.combinations(items, i))
        All_Com.append(comb)
    for i in All_Com:
        if i == 0:
            for j in i:
                for item in j:
                    f = int((data_set[item][0]/transactions)*100)
                    if f > threshold:
                        Final_Frequent_Sets.append(j)
        else:
            for j in i:
                sets = []
                for item in j:
                    s = set(data_set[item][1])
                    sets.append(s)
                    print("For Itemset {}".format(j))
                    print(int((len(set.intersection(*sets))/transactions)*100))
                if int((len(set.intersection(*sets))/transactions)*100) > threshold:
                    Final_Frequent_Sets.append(j)
                    
    return Final_Frequent_Sets

print(SetGenerater(final_set, 50))
print("--- %s seconds ---" % (time.time() - start_time))
