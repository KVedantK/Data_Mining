'''
Script Details:

Author: Vedant Vinayak Kulkarni
        Student, Government College Of Engineering Jalgaon.

Git: 
'''
import csv
import time


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
        SupportSet[key] = CandidateSet[key]/Transactions
    return SupportSet

def Combinator(CandidateSet):
    pass

print(GenerateCandidateSet(CSV_TO_LIST('Market_Basket_Optimisation.csv')))
print("--- %s seconds ---" % (time.time() - start_time))



