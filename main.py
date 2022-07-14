from pygame import mixer  # Playing sound

mixer.init(
    devicename="CABLE Input (VB-Audio Virtual Cable)"
)  # Initialize it with the correct device
mixer.music.load("pia.mp3")  # Load the mp3
mixer.music.play()  # Play it
