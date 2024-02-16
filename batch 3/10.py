def check_panagram(s):
    s = s.lower()
    for each_letter in 'abcdefghijklmnopqrstuvwxyz':
        if each_letter not in s:
            return False
    return True

print(check_panagram('The quick brown fox jumps over the lazy dog'))
