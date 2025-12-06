import pytest
from game import Board

def test_board_min_dimensions():
    with pytest.raises(ValueError):
        Board(4, 4)

def test_start_stop_on_edges():
    b = Board(10, 10)
    w, h = b.width, b.height
    
    for point in [b.start, b.stop]:
        x, y = point
        on_edge = (x == 0 or x == w-1 or y == 0 or y == h-1)
        assert on_edge, f"Punkt {point} nie leży na krawędzi"

def test_start_stop_separation():
    for _ in range(50): 
        b = Board(5, 5)
        dist = abs(b.start[0] - b.stop[0]) + abs(b.start[1] - b.stop[1])
        assert dist > 1, f"Start {b.start} i Stop {b.stop} są zbyt blisko"


def test_move_out_of_bounds():
    b = Board(5, 5)
    b.current_position = (0, 0)
    if (0,0) in b.obstacles: b.obstacles.remove((0,0))

    result = b.move("UP")
    assert "ERROR: Out of bounds" in result
    assert b.current_position == (0, 0) 

    result = b.move("LEFT")
    assert "ERROR: Out of bounds" in result

def test_move_into_obstacle():
    b = Board(5, 5)
    b.current_position = (2, 2)
    b.obstacles.add((3, 2))
    
    result = b.move("RIGHT")
    assert "ERROR: Obstacle hit" in result
    assert b.current_position == (2, 2) 

def test_valid_move():
    b = Board(5, 5)
    b.current_position = (2, 2)
    if (2, 3) in b.obstacles: b.obstacles.remove((2, 3))
    
    result = b.move("DOWN")
    assert result == "MOVED" or result == "STOP REACHED"
    assert b.current_position == (2, 3)

def test_reach_stop():
    b = Board(5, 5)
    stop_x, stop_y = b.stop
    

    b.stop = (4, 4)
    b.current_position = (3, 4)
    if (3, 4) in b.obstacles: b.obstacles.remove((3, 4))
    if (4, 4) in b.obstacles: b.obstacles.remove((4, 4))
    
    result = b.move("RIGHT")
    assert result == "STOP REACHED"