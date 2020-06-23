# a) what are the minimum and maximum possible scores among all possible ways of filling the box?

# maximum score is when all beads are alternate, which is equal to n-1
# minimum score is when all beads are the same, which is equal to -(n-1) 


# b) Derive a general formula for all possible scores for an array of length n 

# the general formula to total number of all possible scores is n-1 where n is the length of the array.
# to find all possible scores, use pascal triangle, for n = 2 it is [1,-1] for n = 3 it is [-2,0,2] for n = 4 is [-3,-1,1,3] 

def all_possible_scores(n):
    """
    general formula for getting all possible scores where n is the length 
    of the array
    """

    scores = []
    num_of_scores = n
    if num_of_scores%2 == 0:
        # for this case there is no zero
        scores = list(range(-(num_of_scores-1),0,2)) + list(range(1,num_of_scores+1,2))
    else:
        scores = list(range(-(num_of_scores-1),0,2)) + [0] + list(range(2,num_of_scores+1,2))
    return scores


# print(all_possible_scores(3))
# print(all_possible_scores(4))
# print(all_possible_scores(5))



# c) Given n = 29, what are all possible scores. For each possible scores, how many ways can we fill the array to achieve this score 

# to find all possible scores for n = 29
print(all_possible_scores(29))
# for each possible score there are 2 ways we can fill the array, we either start with the red bead first or the blue bead first. 

# d) Given n = 938103, what are all possible scores and how many ways can we fill the array to achieve this score
scores_for_d = all_possible_scores(938103)
print('Finished part d')
# the number of ways to fill the array is 938103*2


# e) given n = 51, number of red beads is 17 and number of blue beads is 51-17=34. How many possible ways can you fill the array of boxes? For each way, what is the score of the array?

# there is a total of 51 ways to fill the array of boxes, for each way the score of the array is the same, the score of the array is 33 - 17 = 16

# f) given n = 28,173,831, the number of red beads is 12,249,491 and the remaining boxes are filled with blue seeds. How many possible ways can you fill the array of boxes?

# there is a total of 28,173,831 ways to fill the array of boxes.
    