def pyradmid_decode(size,phrase_array):
    #decodes array by creating step function to keep removing elements from array over time.
    # each loop returns 1 of the words to add to the decoded string
    string = ""
    total = 0
    step = 1
    while total < size:
        string += phrase_array[step - 1]
        phrase_array = phrase_array[step:]
        string += " "
        step += 1
        total += step
    
    return string

# I dogs love cats you computers 