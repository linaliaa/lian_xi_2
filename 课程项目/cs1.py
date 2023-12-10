import pytest
from unittest.mock import Mock, patch
from scoreboard import Scoreboard

# Assuming Scoreboard class is part of a game where stats, font, text_color, settings, and screen_rect are initialized elsewhere

@pytest.mark.parametrize("high_score, expected", [
    (12345, "high score:12,340"),  # ID: test_high_score_round_down
    (12355, "high score:12,360"),  # ID: test_high_score_round_up
    (0, "high score:0"),           # ID: test_high_score_zero
    (999999999, "high score:1,000,000,000"),  # ID: test_high_score_large_number
], ids=["round_down", "round_up", "zero", "large_number"])
def test_prep_high_score(high_score, expected):
    # Arrange
    scoreboard = Scoreboard()
    scoreboard.stats = Mock(high_score=high_score)
    scoreboard.font = Mock()
    scoreboard.text_color = (255, 255, 255)
    scoreboard.settings = Mock(bg_color=(0, 0, 0))
    scoreboard.screen_rect = Mock(centerx=100)
    scoreboard.score_rect = Mock(top=10)
    scoreboard.font.render.return_value = Mock(get_rect=Mock(return_value=Mock(centerx=100, top=10)))

    # Act
    scoreboard.prep_high_score()

    # Assert
    scoreboard.font.render.assert_called_once_with(expected, True, (255, 255, 255), (0, 0, 0))
    assert scoreboard.high_score_rect.centerx == scoreboard.screen_rect.centerx
    assert scoreboard.high_score_rect.top == scoreboard.score_rect.top

# Error cases might involve testing the behavior when dependencies like font.render throw exceptions
# However, without more context on how the Scoreboard class handles exceptions, we cannot write meaningful error case tests
