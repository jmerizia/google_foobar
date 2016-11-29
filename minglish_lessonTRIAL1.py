# Minglish Lesson (TRIAL)

def answer(words):
    # Goal: For each pair of consecutive words,
    # find the largest common prefix. Subtract this prefix
    # from its respective word and compare the next letter.
    # Combine all of these letter comparisons
    import os
    order = []
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        common_prefix = os.path.commonprefix([current_word, next_word])
        # NOTE: common_prefix is a string
        if common_prefix != "":
            # if the prefix is equal to either word, the iteration isn't useful
            if common_prefix != current_word and common_prefix != next_word:
                common_prefix_list = list(common_prefix)
                current_word_list = list(current_word)
                next_word_list = list(next_word)
                for j in range(len(common_prefix)):
                    current_word_list.remove(common_prefix_list[j])
                    next_word_list.remove(common_prefix_list[j])
                order.append(current_word_list[0] + next_word_list[0])
        elif common_prefix == "":
            order.append(current_word[0] + next_word[0])
    # I used a while loops so I could have more control later on
    # initial conditions:
    keep_looking = True
    run_again = True
    k = 0
    l = 0
    errr = False
    print order
    while run_again == True:
        keep_looking = True
        l = 0
        while keep_looking == True:
            # check for a match
            if len(order) == k:
                errr = True
                break
            if order[k][-1:] == order[l][0]:
                combined = order[k] + order[l][1:]
                test = order[k]
                # delete them from order[]...
                if order.index(order[k]) > order.index(order[l]):
                    order.remove(order[k])
                    order.remove(order[l])
                elif order.index(order[k]) < order.index(order[l]):
                    order.remove(order[l])
                    order.remove(order[k])
                # append new comparison...
                order.append(combined)
                break
            # if no match is found...
            if len(order) - 1 == l:
                keep_looking = False
                if len(order) - 1 > k:
                    k += 1
            l += 1
        if len(order) == 1:
            run_again = False
        if errr:
            run_again = False
        break
    if errr:
        return "No possible solution"
    else:
        return order[0]