from typing import List



class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hash_dict = {"A": 1, "C": 2, "G": 3, "T": 4}
        hash_base = 4

        hash_list = []
        for i in range(len(s)):
            hash_list.append(hash_dict.get(s[i]))

        # print(hash_list)
        hash_set = set()
        output = set()
        hash_val = 0

        str_len = 10
        for i in range(len(s) - str_len + 1):
            if i == 0:
                for j in range(str_len):
                    # calculate seq number to use an exponential value 
                    # seq = 10 - 0 - 1 = 9 then 10 - 1 - 1 = 8 then 7 and so on 
                    seq = (str_len - j - 1)

                    # this will calculate like hash_list[j] * (4 ^ 9), then hash_list[j] * ( 4 ^ 8) and so on
                    tmp_hash = hash_list[j] * (hash_base ** seq)
                    # print(f"temp hash for {j} : {tmp_hash}")

                    hash_val += tmp_hash

                    # hash_set.add(hash_val)
                
                # print(hash_val)
            else:
                # take a previous hash value 
                prev_hash = hash_val

                # remove the last value from prev_hash and add the current value 
                prev_hash_to_remove = hash_list[i - 1] * (hash_base ** (str_len-1))
                new_hash_to_add = hash_list[str_len + i -1]
                tmp_new_val = ( (prev_hash - prev_hash_to_remove) * hash_base ) + new_hash_to_add
                # print(f"value to remove: {i -1}: {prev_hash_to_remove} AND to add {str_len + i + 1}: {new_hash_to_add} - calculation {tmp_new_val}")
                hash_val = tmp_new_val

            if hash_val in hash_set:
                output.add(s[i: i+str_len])
            else:
                hash_set.add(hash_val)

        return list(output)
    






def main():
    inpt = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    ret_val = Solution().findRepeatedDnaSequences(inpt)
    print(ret_val)
    ret_val = Solution().findRepeatedDnaSequencesStr(inpt)


if __name__ == "__main__":
    main()

