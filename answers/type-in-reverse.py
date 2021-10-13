# Type in Reverse
'''
    Output a random word. Ask the user to type in the reverse. 
    If the user is correct, output ✅ Else, output ❌
'''
import json
import requests

print("Welcome!")

def get_random_word():
    word_url = requests.get("https://random-word-api.herokuapp.com//word?number=1").text
    words = json.loads(word_url) 
    return words[0]


if __name__ == '__main__':

	random_word = get_random_word()
	user_input = input(f"Type out the word \"{random_word}\" in reverse: ")

	if random_word[::-1] == user_input:
		print('✅')
	else:
		print ('❌')
