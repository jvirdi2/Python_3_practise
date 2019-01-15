# Helps in getting number of instances of an element of a list if repitition is there
# Used dictionary to do this
def minion_game(in_string):
    # your code goes here
    diction=all_strings(in_string)
    vowel=['A','E','I','O','U']
    stuart_score=0
    kevin_score=0
    for key in diction:
        if key[0] in vowel:
            kevin_score=kevin_score+diction[key]
        else:
            stuart_score=stuart_score+diction[key]
    if kevin_score>stuart_score:
        print ('Kevin {}'.format(kevin_score))
    elif stuart_score>kevin_score:
        print ('Stuart {}'.format(stuart_score))
    else:
        print ('Draw')

    
def all_strings(string):
    string_diction={}
    len_string=len(string)
    for i in range(len_string):
        for j in range(i,len_string):
            con_string=string[i:j+1]
            try:
                string_diction[con_string]=string_diction[con_string]+1
            except:
                string_diction[con_string]=1
    return string_diction
