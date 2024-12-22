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

single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""", 
 """'f"*^<''""---~>""")
multi_map = str.maketrans({ 
 '€': '<euro>',
 '…': '...',
 'Œ': 'OE',
 '™': '(TM)',
 'œ': 'oe',
 '‰': '<per mille>',
 '‡': '**',
})
multi_map.update(single_map) 
def dewinize(txt):
 """Replace Win1252 symbols with ASCII chars or sequences"""
 return txt.translate(multi_map) 
def asciize(txt):
 no_marks = shave_marks_latin(dewinize(txt)) 
 no_marks = no_marks.replace('ß', 'ss') 
 return unicodedata.normalize('NFKC', no_marks)
order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
print(dewinize(order))
#'"Herr Voß: - ½ cup of OEtker(TM) caffè latte - bowl of açaí."' 
print(asciize(order))
#'"Herr Voss: - 1⁄2 c