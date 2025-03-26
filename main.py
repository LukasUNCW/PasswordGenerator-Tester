from passwordmeter import test
from urllib.request import urlopen
from os.path import isfile
from random import choice, randint

if not isfile('words.txt'):
    print('Downloading words.txt...')
    url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
    
    with urlopen(url) as response:
        words_data = response.read().decode('utf-8')
        with open('words.txt', 'w', encoding='utf-8') as f:
            f.write(words_data)

with open('words.txt', 'r', encoding='utf-8') as f:
    words = [word.strip() for word in f.readlines() if word.strip()]

specials = ['!', '?', '@', '#', '$', '%', '&', '*']

def create_password(num_words=2, num_numbers=10, num_special=2):
    if not words:
        print("Word list is empty. Exiting...")
        return ""

    pass_str = ''.join(choice(words).capitalize() for _ in range(num_words))
    pass_str += ''.join(str(randint(0, 9)) for _ in range(num_numbers))
    pass_str += ''.join(choice(specials) for _ in range(num_special))
    return pass_str

def main():
    pass_str = create_password()
    
    if pass_str:
        strength, _ = test(pass_str)

        print('\nPassword: %s' % pass_str)
        print('Strength: %0.5f' % strength)

if __name__ == '__main__':
    main()
