import os, sys, re
import time, random
import numpy as np
import wave, math, argparse, pygame
from collections import deque
from  matplotlib import pyplot as plt
import pygame.locals
ShowPlot = False
# notes of a Pentatonic Minor scale
Notes = {'a': 220, 'b': 234, 'b#': 247, 'c1': 262,'c1#': 278, 'd1': 294, 'e1': 330, 'f1': 349, 'g1': 391, 'a1': 440, 'b1': 494, 'c2': 523}
# 在此处修改你想要的声音的频率 上述是根据十二平均律，中央C的对应频率
def WriteWave(fname, data):
    file = wave.open(fname, 'wb')
    nchannels = 1
    samplewidth = 2
    framerate = 44100
    nframes = 44100
    file.setparams((nchannels, samplewidth, framerate, nframes, 'NONE', 'noncompressed'))
    file.writeframes(data)
    file.close()

def GenerateNote(freq):
    nsample = 44100
    samplerate = 44100
    N = int(samplerate/freq)
    buf = deque([random.random() - 0.5 for i in range(N)])
    if ShowPlot:
        axline, = plt.plot(buf)
    samples = np.array([0]*nsample, 'float32')
    for i in range(nsample):
        samples[i] = buf[0]
        avg = 0.5*0.995*(buf[0]+buf[1])
        buf.append(avg)
        buf.popleft()
        if ShowPlot:
            axline.set_ydata(buf)

    samples = np.array(samples*32767, 'int16')
    return samples.tostring()

class NotePlayer:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 2048)
        pygame.init()
        self.notes = {}
    def add(self, filename):
        self.notes[filename] = pygame.mixer.Sound(filename)
    def Play(self, filename):
        try:
            self.notes[filename].play()
        except:
            print(filename + 'Not Found!')
    def PlayRandom(self):
        index = random.randint(0,len(self.notes) - 1)
        note = list(self.notes.values())[index]
        note.play()

def  main():
    global ShowPlot

    parser = argparse.ArgumentParser(description = "Generating Sounds with Karplus String Algorithm...")
    parser.add_argument('--display', action = 'store_true', required=False)
    parser.add_argument('--play', action = 'store_true', required=False)
    parser.add_argument('--piano', action = 'store_true', required=False)
    parser.add_argument('--playasong', action = 'store_true', required=False)
    args = parser.parse_args()

    screen = pygame.display.set_mode((600, 576))

    # 设置应用程序窗口标签名称
    pygame.display.set_caption('Laputa')

    if args.display:
        ShowPlot = True

    nplayer = NotePlayer()

    print('Creating Notes...')
    for name, freq in list(Notes.items()):
        filename = name + '.wav'
        if not os.path.exists(filename) or args.display:
            data = GenerateNote(freq)
            print('Creating' + ' ' +filename + '...')
            WriteWave(filename, data)
        else:
            print('File already exists, skipping...')

        nplayer.add(name + '.wav')

        if args.display:
            nplayer.Play(name + '.wav')
            time.sleep(0.5)
            plt.show()

    if args.play:
        while True:
            try:
                nplayer.PlayRandom()
                rest = np.random.choice([1, 2, 4, 8], 1, p = [0.15, 0.7, 0.1, 0.05])
                time.sleep(0.25*rest[0])
            except KeyboardInterrupt:
                exit()

    if args.playasong:
        space = pygame.image.load("timg.png")
        screen.blit(space, (0, 0))
        pygame.display.update()
        try:
            f = open("song.txt", 'r')
            for line in f.readlines():
                l = line.split( )
                for i in range(len(l)):
                    if l[i] == '0':
                        time.sleep(0.5)
                    else:
                        nplayer.Play(l[i] + '.wav')
                        time.sleep(0.5)
        except IOError:
            exit()

    if args.piano:
        while True:
            space = pygame.image.load("timg.png")
            screen.blit(space, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()  # 退出pygame
                    sys.exit()  # 销毁程序
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print('Key pressed!')
                        nplayer.Play('a.wav')
                        time.sleep(0.5)
                    if event.key == pygame.K_s:
                        print('Key pressed!')
                        nplayer.Play('b#.wav')
                        time.sleep(0.5)
                    if event.key == pygame.K_e:
                        print('Key pressed!')
                        nplayer.Play('b.wav')
                        time.sleep(0.5)
                    if event.key == pygame.K_d:
                        print('Key pressed!')
                        nplayer.Play('c1.wav')
                        time.sleep(0.5)
                    if event.key == pygame.K_f:
                        print('Key pressed!')
                        nplayer.Play('d1.wav')
                        time.sleep(0.5)
                    if event.key == pygame.K_g:
                        print('Key pressed!')
                        nplayer.Play('e1.wav')
                        time.sleep(0.5)
                    if event.key == pygame.K_h:
                        print('Key pressed!')
                        nplayer.Play('f1.wav')
                        time.sleep(0.5)
                    if event.key == pygame.K_j:
                        print('Key pressed!')
                        nplayer.Play('g1.wav')
                        time.sleep(0.5)
                    if event.key == pygame.K_k:
                        print('Key pressed!')
                        nplayer.Play('a1.wav')
                        time.sleep(0.5)
                    if event.key == pygame.K_l:
                        print('Key pressed!')
                        nplayer.Play('b1.wav')
                        time.sleep(0.5)
            pygame.display.update()

if __name__ == '__main__':
    main()
