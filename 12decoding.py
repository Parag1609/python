octets = b'Montr\xe9al' 
print(octets.decode('cp1252')) 
#'Montréal'
print(octets.decode('iso8859_7'))
#'Montrιal'
print(octets.decode('koi8_r')) 
#'MontrИal'
octets.decode('utf_8') 
"""UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5:"""
print(octets.decode('utf_8', errors='replace')) 
#'Montr�al