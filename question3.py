# implement an algorithm to determine if a string has all unique characters. You cannot use additional data structures (eg.Hashmap). Recommended time complexity: O(n) or lesser

# Example:
# input:  'Banana'
# Output: False (as there are 2'n' and 3'a')


def all_unique(word='Banana'):
    characters = [False] * 128 # assume total of 128 cha in ascii

    for ch in word:
        num = ord(ch)
        if characters[num]:
            return False
        characters[num] = True
    return True 
    



if __name__ == "__main__":
    print(all_unique())