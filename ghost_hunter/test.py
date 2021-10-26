"""Test functions"""
from _pytest.monkeypatch import monkeypatch
import pytest
from game.ghost_mode_hunt import Hunt_Mode
from game.player import Player
from game.ghost_mode_action import Action_Mode
from game import constants
from game.ghost import Ghost
from game import ghost


@pytest.mark.parametrize("sanity, expected_output",[(100,False), (25, True)])
def test_hunt_check(sanity, expected_output):
    test_player = Player()
    test_hunt_mode = Hunt_Mode(test_player)
    test_sanity = sanity
    assert test_hunt_mode.hunt_check(test_sanity) == expected_output

pytest.main(["-v", "--tb=line", "-rN", "cse210-project/ghost_hunter/test.py"])


@pytest.mark.parametrize("ghost_type, room_name, target_object, expected_coordinates", [(constants.GHOST_TYPES[1], 
constants.ROOM_LIST[1], "Bed", constants.OBJECT_COORDINATES["Bed"]), (constants.GHOST_TYPES[0], constants.ROOM_LIST[0],
"Sink", constants.OBJECT_COORDINATES["Sink"])])
def test_set_emf(ghost_type, room_name, target_object, expected_coordinates):
    test_action_mode = Action_Mode(ghost_type, room_name)
    test_action_mode.set_emf(target_object)

    assert test_action_mode._emf_position == expected_coordinates

@pytest.mark.parametrize("initial_timer, expected_timer,Initial_hunt_status, expected_hunt_status, initial_hunt_time, expected_hunt_time, Initial_cooldown_time ,expected_cooldown_time", 
[(2, 3, False, False, 0, 0, 5, 6), (5,6, True, False, constants.HUNT_DURATION * 60 + 1, 0, 5, 0),(785,786, False, False, constants.HUNT_DURATION * 60 + 1, constants.HUNT_DURATION * 60 + 1, 5, 6) ])
def test_update_time_and_status(monkeypatch, initial_timer, expected_timer,Initial_hunt_status, expected_hunt_status, initial_hunt_time, expected_hunt_time, Initial_cooldown_time ,expected_cooldown_time):
    test_ghost = Ghost(None, None, None)

    def mock_function():
        return
    monkeypatch.__setattr__("ghost.choose_ghost_action", mock_function)
    test_ghost.timer = initial_timer
    test_ghost.cooldown_time = Initial_cooldown_time
    test_ghost.hunt_time = initial_hunt_time
    test_ghost.hunt_mode_on = Initial_hunt_status
    test_ghost.update_time_and_status(None, None, None, None)

    assert test_ghost.timer == expected_timer
    assert test_ghost.hunt_mode_on == expected_hunt_status
    assert test_ghost.hunt_time == expected_hunt_time
    assert test_ghost.cooldown_time == expected_cooldown_time
    
@pytest.mark.parametrize("sanity, expected_output", [(100, False), (25, True)])
def test_hunt_check(sanity, expected_output):
    test_player = Player()
    test_hunt_mode = Hunt_Mode()
    test_sanity = sanity
    assert test_hunt_mode.hunt_check(test_sanity) == expected_output


def test_check_if_correct_instrument(self):
    test_setup = setup()
    test_setup._player.index_of_instrument = 0
    test_setup._ghost.ghost_type = 0

    assert test_setup.test_check_if_correct_instrument() == True

    test_setup._ghost.ghost_type = 1
    assert test_setup.test_check_if_correct_instrument() == False

    test_setup._player.index_of_instrument = 1
    test_setup._ghost.ghost_type = 2
    assert test_setup.test_check_if_correct_instrument() == False
