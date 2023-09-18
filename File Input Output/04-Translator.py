
# Read the file 
# search python Translator Module using 
# visit pypi page of translate 3.6.1
# read the page for them
# go the Use As A Python Module and follow the instructions 
# change the language from zh to somali and go up options   Available languages:
# visit the link they provide https://en.wikipedia.org/wiki/ISO_639-1
# as you can see ISO 639 — is standard Language codes
# search language code of somali by typing   'somalia ISO 639 code'
# you will get this ISO Somali Language codes are: ISO 639-1: so. ISO 639-2/T: som. ISO 639-2/B: som.
# so this means there are three different standard codes ISO 639-1, ISO 639-2/T and ISO 639-2/B 
# python translator uses the first one ISO 639-1: and the code will 'so'
# use it to and then proceed coding translation part => translation = translate.translate(text)
# after the translation completed write the translation into new file 



from translate import Translator

translate = Translator(to_lang='so')



try:
    with open('english.txt', mode='r') as myfile:
        text = myfile.read()
        translation = translate.translate(text)
        # print(translation)
        with open('somalia.txt', mode='w') as som_file:
            som_file.write(translation)
except FileNotFoundError:
    print('file not found')