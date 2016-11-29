# Minglish Lesson (TRIAL) 

def answer(words):
    # Goal: For each pair of consecutive words,
    # find the largest common prefix. Subtract this prefix
    # from its respective word and compare the next letter.
    # Combine all of these letter comparisons
    import os
    order = []
    answer = ""
    max_letters = len("".join(set("".join(words))))
    
    def commonprefix(m):
        if not m: return ''
        s1 = min(m)
        s2 = max(m)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
		return s1
    
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        common_prefix = commonprefix([current_word, next_word])
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
    order = [list(set(order))] # remove repeats
    # this part took forever btw...


    def A(list, k):
        final_list = []
        for i in range(len(list)):
            if list[k][-1:] == list[i][0]:
                copy_list = list[:]
                one = list[k]
                two = list[i]
                copy_list.remove(one)
                copy_list.remove(two)
                copy_list.append(one + two[1:])
                final_list.append(copy_list)
        if final_list == []:
            final_list = [[]]
        return final_list


    def B(list):
        done_list = list[:]
        for j in range(len(list)):
            for incr in range(len(list[j])):
                if list[j] != []:
                    new_lists = A(list[j], incr)
                    answer = is_it(new_lists)
                    if answer != "":
                        return answer
                    old_list = list[j][:]
                    if new_lists != [[]]:
                        for m in range(len(new_lists)):
                            done_list.append(new_lists[m])
            done_list.remove(old_list)
        return done_list


    def is_it(list_of_orders):
        final = ""
        for p in range(len(list_of_orders[0])):
            if len(list_of_orders[0][p]) == max_letters:
                final = list_of_orders[0][p]
        return final


    while answer == "":
        old_order = order[:]
        order = B(order)
        if old_order == order:
            order = "ERROR"
            break
        elif old_order != order:
            if isinstance(order, basestring):
                break
    return order

#words = ["ae", "afabeb", "b", "c", "decdac", "dfafcf", "ecaefb", "fafcae", "fdcfef", "ffab", "gaefdb", "gcfabd", "gfbdeb"]
#print answer(words)