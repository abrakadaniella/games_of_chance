import random
import time

import pyinputplus as pyip

money = 100


def flip_coin():
    global money
    bet = pyip.inputInt(prompt="We\'re playing flipping the coin now. Please make your bet.\n", min=1, max=money)
    guess = pyip.inputMenu(choices=['Heads', 'Tails'], prompt="What\'s your guess? Enter either Heads or Tails.\n")
    print("Your guess is {} and your bet is {}$. Flipping the coin!".format(guess, bet))
    time.sleep(1)
    money -= bet
    win = 2 * bet
    loss = -bet
    coin = random.randint(1, 2)
    if (coin == 1) and (guess == 'Heads'):
        money += win
        print("Congratulations, it is Heads! You won {}. Your balance is: {}".format(win, money))
        time.sleep(1)
    elif (coin == 2) and (guess == 'Tails'):
        money += win
        print("Congratulations, it is Tails! You won {}. Your balance is: {}.".format(win, money))
        time.sleep(1)
    else:
        print("You lost this time. Amount of your loss is {}. Your balance is: {}.".format(loss, money))
        time.sleep(1)


def cho_han():
    global money
    bet = pyip.inputInt(prompt="We\'re playing cho han now. You need to guess whether the sum of two dice is odd or "
                               "even. Please make your bet.\n", min=1, max=money)
    guess = pyip.inputMenu(choices=['Odd', 'Even'], prompt="What\'s your guess? Enter either Odd or Even.\n")
    print("Your guess is {} and your bet is {}$. Rolling the dice!".format(guess, bet))
    time.sleep(1)
    money -= bet
    win = 2 * bet
    loss = -bet
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_sum = dice1 + dice2
    if (dice_sum % 2 == 1) and (guess == 'Odd'):
        money += win
        print("Congratulations, the sum is {} and it is odd! You won {}. Your balance is {}.".format(dice_sum, win,
                                                                                                     money))
        time.sleep(1)
    elif (dice_sum % 2 == 0) and (guess == 'Even'):
        money += win
        print("Congratulations, the sum is {} and it is even! You won {}. Your balance is {}".format(dice_sum, win,
                                                                                                     money))
        time.sleep(1)
    else:
        print("You lost this time. The sum is {} and it is not {}. Amount of your loss is {}. Your balance is "
              "{}.".format(dice_sum, guess, loss, money))
        time.sleep(1)


def pick_card():
    global money
    bet = pyip.inputInt(prompt="We're randomly picking the card. The winner card is the one which number is larger. "
                               "Please make your bet.\n", min=1, max=money)
    print("Your bet is {}. Let\'s choose cards!".format(bet))
    time.sleep(1)
    money -= bet
    win = 2 * bet
    loss = -bet
    deck = [i for i in range(2, 11)]
    for i in range(2):
        deck += deck[:]
    card1 = random.choice(deck)
    deck.remove(card1)
    card2 = random.choice(deck)
    if card1 > card2:
        money += win
        print("Congratulations! Your card is {} and it is higher than my card, which is {}. You won {}. Your "
              "balance is {}.".format(card1, card2, win, money))
        time.sleep(1)
    elif card1 < card2:
        print("You lost this time. Your card is {} and it is lower than my card which is {}. You lost {}. Your "
              "balance is {}.".format(card1, card2, loss, money))
        time.sleep(1)
    elif card1 == card2:
        money += bet
        print("It's a tie! Both cards are {}. You won {}. Your balance is {}.".format(card1, bet, money))
        time.sleep(1)


def roulette():
    global money
    bet = pyip.inputInt(prompt="We\'re playing roulette now. Please make your bet.\n", min=1, max=money)
    choice = pyip.inputMenu(choices=['number', 'else'], prompt="Will your guess be regarding the nature of number or "
                                                               "the number itself? Please enter either \'number\' of"
                                                               " \'else\'.\n")
    if choice == 'number':
        guess = pyip.inputInt(prompt="Please enter any number between 0 and 36.\n", min=0, max=36,
                              allowRegexes=[r'00'])
    else:
        guess = pyip.inputMenu(choices=['odd', 'even'], prompt='Please enter either odd or even.\n')
    print("Your guess is {} and your bet is {}$.".format(guess, bet))
    time.sleep(1)
    money -= bet
    win = 2 * bet
    loss = -bet
    num = random.randint(0, 36)
    if (guess == 'Even') or (guess == 'Odd'):
        if (guess == "Even") and (num != 0) and (num % 2 == 0):
            money += win
            print("The number on the roulette is {} and it is even! You won {}. Your balance is {}.".fromat(num,
                                                                                                            win, money))
            time.sleep(1)
        elif (guess == "Odd") and (num != 0) and (num % 2 == 1):
            money += win
            print("The number on the roulette is {} and it is odd! You won {}. Your balance is {}.".fromat(num,
                                                                                                           win, money))
            time.sleep(1)
        else:
            print("You didn\'t guess this time. The number on the roulette is {} and it is not {}. You lost {}. "
                  "Your balance is {}.".format(num, guess, loss, money))
            time.sleep(1)
    else:
        if guess == num:
            money += win
            print("The number on the roulette is {}! You won {}. Your balance is {}.".fromat(num, win, money))
            time.sleep(1)
        else:
            print("You didn\'t guess this time. The number on the roulette is {}. You lost {}. "
                  "Your balance is {}.".format(num, loss, money))
            time.sleep(1)


def play():
    game = pyip.inputMenu(choices=['flip coin', 'cho han', 'pick card', 'roulette'], prompt="Enter name of the game "
                                                                                            "you\'d like to play now: "
                                                                                            "flip coin, cho han, pick "
                                                                                            "card, roulette.\n")
    if game == 'flip coin':
        flip_coin()
    elif game == 'cho han':
        cho_han()
    elif game == 'pick card':
        pick_card()
    else:
        roulette()
    time.sleep(1)
    again = pyip.inputMenu(choices=['Yes', 'No'], prompt="Do you want to play some more? Enter 'yes'. If you want to "
                                                         "finish enter 'no'.\n")
    if again == 'Yes':
        play()
    else:
        print("Be back soon! Bye.")


play()