#QUESTION 02
from PIL import Image
import numpy as np
import time

#generating random number by the provided algorithm
current_time = int(time.time())

generated_number = (current_time % 100) + 5

if generated_number % 2 == 0:
    generated_number += 10

#Chapter 01
image_path = 'chapter1.jpg'
image = Image.open(image_path)

image_data = np.array(image)

modified_image_data = image_data + generated_number
modified_image_data = np.clip(modified_image_data, 0, 255)

modified_image = Image.fromarray(modified_image_data.astype('uint8'))

output_image_path = 'chapter1out.jpg'
modified_image.save(output_image_path)

red_pixel_sum = np.sum(modified_image_data[:, :, 0])

print("Sum of Red Pixels: "+ str(red_pixel_sum))