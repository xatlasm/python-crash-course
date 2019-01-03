#OrderedDict Rewrite

from collections import OrderedDict

glossary = OrderedDict()

glossary['dictionary'] = 'object that stores key-value pairs'
glossary['key'] = 'index of dictionary item'
glossary['value'] = 'data of dictionary item'
glossary['loop'] = 'section of code that can be executed repeatedly'
glossary['if'] = 'code structure that allows decision-making'

for key, value in glossary.items():
    print(key + ':\n' + value +'\n')