import pygame
from enum import Enum


class KeyCode(Enum):
    __keys__ = {"1":pygame.K_1, "2":pygame.K_2, "3":pygame.K_3, "4":pygame.K_4, "5":pygame.K_5,"6":pygame.K_6, "7":pygame.K_7, "8":pygame.K_8, "9":pygame.K_9, "0":pygame.K_0,
                "q":pygame.K_q, "w":pygame.K_w, "e":pygame.K_e, "r":pygame.K_r, "t":pygame.K_t, "y":pygame.K_y, "u":pygame.K_u, "i":pygame.K_i, "o":pygame.K_o, "p":pygame.K_p,
                "a":pygame.K_a, "s":pygame.K_s, "d":pygame.K_d, "f":pygame.K_f, "g":pygame.K_g, "h":pygame.K_h, "j":pygame.K_j, "k":pygame.K_k, "l":pygame.K_l,
                "z":pygame.K_z, "x":pygame.K_x, "c":pygame.K_c, "v":pygame.K_v, "b":pygame.K_b, "n":pygame.K_n, "m":pygame.K_m, ",":pygame.K_COMMA, ".":pygame.K_PERIOD,
                ";":pygame.K_SEMICOLON, ":":pygame.K_COLON, "+" : pygame.K_PLUS, "-" : pygame.K_MINUS}
    Return = pygame.K_RETURN
    LeftShift = pygame.K_LSHIFT
    RightShift = pygame.K_RSHIFT
    Tab = pygame.K_TAB
    CapsLock = pygame.K_CAPSLOCK
    Escape = pygame.K_ESCAPE

    NumpadPlus = pygame.K_KP_PLUS
    NumpadMinus = pygame.K_KP_MINUS
    NumpadMultiply = pygame.K_KP_MULTIPLY
    NumpadDivide = pygame.K_KP_DIVIDE

    Numpad0 = pygame.K_KP0
    Numpad1 = pygame.K_KP1
    Numpad2 = pygame.K_KP2
    Numpad3 = pygame.K_KP3
    Numpad4 = pygame.K_KP4
    Numpad5 = pygame.K_KP5
    Numpad6 = pygame.K_KP6
    Numpad7 = pygame.K_KP7
    Numpad8 = pygame.K_KP8
    Numpad9 = pygame.K_KP9
    
def GetKeyCode(key : str) -> int:
    return KeyCode.__keys__[key]
class InputHandler:
    def __init__(self) -> None:
        self.__keydown__ = -1
        self.__keyup__ = -1
        self.quit_event = False
    def GetKey(self, keycode) -> bool:
        if type(keycode) == KeyCode:
            return pygame.key.get_pressed()[keycode.value]
        else:
            return pygame.key.get_pressed()[keycode]
    def GetKeyPressed(self, keycode) -> bool:
        code = keycode
        if type(keycode) == KeyCode:
            code = keycode.value

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.__keydown__ = event.key
            if event.type == pygame.QUIT:
                self.quit_event = True
        if self.__keydown__ == code:
            self.__keydown__ = -1
            return True
        return False
        
    def GetKeyReleased(self, keycode) -> bool:
        code = keycode
        if type(keycode) == KeyCode:
            code = keycode.value
        
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                self.__keyup__ = event.key
                if self.__keyup__ == code:
                    self.__keyup__ = -1
                    return True
                self.__keyup__ = -1
                return False
            if event.type == pygame.QUIT:
                self.quit_event = True
                print("QUIT EVENT")
        
    def __setkeydown__(self, key):
        self.__keydown__ = key
    def __setkeyup__(self, key):
        self.__keyup__ = key