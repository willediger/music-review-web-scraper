__author__ = 'Will'

y = ['asdf', 'xzcv\n', 'qwer']
print(y)
x = [z.rstrip('\n') for z in y]
print(x)
# x = y.strip('\n')
# print(x)