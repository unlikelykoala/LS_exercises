def clean_up(text):
    new_text = ''
    length = len(text)
    for i in range(length):
        if text[i].isalnum():
            new_text += text[i]
        elif (text[i] is text[-1]) or text[i+1].isalnum():
            new_text += ' '
    
    print(new_text)
    return new_text

print(clean_up("---what's my +*& line?") == " what s my line ")
