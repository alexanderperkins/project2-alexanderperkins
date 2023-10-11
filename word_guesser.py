"""
    CS 5001
    Project 2
    Name: Alex Perkins
"""

import random  # library required to randomly choose a secret word

def get_secret_word() -> str:
	"""
	Returns a randomly generated secret word.
	Uses the list of words in the public domain retrieved from:
	https://www-cs-faculty.stanford.edu/~knuth/sgb.html
	Requires a text file called words.txt.	
	"""
	with open('words.txt') as f:
		words = f.read().splitlines() 		
		word = random.choice(words)
	return word

def get_user_guess():
	"""
	Returns user's guessed word. Makes user repeat until word is only 5 letters.
	"""
	guess = input("Guess the 5 letter word: ")
	while len(guess) != 5:
		print("***Error***")
		guess = input("You did not enter a 5 letter word. Please enter a 5 letter word only: ")
	return guess

def match_letter_position(secret_word, guess):
	"""
	Compares letters in user's guess word against those in random word by indexed position.
	"""
	index = 0
	matches = ''
	guess_attempt = ''
	for character in secret_word:
		if character == guess[index]:
			guess_attempt += character
			matches += 'G'
		else:
			guess_attempt += '_'
			matches += '_'
		index += 1
	print(guess_attempt)
	print(matches)
	return guess_attempt, matches

def match_letter():
	pass

def guess_attempts(secret):
	"""
	Allows user to make or repeat up to 6 guesses to match the random word.
	"""
	user_guesses = 0
	max_guesses = 6
	while max_guesses > user_guesses:
		guess = get_user_guess()
		attempt, match = match_letter_position(secret, guess)
		user_guesses += 1
		if guess == secret:
			print(attempt)
			print(match)
			break
		print(f'Nice try! You have {max_guesses - user_guesses} guesses left.')
	return user_guesses, attempt, match

def game_result(attempts, guess, secret):
	"""
	Tells the user if they won or not. If they didn't win, shows the random word.
	"""
	if guess == secret:
		print(f'You won! It took you {attempts} tries.')
	else:
		print("You lose. Better luck next time! Secret word was: ", secret)

def game_wins_losses():
	pass

def main():
	random_word = get_secret_word()
	print(random_word)
	# guessed_word = get_user_guess()
	# print(guessed_word)
	# guess_result, matched_letters = match_letter_position(random_word, guessed_word)
	guesses, guess_result, match_letters = guess_attempts(random_word)
	game_result(guesses, guess_result, random_word)


if __name__ == '__main__':
	main()
