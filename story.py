storyFormat = ''' Once upon a time in an ancient jungle,
there lived a {animal}. This {animal} liked to eat {food},
but the jungle had very little {food} to offer. One day, an
explorer found the {animal} and discoverd it liked {food}.
The explorer took the {animal} back to {city}, where it could 
eat as much {food} as it wanted. However, the {animal} become
homesik, so the explorer brought it back to the jungle, leaving a 
large supply of {food}

The End
..........
'''


def tellStory():
    userPicks = dic()
    addPick('animal', userPicks)
    addPick('food', userPicks)
    addPick('city', userPicks)
    story = storyFormat.format(**userPicks)
    print(story)


def addPick(cue, dictionary):
    '''Prompt for a user response using cue string,
    and place the cue-response pair in the dictionary.'''

    prompt = 'Enter a example for ' + cue + ': '
    response = input(prompt)
    dictionary[cue] = response


tellStory()
input('Press Enter to end the program.')