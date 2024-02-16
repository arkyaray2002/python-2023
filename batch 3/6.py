from os.path import exists
def hash_display(file):
    if exists(file):
        f = open(file, 'r')
        data = f.read() + ' '
        new_data = ''
        for index,char in enumerate(data):
            if char != ' ':
                new_data += char + '#'
                if data[index + 1] == ' ':
                    new_data = new_data[:-1]
            else:
                new_data += '$'
        new_data = new_data[:-1] + '#'
        print(new_data)
    else:
        print("File doesnt exist")

hash_display('matter.txt')
