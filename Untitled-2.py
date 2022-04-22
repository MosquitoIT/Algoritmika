import pygame 
pygame.init()

back = (255,15,21)
mw = pygame.display.set_mode((700,500))
mw.fill(back)

#цвета
black = (0,0,0)
light_blue = (190, 184, 248)
class TextArea():
    def __init__(self,x=0, y=0, width = 10, height = 10 , color = None):
        self.rect = pygame.Rect(x, y, width, height)
        #цвет заливки
        self.fill_color = color
    def set_text(self, text, fsize = 13, text_color = black):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True , text_color)
    def draw(self, shift_x = 0, shift_y = 0):
        pygame.draw.rect(mw, self.fill_color, self.rect)
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
quest_card = TextArea(120,100,290,70, light_blue)
quest_card.set_text('Вопрос', 75)
answer_card = TextArea(120,240,290,70, light_blue)
answer_card.set_text('Ответ', 75)

while True:
    #quest_card.draw(10,10)
    #answer_card.draw(10,10)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K.q:
                quest_carl.set_text('Что мы сейчас изучаем на курсах в Алгоритмике?',75)
                if event_key == pygame.K.a:
                    answer_card.set_text('Pyhton',75)
                answer_card.draw(10,25)
