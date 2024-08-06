# note: the border is off bc the if statement doesn't account for the length + 2 spaces
# also, it doesn't account for more than 1 wrap around

def print_in_box(text, limit = None):
    t_length = len(text)
    wrap_limit = 20
    if limit and t_length > limit:
        diff = limit - t_length
        text = text[:diff]
        t_length = len(text)
    ot_length = t_length
    if t_length > wrap_limit:
        diff2 = wrap_limit - t_length
        line1 = text[:diff2]
        line2 = text[diff2:]
        t_length = len(line1)

    top_bottom = '+' + ('-' * (t_length + 2) + '+')
    spaced = '|' + (' ' * (t_length + 2) + '|')
    print(top_bottom)
    print(spaced)
    if ot_length > wrap_limit:
        print('| ' + line1 + ' |')
        print('| ' + line2 + (' ' * (t_length - len(line2)) + '|'))
    else: print('| ' + text + ' |')
    print(spaced)
    print(top_bottom)

print_in_box('To boldly go where no one has gone before.')
print_in_box('')
