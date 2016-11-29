# NOTE: I don't remember the name of this problem

def answer(x, y, z):
    #month interval: 1 -> 12
    #day interval: 1 -> 31
    #year interval: 0 -> 99
    output = {"month":00, "day":00, "year":00}
    final_answer = ""
    amb = False

    if x != y and x != z and y != z: #none are equal
        if 31 <= x <= 99 or x == 0: # X IS YEAR
            output["year"] = x
            if 12 < y <= 31:
                output["day"] = y
                output["month"] = z
            else:
                if 12 < z <= 31:
                    output["day"] = z
                    output["month"] = y
                else:
                    amb = True
        elif 31 <= y <= 99 or y == 0: # Y IS YEAR
            output["year"] = y
            if 12 < x <= 31:
                output["day"] = x
                output["month"] = z
            else:
                if 12 < z <= 31:
                    output["day"] = z
                    output["month"] = x
                else:
                    amb = True
        elif 31 <= z <= 99 or z == 0: # Z IS YEAR
            output["year"] = z
            if 12 < x <= 31:
                output["day"] = x
                output["month"] = y
            else:
                if 12 < y <= 31:
                    output["day"] = y
                    output["month"] = x
                else:
                    amb = True
        else:
            amb = True

    elif x == y and y == z: #all are equal
        output["month"] = x
        output["day"] = x
        output["year"] = x


    elif x == y: # Z is different
        if 31 <= z <= 99 or z == 0:
            output["year"] = z
            output["month"] = x
            output["day"] = x
        elif 12 < x <= 31:
            output["month"] = z
            output["year"] = x
            output["day"] = x
        else:
            amb = True
    elif x == z: # Y is different
        if 31 <= y <= 99 or y == 0:
            output["year"] = y
            output["month"] = x
            output["day"] = x
        elif 12 < x <= 31:
            output["month"] = y
            output["year"] = x
            output["day"] = x
        else:
            amb = True
    elif y == z: # X is different
        if 31 <= x <= 99 or x == 0:
            output["year"] = x
            output["month"] = y
            output["day"] = y
        elif 12 < y <= 31:
            output["month"] = x
            output["year"] = y
            output["day"] = y
        else:
            amb = True

    if amb:
        return "Ambiguous"
    elif not amb:
        if len(str(output["month"])) == 1:
            output["month"] = "0" + str(output["month"])
        if len(str(output["day"])) == 1:
            output["day"] = "0" + str(output["day"])
        if len(str(output["year"])) == 1:
            output["year"] = "0" + str(output["year"])
        output["month"] = str(output["month"])
        output["day"] = str(output["day"])
        output["year"] = str(output["year"])
        return "%s/%s/%s" %(output["month"], output["day"], output["year"])
        
        
        
        
        