def greetings(name, dct):
    full = " ".join(name)
    title = dct['title']
    occupation = dct['occupation']

    if title[0].casefold in ['a', 'e', 'i', 'o', 'u']:
        return f'Hello, {full}! Nice to have an {title} {occupation} around.'
    
    return f'Hello, {full}! Nice to have a {title} {occupation} around.'


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
