import sys

def make_move(board, player, start, end):
    # check if start and end are on the board
    if start[0] < 0 or start[0] >= len(board):
        return False
    if start[1] < 0 or start[1] >= len(board):
        return False
    if end[0] < 0 or end[0] >= len(board):
        return False
    if end[1] < 0 or end[1] >= len(board):
        return False

    # check if start and end are on the same row or column
    if start[0] != end[0] and start[1] != end[1]:
        return False

    # check if the move is diagonal
    if abs(start[0] - end[0]) != abs(start[1] - end[1]):
        return False

    # check if there is a piece at start
    if board[start[0]][start[1]] == '_':
        return False

    # check if the piece at start is the correct color
    if board[start[0]][start[1]].lower() != player:
        return False

    # check if the space at end is empty
    if board[end[0]][end[1]] != '_':
        return False

    # check if the move is a single space move
    if start[0] == end[0] and start[1] == end[1] - 1:
        return True
    if start[0] == end[0] and start[1] == end[1] + 1:
        return True

    # check if the move is a jump move
    if player == 'b':
        if start[0] == end[0] + 2 and start[1] == end[1] + 2 and board[start[0] - 1][start[1] + 1].lower() == 'w':
            return True
        if start[0] == end[0] + 2 and start[1] == end[1] - 2 and board[start[0] - 1][start[1] - 1].lower() == 'w':
            return True
    if player == 'w':
        if start[0] == end[0] - 2 and start[1] == end[1] + 2 and board[start[0] + 1][start[1] + 1].lower() == 'b':
            return True
        if start[0] == end[0] - 2 and start[1] == end[1] - 2 and board[start[0] + 1][start[1] - 1].lower() == 'b':
            return True

    return False

def make_jump(board, player, start, end):
    # check if start and end are on the board
    if start[0] < 0 or start[0] >= len(board):
        return False
    if start[1] < 0 or start[1] >= len(board):
        return False
    if end[0] < 0 or end[0] >= len(board):
        return False
    if end[1] < 0 or end[1] >= len(board):
        return False

    # check if start and end are on the same row or column
    if start[0] != end[0] and start[1] != end[1]:
        return False

    # check if the move is diagonal
    if abs(start[0] - end[0]) != abs(start[1] - end[1]):
        return False

    # check if there is a piece at start
    if board[start[0]][start[1]] == '_':
        return False

    # check if the piece at start is the correct color
    if board[start[0]][start[1]].lower() != player:
        return False

    # check if the space at end is empty
    if board[end[0]][end[1]] != '_':
        return False

    # check if the move is a jump move
    if player == 'b':
        if start[0] == end[0] + 2 and start[1] == end[1] + 2 and board[start[0] - 1][start[1] + 1].lower() == 'w':
            return True
        if start[0] == end[0] + 2 and start[1] == end[1] - 2 and board[start[0] - 1][start[1] - 1].lower() == 'w':
            return True
    if player == 'w':
        if start[0] == end[0] - 2 and start[1] == end[1] + 2 and board[start[0] + 1][start[1] + 1].lower() == 'b':
            return True
        if start[0] == end[0] - 2 and start[1] == end[1] - 2 and board[start[0] + 1][start[1] - 1].lower() == 'b':
            return True

    return False

def is_king(piece):
    if piece == 'b' or piece == 'w':
        return False
    return True

def get_valid_moves(board, player, start):
    moves = []
    if player == 'b':
        if start[0] < len(board) - 1:
            if is_king(board[start[0]][start[1]]):
                if start[1] > 0:
                    if make_move(board, player, start, (start[0] + 1, start[1] - 1)):
                        moves.append((start[0] + 1, start[1] - 1))
                if start[1] < len(board) - 1:
                    if make_move(board, player, start, (start[0] + 1, start[1] + 1)):
                        moves.append((start[0] + 1, start[1] + 1))
            else:
                if make_move(board, player, start, (start[0] + 1, start[1] - 1)):
                    moves.append((start[0] + 1, start[1] - 1))
                if make_move(board, player, start, (start[0] + 1, start[1] + 1)):
                    moves.append((start[0] + 1, start[1] + 1))
        if is_king(board[start[0]][start[1]]):
            if start[0] > 0:
                if start[1] > 0:
                    if make_move(board, player, start, (start[0] - 1, start[1] - 1)):
                        moves.append((start[0] - 1, start[1] - 1))
                if start[1] < len(board) - 1:
                    if make_move(board, player, start, (start[0] - 1, start[1] + 1)):
                        moves.append((start[0] - 1, start[1] + 1))
    if player == 'w':
        if start[0] > 0:
            if is_king(board[start[0]][start[1]]):
                if start[1] > 0:
                    if make_move(board, player, start, (start[0] - 1, start[1] - 1)):
                        moves.append((start[0] - 1, start[1] - 1))
                if start[1] < len(board) - 1:
                    if make_move(board, player, start, (start[0] - 1, start[1] + 1)):
                        moves.append((start[0] - 1, start[1] + 1))
            else:
                if make_move(board, player, start, (start[0] - 1, start[1] - 1)):
                    moves.append((start[0] - 1, start[1] - 1))
                if make_move(board, player, start, (start[0] - 1, start[1] + 1)):
                    moves.append((start[0] - 1, start[1] + 1))
        if is_king(board[start[0]][start[1]]):
            if start[0] < len(board) - 1:
                if start[1] > 0:
                    if make_move(board, player, start, (start[0] + 1, start[1] - 1)):
                        moves.append((start[0] + 1, start[1] - 1))
                if start[1] < len(board) - 1:
                    if make_move(board, player, start, (start[0] + 1, start[1] + 1)):
                        moves.append((start[0] + 1, start[1] + 1))
    return moves

def get_valid_jumps(board, player, start):
    jumps = []
    if player == 'b':
        if start[0] < len(board) - 1:
            if is_king(board[start[0]][start[1]]):
                if start[1] > 0:
                    if make_jump(board, player, start, (start[0] + 2, start[1] - 2)):
                        jumps.append((start[0] + 2, start[1] - 2))
                if start[1] < len(board) - 1:
                    if make_jump(board, player, start, (start[0] + 2, start[1] + 2)):
                        jumps.append((start[0] + 2, start[1] + 2))
            else:
                if make_jump(board, player, start, (start[0] + 2, start[1] - 2)):
                    jumps.append((start[0] + 2, start[1] - 2))
                if make_jump(board, player, start, (start[0] + 2, start[1] + 2)):
                    jumps.append((start[0] + 2, start[1] + 2))
        if is_king(board[start[0]][start[1]]):
            if start[0] > 0:
                if start[1] > 0:
                    if make_jump(board, player, start, (start[0] - 2, start[1] - 2)):
                        jumps.append((start[0] - 2, start[1] - 2))
                if start[1] < len(board) - 1:
                    if make_jump(board, player, start, (start[0] - 2, start[1] + 2)):
                        jumps.append((start[0] - 2, start[1] + 2))
    if player == 'w':
        if start[0] > 0:
            if is_king(board[start[0]][start[1]]):
                if start[1] > 0:
                    if make_jump(board, player, start, (start[0] - 2, start[1] - 2)):
                        jumps.append((start[0] - 2, start[1] - 2))
                if start[1] < len(board) - 1:
                    if make_jump(board, player, start, (start[0] - 2, start[1] + 2)):
                        jumps.append((start[0] - 2, start[1] + 2))
            else:
                if make_jump(board, player, start, (start[0] - 2, start[1] - 2)):
                    jumps.append((start[0] - 2, start[1] - 2))
                if make_jump(board, player, start, (start[0] - 2, start[1] + 2)):
                    jumps.append((start[0] - 2, start[1] + 2))
        if is_king(board[start[0]][start[1]]):
            if start[0] < len(board) - 1:
                if start[1] > 0:
                    if make_jump(board, player, start, (start[0] + 2, start[1] - 2)):
                        jumps.append((start[0] + 2, start[1] - 2))
                if start[1] < len(board) - 1:
                    if make_jump(board, player, start, (start[0] + 2, start[1] + 2)):
                        jumps.append((start[0] + 2, start[1] + 2))
    return jumps

def get_jumps(board, player, start, end, hops):
    if start == end:
        return hops
    jumps = get_valid_jumps(board, player, start)
    for jump in jumps:
        if jump not in hops:
            hops.append(jump)
            hops = get_jumps(board, player, jump, end, hops)
    return hops

def do_move(board, player, start, end):
    if make_move(board, player, start, end):
        board[end[0]][end[1]] = board[start[0]][start[1]]
        board[start[0]][start[1]] = '_'
        if player == 'b' and end[0] == len(board) - 1:
            board[end[0]][end[1]] = board[end[0]][end[1]].upper()
        if player == 'w' and end[0] == 0:
            board[end[0]][end[1]] = board[end[0]][end[1]].upper()
        return True
    return False

def do_jump(board, player, start, end):
    if make_jump(board, player, start, end):
        board[end[0]][end[1]] = board[start[0]][start[1]]
        board[start[0]][start[1]] = '_'
        mid = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
        board[mid[0]][mid[1]] = '_'
        if player == 'b' and end[0] == len(board) - 1:
            board[end[0]][end[1]] = board[end[0]][end[1]].upper()
        if player == 'w' and end[0] == 0:
            board[end[0]][end[1]] = board[end[0]][end[1]].upper()
        return True
    return False