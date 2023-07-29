s = '\nprint(\'s=\\\'\',s,\'\\\'\\n\',\'\'.join(chr(int(i)) for i in s.split()),sep=\'\',end=\'\')'

with open("test.txt", 'w') as f:    
    f.write(' '.join([str(ord(c)) for c in list(s)]))
