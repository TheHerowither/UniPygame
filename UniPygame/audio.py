from pygame import mixer
from json import load


class AudioPlayer:
    def __init__(self, clip : str, volume : float, channel : int):
        self.clip = clip
        self.volume = volume
        self.channel = channel

        self.__playing__ = False
        self.__channel__ = mixer.Channel(self.get_channel())

        mixer.init()
        #mixer.music.load(self.clip)
        #mixer.Channel(self.get_channel()).play(mixer.Sound(self.get_clip()))
        mixer.Channel(self.get_channel()).set_volume(self.get_volume())
    def get_clip(self) -> str:
        return self.clip
    def get_volume(self) -> float:
        return self.volume
    def get_channel(self) -> int:
        return self.channel
    def get_playing(self) -> bool:
        return self.__playing__

    def play(self):
        self.__playing__ = True
        self.__channel__.play(mixer.Sound(self.get_clip()))
    def pause(self):
        self.__playing__ = False
        self.__channel__.pause()
    def resume(self):
        self.__playing__ = True
        self.__channel__.unpause()
    def stop(self):
        self.__playing__ = False
        self.__channel__.stop()
    def toggle(self):
        if self.get_playing(): self.pause()
        else: self.resume()
    def set_volume(self, new_volume : int):
        self.volume = new_volume
        self.__channel__.set_volume(self.get_volume())

class JsonPlayer:
    def __init__(self, paths_jsonpath : str, volume : float):
        self.path = paths_jsonpath
        self.__clips__ = load(open(self.path))

        self.__players__ = {}
        for key in self.__clips__.keys():
            self.__players__[key] = AudioPlayer(self.__clips__[key], volume, list(self.__clips__.keys()).index(key))
    def get_clips(self) -> dict:
        return self.__clips__
    def get_players(self) -> dict:
        return self.__players__
    
    def playall(self):
        for clip in self.get_clips().keys():
            self.play(clip)
    def pauseall(self):
        for clip in self.get_clips().keys():
            self.pause(clip)
    def resumeall(self):
        for clip in self.get_clips().keys():
            self.resume(clip)
    def stopall(self):
        for clip in self.get_clips().keys():
            self.stop(clip)
    def toggleall(self):
        for clip in self.get_clips().keys():
            self.toggle(clip)
    def setvolumeall(self, volume : float):
        for clip in self.get_clips().keys():
            self.set_volume(clip, volume)
    
    def play(self, clip : str):
        self.__players__[clip].play()
    def pause(self, clip : str):
        self.__players__[clip].pause()
    def resume(self, clip : str):
        self.__players__[clip].resume()
    def stop(self, clip : str):
        self.__players__[clip].stop()
    def toggle(self, clip : str):
        self.__players__[clip].toggle()
    def set_volume(self, clip : str, volume : float):
        self.__players__[clip].set_volume(volume)