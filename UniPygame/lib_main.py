from pygame import surface, Rect, draw, Color, display, time, event, key, font, QUIT, KEYDOWN, KEYUP, SRCALPHA
from inspect import getfullargspec
from UniPygame.utils import *
from UniPygame.exceptions import *
import time as tm


def none(key):
    pass
class Scene:
    def __init__(self, surf : surface.Surface, clear_color : Color = Color(0,0,0), keydown_listener = none, keyup_listener = none):
        self.surf = surf
        self.clear_color = clear_color
        self._in_scene_entities:list(Entity) = []
        self._in_scene_sprites:list(Sprite) = []
        self._Eid_offset = 0
        self._Sid_offset = 0
        self.delta_time = 0
        self._last = tm.time()
        self._start_time = 0
        self._create_time = tm.time()
        self._clock = time.Clock()
        self._active = True

        self.local_scene_time = 0
        self.total_time = 0

        self.total_frames = 0
        self.frames_per_second = 0
        self.fps = 0

        self.keydown_listener = keydown_listener
        self.keyup_listener = keyup_listener

        self.quit_event = None
        self.keydown = None
        self.keyup = None
        self.held_keys = None
    def __getfreeEid__(self):
        return len(self._in_scene_entities) + self._Eid_offset
    def __getfreeSid__(self):
        return len(self._in_scene_sprites) + self._Sid_offset
    def __getentity__(self, index : int):
        return self._in_scene_entities[index]
    def __getbyEid__(self, id : int):
        for e in self._in_scene_entities:
            if e.id == id:
                return e
    def __getbySid__(self, id : int):
        for s in self._in_scene_sprites:
            if s.id == id:
                return s
    def __removeentity__(self, id : int):
        try:
            self._in_scene_entities.pop(self._in_scene_entities.index(self.__getbyEid__(id)))
            self._Eid_offset += 1
        except ValueError:
            pass
    def __removesprite__(self, id : int):
        try:
            self._in_scene_sprites.pop(self._in_scene_sprites.index(self.__getbySid__(id)))
            self._Sid_offset += 1
        except ValueError:
            pass
    def __updateids__(self):
        for e in self._in_scene_entities:
            e.id = self._in_scene_entities.index(e)
    def __checkfunc__(self, func):
        args = getfullargspec(func)[0]
        if "self" not in args:
            raise MissingFunctionParameterError("Missing function keyword parameter 'self'")
    def __checkifunc__(self, func):
        args = getfullargspec(func)[0]
        if "key" not in args:
            raise MissingFunctionParameterError("Missing function keyword parameter 'key'")
    def Awake(self):
        "Function to be called right before the loop starts"
        self._start_time = tm.time()
        for e in self._in_scene_entities:
            self.__checkfunc__(e.awake_function)
            e.awake_function(self = e)
        for s in self._in_scene_sprites:
            self.__checkfunc__(s.awake_function)
            s.awake_function(self = s)
    def Update(self, fps_limit : int = 60):
        if self._active:
            t = time.get_ticks()
            self._clock.tick(fps_limit)

            self.frames_per_second = self._clock.get_fps()
            self.fps = self.frames_per_second
            self.total_frames += 1
        
            self.local_scene_time = tm.time() - self._start_time if self._start_time != 0 else 0
            self.total_time = tm.time() - self._start_time

            self.delta_time = (t - self._last) / 1000.0
            self.held_keys = key.get_pressed()
        
            try: self.surf.fill(self.clear_color)
            except: pass
            for eve in event.get():
                self.quit_event = eve.type == QUIT
                if eve.type == KEYDOWN: 
                    self.keydown_listener(key = eve.key)
                    self.keydown = eve.key
                    self.keyup = None

                if eve.type == KEYUP:
                    self.keyup_listener(key = eve.key)
                    self.keyup = eve.key
                    self.keydown = None
            for e in self._in_scene_entities:
                self.__checkfunc__(e.frame_function)
                if e.enabled:
                    e.frame_function(self = e)
                    e.draw(self.surf)
        
            for s in self._in_scene_sprites:
                self.__checkfunc__(s.frame_function)
                if s.enabled:
                    s.frame_function(self = s)
                    s.draw(self.surf)
            try:
                display.flip()
            except Exception as e:
                print(e)
            self._last = t
    def Create_scene(self):
        "This will create a copy of the scene, use this when creating more than one scene"
        scene = Scene(surf = self.surf, clear_color = self.clear_color, keydown_listener = self.keydown_listener, keyup_listener = self.keyup_listener)
        scene._active = False
        return scene
    def Switch_to_scene(self, scene):
        self._active = False
        scene.Awake()
        scene._active = True

def none(self):
    pass

class Entity:
    def __init__(self, scene : Scene, color : Color, rect : Rect, frame_funtion = none, awake_function = none):
        self.scene = scene
        self.rect = rect
        self.color = color
        self.position = to_vec(self.rect.center)
        self.enabled = True
        self.frame_function = frame_funtion
        self.awake_function = awake_function

        self.id = self.scene.__getfreeEid__()
        self.scene._in_scene_entities.append(self)   
    
    def draw(self, surf : surface.Surface):
        self.rect.center = self.position.to_tuple()
        try:
            draw.rect(surf, self.color, self.rect)
        except:
            pass
    def toggle(self):
        self.enabled = not self.enabled


    def Instantiate(entity, at_position : tuple = ()):
        if (len(at_position) == 2):
            entity.rect.center = at_position
        return Entity(entity.scene, entity.color, entity.rect, entity.frame_function)
    def Destroy(entity):
        entity.scene.__removeentity__(entity.id)

class Sprite:
    def __init__(self, scene : Scene, image : surface.Surface, position : Vec2, frame_function = none, awake_function = none):
        self.scene = scene
        self.image = image
        self.rect = self.image.get_rect()
        self.position = position
        self.enabled = True
        self.frame_function = frame_function
        self.awake_function = awake_function

        self.id = self.scene.__getfreeSid__()
        self.scene._in_scene_sprites.append(self)
    def draw(self, surf : surface.Surface):
        self.position = to_vec(self.position) if type(self.position) == tuple else self.position
        pos = self.position.to_tuple()
        self.rect.center = pos
        try:
            surf.blit(self.image, self.rect)
        except:
            pass
    def toggle(self):
        self.enabled = not self.enabled


    def Instantiate(sprite, at_position : tuple = ()):
        pos = sprite.position
        if (len(at_position) == 2):
            pos = at_position
        return Sprite(sprite.scene,  sprite.image, pos, sprite.frame_function)
    def Destroy(sprite):
        sprite.scene.__removesprite__(sprite.id)
def MultilineTextRender(font_object : font.Font, text : str, color : Color, background : Color = Color(0,0,0,0)):
    lines = text.split("\n")
    surf = surface.Surface((font_object.render(max(lines, key = len), True, color, background).get_rect().width, font_object.render(lines[0], True, color, background).get_rect().height * len(lines)), SRCALPHA).convert_alpha()
    surf.fill(background)
    for line in lines:
        txt = font_object.render(line, True, color)
        height = txt.get_rect().height
        rect = txt.get_rect()
        rect.centery = height * lines.index(line) + (height / 2)

        surf.blit(txt, rect)
    return surf