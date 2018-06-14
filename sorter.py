import random

names = {0:'Nessly', 1:'Jackie', 2:'Luis', 3:'Chris', 4:'Cesar', 5:'Steph', 6:'Vanessa', 7:'David', 8:'Adriana', 9:'Arturo', 10:'Maria', 11: 'Mitch', 12:'Bubba', 13:'Silvia', 14:'Mary', 15:'Jose'}
teams = {0:'Russia', 1:'Brazil', 2:'Iran', 3:'Japan', 4:'Mexico', 5:'Belgium', 6:'South Korea', 7:'Saudi Arabia', 8:'Germany', 9:'England', 10:'Spain', 11:'Nigeria', 12:'Costa Rica', 13:'Poland', 14:'Egypt', 15:'Iceland', 16:'Serbia', 17:'Portugal', 18:'France', 19:'Uruguay', 20:'Argentina', 21:'Colombia', 22:'Panama', 23:'Senegal', 24:'Morocco', 25:'Tunisia', 26:'Switzerland', 27:'Croatia', 28:'Sweden', 29:'Denmark', 30:'Australia', 31:'Peru'}


def rand_sorter(list1, list2):
	if len(list2) % len(list1) == 0:
		num_list1 = range(len(list1))
		num_list2 = range(len(list2))
		random.shuffle(num_list1)
		random.shuffle(num_list2)
	
		count = 0
		ratio = len(list2)/len(list1)
		print '\n'
		for i in num_list1:
			print list1[i] + ': ',
			x = 0
			while x < (ratio-1):
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

