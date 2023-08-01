# UniPygame - A Unity-similar entity system for pygame
UniPygame is a system for unity-similar objects, but in pygame.
It allows you to define single entites and not have to bother with long complicated mainloops. 


## UniPygame Entities
A basic rect on the screen, would look like this:
```python
from UniPygame import Scene, Entity
import pygame



pygame.init()
screen = pygame.display.set_mode((1080,720))
scene = Scene(surf = screen, clear_color = pygame.Color(255,255,255))

cube = Entity(scene = scene, color = pygame.Color(255, 0, 0), rect = pygame.Rect(100,100,100,100))

running = True
scene.Awake()
while running:
    if scene.quit_event:
        pygame.display.quit()
        running = False
    
    scene.Update(fps_limit = 60)
```

## UniPygame Sprites
As you might have seen in the example above, an ``Entity`` can only be a ``rect``.

If you, however want to add something like an image to a scene, you can use a different class, the ``Sprite``. It would look something like this:
```python
from UniPygame import Scene, Sprite, Vec2
import pygame



pygame.init()
screen = pygame.display.set_mode((1080,720))
scene = Scene(surf = screen, clear_color = pygame.Color(255,255,255))

image = Sprite(scene = scene, image = pygame.image.load("image.png"), position = Vec2(100,100))

running = True
scene.Awake()
while running:
    if scene.quit_event:
        pygame.display.quit()
        running = False
    
    scene.Update(fps_limit = 60)
```
As you can see, not terribly different

And however large the amount of Entities and Sprites you add, the ```while running``` loop will always have the same size

## UniPygame Input system
Well, now you might be wondering, since the loop is always the same size, how will inputs work?
Well for that there is a parameter in the Scene class ``Scene.keydown_listener``, this parameter needs a function into it, this function has to have a keyword argument ``key``, everytime a button is pressed, this argument will be set to the pygame key code of the pressed key, and the function will be called.

An effective listener would look like this:
```python
from UniPygame import Scene
import pygame



pygame.init()
def keydown(key):
    if key == pygame.K_1:
        print("Key 1 has been pressed")
    if key == pygame.K_2:
        print("Key 2 has been pressed")
    if key == pygame.K_3:
        print("Key 3 has been pressed")

screen = pygame.display.set_mode((1080, 720))
scene = Scene(surf = screen, clear_color = pygame.Color(255,255,255), keydown_listener = keydown)
```
Also, the same works for the keyup event, using the ``Scene.keyup_listener`` parameter.

But if you want continuus button presses, there is a list in the scene ``Scene.held_keys`` where you just have to index the pygame key code of the key you want to check if its pressed/held pressed, and do something with that.