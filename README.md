# ChessLegalMoves

ChessLegalMoves is a small tool that shows all possible moves a chess piece can make.

## Installation

Use the git clone command to install PasswordGenerator.

```bash
git clone https://github.com/erencan-02/ChessLegalMoves.git
```

## Usage

```python
import LegalMoves

#New knight object
knight = Knight("d4") 

#You don't have to call the function itself; the moves are stored in legalMoves
moves = knight.legalMoves

#decoded: readable positions "e4"
#encoded: Numeric positions (4,4)
decoded = knight.get_decoded_moves(moves)

#Change the position of the piece
knight.set_position("g4")
```

## Note
If you implement a chess board you can determine if a square is occupied or not.

## License
[MIT](https://choosealicense.com/licenses/mit/)

