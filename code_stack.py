
####################################################################################################

# prime sieve

def primeSieve(limit):

    primes = []

    number_span = [True]*(limit+1)

    number_span[0] = False
    number_span[1] = False

    for i in range(2,limit+1):

        if number_span[i] == True:
            primes.append(i)

        for j in range(i,limit+1,i):

            number_span[j] = False

    return primes

#####################################################################################################


# Python3 program to find all subsets 
# by backtracking.  
  
# In the array A at every step we have two  
# choices for each element either we can  
# ignore the element or we can include the  
# element in our subset  


def subsetsUtil(A, subset, index): 
    print(*subset) 
    for i in range(index, len(A)):  
          
        # include the A[i] in subset.  
        subset.append(A[i]) 
          
        # move onto the next element.  
        subsetsUtil(A,subset, i + 1)  
          
        # exclude the A[i] from subset and  
        # triggers backtracking. 
        subset.pop(-1)  
    return
  
# below function returns the subsets of vector A.  
def subsets(A): 
    global res 
    subset = [] 
      
    # keeps track of current element in vector A  
    index = 0
    subsetsUtil(A, subset, index)  
      
# Driver Code 
  
# find the subsets of below vector.  
array = [1, 2, 3] 
  
# res will store all subsets.  
# O(2 ^ (number of elements inside array))  
# because at every step we have two choices  
# either include or ignore.  
subsets(array)  
    