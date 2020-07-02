# Display the count of each word in the file and sort in descending
import os, operator

def count_occurance(mylist):
    count = {}
    for x in mylist:
        count[x] = count.get(x,0) + 1
    return count

def arrange_descending(count):
        return sorted(count.items(), key = operator.itemgetter(1),reverse = True)
        
def accept_file():
    filename = input("Enter the filename: ")
    if os.path.exists(filename):
        word_count = count_occurance(open(filename).read().split())
        print(word_count)
        descending_order = arrange_descending(word_count)
        print("The Descending Order is: \n", descending_order)
    else:
        print("The file does not exist") 
    
accept_file()
