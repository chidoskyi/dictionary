from django.shortcuts import render
from PyDictionary import Dictionary
from PyMultiDictionary import MultiDictionary


# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def word(request):
    search = request.GET.get('search')
    dictionary = MultiDictionary()
    
    # Get the meaning of the word
    meaning = dictionary.meaning('en', search)
    # The meaning method returns a tuple, where the second element is the actual meaning
    meaning_text = meaning[1]if meaning else "No meaning found"
    # 
    
    # Get synonyms and antonyms
    synonyms = dictionary.synonym('en', search)
    antonyms = dictionary.antonym('en', search)
    
    context = {
        'meaning': meaning_text,
        'synonyms': synonyms,
        'antonyms': antonyms,
        'search': search,
    }
    return render(request, 'word.html', context)
