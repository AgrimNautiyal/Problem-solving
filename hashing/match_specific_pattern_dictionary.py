#question url : https://practice.geeksforgeeks.org/problems/match-specific-pattern/1
''' The function returns a  list of strings 
present in the dictionary which matches
the string pattern.
You are required to complete this method '''

def findSpecificPattern(Dict, pattern):
    #Code here
    res=[]
    lp = len(pattern)
    for i in Dict:
        if len(i)!=len(pattern):
            continue
        flag = 0
        for idx in range(lp):
            if pattern.count(pattern[idx])!= i.count(i[idx]):
                flag = 1
                break
        if flag == 0:
            res.append(i)
    return res
