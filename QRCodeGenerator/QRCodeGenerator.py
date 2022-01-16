import qrcode
import image

qr = qrcode.QRCode(
    
    version = 15,
    # Version denotes the size of the qr code to be generated. 
    # Higher the value of version, bigger and more complicated will be the qr code generated.

    box_size = 10,
    # Box Size denotes the size of the window in which qr code will be ddisplayed.

    border = 5,
    # Border is the space on all sides, here giving the border width to be 5.

)

# Data is the variable which stores the URL of the site where you want to go after scanning the qr code.
data = "https://github.com/Harshul-18"

# Adding the data to the qr code
qr.add_data(data)
qr.make(fit = True)

# Making the image of the qr code and Saving it.
img = qr.make_image(fill="black", back_color="white") # You can change the color.
# Fill argument takes a color in which the qr code in generated.
# Back color argument is the color which denotes the background color.
img.save("test.png")

