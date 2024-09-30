user_string = input('Enter a string:')

has_python = False

string_length = len(user_string)

if 'Python' in user_string: has_python = True

print('Length:' , string_length)
print('First and last letter:', user_string[0], user_string[string_length - 1])
print('Number of spaces:', str.count(user_string, ' '))
print('Does it contain "Python"?', has_python)
