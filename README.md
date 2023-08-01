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

And however large the amount of Entities and Sprites you add, the ```while running``` loop will allways have the same size