
class GamePiece:
    def __init__(self, polarity: int, symbol: str, color: str, name: str):
        self.polarity=polarity
        self.symbol=symbol
        self.color=color
        self.name=name


class GamePieceCreator:
    def __init__(self, board: list):
        self._board = board

    def create_space_piece(polarity: int, symbol: str, color: str) -> GamePiece:
        return GamePiece(polarity=polarity, symbol=symbol, color=color, name="space")

    def create_infantry_piece(polarity: int, symbol: str, color: str) -> GamePiece:
        return GamePiece(polarity=polarity, symbol=symbol, color=color, name="infantry")
    


def blank_space():
    return GamePiece(0, " ", "blank", "space")
def white_infantry():
    return GamePiece(1, "♙", "white", "infantry")
def black_infantry():
    return GamePiece(-1, "♟︎", "black", "infantry")

GameState.board=[[blank_space() for i in range(9)] for j in range 9]