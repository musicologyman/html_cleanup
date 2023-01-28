# coding: utf-8
from bs4 import BeautifulSoup
with open('index.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    
script_blocks = soup.find_all('script')
len(script_blocks)
for block in script_blocks:
    block.extract()

script_blocks = soup.find_all('script')

len(script_blocks)
style_elements = soup.find_all('style')
len(style_elements)
for elt in style_elements:
    elt.extract()

style_elements = soup.find_all('style')
len(style_elements)
soup.prettify(formatter='html5')
print(_)

def delete_elements(soup, tag_name):
    for elt in soup.find_all(tag_name):
        elt.extract()
        
delete_elements(soup, 'link')
len(soup.find_all('link'))

soup.prettify(formatter='html5')
print(_)
s = soup.prettify(formatter='html5')
print(s)
delete_elements(soup, 'meta')

print(f'Remaining meta tags: len(soup.find_all("meta"))')
pretty = soup.prettify(formatter='html5')
print(pretty)
def has_class(tag):
    return tag.has_attr('class')
    
all_elements_with_class_attr = soup.find_all(has_class)
len(all_elements_with_class_attr)

for tag in all_elements_with_class_attr:
    del tag['class']

pretty = soup.prettify(formatter='html5')
print(pretty)

delete_elements(soup, 'img')

pretty = soup.prettify(formatter='html5')
print(pretty)
with open('index.html', mode='w') as fp:
    fp.write(pretty)

delete_elements(soup, 'section')
delete_elements(soup, 'footer')

with open('index.html', mode='w') as fp:
    fp.write(pretty)
soup.find_all('section')

pretty = soup.prettify(formatter='html5')
print(pretty)
with open('index.html', mode='w') as fp:
    fp.write(pretty)

delete_elements(soup, 'header')

pretty = soup.prettify(formatter='html5')
print(pretty)
with open('index.html', mode='w') as fp:
    fp.write(pretty)

def is_empty(tag):
    return len(tag.string.strip()) == 0

empty_tags = soup.find_all(is_empty)
def is_empty(tag):
    if tag.string:
        return len(tag.string.strip()) == 0
    return False
    
empty_tags = soup.find_all(is_empty)
len(empty_tags)
empty_tags

for tag in empty_tags:
    tag.extract()

pretty = soup.prettify(formatter='html5')
print(pretty)
with open('index.html', mode='w') as fp:
    fp.write(pretty)

