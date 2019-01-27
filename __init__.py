import itertools

def get_headers(filename, lines):
    '''
    Generates markdown headers in format:
    line_index, header_level, header_text
    '''
    yield (2, 1, 'tst...')