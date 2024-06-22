# An Image Viewer Application called Cats Picsy 

# *********************** Add Libraries ********************************

# Pygame library is used to make the GUI
import pygame 
# OS library allows us to interact with the operating system 
import os 
# from pygame import mixer for sound effect 
from pygame import mixer
# Start the mixer
mixer.init()
# Load the Halloween sound effect 
mixer.music.load("dont-be-scared-halloween-v2.mp3")
# Setting the volume
mixer.music.set_volume(0.8)
# Start playing the song
mixer.music.play()




# *********************** Pygame Objects ********************************
# Initialize pygame - Create an instance of Pygame 
pygame.init()

# ************************ Window Init ******************************
# Create constants for the screen width and height 
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900
# Create a window object 
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Set the title of the window
pygame.display.set_caption("Mariam Cat Picsy")


# ************************ Files Init ******************************
# Set the path to our images folder, this will be a constant
IMAGE_DIRECTORY = "Images"
# Get a list of all the files in the images folder 
# os.listdir() method in python gets the list of all files in the specified folder
# The python string endswith() method
image_filenames = [filename for filename in os.listdir(IMAGE_DIRECTORY) if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".gif") or filename.endswith(".jpeg") or filename.endswith("jfif")]

# ************************ Load each image into a list we can loop through ******************************
# Create an empty list to hold our images
images = []
# Loop through each image filename
# os.path.join() -- join() is a method in .path module in os library
for filename in image_filenames:
    # Get the full path to the image
    image_path = os.path.join(IMAGE_DIRECTORY, filename)
    # Load the image into memory 
    # into our single variable called image
    # with a single image using pygame.
    image = pygame.image.load(image_path)
    # Resize the image to fit the window
    image = pygame.transform.scale(image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    # Add the image to our list of images
    images.append(image)

# ************************ Main Program Loop - Display Images ******************************
# Create a variable to hold the current image
current_image_index = 0
# Create a variable to hold the current image
current_image = images[current_image_index]
# Create a clock object to control the frame rate
clock = pygame.time.Clock()
# Create and start our main program loop 
# This bool will keep the window open until we set it to false
is_running = True
# Loop until running is set to false
while is_running:
    # Clear the screen
    window.fill((255, 255, 255))
    # Display the current image
    window.blit(current_image, (0, 0))
    # Update the display 
    pygame.display.flip()
    # ********************** Handle any events *********************************
    # Has the user pressed a key? 
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            
            # Has the user pressed the escape key to close the application? 
            if event.key == pygame.K_ESCAPE:
                # Set is_running to false to exit the main program loop 
                is_running = False
 

    # ******************* End of event handling ****************************
    # Set the frame rate to 30 frames per second 
    clock.tick(1)
    
    current_image_index = (current_image_index + 1) % len(images)
    current_image = images[current_image_index]

# ****************** End program ***************************
# Quit the applicaiton     
pygame.quit()    
