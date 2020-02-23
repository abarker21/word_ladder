#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    #Base case: if both words are the same, then the pathway to get from the start to the end
    #word is 0 so the whole path is just the start of the word
    if start_word == end_word:
        same_word = [start_word]
        return same_word

    #This is opening and reading in the dictionary file and it's splitting the file into a new
    #element for each line break we have. The ladder_stack makes an empty list and adds in the
    #start word with the append funciton and then we create an empty deque which is has the
    #stack created above as the first element in the deque.
    Dictionary = open(dictionary_file)
    Dictionary_List = Dictionary.read().split("\n")
    ladder_stack = []
    ladder_stack.append(start_word)
    ladder_deque = deque()
    ladder_deque.append(ladder_stack)

    #Keeps going until we've gotten from the start word to the end word. x is the current step in
    #functions process in moving towards the end_word. Now we check through the dictionary file
    #for words that are only one letter different from current word we're checking and if it's only
    #one word different then we check first if the word we currently have is equal to the end word.
    #If it is, then we return x which will show the  current pathway which gets to end_word. If we're
    #not at end_word yet, then we create a deepcopy of x as another stack and put in the next word in
    #the dictionary into the stack and then append that into the deque using appendleft. Then we run
    #through the function again until we reach the path we're looking for.
    while len(ladder_deque) > 0:
        x = ladder_deque.pop()
        print(x)
        for word in Dictionary_List:
            if _adjacent(word,x[len(x)-1]) == True:
                if word == end_word:
                    x.append(word)
                    return x
                else:
                    ladder_copy = deepcopy(x)
                    ladder_copy.append(word)
                    ladder_deque.appendleft(ladder_copy)
                    Dictionary_List.remove(word)


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    if len(ladder) == 0:
        return False
    else:
        for i in range(len(ladder)):
            if _adjacent(ladder[i],ladder[i+1]) == False:
                return False
            else:
                return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    diff = 0
    n = len(word1)
    if len(word1) != len(word2):
        return False
    else:
        for i in range(n):
            if word1[i] == word2[i]:
                diff + 0
            else:
                diff += 1
    if diff == 1:
        return True
    else:
        return False






