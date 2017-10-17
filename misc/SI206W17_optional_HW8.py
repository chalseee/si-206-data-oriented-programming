import unittest # just in case
import json # just in case
from PIL import Image, ImageFilter, ImageColor, ImageFile, ImagePalette, ImageMorph # tons of options, and OK to add more: http://pillow.readthedocs.io/en/3.4.x/index.html to import directly...
import glob, os # tools to help you deal with files, in standard library, not necessary

## SI 206 Winter 2017
## Optional HW: Building an Album

## Comment with your name:
## Anyone you worked with on this assignment:

## The score for this assignment can replace your lowest score on HW 2 - HW 7. 
## It is due THURSDAY, APRIL 13 at 11:59 PM and cannot be submitted late, because it is due so soon before the end of classes.

#########

## Your goal for this assignment is to use image manipulation code to create a photo album and manipulate it!

## PART 1: Define a class PhotoAlbum, which will represent one Photo Album. It should accept, at minimum, a list of strings, which each represent filenames.

## Creating an instance won't work if the file names don't exist, and won't work if the fnames_lst input is empty. There must be at least one photo file, and all file names in that list must represent real image files.

## PART 2: The class should contain at least 6 additional methods which allow you to manipulate either one particular image in the album or all of the images in the album at once.

## It also might be nice to include a string method that represents a printed (non-image) representation of this photo album data...

## At least one of the methods you create MUST show either one of the images (per input specification, e.g. invoke a method to say "show me the first one" or "show me the image at index 4"...) or show ALL of the images somehow. Everything else is up to you. Here are some suggestions/possibilities:

## A method that creates thumbnails of all the images and saves a list of them in a thumbnails instance variable
## A method that allows you to change the cover photo
## A method that allows you to blend a random set of 2 photos, or a specific set of 2 photos (note that the photos must all be the same size and the same mode for this to work!)
## A method that makes all or one of the photos greyscaled and shows the first one
## A method that allows you to pick a new size and resize one of the album images
## A method that allows you to select part of an image, given certain input to determine what image to select from, and how much to select
## ...

## The methods you create should vary, not be exactly the same as one another with a few characters' difference.

## You can use as your references, among other things:
# http://pillow.readthedocs.io/en/3.4.x/reference/Image.html
# http://pillow.readthedocs.io/en/3.4.x/handbook/concepts.html#concept-modes

## Be careful: you're manipulating references to files, which can be tricky. Pay attention to what Image methods return a value, and which modify objects in place!

## After you define your class (which you should be testing out as you go to make sure everything works as you expect), you should create at least 2 PhotoAlbum instances with real images, beneath your class definition, and invoke the methods you've defined to show how they all work, including brief comments. 

## You should submit your edited file to the HW8-Optional assignment, along with all of the image files you refer to/use in your sample code.

## Note that the default photo-editing programs on your computer AND PIL Image methods themselves can help with resizing/cropping as needed!

## As goes without saying, make sure all images you submit are totally in-school-sharing-appropriate or your assignment will not be accepted. Fine to use screenshots of e.g. astronomy pictures, flickr photos you download, famous photographs from the NYTimes you find online (though note that for some of these things it's probably most fun to work with photographs in color!)...anything you want.


# Define your PhotoAlbum class here:
class PhotoAlbum(object):
	im = []
	def __init__(self, filenames):
		self.filenames = list(filenames)
		for f in filenames:
			im = Image.open(f)
			print()

filenames = ['C:\Users\chalse\Pictures\GroupMe\boi.jpeg', 'C:\Users\chalse\Pictures\GroupMe\drake.jpeg', 'C:\Users\chalse\Pictures\GroupMe\will.jpeg' ]





# Write some sample code with comments to show how your PhotoAlbum class methods work, here:




# No tests: you decide what it means for your code to work. Make sure your file runs! We won't grade code that does not run.

# And please share the cool images you come up with during the process on Piazza! If someone is curious how you made it happen, share the code and explain!