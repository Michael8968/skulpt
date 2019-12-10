"""
Demonstration of a draggable magnifier on a map
"""
import simplegui

# 1521x1818 pixel map of native American language
# Source - Gutenberg project
MAP_WIDTH = 1521
MAP_HEIGHT = 1818
map_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

# Constants
MAP_SCALE = 3
CANVAS_WIDTH = MAP_WIDTH / MAP_SCALE
CANVAS_HEIGHT = MAP_HEIGHT / MAP_SCALE
MAGNIFIER_SIZE = 120


# Event handlers
def click(pos):
    """
    Reset center of magnifier pane to current click position
    """
    magnifier_center[0] = pos[0]
    magnifier_center[1] = pos[1]

def drag(pos):
    """
    Reset center of magnifier pane to current click position
    """
    magnifier_center[0] = pos[0]
    magnifier_center[1] = pos[1]


def draw(canvas):
    """
    Draw handler - draws map, magnifier pane, and box around magnifier
    """
    # Draw map
    canvas.draw_image(map_image, (MAP_WIDTH / 2, MAP_HEIGHT / 2), (MAP_WIDTH, MAP_HEIGHT), 
                     (CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2), (CANVAS_WIDTH, CANVAS_HEIGHT))

    # Draw magnifier    
    source_center = (MAP_SCALE * magnifier_center[0], MAP_SCALE * magnifier_center[1])
    canvas.draw_image(map_image, source_center, [MAGNIFIER_SIZE, MAGNIFIER_SIZE], 
                      magnifier_center, [MAGNIFIER_SIZE, MAGNIFIER_SIZE])

    # Draw outline around magnifier
    mag_left = magnifier_center[0] - MAGNIFIER_SIZE / 2
    mag_right = magnifier_center[0] + MAGNIFIER_SIZE / 2
    mag_top = magnifier_center[1] - MAGNIFIER_SIZE / 2
    mag_bottom = magnifier_center[1] + MAGNIFIER_SIZE / 2
    mag_topleft = (mag_left, mag_top)
    mag_topright = (mag_right, mag_top)
    mag_botleft = (mag_left, mag_bottom)
    mag_botright = (mag_right, mag_bottom)
    box = [mag_topleft, mag_botleft, mag_botright, 
           mag_topright, mag_topleft]
    canvas.draw_polyline(box, 4, "Blue")

    


# event handler for timer
def tick():
    """
    Move center of magnifier pane slowly down/right
    """
    magnifier_center[0] += 1
    magnifier_center[1] += 1

# Create frame for map
frame = simplegui.create_frame("Map magnifier", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.set_mousedrag_handler(drag)

# Create timer that slowly slides the magnifier pane
timer = simplegui.create_timer(60.0,tick)

# Start timer and frame animation
magnifier_center = [CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2]
timer.start()
frame.start()

