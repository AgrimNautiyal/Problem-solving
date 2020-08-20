#question url : https://practice.geeksforgeeks.org/problems/pangram-checking-1587115620/1
''' Your task is to check if the given string is
	a panagram or not.
	
	Function Arguments: s (given string)
	Return Type: boolean
'''
def checkPangram(s):
    #code here
    s = s.lower()
    s=set([i for i in s if i.isalpha()])
    if len(s) == 26:
        return True
    else:
        return False