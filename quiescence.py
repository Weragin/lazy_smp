
import psqt

def quiescence_search(board, player, alpha, beta):
    stand_pat = player * psqt.board_value_piece_square(board)
    if(stand_pat >= beta):
        return beta
    if( alpha < stand_pat ):
        alpha = stand_pat

    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)        
            score = -quiescence_search(board, -player, -beta, -alpha )
            board.pop()

            if(score >= beta):
                return score
            if(score > alpha):
                alpha = score  
    
    return alpha