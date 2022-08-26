# =============================================================================
# ROUND A EXERCISE 2 - Challenge Nine
# Google Kickstart 2022
#
# Programming language: Python
#
# Friday 08/26/2022 
#
# Name: Anh Duc Nguyen
# Age: 16
# =============================================================================
 
def solve(n):
    # create a list filled with digits from the n number
    w = [int(i) for i in str(n)]
    
    # check if the number is already divisible by 9, if so, 
    # we're just going to insert to the 2nd position (index 1) of the 
    # n number so we receive the smallest number possible
    if sum(w)%9==0: 
        w.insert(1,0)
        return "".join(map(str,w))
    # We do this because the additional number 0 cannot be inserted at
    # the beginning (no leading zeros)
    
    # if n % 9 !==0, create an array filled with numbers,
    # that - when you insert them, the sum of all the digits
    # will be divisible by 9. 
    ar = []
    for i in range(1,9):
        if (sum(w)+i)%9==0:
            ar.append(i)
    # what we need only is the smallest number that will
    # fulfill the requirement
    ans = min(ar)
    # now we find the place to insert the additional number
    # so that we receive the smallest possible number divisible by 9
    for j in range(len(w)): 
        # that's why here we're checking if the additional number is
        # smaller then the current digit in the "list of digits of n"
        # eg. in the number 915, the smallest number needed to insert
        # is 3. if 3<9, we should insert it before 9 to minimize the 
        # number -> 915 -> 3915
        if ans<w[j]: 
            w.insert(j,str(ans))
            return "".join(map(str,w))
            break
    else: 
        # else we're gonna insert that number at the end 
        # because it's greater than any other digits in the n number
        w.insert(len(w),str(ans))
        return "".join(map(str,w))

#this is the output format that kickstart requires us to print out. 
T = int(input("c:"))
for i in range(1,T+1):
    n = int(input("n: "))
    print("Case #{}: {}".format(i, solve(n)))