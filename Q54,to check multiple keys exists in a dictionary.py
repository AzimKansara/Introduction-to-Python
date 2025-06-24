my_dic={'a':1,'b':2,'c':3}
key_check=['a','b','c']

all_excite= True

for i in key_check:
    if i not in my_dic:
        all_excite= False
         
print("All key Exciste",all_excite)