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
    meaning_text = meaning[1] if meaning else "No meaning found"
    
    # Get synonyms and antonyms
    synonyms = dictionary.synonym('en', search)
    antonyms = dictionary.antonym('en', search)
    
    # Check if results are empty or None
    if not meaning_text or not synonyms or not antonyms:
        meaning_text = "No meaning found"
        synonyms = "No synonyms found"
        antonyms = "No antonyms found"
        
    

    
    context = {
        'meaning': meaning_text,
        'synonyms': synonyms,
        'antonyms': antonyms,
        'search': search,
    }
    return render(request, 'word.html', context)
