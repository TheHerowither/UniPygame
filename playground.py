from UniPygame import *
import pygame



pygame.init()
surf = pygame.display.set_mode((1080,720))


def move(self):
    if scene.held_keys[pygame.K_s]:
        self.position.y += 20 * scene.delta_time
def keydown(key):
    global font1, fontsize
    if key == pygame.K_1:
        obj2.toggle()
    if key == pygame.K_2:
        imobj2.toggle()
    
    if key == pygame.K_KP_MINUS:
        font1 = pygame.font.Font("freesansbold.ttf", fontsize - 1)
        fontsize -= 1
    if key == pygame.K_KP_PLUS:
        font1 = pygame.font.Font("freesansbold.ttf", fontsize + 1)
        fontsize += 1
    if key == pygame.K_TAB:
        dbg_text.toggle()
def update_text(self):
    self.image = MultilineTextRender(font1, f"Local scene time: {round(scene.local_scene_time, 3)}\nTotal time: {round(scene.total_time, 3)}\nTotal frames: {scene.total_frames}", pygame.Color(255,255,255), pygame.Color(255, 255, 255, 127))

scene = Scene(surf, keydown_listener = keydown)

im1 = pygame.image.load("image.jpg")


obj1 = Entity(scene = scene, color = pygame.Color(255,255,255), rect = pygame.Rect(100,100,10,10), frame_funtion = move)
imobj1 = Sprite(scene = scene, image = im1, position = Vec2(400, 400), frame_function = move)

obj2 = Entity.Instantiate(obj1, (10,10))
imobj2 = Sprite.Instantiate(imobj1, (200, 200))

running = True


pygame.display.set_caption('RendPyGame Playgroud')

fontsize = 32
font1 = pygame.font.Font('freesansbold.ttf', fontsize)
text = font1.render("", True, pygame.Color(255,255,255))

dbg_text = Sprite(scene = scene, image = text, position = Vec2(500, 100), frame_function = update_text)


scene.Awake()
while running:
    if scene.quit_event:
        pygame.quit()
        running = False
        break
    
    
    scene.Update()