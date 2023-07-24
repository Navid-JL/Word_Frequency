
word_lst=[]
word_counter_lst=[]
input_sent="Car Car is big big"

word_lst=input_sent.split()

def extractDigits(lst):
    return [[element,0] for element in lst]

word_index_lst=extractDigits(word_lst)

for i in range (len(word_index_lst)):
    j=i+1
    while j < len(word_index_lst):
        if word_index_lst[i][0]==word_index_lst[j][0]:
            word_index_lst[i][1]+=1
            word_index_lst.pop(j)
        j+=1

print(word_index_lst)

x=sorted(word_index_lst)

print(x)