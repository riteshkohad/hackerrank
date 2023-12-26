

"""
Time complexity:
The time complexity of this function is O(n * k), where n is the length of the input DNA sequence s and k is the 
length of the subsequences we are looking for. This is because we iterate through the DNA sequence once with a 
sliding window of length k, and for each window, we perform a lookup in the set all_sets, which has a time complexity 
of O(1) on average. Therefore, the overall time complexity is O(n * k).

Space complexity:
The space complexity of the function is O(n), where n is the length of the input string s. This is because we are using 
two sets, all_sets and output, to store the subsequences and repeating patterns. The size of these sets will depend on 
the number of repeated subsequences found in the input string. Additionally, the space complexity of the built-in Python 
functions used (such as set() and add()) is constant and does not depend on the size of the input.
"""

def find_repeated_sequences_brute_force(s, k):
    # define empty sets
    all_sets = set()
    output = set()

    # define pointers for the window 
    start = 0
    end = k

    # loop 
    while end <= len(s) -1:
        # take a substring, when slicing internally it will loop from start to end 
        # this needs to be optimized
        # to optimize, we can use hash set 
        sub = s[start: end]

        # check if substring exists in the all sets
        if sub in all_sets:
            # if it does, then add to the output its repeating pattern 
            output.add(sub)
        else: 
            # if not, add it in the all sets to compare it again 
            all_sets.add(sub)

        # move the window 
        start += 1
        end += 1

    # return the output set 
    return output


"""
Time complexity: 
The time complexity of the function is O(n), where n is the length of the input DNA sequence. This is because we 
iterate through the DNA sequence once to convert each character to its corresponding numeric value, and then iterate 
through the sequence again to calculate the hash values and check for duplicates. The built-in Python functions used 
in the code, such as len(), append(), get(), and set.add(), have constant time complexity and do not significantly 
affect the overall time complexity of the function.

Space complexity:
The space complexity of the function Repeated DNA Sequences is O(n), where n is the length of the input DNA sequence s. 
This is because the function uses additional space to store the numeric values of each character in the DNA sequence (str_numbs), 
a hash set to store the hash values (hash_set), and an output set to store the repeated subsequences (output_set). 
The space complexity of built-in Python functions invoked by the code is not considered in this analysis.
"""

def find_repeated_sequences(s, k):
    len_str = len(s)

    # matching pattern could be any of these combination upto "k" length 
    # so defining its code 
    dna_series = {"A": 1, "C": 2, "G": 3, "T": 4}

    # defining a base value as 4 because there can be only 4 dna series 
    base_value = 4 

    # define an array same length as k
    str_numbs = []

    # fill in a corresponding numeric values of each char from string s 
    for i in range(len_str):
        str_numbs.append(dna_series.get(s[i]))

    # print(str_numbs)
    
    # declare variables 
    hash_val = 0
    hash_set = set()
    output_set = set()

    # loop thru length - k + 1
    for i in range(len_str - k + 1):
        # if i == 0 that means look just started 
        if i == 0:
            # calculate the hash value of first k chars
            for j in range(k):
                # look thru all first k chars 
                hash_val += str_numbs[j] * (base_value ** (k-j-1))
                # print(hash_val)
            
            # print("-"*10)

        else:
            # otherwise preserve the hash value 
            prev_hash_val = hash_val 
            
            # compute the new hash value by 
            # removing previous element, shifting remaining value by 1 base value
            # adding new value of new char
            hash_val = ((prev_hash_val - str_numbs[i - 1] * (base_value ** (k-1))) * base_value) + str_numbs[k + i -1]
            # print(hash_val)
        
        # check if hash value is in the hash set
        if hash_val in hash_set:
            # if yes, add slice of a string in the output because it is duplicate
            output_set.add(s[i: i+k])
        else: 
            # if no, add it in the hash val set to check next time 
            hash_set.add(hash_val)

    # return the output 
    return output_set


if __name__ == "__main__":
    input_str = "AAAAACCCCCAAAAACCCCCC"
    numbs = 8

    result = find_repeated_sequences(input_str, numbs)
    print(result)
