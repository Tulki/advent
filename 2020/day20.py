from shared import *
import math
import random

class ImageTile:
    subTileIDs = []
    tileImage = None

    def __init__(self, tileID, tileImage):
        self.subTileIDs = []
        self.subTileIDs.append([tileID])
        self.tileImage = []
        for line in tileImage:
            self.tileImage.append(line)

    def pretty(self):
        for line in self.tileImage:
            print(line)
        print()
        for line in self.subTileIDs:
            print(line)

    def width(self):
        return len(self.tileImage[0])

    def height(self):
        return len(self.tileImage)

    def flipHorizontal(self):
        i = 0
        while i < self.height():
            self.tileImage[i] = self.tileImage[i][::-1]
            i += 1

        i = 0
        while i < len(self.subTileIDs):
            self.subTileIDs[i].reverse()
            i += 1

    def rotateClockwise(self):
        newImage = []
        i = 0
        while i < self.width():
            newImage.append('')
            j = 0
            while j < self.height():
                newImage[i] = newImage[i] + self.tileImage[self.height()-j-1][i]
                j += 1
            i += 1
        self.tileImage = newImage

        newIDs = []
        i = 0
        while i < len(self.subTileIDs[0]):
            newIDs.append([])
            j = 0
            while j < len(self.subTileIDs):
                newIDs[i].append(self.subTileIDs[len(self.subTileIDs)-j-1][i])
                j += 1
            i += 1
        self.subTileIDs = newIDs

    def getWestTopToBottom(self):
        i = 0
        result = ''
        while i < self.height():
            result = result + self.tileImage[i][0]
            i += 1
        return result

    def getEastTopToBottom(self):
        i = 0
        result = ''
        while i < self.height():
            result = result + self.tileImage[i][self.width()-1]
            i += 1
        return result

    def matchMyEastToTheirWest(self, them, maxWidth):
        # Do not want to join image tiles if this would exceed the full image's width.
        if self.width() + them.width() > maxWidth:
            return False

        myEast = self.getEastTopToBottom()
        theirWest = them.getWestTopToBottom()

        return (myEast == theirWest)

    def tryToLineUp(self, them, maxWidth):
        for j in range(4):
            for i in range(4):
                if self.matchMyEastToTheirWest(them, maxWidth):
                    return True
                self.rotateClockwise()
            self.flipHorizontal()
            for i in range(4):
                if self.matchMyEastToTheirWest(them, maxWidth):
                    return True
                self.rotateClockwise()
            self.flipHorizontal()
            them.rotateClockwise()
        them.flipHorizontal()
        for j in range(4):
            for i in range(4):
                if self.matchMyEastToTheirWest(them, maxWidth):
                    return True
                self.rotateClockwise()
            self.flipHorizontal()
            for i in range(4):
                if self.matchMyEastToTheirWest(them, maxWidth):
                    return True
                self.rotateClockwise()
            self.flipHorizontal()
            them.rotateClockwise()
        return False

    def joinMyEastToTheirWest(self, them):
        for i in range(self.height()):
            self.tileImage[i] = self.tileImage[i] + them.tileImage[i]

        for i in range(len(self.subTileIDs)):
            self.subTileIDs[i] = self.subTileIDs[i] + them.subTileIDs[i]

# Part A
def solveA():
    lines = split_lines('day20.input')
    tiles = []
    tileID = -1
    tileLines = []
    
    for i in range(len(lines)):
        if lines[i] == '':
            tiles.append(ImageTile(tileID, tileLines))
            tileID = -1
            tileLines = []
        elif lines[i].startswith('Tile'):
            tileID = (int)(lines[i][5:len(lines[i])-1])
        else:
            tileLines.append(lines[i])
    tiles.append(ImageTile(tileID, tileLines))

    tilesAcross = (int)(math.sqrt(len(tiles)))
    fullWidth = tilesAcross * tiles[0].width()

    while len(tiles) > 1:
        print(len(tiles))
        tileA = tiles[0]
        tiles = tiles[1:]
        match = False
        for i in range(len(tiles)):
            if tileA.tryToLineUp(tiles[i], fullWidth):
                tileA.joinMyEastToTheirWest(tiles[i])
                tiles = tiles[0:i] + tiles[i+1:len(tiles)]
                match = True
                break

        if match:
            tiles = [tileA] + tiles
        else:
            tiles.append(tileA)

    wholePicture = tiles[0]
    subTileIDs = wholePicture.subTileIDs
    answer = subTileIDs[0][0] * subTileIDs[0][tilesAcross-1] * subTileIDs[tilesAcross-1][0] * subTileIDs[tilesAcross-1][tilesAcross-1]
    return answer
