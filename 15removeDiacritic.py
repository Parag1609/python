import unicodedata
import string
def shave_marks(txt):
 """Remove all diacritic marks"""
 norm_txt = unicodedata.normalize('NFD', txt) 
 shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c)) 
 return unicodedata.normalize('NFC', shaved)

text = "Café à la mode, mañana, São Paulo"
shaved_text = shave_marks(text)
print(shaved_text)
order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
print(shave_marks(order))
Greek = 'Ζέφυρος, Zéfiro'
print(shave_marks(Greek))