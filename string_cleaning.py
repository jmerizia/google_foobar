# String Cleaning

def answer(chunk, word):

    # This script starts from the end of the chunk
    # and uses a pointer to check each set of
    # letters that are as long as the given word
    # for a copy for the word. In order to create
    # the loxicographically earliest string, a 
    # breadth-first search finds all of the 
    # end-nodes, then the script orders them by
    # loxicographical/alphabetical order. The
    # first occurance in that list is returned.

    # initialtize the first node...
    chunks = [chunk]

    while True:
        # the good old macgyver before/after technique...
        chunks_before = chunks[:]
        chunks = checkMatches(chunks, word)
        if chunks_before == chunks:
            return sorted(chunks)[0]

def checkMatches(chunks, word):
    new_chunks = []
    for elem in chunks:
        match_found = False
        for pointer in range(len(elem) - len(word) + 1):
            if ( elem[pointer:len(word)+pointer] == word ):
                # word matches
                new_chunk = elem[:pointer] + elem[pointer+len(word):]
                if new_chunk not in new_chunks:
                    new_chunks.append(new_chunk)
                match_found = True
        if match_found == False:
            # if there is no match...
            new_chunks.append(elem)
    return new_chunks

print answer("cadodogdogdogdoggtdogddogododogggdog", "dog")






