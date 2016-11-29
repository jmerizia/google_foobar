# NOTE: I don't remember the name of this problem

def answer(words):
    # Goal: Determine all the letters
    # then check first letters for similarity; if they're different
    # that's their order. Fir similar first letters, check the
    # next letter. Once all letters are account for, output
    # the order string.
    first_letters = [each_word[:1] for each_word in words]
    unique_letters = []
    for x in first_letters:
        if x not in unique_letters:
            unique_letters.append(x)
    print unique_letters
    number_of_words = len(words)
    order = []
    for j in range(len(unique_letters)): # repeats for every unique first letter
        if first_letters.count(unique_letters[j]) == 1:
            # find corresponding word in words
            same_letter_word = [each_word for each_word in words if (each_word[0] in unique_letters[j])][0]
            order.append(same_letter_word)
            words.remove(same_letter_word)
        if first_letters.count(unique_letters[j]) > 1:
            # find words that start with unique_letters[j]
            same_letter_words = [each_word for each_word in words if (each_word[0] in unique_letters[j])]
            print same_letter_words
            # take length of words and find the shortest length
            #shortest_length = min([len(each_word) for each_word in same_letter_words])
            for i in range(len(same_letter_words)):
                # remove first letter
                trimmed_word = same_letter_words[i][1:]
                # replace in words list
                word_index = words.index(same_letter_words[i])
                words[word_index] = trimmed_word
    print words
    return order