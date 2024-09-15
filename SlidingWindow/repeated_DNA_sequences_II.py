
def find_repeated_sequences(s, k):
    matching_set = set()
    output_set = set()

    dna_numbers = {"A": 1, "C": 2, "G": 3, "T": 4}
    base_value = 10

    hash_val = 0

    for i in range(k):
        dna_num = dna_numbers.get(s[i])
        print(f"dna num: {dna_num} for {s[i]}")
        hash_val += dna_num * (base_value ** (k - i -1))
        print(f"hash value: {hash_val}")

    matching_set.add(hash_val)
    prev_hash_val = hash_val
    for i in range(len(s)-k):

        if i == 0:
            continue
        
        hash_val_remove = dna_numbers.get(s[i - 1]) * (base_value ** (k-1))
        hash_val_add = dna_numbers.get(s[i - 1])
        print(f"value to remove: {hash_val_remove}, val to add {hash_val_add}")
        hash_val = ((prev_hash_val - hash_val_remove) * base_value) + hash_val_add
        # hash_val = ((prev_hash_val - dna_numbers.get(s[i - 1]) * (base_value ** (k-1))) * base_value) + dna_numbers.get(s[k + i -1])
        print(f"new hash val: {hash_val} - old hash val: {prev_hash_val}")
        if hash_val in matching_set:
            output_set.add(s[i:k+i])
        else:
            matching_set.add(hash_val)
        
        prev_hash_val = hash_val

    return output_set





if __name__ == "__main__":
    input_str = "AAAAACCCCCAAAAACCCCCC"
    numbs = 8

    result = find_repeated_sequences(input_str, numbs)
    print(result)