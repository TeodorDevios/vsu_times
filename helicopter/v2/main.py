import time, math
from config import LETTER_COUNT, STRING_COUNT, TRACK, HELICOPTER, LAND_POSITION, TIMEOUT

def generate_frame(symbol: str) -> list: # Генирируем кадр
    frame = []
    for _ in range(STRING_COUNT):
        frame.append(symbol * LETTER_COUNT)
    return frame

def paint_land(frame: list, level: int) -> None: # Рисуем землю
    frame[level - 1] = ''.join(['_' * LETTER_COUNT])

def prepare_helicopter(x: int, y: int, mirror: bool) -> list: # Форматируем вертолет смотря от его положения
    copter = HELICOPTER.copy()
    if mirror:
        copter = [line[::-1] for line in copter] # Зеркалим
    height = len(copter)
    width = len(copter[0])
    if y < -1 * height + 1:
        copter = ['']
    elif y < 0:
        for _ in range(-1 * y):
            copter.pop(0)
    elif y > STRING_COUNT - height:
        for _ in range(height - (STRING_COUNT - y)):
            copter.pop(len(copter) - 1)
    height = len(copter)
    if x < -1 * len(copter[0]) + 1:
        copter = ['']
    elif x < 0:
        for i in range(height):
            copter[i] = copter[i][width + x:]
    elif x > LETTER_COUNT - width:
        for i in range(height):
            copter[i] = copter[i][:width + (LETTER_COUNT - width - x)]
    return copter

def paint_helicopter(frame: list, x: int, y: int, gorizontal: bool) -> None: # Рисуем вертолет
    mirror = gorizontal
    copter = prepare_helicopter(x, y, mirror)
    new_y = 0 if y < 0 else y
    new_x = 0 if x < 0 else x 
    for h in range(len(copter)):
        frame[y + h] = frame[y + h][:x] + copter[h] + frame[y + h][x + len(copter[h]):]
        time.sleep(TIMEOUT)

def get_copter_positions(track: list) -> list: # Узнаем позицию вертолета
    points = []
    for stage_number in range(len(track) - 1):
        gorizontal = False
        x_range = track[stage_number + 1]["x"] - track[stage_number]["x"]
        if x_range > 0:
            gorizontal = True
        y_range = track[stage_number + 1]["y"] - track[stage_number]["y"]
        stage_shift = math.sqrt(x_range * x_range + y_range * y_range)
        frame_count = int(abs(x_range)) if abs(x_range) >= abs(y_range) else int(abs(y_range))
        delta_shift = stage_shift / frame_count
        x_shift = delta_shift * x_range / stage_shift
        y_shift = delta_shift * y_range / stage_shift
        x = track[stage_number]["x"]
        y = track[stage_number]["y"]
        for _ in range(frame_count):
            x += x_shift
            y += y_shift
            points.append({ "x": int(x), "y": int(y), "gorizontal": gorizontal }) 
    return points

def paint_frame(frame: list) -> None: # Рисуем кадр
    for f in frame:
        print(f)

def print_frames(track: list, land: int) -> None: # Рисуем кадры
    positions = get_copter_positions(track)
    for point in positions:
        frame = generate_frame(' ')
        paint_land(frame, land)
        x = point["x"]
        y = point["y"]
        paint_helicopter(frame, x, y, point["gorizontal"])
        paint_frame(frame)

if __name__ == '__main__':
    print_frames(TRACK, LAND_POSITION)