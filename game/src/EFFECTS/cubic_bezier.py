from .settings import *

class CubicBezier(object):
    """docstring for CubicBEzier."""

    def __init__(self, points):
        points = list(points)
        print(len(points))
        pts = []
        if len(points) not in [2, 4]:
            raise Exception('Invalid Argument Count Error')
        if len(points) == 2:
            pts = [[0, 0]]
            pts.append(points[0])
            pts.append(points[1])
            pts.append([1, 2])
            # points = [0, 0] + points + [1, 1]
        print(pts)
        self.points = pts

    def calculate(self, t):
        x = (1 - t) ** 3 * self.points[0][0] + 3 * t * (1 - t) ** 2 * self.points[1][0] + 3 * t ** 2 * (1 - t) * self.points[2][0] + t ** 3 * self.points[3][0]
        y = (1 - t) ** 3 * self.points[0][1] + 3 * t * (1 - t) ** 2 * self.points[1][1] + 3 * t ** 2 * (1 - t) * self.points[2][1] + t ** 3 * self.points[3][1]

        return [x, y]

    def calculate_x(self, t):
        return self.calculate(t)[0]

class LineChainVFX():
    def __init__(self, point_config, location, bezier, rate, colour, width=1, time_cap=True):
        total_line_length = sum([math.sqrt((p[0] - point_config[i - 1][0]) ** 2 + (p[1] - point_config[i - 1][1]) ** 2) for i, p in enumerate(point_config) if i != 0])
        point_config_with_times = []
        cumulative_length = 0
        for i, point in enumerate(point_config):
            if i != 0:
                cumulative_length += math.sqrt((point[0] - point_config[i - 1][0]) ** 2 + (point[1] - point_config[i - 1][1]))
                point_config_with_times.append(point + [cumulative_length])
        self.point_config = point_config_with_times
        self.bezier = bezier
        self.time = 0
        self.colour = colour
        self.rate = rate
        self.base_offset = location
        self.width = width
        self.time_cap = time_cap

    def update(self, dt):
        if self.time_cap:
            self.time = min(self.rate * dt, 1)
        else:
            self.time += self.rate * dt

    def draw(self, surf, offset=[0, 0]):
        length = self.bezier.calculate_x(self.time)

        for i, point in enumerate(self.point_config):
            if i != 0:
                first_point = [self.point_config[i - 1][0] + self.base_offset[0] + offset[0], self.point_config[i - 1][1] + self.base_offset[1] + offset[1]]

                if point[2] < length:
                    pygame.draw.line(surf, self.colour, first_point, [point[0] + self.base_offset[0] + base_offset[0], point[1] + self.base_offset[1] + offset[1]], self.width)

                else:
                    diff_x = point[0] - self.point_config[i - 1][0]
                    diff_y = point[0] - self.point_config[i - 1][1]
                    line_angle = math.atan2(diff_y, diff_x)
                    print(self.point_config[i-1], point[2])
                    relative_time = (self.time - self.point_config[i - 1]) / (point[2] - self.point_config[i - 1])
                    line_length = math.sqrt(diff_x ** 2 + diff_y **2) * relative_time
                    line_end = [self.point_config[i - 1][0] + math.cos(line_angle) * line_length, self.point_config[i - 1][1] + math.sin(line_angle) * line_length]
                    pygame.draw.line(surf, self.colour, first_point, [line_end[0] + self.base_offset[0] + self.base_offset[0], line_end[1] + self.base_offset[1] + offset[1]], self.width)

def generate_line_chain_vfx(location):
    b_type = CubicBezier([[0.41, 2.5], [1.66, -0.06]])
    pts = [[0, 0], [1, 1], [1.5, 1.1]]

    return LineChainVFX(pts, location, b_type, 0.02, WHITE, 3)
