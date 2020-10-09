#! python3
# hangman.py - play the classic game of hangman

import assets, random, re

print('Welcome to Hangman.')

# replay loop

replay = True
while replay:
    # picks a random word from the list of words
    secret_word = assets.words[random.randint(0,(len(assets.words)-1))]

    # reset the number of incorrect guesses to zero
    wrong_guess_count = 0

    # create a dictionary of guessed letters and of letters in the secret word
    secret_word_dictionary = []
    guessed_letters = []
    for letter in secret_word:
        secret_word_dictionary += letter
    # gameplay loop
    while True:
        # show the correct gallows
        print(assets.hanged_men[wrong_guess_count])
        # show the secret word (in progress)
        for letter in secret_word:
            if letter in guessed_letters:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        # show the guessed letters
        print('\n\nGuessed letters: ' + ' '.join(guessed_letters) + '\n')
        # test if the player has won
        winning_condition = True
        for letter in secret_word_dictionary:
            if letter in guessed_letters:
                pass
            else:
                winning_condition = False
        # if the player has won, exit the loop with game_won true
        if winning_condition:
            game_won = True
            break
        # if the player has lost, exit the loop with game_won false
        if wrong_guess_count == 6:
            game_won = False
            break
        # ask the player to guess a letter
        valid_input = False
        while not valid_input:
            guessed_letter = input('Guess a letter: ')
            # if they input anything other than a single letter that they haven't guessed already, make them do it again
            if len(guessed_letter) != 1:
                print('\nInvalid input. Only single characters please.\n')
            elif not re.findall('[a-z]', guessed_letter):
                print('\nInvalid input. Only alphabetical characters please.\n')
            elif guessed_letter in guessed_letters:
                print("\nYou've already guessed this letter. Try again.\n")
            else:
                valid_input = True
        # add the letter to the list of guessed letters
        guessed_letters += guessed_letter
        # if the letter isn't in the word, increase the count of incorrect guesses
        if guessed_letter not in secret_word_dictionary:
            wrong_guess_count += 1
        # return to the beginning of the loop
    if game_won:
        print('You win!')
    else:
        print('You lose! The secret word was "' + secret_word + '."')
    valid_replay_input = False
    while not valid_replay_input:
        play_again = input('\nPlay again? (yes or no): ').lower()
        if play_again == 'no':
            replay = False
            valid_replay_input = True
        elif play_again == 'yes':
            replay = True
            valid_replay_input = True
        else:
            print('Invalid response.')
