from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')

# print(img)
# print(img.format)
# print(img.size)
# print(img.mode) # indicates how the image's pixel data is organized and how color information is stored for each pixel

# print(dir(img))
# print(img.show())

# filteredImage = img.filter(ImageFilter.BLUR)

# filteredImage.save('blur.png', 'png')

# smoothed_image = img.filter(ImageFilter.SMOOTH)  # it usually works better on landscape images 
# smoothed_image.save('smooth.png', 'png')

sharpen_image = img.filter(ImageFilter.SHARPEN)
sharpen_image.save('sharpen.png', 'png')


# Now, the reason that I've converted this into a P&G is because P&G supports these image filters So you might get an error if you actually keep it as a jpeg.

# So instead of this filter image, we can actually do something called convert. And this converts the image to different formats.

convertedImage = img.convert('L')  # one of the formats that we can actually do is something called grayscale, also the RGB we saw is another format    
# convertedImage.save('grayscale.png', 'png')  # Pikachu is in black and white.


# We can also rotate our images 
crooked = convertedImage.rotate(90)
# crooked.save('crooked.png', 'png')  

# Let's do 180.  ( do it for your self and show them )

# We can also resize the images.
resized = img.resize((200,200)) # the original image was (640, 640)
# resized.save('resized.png', 'png')


# We can also crop the images.
# box = (100, 100, 400, 400)
# crop = img.crop(box)
# crop.save('crop.png', 'png')


# astro thumbnail 

astro = Image.open('./astro.jpg')
# new_astro = astro.resize((400,400))
new_astro = astro.resize((400,200))
new_astro.save('new-astro.png', 'png')
# as you can see the image looks kind of squished in. So how can we fix that? And this is a common problem with images

# how can we fix this ? we can actually use a useful thumbnail method instead of resize,

astro.thumbnail((400,200)) # thumbnail actually doesn't return a new image. It just modifies the current one.

# astro.save('thumbnail.png', 'png') 
# so thumbnail  keeps the aspect ratio. but important thing to note here is thumbnail didn't give the image 400x200 size at a that exactly that just means the maximum size it can be you can check the size of the image 

print(astro.size) # 210x200

