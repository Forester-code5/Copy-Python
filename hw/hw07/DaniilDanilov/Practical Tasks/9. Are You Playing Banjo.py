# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"

def are_you_playing_banjo(name):
    return name + " plays banjo" if name.startswith(("R", "r")) else name + " does not play banjo"
