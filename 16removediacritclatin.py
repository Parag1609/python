import unicodedata
import string
def shave_marks_latin(txt):
 """Remove all diacritic marks from Latin base characters"""
 norm_txt = unicodedata.normalize('NFD', txt) 
 latin_base = False
 keepers = []
 for c in norm_txt:
  if unicodedata.combining(c) and latin_base: 
   continue # ignore diacritic on Latin base char
  keepers.append(c)
  if not unicodedata.combining(c):
   latin_base = c in string.ascii_letters
 shaved = ''.join(keepers)
 return unicodedata.normalize('NFC', shaved)

text = "Café São Paulo, mañana, ありがとう"
shaved_text = shave_marks_latin(text)
print(shaved_text)
