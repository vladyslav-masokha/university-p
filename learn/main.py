user_data = input('Enter your name: ')
text = 'Hello '

# if user_data == 'vlad':
#   string = text + user_data
# else:
#   string = text + 'no name :)'
  
string = text + user_data if user_data == 'vlad' else text + 'no name :)'
  
print(string)