# 2. Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, and their capitals as values. (Use the Internet to get a list of the states and their capitals.) The program
# should then randomly quiz the user by displaying the name of a state and asking the user
# to enter that state’s capital. The program should keep a count of the number of correct and
# incorrect responses. (As an alternative to the U.S. states, the program can use the names of
# countries and their capitals.)

import random


def baseStateCapital():
    dictStateCapital = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Monies',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta',
        'Maryland': 'Annapolis',
        'Massachusetts': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota': 'St. Paul',
        'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helena',
        'Nebraska': 'Lincoln',
        'Nevada': 'Carson City',
        'New Hampshire': 'Concord',
        'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe',
        'New York': 'Albany',
        'North Carolina': 'Raleigh',
        'North Dakota': 'Bismarck',
        'Ohio': 'Columbus',
        'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem',
        'Pennsylvania': 'Harrisburg',
        'Rhoda Island': 'Providence',
        'South Carolina': 'Columbia',
        'South Dakota': 'Pierre',
        'Tennessee': 'Nashville',
        'Texas': 'Austin',
        'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier',
        'Virginia': 'Richmond',
        'Washington': 'Olympia',
        'West Virginia': 'Charleston',
        'Wisconsin': 'Madison',
        'Wyoming': 'Cheyenne'
    }
    states = list(dictStateCapital.keys())
    return dictStateCapital, states


def getAnswers(dictStateCapital, states):
    again = 'y'
    correct = 0
    incorrect = 0
    while again == 'y':
        stateToAsk = random.choice(states)
        capitalCorrect = dictStateCapital[stateToAsk]
        capitalFromUser = input("What is the capital of " + stateToAsk + ": ")
        if capitalFromUser == capitalCorrect:
            correct += 1
        else:
            incorrect += 1
        again = str.lower(input("Do you want to play again? Enter y for yes"))
    return correct, incorrect


def main():
    dictStateCapital, states = baseStateCapital()
    correct, incorrect = getAnswers(dictStateCapital, states)
    print("The number of correct answers: ", correct)
    print("The number of incorrect answers: ", incorrect)


if __name__ == '__main__':
    main()
