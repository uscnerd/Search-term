import re
file1 = "hitchhikers.txt"
file2 = "warp_drive.txt"
file3 = "french_armed_forces.txt"
def string_matching(search_term):
    
	file  = open(file1, 'r').read()
	count = file.count(search_term)
	print("search term ", search_term," ",file1, " count ",count)
	file2_open = open(file2, 'r').read()
	count = file2_open.count(search_term)
	print("search term ", search_term," ",file2, " count ",count)
	file3_open = open(file3, 'r').read()
	count = file3_open.count(search_term)
	print("search term ", search_term," ",file3, " count ",count)

def regex_text_search(search_text):
	f = open(file1, 'r')
	words = sum(len(re.findall(search_text, w, re.M|re.I)) for w in f)
	print (search_text, " count using regex in ", file1, " ",words)
	f.close()
	f = open(file2, 'r')
	words = sum(len(re.findall(search_text, w, re.M|re.I)) for w in f)
	print (search_text ," count using regex in ", file2, " ",words)
	f.close()
	f = open(file3, 'r')
	words = sum(len(re.findall(search_text, w, re.M|re.I)) for w in f)
	print (search_text ," count using regex in ", file3, " ",words)
	f.close()

word_count_f1 = {}
word_count_f2 = {}
word_count_f3 = {}
def preprocess():
	print("PREPROCESS")
	logfile = open(file1, "r") 
	for word in logfile.read().split():
		if word not in word_count_f1:
			word_count_f1[word] = 1
		else:
			word_count_f1[word] += 1
	logfile = open(file2, "r") 
	for word in logfile.read().split():
		if word not in word_count_f2:
			word_count_f2[word] = 1
		else:
			word_count_f2[word] += 1
	logfile = open(file3, "r") 
	for word in logfile.read().split():
		if word not in word_count_f3:
			word_count_f3[word] = 1
		else:
			word_count_f3[word] += 1
def preprocess_search(search_word):
	if search_word in word_count_f1.keys():
		print(search_word ," count  in", file1, word_count_f1[search_word])  
	else:# search_word in word_count_f1.keys():
		print(search_word ," count  in", file1, 0)  
	if search_word in word_count_f2.keys():
		print(search_word ," count  in", file2, word_count_f2[search_word])  
	else:# search_word in word_count_f2.keys():
		print(search_word ," count  in", file2, 0)  
	if search_word in word_count_f3.keys():
		print(search_word ," count  in", file3, word_count_f3[search_word])  
	else:# search_word in word_count_f3.keys():
		print(search_word ," count  in", file3, 0)  
preprocess()   
search_term = input("Enter search term ")    
finish = False
while finish == False:
	option = input(" Choose an option for search 1.)string match 2.) regex match 3.) preprocess 4.) Enter new Search Term ")
	if option == "1":
		string_matching(search_term)
	elif option == "2":
		regex_text_search(search_term)
	elif option == "3":
		preprocess_search(search_term)
	elif option == "4":
		search_term = input("Enter new Search term")
	else:
		finish = True
		print("finish")
		break

