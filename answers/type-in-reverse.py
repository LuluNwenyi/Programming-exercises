# Type in Reverse
'''
    Output a random word. Ask the user to type in the reverse. 
    If the user is correct, output ✅ Else, output ❌
'''
import json
import requests

print("Welcome! Type out the following word in reverse.")

def get_random_word():
    word_url = requests.get("https://random-word-api.herokuapp.com//word?number=1").text
    word = json.loads(word_url)
    global reversed_word 
    reversed_word = word[0][::-1]
    return word


input_word = print(get_random_word())
reverse = input("Type out the word in reverse: ")

def check_input():

    reverse_lower = reverse.lower()
    reversed_word_lower = reversed_word.lower()
    if reverse_lower == reversed_word_lower:
        print ('✅')
    else:
        print ('❌')

if __name__ == '__main__':
    check_input()
