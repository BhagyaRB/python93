Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'cup''cake'
'cupcake'
>>> 5*'cup''cake'
'cupcakecupcakecupcakecupcakecupcake'
>>> 'cup','cake'
('cup', 'cake')
>>> 'cup'"\n"'cake'
'cup\ncake'
>>> 5*'cup','cake'
('cupcupcupcupcup', 'cake')
>>> 5*'cup''cake','cup''cake'
('cupcakecupcakecupcakecupcakecupcake', 'cupcake')
>>> 5*,'cup''cake'
SyntaxError: invalid syntax
>>> 5*"\n"'cup''cake'
'\ncupcake\ncupcake\ncupcake\ncupcake\ncupcake'
>>> 
