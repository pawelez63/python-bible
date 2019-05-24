# get sentence from user
original = input("Please enter a sentence to be translated: ").strip().lower()

# split sentence into words

words = original.split()

# loop through words and convert to pig latin

new_words = []
for word in words:

        # if starts with vowel, just add "yay"
        if word[0] in "aeiou":
                new_words.append(word + "Yay")

        # otherwise, move the first consonant cluser to end, and add "ay"
        else:
                vowel_pos = 0
                for letter in word:
                        if letter in "aeiou":
                                new_words.append(word[vowel_pos:] + word[:vowel_pos].capitalize() + "ay")
                                break            
                        else:
                                vowel_pos = vowel_pos + 1 
        
# stick words back together

print(" ".join(new_words).capitalize())

