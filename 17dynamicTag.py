def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class']=cls
    if attrs:
        attrs_str= ''.join(' %s="%s"' %(attr, value) for attr, value in sorted(attrs.items()))
    else:
        attrs_str=''
    if content:
        return '\n'.join('<%s %s>%s<%s/>'% (name ,attrs_str, c, name) for c in content)
    else:
        return '<%s%s/>'%(name, attrs_str)
    
print(tag('br')) 
#'<br />'
print(tag('p', 'hello')) 
#'<p>hello</p>'
print(tag('p', 'hello', 'world'))
#<p>hello</p>
#<p>world</p>
print(tag('p', 'hello', id=33)) 
#'<p id="33">hello</p>'
print(tag('p', 'hello', 'world', cls='sidebar')) 
#<p class="sidebar">hello</p>
#<p class="sidebar">world</p>
print(tag(content='testing', name="img")) 
#'<img content="testing" />'
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
print(tag(**my_tag))

