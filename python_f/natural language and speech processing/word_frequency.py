'''
pre: none
post: stores an imported file and the name for a file to be outputted
'''
def get_fin_and_fout():
    while(True):
        plain_txt = input("Enter an input file name.\n")
        try:
            fin = open(plain_txt, 'r')
            break
        except:
            print("Bad File Name")
    cipher_txt = input("Input a name for the output file that will be created.\n")
    fout = open(cipher_txt,'w')
    return fin, fout

'''
pre: takes the inputted text files and then "cooks" the contents
post: outputted file is fully tokenized, including the removal of all numbers
'''
def tokenize(msg, fout):
    bad_token = [',','.','?','!','"',':',';','#','/','-','_','$','%','*','(',')','[',']','1','2','3','4','5','6','7','8','9','0']
    new_msg = ''
    for ch in msg:
        if ch not in bad_token:
            new_msg = new_msg + ch
    new_msg = new_msg.lower()
    new_msg = new_msg.replace("\n"," ")
    lst = new_msg.split()
    return lst

'''
pre: creates a dictionary with the tokenized text file
post: dictionary is made with words being keys and the num of times each word
      is counted as corresponding values
'''
def make_dict(lst):
    pp_dict = {}
    for word in lst:
        if word in pp_dict:
            pp_dict[word] = pp_dict[word] + 1
        else:
            pp_dict[word] = 1
    return pp_dict

'''
pre: takes newly created dictionary
post: creates a list of tuples out of the dictionary in which values are in
      the first position and corresponing keys are in the second position 
'''
def tupelize(pp_dict):
    lst_keys = list(pp_dict.keys())
    tuple_lst = []
    for key in lst_keys:
        tuple_lst.append((pp_dict[key], key))
    return tuple_lst

'''
pre: accepts the list of tuples
post: orders tuples in order of largest keys to smallest keys
'''
def sort_tuple_lst(tuple_lst):
    tuple_lst.sort()
    tuple_lst.reverse()
    return tuple_lst

'''
pre: accepts the ordered list of tuples
post: writes the first 50 tuples in the list in the form of a table with
      a spacing buffer that keeps all of the tuples in line
      this table is written to an output file named by the user
'''
def display_freq(tuple_lst, fout):
    fout.write("FREQUENCY            WORD\n\n")
    for tuples in tuple_lst[0:50]:
        spaces = 21 - len(str(tuples[0]))
        spaces = spaces*' '
        fout.write(str(tuples[0]) + spaces + tuples[1] + '\n')
    
    
def main():
    fin, fout = get_fin_and_fout()
    msg = fin.read()
    lst = tokenize(msg, fout)
    pp_dict = make_dict(lst)
    tuple_lst = tupelize(pp_dict)
    tuple_lst = sort_tuple_lst(tuple_lst)
    display_freq(tuple_lst, fout)

    fin.close()
    fout.close()


main()



