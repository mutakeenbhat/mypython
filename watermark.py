import numpy as np
from PIL import Image as im
i=im.open(r'C:\\Users\\MUTAKEEN\\Pictures\\Saved Pictures.\\family.jpg')
# i.show()
i = i.convert('RGB')
red_channel, green_channel, blue_channel = i.split() #image.split() separates the Red, Green, and Blue channels into individual grayscale images.

# Display each channel
#show() opens each channel in a separate window using the default image viewer on your system.
# red_channel.show(title="Red Channel")
# green_channel.show(title="Green Channel")
# blue_channel.show(title="Blue Channel")
image_array = np.array(i)

# Compute the average of the RGB channels
grayscale_array = image_array.mean(axis=2).astype(np.uint8)

# Convert the grayscale array back to an image
grayscale_image = im.fromarray(grayscale_array)

# Display the grayscale image
grayscale_image.show(title="Grayscale Image")