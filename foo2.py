# NOTE: I don't remember the name of this problem

def answer(x):
    # This one sounds fun!!
    # I wonder if the Google team is reading my comments...
    # I would go out and learn to do a backflip like immediately
    # Goal: Take length of string and narrow it down
    # then take length again
    # BTW I showered & watched a movie between writing this.
    # That's why it took so long.
    new_list = []
    total = len(x)
    while x != []:
        a = x[0]
        b = x[0][::-1]
        new_list.append(a)
        x = [value for value in x if value != a]
        x = [value for value in x if value != b]
    return len(new_list)