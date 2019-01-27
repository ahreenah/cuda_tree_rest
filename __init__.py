import itertools

def is_line_of(ln,sym):
    if ln=='':
        return False
    for i in ln:
        if not i==sym:
            return False
    return True

def is_line_of_arr(ln,arr):
    for i in arr:
        if is_line_of(ln,i):
            return True
    return False

def get_headers(filename, lines):
    '''
    Generates markdown headers in format:
    line_index, header_level, header_text
    '''
    for n,i in enumerate(lines):
        if is_line_of_arr(i,'-=\'"`:^~_*+#<>'):
            if n>0:
                if len(lines[n-1])==len(i):
                    yield (n-1,True,lines[n-1])
            print(i)