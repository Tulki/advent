from shared import *

class Ship:
    facing = 90 # degrees; north-facing is 0, 90 is east
    vert = 0 # north distance from origin is positive, south negative
    hori = 0 # east distance from origin is positive, west negative

    wp_vert = 1
    wp_hori = 10

    def __init__(self):
        self.facing = 90
        self.vert = 0
        self.hori = 0
        self.wp_vert = 1
        self.wp_hori = 10

    def left(self, degrees):
        self.facing -= degrees
        if self.facing < 0:
            self.facing += 360

    def right(self, degrees):
        self.facing += degrees
        if self.facing >= 360:
            self.facing -= 360

    def forward(self, units):
        if self.facing == 0:
            self.north(units)
        elif self.facing == 90:
            self.east(units)
        elif self.facing == 180:
            self.south(units)
        elif self.facing == 270:
            self.west(units)
        else:
            raise('facing not an increment of 90 degrees!')

    def north(self, units):
        self.vert += units

    def south(self, units):
        self.vert -= units

    def east(self, units):
        self.hori += units

    def west(self, units):
        self.hori -= units

    def dispatchA(self, instruction):
        command = instruction[0]
        quantity = (int)(instruction[1:])

        if command == 'N':
            self.north(quantity)
        elif command == 'E':
            self.east(quantity)
        elif command == 'S':
            self.south(quantity)
        elif command == 'W':
            self.west(quantity)
        elif command == 'L':
            self.left(quantity)
        elif command == 'R':
            self.right(quantity)
        elif command == 'F':
            self.forward(quantity)
        else:
            raise('unknown command!')

    def manhattanDistance(self):
        return abs(self.vert) + abs(self.hori)

    def wp_left(self, degrees):
        for i in range((int)(degrees / 90)):
            self.wp_vert, self.wp_hori = self.wp_hori, (-1*self.wp_vert)

    def wp_right(self, degrees):
        for i in range((int)(degrees / 90)):
            self.wp_vert, self.wp_hori = (-1*self.wp_hori), self.wp_vert

    def wp_north(self, units):
        self.wp_vert += units

    def wp_south(self, units):
        self.wp_vert -= units

    def wp_east(self, units):
        self.wp_hori += units

    def wp_west(self, units):
        self.wp_hori -= units

    def wp_goto(self, times):
        self.vert += (times * self.wp_vert)
        self.hori += (times * self.wp_hori)

    def dispatchB(self, instruction):
        command = instruction[0]
        quantity = (int)(instruction[1:])

        if command == 'N':
            self.wp_north(quantity)
        elif command == 'E':
            self.wp_east(quantity)
        elif command == 'S':
            self.wp_south(quantity)
        elif command == 'W':
            self.wp_west(quantity)
        elif command == 'L':
            self.wp_left(quantity)
        elif command == 'R':
            self.wp_right(quantity)
        elif command == 'F':
            self.wp_goto(quantity)
        else:
            raise('unknown command!')
    
# Part A
def solveA():
    instructions = split_lines('day12.input')
    ship = Ship()
    
    for instr in instructions:
        ship.dispatchA(instr)

    return ship.manhattanDistance()

# Part B
def solveB():
    instructions = split_lines('day12.input')
    ship = Ship()
    
    for instr in instructions:
        ship.dispatchB(instr)

    return ship.manhattanDistance()
