with open("story.txt", 'r') as f:
    story = f.read()

target_index = -1

start_pos = '<'
end_pos = '>'

words = set()

for index,char in enumerate(story):
    if char == start_pos:
        target_index = index

    if char  == end_pos:
        word = story[target_index:index+1]
        words.add(word)
        target_index = -1


answers = {}
for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer
print(story)
for key,value in answers.items():
    print(key,value)
    story = story.replace(key,value)

print(story)

