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
    
def header_level(hsym):
    if hsym=='=':
        return 1
    elif hsym=='-':
        return 2
    elif hsym=='~':
        return 3
    elif hsym=='"':
        return 4
    return 1

def get_headers(filename, lines):
    '''
    Generates reStructuredText headers in format:
    line_index, header_level, header_text
    '''
    for n,i in enumerate(lines):
        if is_line_of_arr(i,'-=\'"`:^~_*+#<>'):
            if n>0:
                if 0<len(lines[n-1])<=len(i):
                    yield (n-1,header_level(i[0]),lines[n-1])
