Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Lst=[2,4,9,1,7]
>>> #display list
>>> print(Lst[0:3])
[2, 4, 9]
>>> x=[2,4,9,1,7]
>>> replacements={2:0,7:0}
>>> replacer=replacements.get#for faster gets
>>> print([replacer(n,n)for in x])
SyntaxError: invalid syntax
>>> print([replacer(n,n)for n in x])
[0, 4, 9, 1, 0]
>>> a=[2,4,9]
>>> replacements={2:0,9:0}
>>> replacer=replacements.get#for faster gets
>>> print([replacer(n,n) for n in a])
[0, 4, 0]
>>> 
