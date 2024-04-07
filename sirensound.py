import pygame 

#playing alert sound
pygame.mixer.init()       #initialize the pygame library
pygame.mixer.music.load('sound1.wav')    #loading the audio file of siren sound
pygame.mixer.music.play()                #playing the siren sound


input('enter to exit the sound : ')# enter a key to exit the sound