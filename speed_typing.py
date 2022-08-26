# =============================================================================
# ROUND A EXERCISE 1 - Speed Typing
# Google Kickstart 2022
#
# Programming language: Python
#
# Friday 08/26/2022 
#
# Name: Anh Duc Nguyen 
# Age: 16
# =============================================================================

# logic -> We have an "I" string, for example:
# qwertyuiop
#
# the "P" string is:
# qwertayuiopa
# 
# we see that there are two additional "a" in the "P" string
# now, we want to see if I-kth letter is equal to P-jth letter,
# if not, we are going to move to the next P-(j+1)th letter to see
# if it is equal to the I-kth  letter.
# This is the case when I-kth letter is "y". Then, the P-jth letter is "a".
# Since it is not equal, it'll move to the next P-(j+1)th letter. 
# If it is, we exclude the I-kth letter (by moving to the next 
# I-(k+1)th letter) and add it to a new variable, called c (from count) 
# -> this counts if I-kth is equal to the current P-jth letter. 
# then we compare, if c is equal to the length of the initial "I" string.
# if it's not equal, it means that there is a letter in "I" that 
# does not exist in the "P" string in the correct order.
# here for the example above, we can remove the two "a" and then
# everything will be the same.

def solve(i,p):
    # create two variables that will track the letters in "I" and "P" strings
    k,j=0,0
    # the count "c" that will allow us to check, if the letters in 
    # the "I" string are in the same order in the "P" string 
    # no matter how many letters we have to remove
    c=0
    # scan through all the letters in "I" and "P" string,
    # it'll end when either of the k,j values reach the length of 
    # either of the strings
    while k<len(i) and j<len(p):
        # check if the current letters from string "I" and "P"
        # are the same
        if i[k]==p[j]:
            # if yes, move to the next I-(k+1)th letter and P-(j+1)th letter
            k+=1
            j+=1
            # count += 1
            c+=1
        else:
            # if not, we're just gonna omit it, so we move to the 
            # next P-(j+1)th letter
            j+=1
    # check if count == length of the initial string "I"
    if c==len(i):
        # if so, we can just check the difference in the length of both
        # strings to see, how many removals we have to execute
        return len(p)-len(i)
    else:
        # otherwise, return "IMPOSSIBLE" 
        return "IMPOSSIBLE"   
    
#this is the output format that kickstart requires us to print out. 
T = int(input())
for i in range(1,T+1):
    m = input()
    n = input()
    print("Case #{}: {}".format(i, solve(m,n)))