import pytest
from game.ghost_mode_hunt import Hunt_Mode
from game.player import Player


@pytest.mark.parametrize("sanity, expected_output",[(100,False), (5, True)])
def test_hunt_check(sanity, expected_output):
    test_player = Player()
    test_hunt_mode = Hunt_Mode(test_player)
    test_sanity = sanity
    assert test_hunt_mode.hunt_check(test_sanity) == expected_output

pytest.main(["-v", "--tb=line", "-rN", "cse210-project/ghost_hunter/test.py"])