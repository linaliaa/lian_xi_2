import pytest
from alien_invasion import AlienInvasion
from unittest.mock import patch, MagicMock

# Test IDs for parametrization
HAPPY_PATH_ID = "happy_path"
EDGE_CASE_ID = "edge_case"
ERROR_CASE_ID = "error_case"

@pytest.mark.parametrize("test_id, file_name, call_count", [
    (HAPPY_PATH_ID, 'z_biubiu.mp3', 1),
    (EDGE_CASE_ID, '', 0),  # Assuming an empty string is an edge case
    (ERROR_CASE_ID, 'non_existent_file.mp3', 0),
])
def test_play_sound(test_id, file_name, call_count):
    # Arrange
    alien_invasion_instance = AlienInvasion()
    with patch('pygame.mixer.init'), \
        patch('pygame.mixer.music.load') as mock_load, \
        patch('pygame.mixer.music.play') as mock_play:
        
        # Act
        if test_id == ERROR_CASE_ID:
            with pytest.raises(pygame.error):
                alien_invasion_instance.play_sound()
        else:
            alien_invasion_instance.play_sound()
        
        # Assert
        if test_id != ERROR_CASE_ID:
            mock_load.assert_called_with(file_name)
            assert mock_play.call_count == call_count
        # For the error case, the assertion is handled by the pytest.raises context manager
        