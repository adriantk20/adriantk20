import pygame, sys

pygame.init()

#Map layout
level_map = [
'                           ',
'           X               ',
'     X                     ',
'                    X      ',
'                           ',
'           X               ',
'     X                     ',
'                           ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXX']

#defining essential variables
tile_size = 64
screen_width = 1200
screen_height = len(level_map)*tile_size
bg_img = pygame.image.load('./GameGraphics/64_bit_background.png')
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

#level blocks sprites
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)

#level setup
class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.level_setup(level_data)
    def level_setup(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                if cell == 'X':
                    x = col_index*tile_size
                    y = row_index*tile_size
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
    def run(self):
        self.tiles.draw(self.display_surface)

#Defining player
class Player:
    def __init__(self, x, y, speed, height, width, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.height = height
        self.width = width
        self.color = color

        #Player controlls
    def move(self, pressed_keys):
        if pressed_keys[pygame.K_a]:
            self.x -= self.speed
        elif pressed_keys[pygame.K_d]:
            self.x += self.speed
        #elif pressed_keys[pygame.K_SPACE]:

    def draw_player(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))


print('funkar')
level = Level(level_map, screen)
#Game running loop
while True:
    screen.blit(bg_img, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    player = Player(200, 100, 5, 20, 5, (155,155,155))

    player.move(pressed_keys)
    screen.fill('black')
    level.run()
    pygame.display.update()
    clock.tick(60)