from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
	return render(request ,'home.html')
def count(request):
	fulltext = request.GET['fulltext']

	dictionary = {}
	wordlist = fulltext.split()
	for word in wordlist:
		if word in dictionary:
			dictionary[word] +=1
		else:
			dictionary[word] = 1 

	sortedwords = sorted(dictionary.items(),key=operator.itemgetter(1),reverse=True)

	return render(request, 'count.html', {'sortedwords':sortedwords, 'count':len(wordlist), 'fulltext':fulltext})

def about(request):
	return render(request, 'about.html')