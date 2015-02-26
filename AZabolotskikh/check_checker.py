import chess

def main():
    fens = [x.split("\t")[0] for x in open("position_scores.txt").readlines()]
    for fen in fens:
        print (fen, chess.Bitboard(fen).is_check())

main()
