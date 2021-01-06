
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	reverse_text = user_text [::-1]
	temp_words_in_string = user_text.split()
	words_in_string = len(temp_words_in_string)
	return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reverse_text, 'words':words_in_string})


