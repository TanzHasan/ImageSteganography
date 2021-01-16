import numpy as np
import PIL
import sys
from PIL import Image

def userInput(msg):
    msg += "aspscv"
    binary = ''
    for i in msg:
        nbinary = format(ord(i), 'b')
        binary = binary + '0' * (8-len(nbinary)) +nbinary
    return binary

def encode(msg, filename, res_file, color):
    image = Image.open(filename)
    width, height = image.size
    totalPix =  width * height
    binary = userInput(msg)
    bitlength = len(binary)
    if (bitlength < totalPix):
        numpy_array = np.array(image)
        image.close()
        encodeBit(binary, numpy_array, width, height, res_file, color)
        print("Encoded")
    else:
        print("message too long or image too small")

def encodeBit(binary, numpy_array, width, height, res_file, color):
    for i in range(len(binary)):
        h = i%height
        w = i//height
        if (numpy_array[w, h, color]%2 != 0):
            numpy_array[w, h, color] = numpy_array[w, h, color] - 1
        numpy_array[w, h, color] += int(binary[w + h])
        #print(int(binary[w + h]))
##        print ("w: ", w, "h: ", h, "value ", numpy_array[w, h, 1])
        #print(numpy_array[w][h][2])
    PIL_image = Image.fromarray(numpy_array.copy().astype(np.uint8))
    PIL_image.save(res_file)
    PIL_image.close()
##    image = Image.open("test.png")
##    newarr = np.array(image)
##    image.close()
##    for i in range(len(binary)):
##        h = i%height
##        w = i//height
##        print ("w: ", w, "h: ", h, "value ", newarr[w, h, 1])
    

def decode(filename, color):
    Dimage = Image.open(filename)
    width, height = Dimage.size
    numpy_array = np.array(Dimage)
    binary = ""
    answer = ""
    found = False
##    for i in range(80):
##        h = i%height
##        w = i//height
##        print ("w: ", w, "h: ", h, "value ", numpy_array[w, h, 1])
    for w in range (width):
        if (not found):
            for h in range (height):
                binary += str(numpy_array[w][h][color]%2)
                #print(binary)
                if (len(binary)==8):
                    answer += chr(int(binary,2))
                    #print (binary)
                    #print (chr(int(binary,2)))
                    binary = ""
                if ("aspscv" in answer):
                    found = True
                    break
    print (answer[:len(answer)-6])

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "encode":
        filename = sys.argv[2]
        message = open(sys.argv[3], "r")
        res_file = sys.argv[4]
        color = int(sys.argv[5])
        encode(message.read(), filename, res_file, color)
    else:
        dfile = sys.argv[2]
        dcolor = int(sys.argv[3])
        decode(dfile, dcolor)
