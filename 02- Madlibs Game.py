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


# functional code
# import re

# def read_story_from_file(file_name):
#     with open(file_name, 'r') as file:
#         story = file.read()
#     return story

# def get_user_input(placeholders):
#     user_inputs = {}
#     for placeholder in placeholders:
#         user_input = input(f"Enter a {placeholder}: ")
#         user_inputs[placeholder] = user_input
#     return user_inputs

# def fill_in_story(story, user_inputs):
#     filled_story = story
#     for placeholder, value in user_inputs.items():
#         filled_story = re.sub(r'\[' + placeholder + r'\]', value, filled_story)
#     return filled_story

# def main():
#     story_file = 'story.txt'
#     story = read_story_from_file(story_file)
    
#     placeholders = re.findall(r'\[(.*?)\]', story)
#     user_inputs = get_user_input(placeholders)
    
#     filled_story = fill_in_story(story, user_inputs)
#     print("\nFilled Story:\n" + filled_story)

# if __name__ == "__main__":
#     main()
