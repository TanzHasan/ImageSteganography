# ImageSteganography

Our code is able to both retrieve a message from an image and encrypt and image with a message. 

To launch:
 encode:
  python stegoCode.py encode image_name text_file new_image_name color
  python stegoCode.py encode green.jpg test.txt test.png 0
 
 decode:
  python stegoCode.py decode image_name color
  python stegoCode.py decode test.png 0

