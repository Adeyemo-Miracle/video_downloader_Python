while True:
    _input = input('value: ')
    if not _input.startswith('dddd') and not _input.startswith('aaaa'):
        print('invalid input please input "dddd" or "aaaa"')
    else:
        print('valid input')
        break