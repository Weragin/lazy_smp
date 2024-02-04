from multiprocessing import Manager, Pool, cpu_count

from chess import Board

from engines.alpha_beta import AlphaBeta


class LazySMP(AlphaBeta):

    def search_move(self, board: Board, depth: int, null_move: bool) -> str:
        # start multiprocessing
        nprocs = cpu_count()
        pool = Pool(processes=nprocs)
        manager = Manager()
        shared_cache = manager.dict()
        # executing all the moves at layer 1 in parallel
        # starmap blocks until all process are done
        pool.starmap(
            self.negamax,
            [(board, depth, null_move, shared_cache) for _ in range(nprocs)],
        )

        # return best move for our original board
        return shared_cache[(board.fen(), depth)][1]
