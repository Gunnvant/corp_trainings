import re
## 1
ip = 'They ate 5 apples and 5 oranges'
re.sub('5','five',ip)

## 2
items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
def exists(item):
    pattern = re.compile(r'e')
    if len(re.findall(pattern,item))==0:
        return False
    else:
        return True
[w for w in items if not exists(w)] 

## 3
para = '''good start
    Start working on that
    project you always wanted
    stars are shining brightly
    hi there
    start and try to
    finish the book
    bye'''
pattern = re.compile(r'^Start', re.IGNORECASE)
sents = para.split("\n")
for sent in sents:
    if len(re.findall(pattern,sent.strip()))==0:
        print(sent)
