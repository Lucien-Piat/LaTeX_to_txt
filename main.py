import re

#Open the pasting file
with open('input_folder/paste_file.txt', 'r', encoding='utf-8') as file:
    untreated_lines = file.readlines()

#Split the line into a list of words
def string_to_list(string):
    return re.split(r'[ {}\n\t]+', string)

#Remove any lone bracket
def remove_empty_list_item(list):
    cleaned_list = []
    for i in list : 
        if i != "":
            cleaned_list.append(i)
    return cleaned_list

#Remove any string with \ 
def remove_backslash(list):
    cleaned_list = []
    for i in list : 
        if i[0] != "\\":
            cleaned_list.append(i)
    return cleaned_list

#Rebuild string
def rebuild_string(list):
    build_string = ""
    for item in list : 
        build_string += item + " "
    return build_string

# Apply all the computation to the 
def compute_line(line, keywords):
    list = string_to_list(line)
    if list[0] == '%': 
        return 
    treated_list = remove_empty_list_item(list)
    treated_list = remove_backslash(treated_list)
    treated_list = remove_keywords(treated_list, keywords)
    return rebuild_string(treated_list)
    

def remove_keywords(list, keywords):
    for word in keywords :
         list = remove_a_word(word, list)
    return list


def remove_a_word(word_to_remove, list):
    cleaned_list = [] 
    for item in list :
        if item != word_to_remove:
            cleaned_list.append(item)
    return cleaned_list

def compute_text(text, keywords):
    for line in text : 
        print(compute_line(line, keywords))


keywords = ['frame', 'itemize']
compute_text(untreated_lines, keywords)



