from unipygame import *
import pygame
def main():
    global fontsize, font1


    pygame.init()
    surf = pygame.display.set_mode((1080,720))

    text = font1.render("", True, pygame.Color(255,255,255))

    def move(self):
        if scene.held_keys[pygame.K_s]:
            self.position.y += 20 * scene.delta_time
    def keydown():
        global font1, fontsize
        if Input.GetKeyPressed(GetKeyCode("1")):
            obj2.toggle()
        if Input.GetKeyPressed(GetKeyCode("2")):
            imobj2.toggle()
    
        if Input.GetKeyPressed(KeyCode.NumpadMinus):
            font1 = pygame.font.Font("freesansbold.ttf", fontsize - 1)
            fontsize -= 1
        if Input.GetKeyPressed(KeyCode.NumpadPlus):
            font1 = pygame.font.Font("freesansbold.ttf", fontsize + 1)
            fontsize += 1
        if Input.GetKeyPressed(KeyCode.Tab):
            dbg_text.toggle()
    
        if Input.GetKeyPressed(KeyCode.Return):
            if scene.get_active():
                scene.switch_to_scene(scene2)
            if scene2.get_active():
                scene2.switch_to_scene(scene)

    def update_text(self):
        self.image = MultilineTextRender(font1, f"Local scene time: {round(scene.local_scene_time, 3)}\nTotal time: {round(scene.total_time, 3)}\nTotal frames: {scene.total_frames}", pygame.Color(255,255,255), pygame.Color(255, 255, 255, 127))

    scene = Scene(surf, update_func = keydown)
    scene2 = scene.create_scene()


    im1 = pygame.image.load("unipygame/image.jpg")


    obj1 = Entity(scene = scene, color = pygame.Color(255,255,255), rect = pygame.Rect(100,100,10,10), frame_funtion = move)
    imobj1 = Sprite(scene = scene, image = im1, position = Vec2(400, 400), frame_function = move)

    obj3 = Entity(scene = scene2, color = pygame.Color(255,255,255), rect = pygame.Rect(100,100,10,10), frame_funtion = move)

    obj2 = Entity.Instantiate(obj1, (10,10))
    imobj2 = Sprite.Instantiate(imobj1, (200, 200))



    pygame.display.set_caption('UniPygame Playgroud')

    

    dbg_text = Sprite(scene = scene, image = text, position = Vec2(500, 100), frame_function = update_text)


    scene.Awake()
    while scene.get_running():
        if Input.quit_event:
            scene.stop()
            break
    
    
        scene.Update()
def physics_main():
    pygame.init()

    surf = pygame.display.set_mode((1080,720))
    pygame.display.set_caption("UniPygame Physics Playground")

    scene = Scene(surf)
    obj = Entity(scene = scene, color = pygame.Color(255,255,255), rect = pygame.Rect(100,100,50,50), components=[Ridgidbody,])
    ground = Entity(scene = scene, color = pygame.Color(155,155,155), rect = pygame.Rect(100,500,100,20), components=[Collider, Ridgidbody])

    

    scene.Awake()

    ground.GetComponent(Ridgidbody).simulated = False
    ground.GetComponent(Ridgidbody).bouncieness = .9
    obj.GetComponent(Ridgidbody).density = 1.0

    while scene.get_running():
        if Input.quit_event:
            pygame.quit()
            break
    
    
        scene.Update()
def layering_main():
    pygame.init()

    app = pygame.display.set_mode((1080,720))

    def keydown():
        if Input.GetKeyPressed(KeyCode.Tab):
            if obj1.layer == 1: obj1.layer = 0
            elif obj1.layer == 0: obj1.layer = 1
            if obj2.layer == 1: obj2.layer = 0
            elif obj2.layer == 0: obj2.layer = 1

    scene = Scene(app, update_func=keydown)
    obj1 = Entity(scene, color = pygame.Color(0,155,255), rect=pygame.Rect(100,100,50,50), layer=1)
    obj2 = Entity(scene, color = pygame.Color(255,155,0), rect=pygame.Rect(130,130,50,50), layer=0)

    scene.Awake()

    while scene.get_active():
        if Input.quit_event:
            pygame.quit()
            break
    
    
        scene.Update()
def music_main():
    pygame.init()

    app = pygame.display.set_mode((1080,720))


    music_player = JsonPlayer("test_music.json", .05)

    def awake(self):
        music_player.playall()
    def update():
        if Input.GetKeyPressed(KeyCode.Escape):
            scene.stop()
        if Input.GetKeyPressed(GetKeyCode("1")):
             music_player.toggle("twists")
             print("Toggling song 1")
        if Input.GetKeyPressed(GetKeyCode("2")):
             music_player.toggle("waking-the-devil")
             print("Toggling song 2")
    scene = Scene(app, update_func=update)
    Entity(scene, pygame.Color(0,0,0,0), pygame.Rect(0,0,0,0), awake_function=awake)

    scene.Awake()

    while scene.get_running():
        if Input.quit_event:
            scene.stop()
            break
    
    
        scene.Update()
if __name__ == "__main__":
    fontsize = 32
    pygame.font.init()
    font1 = pygame.font.Font('freesansbold.ttf', fontsize)
    main()