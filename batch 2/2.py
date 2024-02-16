d = [
    {'name' : 'Ryan', 'phone' : '1234', 'email' : 'ryan@gmail.com'},
    {'name' : 'Cyan', 'phone' : '4325', 'email' : 'cyan@gmail.com'},
    {'name' : 'Nice', 'phone' : '5467'},
    {'name' : 'Jan', 'phone' : '9999', 'email' : 'jan@gmail.com'},
]

for each_dict in d:
    if each_dict['phone'][-1] == '5':
        print(each_dict['name'])
    
        
for each_dict in d:
    try:
        each_dict['email']
    except:
        print(each_dict['name'])


for each_dict in d:
    if each_dict['phone'][0] == '9':
        print(each_dict['name'])
    
