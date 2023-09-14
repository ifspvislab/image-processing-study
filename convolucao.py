from PIL import Image, ImageFilter

im = Image.open("assets/img1.jpg")
im1 = Image.open("assets/img2.jpg")

convolution_kernel = ImageFilter.Kernel((3,3), (2,1,0,-1,1,-1,0,-1,2), scale=1, offset=0)

im_convolution = im.filter(filter= convolution_kernel)
im1_convolution = im1.filter(filter= convolution_kernel)
im.show()
im_convolution.show()
im1.show()
im1_convolution.show()