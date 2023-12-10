import os

class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self,ai_game):
        """初始化信息"""
        self.settings = ai_game.settings
        self.rest_stats()
        self.game_active = False

        file = 'x.txt'
        if os.path.exists(file):
            with open('x.txt','r',encoding='utf-8') as f:
                a=f.read()
            self.high_score=int(a)
        else:
            self.high_score=0

    def rest_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        #self.high_score = 0
        