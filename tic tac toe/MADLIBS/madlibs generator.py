
    
    # MadLibs Generator


def madlibs():
        # Prompt user for inputs
        adjective1 = input("Enter an adjective: ")
        adjective2 = input("Enter another adjective: ")
        animal1 = input("Enter an animal: ")
        verb1 = input("Enter a verb: ")
        place1 = input("Enter a place: ")
        adjective3 = input("Enter another adjective: ")
        object1 = input("Enter an object: ")
        animal2 = input("Enter another animal: ")
        place2 = input("Enter another place: ")
        verb2 = input("Enter another verb: ")
        plural_noun = input("Enter a plural noun: ")
        verb3 = input("Enter another verb: ")

        # MadLibs story
        story = f"""
        Once upon a time, in a {adjective1} forest, there lived a {adjective2} {animal1}.
        Every day, it loved to {verb1} near the {place1}.
        One day, it found a {adjective3} {object1} that changed its life forever. It decided to take it to its best friend, a {adjective2} {animal2}, who lived in a {place2}.
        Together, they {verb2} the {object1} and discovered it was magical!
        From that day on, they became the most {adjective3} duo in the {place2}, always looking for {plural_noun} to {verb3}.
        """

        # Print the story
        print("\nHere is your MadLibs story:")
        print(story)

# Run the MadLibs generator
madlibs()

#####################################
#second version of code
with open("story.txt", "r") as f:
        story = f.read()

words = []
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
        if char == target_start:
                start_of_word = i

        if char == target_end and start_of_word != -1:
                word = story[start_of_word: i + 1]
                words.add(word)
                start_of_word = -1
           
answers = {}#dictionary
answers = input("Enter a word for" + word + ":")
answers[word] = answers
#print(answers)
for word in words :
        story = story.replace(word, answers[word])

print(story)        

        

    