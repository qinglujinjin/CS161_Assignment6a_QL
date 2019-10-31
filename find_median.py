#Author: Qing Lu
#Date: 10/30/2019
#Description: Find median of list of numbers through sorting

def find_median(lst):
    n = len(lst) # find length of the list
    s = sorted(lst) # sort list
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2]

print(find_median([1, -4, -1, -1, 1, -3]))