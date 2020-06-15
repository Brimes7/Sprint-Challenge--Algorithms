'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #We need to check if it is less than 2 letters or if nothing is entered
    if len(word) < 2 or len(word) == 0:
        #This cannot be none
        return 0
    #This slices these 2 letters
    elif word[:2] == "th":
        #here we are goig to return the occurrense recursively
        #we must increment by 1
        return count_th(word[1:]) + 1
    else:
        #otherwise return the occurrences and be done.
        return count_th(word[1:])
