import time
import traceback

import mido
import pygame.time
import midisettings as ms

# pygame mixer init
freq = 44100
bitsize = 16
channels = 1
buffer = 2048
pygame.mixer.init(freq, bitsize, channels, buffer)
bpm = 170


def main():
    mid = []
    for i in range(len(ms.notelist)):
        mid.append(mido.MidiFile())
        track = mido.MidiTrack()
        mid[i].tracks.append(track)
        track.append(mido.MetaMessage('track_name', name='track1', time=0))
        track.append(mido.Message('program_change', program=1, time=0))
        track.append(mido.MetaMessage('set_tempo', tempo=int(6 * 1e7) // ms.bmp[i], time=0))
        for j in ms.notelist[i]:
            track.append(mido.Message('note_on', note=j[0], velocity=j[1], time=j[2]))
            track.append(mido.Message('note_off', note=j[0], velocity=j[1], time=j[3]))
    mid[0].save('internationale.mid')
    mid[1].save('katyusha.mid')
    play_midi('internationale.mid')
    time.sleep(2)
    play_midi('katyusha.mid')


def play_midi(file):
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(file)
    except pygame.error:
        traceback.print_exc()
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(30)


if __name__ == '__main__':
    main()
