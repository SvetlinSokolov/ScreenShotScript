from PIL import ImageGrab
import keyboard
import os

# Get name form input and setting its format type
nameFromInput = str(input())
name = nameFromInput + ".png"

# Path for saved screenshots
dir = nameFromInput + "ScreenShots"
usern = os.getlogin()
path = "C:\\Users\\" + usern + "\\" + dir
os.mkdir(path)
n = 0

# Main loop
while True:
    try:
        # Taking screenshots logic
        if keyboard.is_pressed('p'):
            imagename = name
            im = ImageGrab.grab()
            imagename = imagename[:-4] + str(n) + '.png'
            n = n + 1
            im.save(path + "\\" + imagename, 'PNG')
            print(f"Saving image {imagename} in ")

        # Exiting program
        elif keyboard.is_pressed('q'):
            print("Shutting down program!")
            print(f"You took {n} screenshots")
            print(f"Files can be found at {path}")
            break

        else:
            pass

    except:
        pass
