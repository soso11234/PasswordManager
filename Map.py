import pygame
class Map:
    def __init__(self):
        self.passcode = []

    def password_drawing(self):
        pygame.init()
        size = (500,500)
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        self.passcode = []
        screen = pygame.display.set_mode(size)
        running = True
        for x in range (4):
            for y in range(4):
                pygame.draw.rect(screen,white,(100*x,100*y,100,100))
                pygame.draw.rect(screen,black,(100*x,100*y,101,101),1)
                pygame.draw.circle(screen,black,(50+100*x,50+100*y),10)     
        while running:
            if len(self.passcode) == 4: #the length of pattern 
                running = False
            else:
                pass
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    if len(self.passcode) <= 4:   #The pattern has to be 4, and a user has to know how many box the user pick, and how many box left               
                        if x < 100 and y < 100: #0
                            pygame.draw.circle(screen,red,(50,50),10)
                            self.passcode.append(1)
                        elif x < 100 and y < 200: # 1
                            pygame.draw.circle(screen,red,(50,150),10)
                            self.passcode.append(2)
                        elif x < 100 and y < 300: # 2
                            pygame.draw.circle(screen,red,(50,250),10)
                            self.passcode.append(3)
                        elif x < 100 and y < 400: #3
                            pygame.draw.circle(screen,red,(50,350),10)
                            self.passcode.append(4)
                        elif 100 < x < 200 and y < 100: 
                            pygame.draw.circle(screen,red,(150,50),10)
                            self.passcode.append(5)
                        elif 100 < x < 200 and y < 200:
                            pygame.draw.circle(screen,red,(150,150),10)
                            self.passcode.append(6)
                        elif 100 < x < 200 and y < 300:
                            pygame.draw.circle(screen,red,(150,250),10)
                            self.passcode.append(7)
                        elif 100 < x < 200 and y < 400:
                            pygame.draw.circle(screen,red,(150,350),10)
                            self.passcode.append(8)
                        elif 200 < x < 300 and y < 100:
                            pygame.draw.circle(screen,red,(250,50),10)
                            self.passcode.append(9)
                        elif 200 < x < 300 and y < 200:
                            pygame.draw.circle(screen,red,(250,150),10)
                            self.passcode.append(10)
                        elif 200 < x < 300 and y < 300:
                            pygame.draw.circle(screen,red,(250,250),10)
                            self.passcode.append(11)
                        elif 200 < x < 300 and y < 400:
                            pygame.draw.circle(screen,red,(250,350),10)
                            self.passcode.append(12)
                        elif 300 < x < 400 and y < 100:
                            pygame.draw.circle(screen,red,(350,50),10)
                            self.passcode.append(13)
                        elif 300 < x < 400 and y < 200:
                            pygame.draw.circle(screen,red,(350,150),10)
                            self.passcode.append(14)
                        elif 300 < x < 400 and y < 300:
                            pygame.draw.circle(screen,red,(350,250),10)
                            self.passcode.append(15)
                        elif 300 < x < 400 and y < 400:
                            pygame.draw.circle(screen,red,(350,350),10)
                            self.passcode.append(16)
                        else:
                            break
                    else:
                        print('click 5, close it ')
                        running = False
                    
            pygame.display.update()
        self.passcode.sort() # Password has to be same, even though a user start from any points ex)1,2,3,4 = 4,3,2,1
        return self.passcode

    def get_passcode(self):
        return self.passcode