import re
import random
import nltk

colors = ['red','green','yellow','blue','white','black']

def main():
    print(' '*100)
    print("Welcome Here!!")
    print('-'*80)
    print("* Type 'quit' when you have had enough.")
    print('-'*80)

     
    print("\nChatBot :-> Please enter your favourite colour\n")
    print '\n'.join(colors)
    

    clr = raw_input("\n""I->")
    r = re.compile(clr)

    if not filter(r.match,colors):
	print("ChatBot :-> Please enter any colour from the displayed list")
    else:
       if re.search(r'blue|Blue',clr):
	   print("ChatBot :-> Wrong!")
           exit()
       else:
           fav_clr = clr 
           print('\n ChatBot :->', clr , ' is fine. Thank you!')
        	
    
if __name__ == "__main__":
    main()
