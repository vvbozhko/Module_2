calls = 0
def count_calls ():
     global calls
     calls = calls + 1
     return (calls)

def string_info (string):
     count_calls ()
     return ([len(string), string.upper(), string.lower()])

def is_contains (contains1, contains2):
     count_calls ()
     c = bool
     for i in range(0, len(contains2)):
        b = (contains2[i].lower())
        if contains1.lower() == contains2[i].lower():
            c = True
            break
        else:
            c = False
     return c

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN', 'UrbAnk'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)