'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.


Can do some array method ... Search 
'''
def count_th(word):
    #Need to put a base case for index 0 .. add 1 when "th" is found 
    th = 'th'

    if len(word) == 0 or len(word) < len(th): #if the word is less than "th" return 0
        return 0
    if word[0:len(th)] == th: #go from index 0 to th length
        return count_th(word[len(th)-1:]) + 1 #add +1 when th is found and run it recursively; Basically checks every array indice one by one and adds a count if "th" is found
    
    return count_th(word[len(th)-1:]) #return when th is no longer found 


#recursive yes .. efficient?  debatable
