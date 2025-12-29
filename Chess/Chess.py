from ChessPieces import ChessPiece as cp
import time

turn = 0 # determiner for white or black

def genChessboard(pieces:bool = False): # generate starting chessboard w or w/o pieces
    chessboard = list()
    for i in range(8):
        if pieces:
            match i:
                case 0:
                    chessboard.append([cp("bR1","♜",[0,0]), cp("bN1","♞",[0,1]), cp("bB1","♝",[0,2]), cp("bQ1","♛",[0,3]), cp("bK","♚",[0,4]), cp("bB2","♝",[0,5]), cp("bN2","♞",[0,6]), cp("bR2","♜",[0,7])])
                    continue
                case 1:
                    chessboard.append([cp("bP1","♟",[1,0]), cp("bP2","♟",[1,1]), cp("bP3","♟",[1,2]), cp("bP4","♟",[1,3]), cp("bP5","♟",[1,4]), cp("bP6","♟",[1,5]), cp("bP7","♟",[1,6]), cp("bP8","♟",[1,7])])
                    continue
                case 6:
                    chessboard.append([cp("wP1","♙",[6,0]), cp("wP2","♙",[6,1]), cp("wP3","♙",[6,2]), cp("wP4","♙",[6,3]), cp("wP5","♙",[6,4]), cp("wP6","♙",[6,5]), cp("wP7","♙",[6,6]), cp("wP8","♙",[6,7])])
                    continue
                case 7:
                    chessboard.append([cp("wR1","♖",[7,0]), cp("wN1","♘",[7,1]), cp("wB1","♗",[7,2]), cp("wQ1","♕",[7,3]), cp("wK","♔",[7,4]), cp("wB2","♗",[7,5]), cp("wN2","♘",[7,6]), cp("wR2","♖",[7,7])])
                    continue

        if i % 2 == 0:
            chessboard.append([cp(None,"◼",None), cp(None,"◻",None), cp(None,"◼",None), cp(None,"◻",None), cp(None,"◼",None), cp(None,"◻",None), cp(None,"◼",None), cp(None,"◻",None)])
        else:
            chessboard.append([cp(None,"◻",None), cp(None,"◼",None), cp(None,"◻",None), cp(None,"◼",None), cp(None,"◻",None), cp(None,"◼",None), cp(None,"◻",None), cp(None,"◼",None)])
    return chessboard

def updChessboard(chessboard):   # update chessboard display
    num = 8
    print("A B C D E F G H")
    for i in range(len(chessboard)):
        for piece in range(len(chessboard[i])):
            print(chessboard[i][piece].symbol, end=" ")
            chessboard[i][piece].piecePos = [i, piece]
        print(num)
        num -= 1
    print()

def gridToCol(coord):   # turns chess grid notation to list cols-rows
    coord = ord(coord)
    if coord > 48 and coord <= 56: # column (numbers)
        return (56 - coord)
    elif coord >= 97 and coord < 105:   # row (letters)
        return (coord - 97)
    else:
        return "ERROR 019gtc: OUT OF BOUNDS"

def isWhite() -> bool:  # Check if white turn
    if turn % 2 == 0:
        return True
    return False

def isFree(cell) -> bool:   # Check if cell is empty/free
    if cell == '◼' or cell == '◻':
        return True
    return False

def pieceMoved(piece) -> bool:    # Check if chess piece moved
    if piece.pieceID[-1] == 'm':
        return piece
    piece.pieceID += "m"
    return piece

def pcToLtr(piece):   # converts chess piece symbol to chess notation
    match piece:
        case '♟'|'♙': return ''
        case '♜'|'♖': return 'R'
        case '♞'|'♘': return 'N'
        case '♝'|'♗': return 'B'
        case '♛'|'♕': return 'Q'
        case '♚'|'♔': return 'K'
        case _: 
            print("ERROR 008: INVALID CHESS PIECE")
            return None

def ltrToPc(letter):  # converts chess notation to chess piece symbol
    if isWhite():
        match letter:
            case '': return '♙'
            case 'R': return '♖'
            case 'N': return '♘'
            case 'B': return '♗'
            case 'Q': return '♕'
            case 'K': return '♔'
            case _:
                print('ERROR 007: INVALID CHESS NOTATION')
                return None
    else:
        match letter:
            case '': return '♟'
            case 'R': return '♜'
            case 'N': return '♞'
            case 'B': return '♝'
            case 'Q': return '♛'
            case 'K': return '♚'
            case _:
                print('ERROR 007: INVALID CHESS NOTATION')
                return None

def pgnConverter(chess_game):   # converts PGN chess game to 2D matrix
    output = []
    for i in chess_game.split():
        if "+" in i:
            i = i[:len(i)-1]
        if "." in i:
            output.append(i[i.index(".")+1:])
            continue
        output.append(i)
    return output

def checkPathing(frX:int, frY:int, toX:int, toY:int, chessboard:list) -> bool:  # Validate pathing of chess piece
    if frY == toY:  # horizontal movement
        if toX - frX > 0:
            for i in range(frX + 1, toX + 1):   # left to right
                if not isFree(chessboard[frY][i].symbol):
                    print("ERROR 003: PIECE IS BLOCKING WAY")
                    return False
        else:
            for i in range(frX - 1, toX - 1, -1):   # right to left
                if not isFree(chessboard[frY][i].symbol):
                    print("ERROR 004: PIECE IS BLOCKING WAY")
                    return False
    elif frX == toX:   # vertical
        if toY - frY > 0:
            for i in range(frY + 1, toY + 1):   # up to down
                if not isFree(chessboard[i][frX].symbol):
                    print(chessboard[i][frX].symbol)
                    print("ERROR 005: PIECE IS BLOCKING WAY HELLO")
                    return False
        else:
            for i in range(frY - 1, toY - 1, -1):   # down to up
                if not isFree(chessboard[i][frX].symbol):
                    print("ERROR 006: PIECE IS BLOCKING WAY")
                    return False
    else:   # slanted
        if toY - frY > 0: 
            if toX - frX > 0:   # TL to BR
                x = frX + 1
                for y in range(frY + 1, toY + 1):
                    if not isFree(chessboard[y][x].symbol):
                        print("ERROR 010: PIECE IS BLOCKING WAY")
                        return False
                    x += 1
            else:   # TR to BL
                x = frX - 1
                for y in range(frY + 1, toY + 1):
                    if not isFree(chessboard[y][x].symbol):
                        print("ERROR 011: PIECE IS BLOCKING WAY")
                        return False
                    x -= 1
        else:
            if toX - frX > 0:   # BL to TR
                x = frX + 1
                for y in range(frY - 1, toY - 1, -1):
                    if not isFree(chessboard[y][x].symbol):
                        print("ERROR 012: PIECE IS BLOCKING WAY")
                        return False
                    x += 1
            else:   # BR to TL
                x = frX - 1
                for y in range(frY - 1, toY - 1, -1):
                    if not isFree(chessboard[y][x].symbol):
                        print("ERROR 013: PIECE IS BLOCKING WAY")
                        return False
                    x -= 1
    return True

def checkPathingCap(frX:int, frY:int, toX:int, toY:int, chessboard:list) -> bool:  # Validate pathing of chess piece for capturing
    if frY == toY:  # horizontal movement
        if toX - frX > 0:
            for i in range(frX + 1, toX):   # left to right
                if not isFree(chessboard[frY][i].symbol):
                    print("ERROR 003: PIECE IS BLOCKING WAY")
                    return False
        else:
            for i in range(frX - 1, toX, -1):   # right to left
                if not isFree(chessboard[frY][i].symbol):
                    print("ERROR 004: PIECE IS BLOCKING WAY")
                    return False
    elif frX == toX:   # vertical
        if toY - frY > 0:
            for i in range(frY + 1, toY):   # up to down
                if not isFree(chessboard[i][frX].symbol):
                    print("ERROR 005: PIECE IS BLOCKING WAY hi")
                    return False
        else:
            for i in range(frY - 1, toY, -1):   # down to up
                if not isFree(chessboard[i][frX].symbol):
                    print("ERROR 006: PIECE IS BLOCKING WAY")
                    return False
    else:   # slanted
        if toY - frY > 0: 
            if toX - frX > 0:   # TL to BR
                x = frX + 1
                for y in range(frY + 1, toY):
                    if not isFree(chessboard[y][x].symbol):
                        print("ERROR 010: PIECE IS BLOCKING WAY")
                        return False
                    x += 1
            else:   # TR to BL
                x = frX - 1
                for y in range(frY + 1, toY):
                    if not isFree(chessboard[y][x].symbol):
                        print("ERROR 011: PIECE IS BLOCKING WAY")
                        return False
                    x -= 1
        else:
            if toX - frX > 0:   # BL to TR
                x = frX + 1
                for y in range(frY - 1, toY, -1):
                    if not isFree(chessboard[y][x].symbol):
                        print("ERROR 012: PIECE IS BLOCKING WAY")
                        return False
                    x += 1
            else:   # BR to TL
                x = frX - 1
                for y in range(frY - 1, toY, -1):
                    if not isFree(chessboard[y][x].symbol):
                        print("ERROR 013: PIECE IS BLOCKING WAY")
                        return False
                    x -= 1
    return True

def locatePiece(toX:int, toY:int, piece:str, chessboard:list):  # locates chess pieces on the board
    pieceSymbol = ltrToPc(piece)
    frX, frY = "", ""
    
    if piece == "": # locate pawn
        if isWhite():   # White
            if toY + 2 == 6:    # starting pawn place
                for y in range(toY+1, toY+3):   # check pawn between pawn starting place to 2 cells
                    if chessboard[y][toX].symbol == pieceSymbol:
                        frX, frY = chessboard[y][toX].piecePos[1], chessboard[y][toX].piecePos[0]
            else:
                y = toY + 1
                if chessboard[y][toX].symbol == pieceSymbol:
                    frX, frY = chessboard[y][toX].piecePos[1], chessboard[y][toX].piecePos[0]
                #for y in range(7, -1, -1):
                #    if chessboard[y][toX].symbol == pieceSymbol:
                #        frX, frY = chessboard[y][toX].piecePos[1], chessboard[y][toX].piecePos[0]   #toX, y
                #        return frX, frY
        else:   # Black
            if toY - 2 == 1:
                for y in range(toY-1, toY-3, -1):   # check pawn between pawn starting place to 2 cells
                    if chessboard[y][toX].symbol == pieceSymbol:
                        frX, frY = chessboard[y][toX].piecePos[1], chessboard[y][toX].piecePos[0]
            else:
                y = toY - 1
                if chessboard[y][toX].symbol == pieceSymbol:
                    frX, frY = chessboard[y][toX].piecePos[1], chessboard[y][toX].piecePos[0]
        return frX, frY
    elif piece == "Q" or piece == "K":  # locate queen or king
        for y in range(len(chessboard)):
            for x in range(len(chessboard[y])):
                if pieceSymbol == chessboard[y][x].symbol:
                    frX, frY = chessboard[y][x].piecePos[1], chessboard[y][x].piecePos[0]   #chessboard[y].index(pieceSymbol), y
                    return frX, frY
    elif piece == "B":  # locate bishop
        # TL to BR
        x = toX + 1
        for y in range(toY + 1, 8):
            if x >= 8:
                break
            if pieceSymbol == chessboard[y][x].symbol:
                frX, frY = chessboard[y][x].piecePos[1], chessboard[y][x].piecePos[0]
                return frX, frY
            x += 1
        # TR to BL
        x = toX - 1
        for y in range(toY + 1, 8):
            if x <= -1:
                break
            if pieceSymbol == chessboard[y][x].symbol:
                frX, frY = chessboard[y][x].piecePos[1], chessboard[y][x].piecePos[0]
                return frX, frY
            x -= 1
        # BL to TR
        x = toX + 1
        for y in range(toY - 1, -1, -1):
            if x >= 8:
                break
            if pieceSymbol == chessboard[y][x].symbol:
                frX, frY = chessboard[y][x].piecePos[1], chessboard[y][x].piecePos[0]
                return frX, frY
            x += 1
        # BR to TL
        x = toX - 1
        for y in range(toY - 1, -1, -1):
            if x <= -1:
                break
            if pieceSymbol == chessboard[y][x].symbol:
                frX, frY = chessboard[y][x].piecePos[1], chessboard[y][x].piecePos[0]
                return frX, frY
            x -= 1
    elif piece == "N":
        y, x = -2, -1   # determiner for y and x
        a = "00"        # switches for inverse multiplication
        for i in range(8):
            if a[0] == "1":
                y *= -1
            if a[1] == "1":
                x *= -1
            try:
                if pieceSymbol == chessboard[toY + y][toX + x].symbol:
                    frX, frY = chessboard[toY + y][toX + x].piecePos[1], chessboard[toY + y][toX + x].piecePos[0]
                    return frX, frY
            except: # catch error
                print("ERROR 019: LOCATE CELL FOR KNIGHT OUT OF BOUNDS")
            a = str(bin(int(a,2) + int("01",2)))    # change switch
            a = a[2:]
            if a == "1" or i == 2 or i == 6:        # follow structure of correct switches
                a = "01"
            if i == 3:
                a = "00"                            # follow structure of correct switches and switch y and x values
                y, x = 1, 2
        
        frX, frY = "", ""
    else:   # locate other pieces
        for y in range(8):  # locate by column (R, Q, K)
            if chessboard[y][toX].symbol == pieceSymbol:
                frX, frY = chessboard[y][toX].piecePos[1], chessboard[y][toX].piecePos[0]   #toX, y
                return frX, frY
        for x in range(8):  # locate by row (R, Q, K)
            if chessboard[toY][x].symbol == pieceSymbol:
                frX, frY = chessboard[toY][x].piecePos[1], chessboard[toY][x].piecePos[0]   #x, toY
                return frX, frY
    print("ERROR 020: CANNOT LOCATE PIECE")

def capturePiece(move:str, chessboard): # Capture pieces
    blankChessboard = genChessboard()
    frX, frY, frX_move, frY_move = "","","",""
    
    toX, toY = gridToCol(move[2]), gridToCol(move[3])   # common for normal capture
    
    if move[0].islower():   # Pawn
        piece = ltrToPc("")
        file = gridToCol(move[0])
        if isWhite():   # White
            if chessboard[toY + 1][file].symbol == piece:
                try:
                    frX, frY = chessboard[toY + 1][file].piecePos[1], chessboard[toY + 1][file].piecePos[0]
                except:
                    print("ERROR 019w: OUT OF BOUNDS")
                    return chessboard
            else:
                print("ERROR 016: PAWN DOES NOT EXIST OR MOVE NOT SLANTED")
                return chessboard
        else:   # Black
            if chessboard[toY - 1][file].symbol == piece:
                try:
                    frX, frY = chessboard[toY - 1][file].piecePos[1], chessboard[toY - 1][file].piecePos[0]
                except:
                    print("ERROR 019b: OUT OF BOUNDS")
                    return chessboard
            else:
                print("ERROR 016: PAWN DOES NOT EXIST OR MOVE NOT SLANTED")
                return chessboard
    else:   # Rank
        if len(move) > 4:   # Ambiguous capture
            frX_move, frY_move = gridToCol(move[1]), gridToCol(move[2])
            toX, toY = gridToCol(move[4]), gridToCol(move[5])
            if chessboard[frY_move][frX_move].symbol != ltrToPc(move[0]):   # Check if cell piece == piece mentioned
                print("ERROR 024: MISMATCH RANK PIECE")
                return chessboard
        # Normal capture
        piece = move[0]
        match piece:
            case 'R':   # Rook
                if frX_move == "":  # check if not ambiguous
                    try:
                        frX, frY = locatePiece(toX, toY, piece, chessboard)
                    except:
                        return chessboard
                else:
                    frX, frY = frX_move, frY_move
                # check rook pathing
                if not checkPathingCap(frX, frY, toX, toY, chessboard):
                    return chessboard
            case 'K':   # King
                if frX_move == "":  # check if not ambiguous
                    try:
                        frX, frY = locatePiece(toX, toY, piece, chessboard)
                    except:
                        return chessboard
                else:
                    frX, frY = frX_move, frY_move
                # check if valid move
                adjCell = f"{abs(frY - toY)}{abs(frX - toX)}"
                if adjCell not in ['11','10','01']:
                    print("ERROR 009c: KING MOVE INVALID")
                    return chessboard
            case 'N':   # Knight
                if frX_move == "":  # check if not ambiguous
                    try:
                        frX, frY = locatePiece(toX, toY, piece, chessboard)
                    except:
                        print("ERROR: 014: KNIGHT MOVE INVALID")
                        return chessboard
                else:
                    frX, frY = frX_move, frY_move
            case 'B':   # Bishop
                if frX_move == "":  # check if not ambiguous
                    try:
                        frX, frY = locatePiece(toX, toY, piece, chessboard)
                    except:
                        return chessboard
                else:
                    frX, frY = frX_move, frY_move
                # check bishop pathing
                if not checkPathingCap(frX, frY, toX, toY, chessboard):
                    return chessboard
            case 'Q':   # Queen
                if frX_move == "":  # check if not ambiguous
                    try:
                        frX, frY = locatePiece(toX, toY, piece, chessboard)
                    except:
                        return chessboard
                else:
                    frX, frY = frX_move, frY_move
                # check queen pathing
                if not checkPathingCap(frX, frY, toX, toY, chessboard):
                    return chessboard
            case _:
                print("ERROR 021: INVALID CHESS PIECE")
                return chessboard
            

    if isFree(chessboard[toY][toX].symbol): # checks if 'to' cell is empty
        print("ERROR 017: CAPTURING CELL IS FREE")
        return chessboard
    
    othKingUni = ord(ltrToPc("K"))  # turn king symbol to unicode
    if isWhite():   # turns white king to black king
        othKingUni += 6
    else:   # vice versa
        othKingUni -= 6
    if ord(chessboard[toY][toX].symbol) == othKingUni: # checks if 'to' cell is not the opponent's king
        print("ERROR 018: CAPTURED PIECE IS A KING")
        return chessboard

    # Execute code block if chess piece is valid
    # 0 - column; 1 - row
    print(f"{chessboard[toY][toX].symbol}🔫{chessboard[frY][frX].symbol}")
    chessboard[toY][toX] = chessboard[frY][frX]
    chessboard[frY][frX] = blankChessboard[frY][frX]

    # updates chessboard's display and turn
    updChessboard(chessboard)
    global turn
    turn += 1
    return chessboard

def movePiece(fr, to, chessboard):  # col row movemen
    blankChessboard = genChessboard()

    # convert chess grid to column rows
    frX, frY = gridToCol(fr[0]), gridToCol(fr[1])
    toX, toY = gridToCol(to[0]), gridToCol(to[1])

    # 0 - column; 1 - row
    chessboard[toY][toX] = chessboard[frY][frX]
    chessboard[frY][frX] = blankChessboard[frY][frX]

    # updates chessboard's display
    updChessboard(chessboard)
    return chessboard

def movePiece(move:str, chessboard):  # user input chess notation
    blankChessboard = genChessboard()
    frX, frY, frX_move, frY_move, toX, toY= "","","","","",""

    if move[0].islower():   # Pawn movement
        toX, toY = gridToCol(move[0]), gridToCol(move[1])
        try:
            frX, frY = locatePiece(toX, toY, "", chessboard)
        except:
            print("ERROR 019m: OUT OF BOUNDS")
            return chessboard
        # check pawn pathing
        if isWhite():
            if frY == 6:    # check if starting, white
                if frY - toY > 2:
                    print("ERROR 002: PAWN MOVE INVALID")
                    return chessboard
            else:
                if frY - toY > 1:
                    print("ERROR 001: PAWN MOVE INVALID")
                    return chessboard
        else:
            if frY == 1:    # check if starting, black
                if toY - frY > 2:
                    print("ERROR 002: PAWN MOVE INVALID")
                    return chessboard
            else:
                if toY - frY > 1:
                    print("ERROR 001: PAWN MOVE INVALID")
                    return chessboard
        if not checkPathing(frX, frY, toX, toY, chessboard):
            return chessboard
    else:   # Rank movement    
        toX, toY = gridToCol(move[1]), gridToCol(move[2]) # destination move
        if len(move) > 4:   # Ambiguous move
            frX_move, frY_move, toX, toY = gridToCol(move[1]), gridToCol(move[2]), gridToCol(move[3]), gridToCol(move[4])
            if chessboard[frY_move][frX_move].symbol != ltrToPc(move[0]):   # check cell piece == piece mentioned
                print("ERROR 025: MISMATCH RANK PIECE")
                return chessboard

        piece = move[0]
        match piece:
            case 'R':
                if frX_move == "":  # check if not ambiguous
                    try:
                        frX, frY = locatePiece(toX, toY, piece, chessboard)
                    except:
                        return chessboard
                else:
                    frX, frY = frX_move, frY_move
                # check rook pathing
                if not checkPathing(frX, frY, toX, toY, chessboard):
                    return chessboard
            case 'K':
                if frX_move == "":  # check if not ambiguous
                    try:
                        frX, frY = locatePiece(toX, toY, piece, chessboard)
                    except:
                        return chessboard
                else:
                    frX, frY = frX_move, frY_move
                # check king pathing
                adjCell = f"{abs(frY - toY)}{abs(frX - toX)}"
                if adjCell not in ['11','10','01']:     # checks if move is in adjacent cells
                    print("ERROR 009m: KING MOVE INVALID")
                    return chessboard
                if not checkPathing(frX, frY, toX, toY, chessboard):    
                    return chessboard
            case 'N':
                if frX_move == "":  # check if not ambiguous
                    try:
                        frX, frY = locatePiece(toX, toY, piece, chessboard)
                    except:
                        print("ERROR 014: KNIGHT MOVE INVALID")
                        return chessboard
                else:
                    frX, frY = frX_move, frY_move
                if not isFree(chessboard[toY][toX].symbol):
                    print("ERROR 022: CELL OCCUPIED")
                    return chessboard
            case 'B':
                if frX_move == "":  # check if not ambiguous
                    try:
                        frX, frY = locatePiece(toX, toY, piece, chessboard)
                    except:
                        return chessboard
                else:
                    frX, frY = frX_move, frY_move
                # check bishop pathing
                if not checkPathing(frX, frY, toX, toY, chessboard):
                    return chessboard
            case 'Q':
                if frX_move == "":  # check if not ambiguous
                    try:
                        frX, frY = locatePiece(toX, toY, piece, chessboard)
                    except:
                        return chessboard
                else:
                    frX, frY = frX_move, frY_move
                # check queen pathing
                if not checkPathing(frX, frY, toX, toY, chessboard):
                    return chessboard
            case _:
                print("ERROR 021: INVALID CHESS PIECE")
                return chessboard

    
    # Execute code block if chess piece is valid
    # updates pieceID to moved
    if not chessboard[frY][frX].pieceID[-1] == 'm':
        chessboard[frY][frX] = pieceMoved(chessboard[frY][frX])

    # 0 - column; 1 - row
    chessboard[toY][toX] = chessboard[frY][frX]
    chessboard[frY][frX] = blankChessboard[frY][frX]

    # updates chessboard's display and turn
    updChessboard(chessboard)
    global turn
    turn += 1
    return chessboard

def castling(move:str, chessboard): # Castling 
    blankChessboard = genChessboard()
    global turn

    if isWhite():
        if move == "O-O" and isFree(chessboard[7][5].symbol) and isFree(chessboard[7][6].symbol):   # Kingside white
            if chessboard[7][4].pieceID == "wK" and chessboard[7][7].pieceID == "wR2":  # check if white king and kingside rook hasn't moved
                king = chessboard[7][4]
                king.piecePos = [7,6]
                rook = chessboard[7][7]
                rook.piecePos = [7,5]
                chessboard[7][5], chessboard[7][7] = rook, blankChessboard[7][7]
                chessboard[7][6], chessboard[7][4] = king, blankChessboard[7][4]
                updChessboard(chessboard)
                turn += 1
                return chessboard
        elif move == "O-O-O" and isFree(chessboard[7][1].symbol) and isFree(chessboard[7][2].symbol) and isFree(chessboard[7][3].symbol):   # Queenside white
            if chessboard[7][4].pieceID == "wK" and chessboard[7][0].pieceID == "wR1":  # check if white king and queenside rook hasn't moved
                king = chessboard[7][4]
                rook = chessboard[7][0]
                chessboard[7][3], chessboard[7][0] = rook, blankChessboard[7][0]
                chessboard[7][2], chessboard[7][4] = king, blankChessboard[7][4]
                updChessboard(chessboard)
                turn += 1
                return chessboard
    else:
        if move == "O-O" and isFree(chessboard[0][5].symbol) and isFree(chessboard[0][6].symbol):   # Kingside black
            if chessboard[0][4].pieceID == "bK" and chessboard[0][7].pieceID == "bR2":  # check if black king and kingside rook hasn't moved
                king = chessboard[0][4]
                rook = chessboard[0][7]
                chessboard[0][5], chessboard[0][7] = rook, blankChessboard[0][7]
                chessboard[0][6], chessboard[0][4] = king, blankChessboard[0][4]
                updChessboard(chessboard)
                turn += 1
                return chessboard
        elif move == "O-O-O" and isFree(chessboard[0][1].symbol) and isFree(chessboard[0][2].symbol) and isFree(chessboard[0][3].symbol):   # Queenside black
            if chessboard[0][4].pieceID == "bK" and chessboard[0][0].pieceID == "bR1":  # check if black king and queenside rook hasn't moved
                king = chessboard[0][4]
                rook = chessboard[0][0]
                chessboard[0][3], chessboard[0][0] = rook, blankChessboard[0][0]
                chessboard[0][2], chessboard[0][4] = king, blankChessboard[0][4]
                updChessboard(chessboard)
                turn += 1
                return chessboard
    print("ERROR 023: INVALID CASTLING")
    return chessboard

def autoChess(game:list, chessboard):
    for user in game:
        if isWhite(): print("White", end=" ")
        else: print("Black", end=" ")
        print(user)
        time.sleep(1)
        if len(user) > 4:
            if user[3] == "x":
                chessboard = capturePiece(user, chessboard)
            elif user == "O-O-O":
                chessboard = castling(user, chessboard)
            else:
                chessboard = movePiece(user, chessboard)
        else:
            if user[1] == "x":
                chessboard = capturePiece(user, chessboard)
            elif user == "O-O":
                chessboard = castling(user, chessboard)
            else:
                chessboard = movePiece(user, chessboard)

def __main__():
    chessboard = genChessboard(pieces=True)
    updChessboard(chessboard)

    # while True:
    #     if isWhite(): print("White")
    #     else: print("Black")
    #     user = input()
    #     if len(user) > 4:
    #         if user[3] == "x":
    #             chessboard = capturePiece(user, chessboard)
    #         elif user == "O-O-O":
    #             chessboard = castling(user, chessboard)
    #         else:
    #             chessboard = movePiece(user, chessboard)
    #     else:
    #         if user[1] == "x":
    #             chessboard = capturePiece(user, chessboard)
    #         elif user == "O-O":
    #             chessboard = castling(user, chessboard)
    #         else:
    #             chessboard = movePiece(user, chessboard)
    game = """
        1.e4 .d5 2.exd5 .Nf6 3.d4 .Nxd5 4.Nf3 .g6 5.Be2 .Bg7 6.O-O .O-O 7.Na3 .Nc6 
        8.Nc4 .Nb6 9.c3 .Nxc4 10.Bxc4 .Bg4 11.Be2 .Qd6 12.h3 .Bxf3 13.Bxf3 .Rab8 
        14.Be3 .Rfd8 15.Re1 .e6 16.Qb3 .h6 17.Rad1 .b5 18.d5 .Na5 19.Qc2 .e5 20.Bxa7 .Ra8 
        21.Be3 .Nc4 22.b3 .Nxe3 23.fxe3 .e4 24.Bxe4 .Ra6 25.Bd3 .Qg3 26.Qf2 .Qxf2+ 
        27.Kxf2 .Bxc3 28.Re2 .Rxd5 29.Bc2 .Rf6+ 30.Kg1 .Rxd1+ 31.Bxd1 .Rd6 32.Bc2 .c5 
        33.Kf2 .Kg7 34.Be4 .Bd2 35.Bc6 .c4 36.bxc4 .bxc4 37.Ba4 .c3 38.Kf3 .Ra6 39.Bb3 .Rb6 
        40.Bd1 .Rb1 41.Ba4 .Rb2 42.a3 .c2 43.Bxc2 .Rxc2 44.Ke4 .Rb2 45.Kd3 .Bc3
        """
    game = pgnConverter(game)
    autoChess(game, chessboard)
        # break

if __name__ == "__main__":
    __main__()