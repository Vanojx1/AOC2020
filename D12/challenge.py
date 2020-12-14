import math

with open('input') as f:
    chal_input = [(lambda x: (x[0], int(x[1:])))(l.rstrip()) for l in f.readlines()]

class Ship:
    DIRS = [-1j, 1, 1j, -1]
    def __init__(self):
        self.dir_index = 1
        self.curr_pos = 0j
        self.waypoint_offset = 10-1j
        self.p1_action_map = {
            'N': lambda o: self.apply_offset(-1j * o),
            'S': lambda o: self.apply_offset(1j * o),
            'E': lambda o: self.apply_offset(o),
            'W': lambda o: self.apply_offset(-1 * o),
            'L': lambda o: self.turn(-1 * (o//90)),
            'R': lambda o: self.turn(o//90),
            'F': lambda o: self.apply_offset(self.curr_dir * o)
        }

        self.p2_action_map = {
            'N': lambda o: self.move_waypoint(-1j * o),
            'S': lambda o: self.move_waypoint(1j * o),
            'E': lambda o: self.move_waypoint(o),
            'W': lambda o: self.move_waypoint(-1 * o),
            'L': lambda o: self.rotate_waypoint(-o),
            'R': lambda o: self.rotate_waypoint(o),
            'F': lambda o: self.move_to_waypoint(o)
        }
    
    @property
    def curr_dir(self):
        return self.DIRS[self.dir_index]

    @property
    def distance(self):
        return int(abs(self.curr_pos.real) + abs(self.curr_pos.imag))
    
    @property
    def waypoint_pos(self):
        return self.curr_pos + self.waypoint_offset

    def apply_offset(self, offset):
        self.curr_pos += offset
    
    def move_waypoint(self, offset):
        self.waypoint_offset += offset
    
    def move_to_waypoint(self, times):
        for _ in range(times):
            self.curr_pos = self.waypoint_pos

    def turn(self, side):
        self.dir_index = (self.dir_index+side) % 4
    
    def rotate_waypoint(self, angle):
        angle = angle*math.pi/180
        s = math.sin(angle)
        c = math.cos(angle)
        wo = self.waypoint_offset
        self.waypoint_offset = complex(round(wo.real * c - wo.imag * s), round(wo.real * s + wo.imag * c))

x = Ship()
for a, o in chal_input:
    x.p1_action_map[a](o)
print('Part 1:', x.distance)

x = Ship()
for a, o in chal_input:
    x.p2_action_map[a](o)
print('Part 2:', x.distance)