import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Set up the images
chosenletterimages = [
    pygame.image.load("ASLImages\\A.png").convert(),
    pygame.image.load("ASLImages\\B.png").convert(),
    pygame.image.load("ASLImages\\C.png").convert(),
    pygame.image.load("ASLImages\\D.png").convert(),
    pygame.image.load("ASLImages\\E.png").convert(),
    pygame.image.load("ASLImages\\F.png").convert(),
    pygame.image.load("ASLImages\\G.png").convert(),
    pygame.image.load("ASLImages\\H.png").convert(),
    pygame.image.load("ASLImages\\I.png").convert(),
    pygame.image.load("ASLImages\\J.png").convert(),
    pygame.image.load("ASLImages\\K.png").convert(),
    pygame.image.load("ASLImages\\L.png").convert(),
    pygame.image.load("ASLImages\\M.png").convert(),
    pygame.image.load("ASLImages\\N.png").convert(),
    pygame.image.load("ASLImages\\O.png").convert(),
    pygame.image.load("ASLImages\\P.png").convert(),
    pygame.image.load("ASLImages\\Q.png").convert(),
    pygame.image.load("ASLImages\\R.png").convert(),
    pygame.image.load("ASLImages\\S.png").convert(),
    pygame.image.load("ASLImages\\T.png").convert(),
    pygame.image.load("ASLImages\\U.png").convert(),
    pygame.image.load("ASLImages\\V.png").convert(),
    pygame.image.load("ASLImages\\W.png").convert(),
    pygame.image.load("ASLImages\\X.png").convert(),
    pygame.image.load("ASLImages\\Y.png").convert(),
    pygame.image.load("ASLImages\\Z.png").convert()
]

# Set up the letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Set up the font
font = pygame.font.Font(None, 36)

def display_question(imageletter, letteranswers):
    # Clear the screen
    screen.fill((255, 255, 255))
    


    # Display the image
    screen.blit(imageletter, (325,100))

    # Display the possible answers
    y = 300

    answernumber = 1
    for i in range(4):
        answer = letteranswers[i]
        answer_text = font.render(answer, True, (0, 0, 0))
        answer_rect = answer_text.get_rect(center=(400, y))
        screen.blit(answer_text, answer_rect)
        answernumber += 1
        y += 50

    pygame.display.update()



score = 0
question_index = 0

letteranswers = ["A","B","C","D"]
permutednumbers = random.sample(range(26), 4)
correct_index = random.randint(0, 3)

for i in range(4):
    pickedletter = letters[permutednumbers[i]]
    letteranswers[i] = pickedletter

imageletter = chosenletterimages[permutednumbers[correct_index]]

display_question(imageletter, letteranswers)




while question_index < 26:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if y >= 300:
                answer_index = (y - 300) // 50
                selected_answer = letteranswers[answer_index]

                if selected_answer == letters[permutednumbers[correct_index]]:
                    score += 1
                    text = font.render("That's Correct!", True, (0, 0, 0))
                    text_rect = text.get_rect(center=(400, 50))
                    screen.blit(text, text_rect)
                    pygame.display.update()
                    time.sleep(1)
                    
                if selected_answer != letters[permutednumbers[correct_index]]:
                    text = font.render("Sorry, that's Incorrect.", True, (0, 0, 0))
                    text_rect = text.get_rect(center=(400, 50))
                    screen.blit(text, text_rect)
                    pygame.display.update()
                    time.sleep(1)

                question_index += 1
                permutednumbers = random.sample(range(26), 4)
                correct_index = random.randint(0, 3)

                for i in range(4):
                    pickedletter = letters[permutednumbers[i]]
                    letteranswers[i] = pickedletter

                imageletter = chosenletterimages[permutednumbers[correct_index]]

                display_question(imageletter, letteranswers)


if question_index == 10:
    screen.fill((255, 255, 255))

    font = pygame.font.Font(None, 36)
    text = font.render("Your final score is: {}".format(score), True, (0, 0, 0))
    text_rect = text.get_rect(center=(400, 300))
    screen.blit(text, text_rect)

    pygame.display.update()
    pygame.time.wait(3000)

pygame.quit()
