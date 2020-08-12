#question url : https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0
from itertools import permutations
t = int(input())
for i in range(t):
    inp = input()

    #simple logic : just create sorted list of permutations of a string and join into a string using a ' ' separator
    perm = ' '.join(sorted([''.join(i) for i in list(permutations(inp, len(inp)))]))
    print(perm)