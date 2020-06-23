from itertools import permutations

def check_perm_palindrome(word="Tact Coa"):
    word = word.replace(' ','').lower()
    perms = [''.join(x) for x in list(permutations(word))]
    perms = list(set(perms))
    print(perms)
    for word in perms:
        if word == word[::-1]:
            return True


if __name__ == "__main__":
    print(check_perm_palindrome())