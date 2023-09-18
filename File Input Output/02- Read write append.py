# now let's learn how we read files without needing explicitly to close it 
# in that case we need to use built in method for input outputs called 'with'

# READ
# with open('test.txt') as myfile:
#     print(myfile.read())
    # and now you dont have to worry about closing 

# so far we were only reading files what if we want to write something on files or to append something at the end of the file   , in that case you just the change the mode to read and write but write doesn't use write you just say r+ and that plus sign allows you write something on that file 


# WRITE

# with open('test_write.txt', mode='r+') as myfile:
    # by default it used read mode so if you need to write you have explicitly change the mode 
    # text = 'This is a new file \n'
    # myfile.write(text)
    # so  change the text again and write the file again
    # text = 'i am busy'
    # myfile.write(text)

    # so what actually happened ? you remember the cursor idea we talked before. so each time you open a file  The cursor goes to zero. And if we write something to the file. And if there's something already existing in there, well, we overwrite so that is what happens



    # so how do we keep what was there and write the file into something new without overwriting  we use append mode 

# APPEND MODE 

# with open('test_write.txt', mode='a') as myfile:
#     text = 'hey there :)'
#     myfile.write(text)
    # as you can see it appends to the end.

# so what happens is we just use write only without reading like we doing in append mode
# with open('test_write.txt', mode='w') as myfile:
#     text = 'it\'s new text'
#     myfile.write(text)

    # so what happened ? so previously we first reading the file and then write something in it that case we overwrote the text but didn't remove anything from that file but if use write only it doesn't read anything it just overwrites the whole file 


# so the main difference is r+ reads first and then writes while w mode assumes this is new file and write something in it so let's compare this to get idea fully

# the file sad.txt doesn't exist see what happens if when you use r+ 
# with open('sad.txt', mode='r+') as myfile:
#     text = 'it\'s new text'
#     myfile.write(text)

# you get an error saying FileNotFoundError: [Errno 2] No such file or directory: 'sad.txt'

# but now do it w mode only 
with open('sad.txt', mode='w') as myfile:
    text = 'it\'s new text'
    myfile.write(text)

# nothing happened cause write it either creates a new file if it doesn't exist already or overwrites the existing one.