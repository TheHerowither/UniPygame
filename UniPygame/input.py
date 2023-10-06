import pygame
from enum import Enum


class KeyCode(Enum):
    __keys__ = {"1" : pygame.K_1, "2" : pygame.K_2, "3" : pygame.K_3, "4" : pygame.K_4, "5" : pygame.K_5,"6" : pygame.K_6, "7" : pygame.K_7, "8" : pygame.K_8, "1" : pygame.K_9, "0" : pygame.K_0,
                "q" : pygame.K_q, "w" : pygame.K_w, "e" : pygame.K_e, "r" : pygame.K_r, "t" : pygame.K_t, "y" : pygame.K_y, "u" : pygame.K_u, "i" : pygame.K_i, "o" : pygame.K_o, "p" : pygame.K_p,
                "a" : pygame.K_a, "s" : pygame.K_s, "d" : pygame.K_d, "f" : pygame.K_f, "g" : pygame.K_g, "h" : pygame.K_h, "j" : pygame.K_j, "k" : pygame.K_k, "l" : pygame.K_l,
                "z" : pygame.K_z, "x" : pygame.K_x, "c" : pygame.K_c, "v" : pygame.K_v, "b" : pygame.K_b, "n" : pygame.K_n, "m" : pygame.K_m, "," : pygame.K_COMMA, "." : pygame.K_PERIOD,
                ";" : pygame.K_SEMICOLON, ":" : pygame.K_COLON}
    Return = pygame.K_RETURN
    LeftShift = pygame.K_LSHIFT
    RightShift = pygame.K_RSHIFT
    Tab = pygame.K_TAB
    CapsLock = pygame.K_CAPSLOCK
    Escape = pygame.K_ESCAPE
    def FromStr(self, key : int) -> int:
        return self.__class__.__keys__[key]
class InputHandler:
    def __init__(self) -> None:
        pass
    def GetKey(self, keycode) -> bool:
        if type(keycode) == KeyCode:
            return pygame.key.get_pressed()[keycode.value]
        else:
            return pygame.key.get_pressed()[keycode]