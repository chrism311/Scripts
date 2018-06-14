'''
In the spirit of the upcoming World Cup, I came up with a quick script.
The following script takes two lists, or dictionaries, and splits them up
evenly, according to their size. I am in a pot of 16 people, there are 32 teams 
participating. We each, randomly, draw two teams. This script gets the job done 
in 0.5s '''

import random

names = {0:'Dwight', 1:'Micheal', 2:'Kevin', 3:'Chris', 4:'Stanly', 5:'Toby', 6:'Oscar', 7:'Ryan', 8:'Angela', 9:'Phyllius', 10:'Jim', 11: 'Pam', 12:'Andy', 13:'Creed', 14:'Meredith', 15:'Erin'}
teams = {0:'Russia', 1:'Brazil', 2:'Iran', 3:'Japan', 4:'Mexico', 5:'Belgium', 6:'South Korea', 7:'Saudi Arabia', 8:'Germany', 9:'England', 10:'Spain', 11:'Nigeria', 12:'Costa Rica', 13:'Poland', 14:'Egypt', 15:'Iceland', 16:'Serbia', 17:'Portugal', 18:'France', 19:'Uruguay', 20:'Argentina', 21:'Colombia', 22:'Panama', 23:'Senegal', 24:'Morocco', 25:'Tunisia', 26:'Switzerland', 27:'Croatia', 28:'Sweden', 29:'Denmark', 30:'Australia', 31:'Peru'}

#Takes two lists of even distribution
def rand_sorter(list1, list2):
	if len(list2) % len(list1) == 0:		#Checks for even distribution
		num_list1 = range(len(list1))
		num_list2 = range(len(list2))
		random.shuffle(num_list1)
		random.shuffle(num_list2)
	
		count = 0
		ratio = len(list2)/len(list1)		#Sets the ratio of elements in list2 per element of list1
		print '\n'
		for i in num_list1:
			print list1[i] + ': ',
			x = 0
			while x < (ratio-1):				#Assigns the number of elements in list2 for each element in list1
				print list2[num_list2[count]] + ', ',
				x += 1		
				count += 1
			print list2[num_list2[count]]
			count += 1
		print '\n'
	else:
		print 'Your lists are not evenly divisible.'

if __name__ == '__main__':
	rand_sorter(names, teams)

