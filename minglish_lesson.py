# Minglish Lesson

def answer(words):
    # Goal: For each pair of consecutive words, find the
    # largest common prefix and compare the next letters
    # of each consecutive word pair. Then combine all of
    # these letter comparisons in a tree diagram/graph.
    # Parse the tree with a depth-first search to find
    # the longest strand containing the lexical order.
    tree = {}
    num_of_words = len(words)
    # subtract one b/c last word has no next pair
    for word in range(num_of_words - 1):
        branch = look_for_branches(words[word], words[word + 1])
        #print branch
        if branch != None:
            node, target = branch
            #print target
            if node in tree:
                tree[node].append(target)
            else:
                tree[node] = [target]
    temp_set = set()
    for branches in tree.values():
        for branch in branches:
            temp_set.add(branch)
    first_points = set() # initialize the node set
    for node in tree:
        if node not in temp_set:
            first_points.add(node)
    order = [] # contains final order of letters after search
    log_visited = []
    # functional depth-first search of possible orders
    # (functional equations are so cooool...)
    def traverse(node):
        if node not in log_visited:
            log_visited.append(node)
            if node in tree:
                for branch in tree[node]:
                    traverse(branch)
            order.append(node)
    for node in first_points:
        traverse(node)
    #print log_letters
    order.reverse()
    final_string = "".join(order)
    return final_string
# function to search each pair of words and look for an edge
# because of the number of embedded for loops, this seemed
# to be the most 'readable' solution
def look_for_branches(first_word, second_word):
    length = min(len(first_word), len(second_word))
    for letter_index in range(length):
        if first_word[letter_index] != second_word[letter_index]:
            return first_word[letter_index], second_word[letter_index]
# ignore my debugging cases...
#words = ["baa", "abcd", "abca", "cab", "cad"]
#words = ["ab", "bcd", "ce", "de", "e"]
#words = ["aababc", "b", "bdabbd", "cbbacd", "cbbcab", "cd", "dbda", "dcdaca"]
#words = ["ae", "afabeb", "b", "c", "decdac", "dfafcf", "ecaefb", "fafcae", "fdcfef", "ffab", "gaefdb", "gcfabd", "gfbdeb"]
#print answer(words)