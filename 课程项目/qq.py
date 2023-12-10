import pytest
import pygame
from alien_invasion import Game

# Mocking necessary pygame functionalities and objects
class MockShip:
    def __init__(self):
        pass

class MockAlien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

@pytest.fixture
def game():
    game = Game()
    game.ship = MockShip()
    game.aliens = pygame.sprite.Group()
    return game

@pytest.mark.parametrize("aliens_pos, ship_pos, is_ship_hit, aliens_reach_bottom", [
    pytest.param([(50, 50)], (50, 50), True, False, id="ship-alien-collision"),
    pytest.param([(10, 10)], (100, 100), False, False, id="no-collision"),
    pytest.param([(10, 600)], (100, 100), False, True, id="alien-reach-bottom"),
    # Add more test cases for different scenarios
])
def test_update_aliens(game, aliens_pos, ship_pos, is_ship_hit, aliens_reach_bottom, mocker):
    # Arrange
    for pos in aliens_pos:
        alien = MockAlien()
        alien.rect = pygame.Rect(pos[0], pos[1], 10, 10)
        game.aliens.add(alien)
    game.ship.rect = pygame.Rect(ship_pos[0], ship_pos[1], 10, 10)
    mocker.patch.object(game, '_check_fleet_edges')
    mocker.patch.object(game, '_ship_hit')
    mocker.patch.object(game, '_check_aliens_bottom')

    # Act
    game._update_aliens()

    # Assert
    if is_ship_hit:
        game._ship_hit.assert_called_once()
    else:
        game._ship_hit.assert_not_called()
    if aliens_reach_bottom:
        game._check_aliens_bottom.assert_called_once()
    else:
        game._check_aliens_bottom.assert_not_called()
