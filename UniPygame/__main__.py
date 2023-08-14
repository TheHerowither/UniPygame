from commons import MultilineTextRender, Scene, Entity, Sprite, Vec2
import pygame
def main():
    global fontsize, font1


    pygame.init()
    surf = pygame.display.set_mode((1080,720))

    text = font1.render("", True, pygame.Color(255,255,255))

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
    
        if key == pygame.K_RETURN:
            if scene.get_active():
                scene.switch_to_scene(scene2)
            if scene2.get_active():
                scene2.switch_to_scene(scene)

    def update_text(self):
        self.image = MultilineTextRender(font1, f"Local scene time: {round(scene.local_scene_time, 3)}\nTotal time: {round(scene.total_time, 3)}\nTotal frames: {scene.total_frames}", pygame.Color(255,255,255), pygame.Color(255, 255, 255, 127))

    scene = Scene(surf, keydown_listener = keydown)
    scene2 = scene.create_scene()


    im1 = pygame.image.load("unipygame/image.jpg")


    obj1 = Entity(scene = scene, color = pygame.Color(255,255,255), rect = pygame.Rect(100,100,10,10), frame_funtion = move)
    imobj1 = Sprite(scene = scene, image = im1, position = Vec2(400, 400), frame_function = move)

    obj3 = Entity(scene = scene2, color = pygame.Color(255,255,255), rect = pygame.Rect(100,100,10,10), frame_funtion = move)

    obj2 = Entity.Instantiate(obj1, (10,10))
    imobj2 = Sprite.Instantiate(imobj1, (200, 200))

    running = True


    pygame.display.set_caption('UniPygame Playgroud')

    

    dbg_text = Sprite(scene = scene, image = text, position = Vec2(500, 100), frame_function = update_text)


    scene.Awake()
    while running:
        if scene.quit_event:
            pygame.quit()
            running = False
            break
    
    
        scene.Update()
def physics_main():
    pygame.init()

    surf = pygame.display.set_mode((1080,720))

    scene = Scene(surf)
    obj = Entity(scene = scene, color = pygame.Color(255,255,255), rect = pygame.Rect(100,100,50,50), ridgidbody = True, collider = True)
    ground = Entity(scene = scene, color = pygame.Color(155,155,155), rect = pygame.Rect(100,500,100,20), ridgidbody = False, collider = True)

    ground.bouncieness = 1

    running = True
    scene.Awake()
    while running:
        if scene.quit_event:
            pygame.quit()
            running = False
            break
    
    
        scene.Update()

if __name__ == "__main__":
    fontsize = 32
    pygame.font.init()
    font1 = pygame.font.Font('freesansbold.ttf', fontsize)
    physics_main()