# SAMF or Sam file :)

This python library going to read a .samf for you

myfile.samf
```text
<Patterns>
email = ^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9]{2,}$
nome = ^[a-z]+S[0-9]$
```

### in python, you can use it like that:

myfile.py
```python
from samfile.SamF import SamfReader
import re

file = SamfReader()

email = "example@gmail.com"


learn = file.read("myfile.samf")

print(re.findall(learn["Patterns"]["email"], email)) # ['example@gmail.com']
```

At the moment, you can just put one section <Section># samfile
