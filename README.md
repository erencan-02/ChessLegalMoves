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
knight = LegalMoves.Knight("d4") 

#You don't have to call the function itself; the moves are stored in legalMoves
moves = knight.legalMoves

#decoded: Numeric positions (4,4)
#encoded: Readable positions "e4"
decoded = knight.get_decoded_moves(moves)

#Change the position of the piece
knight.set_position("g4")
```

## Note
It could be that I mixed up the terms encoded and decoded.

## License
[MIT](https://choosealicense.com/licenses/mit/)

