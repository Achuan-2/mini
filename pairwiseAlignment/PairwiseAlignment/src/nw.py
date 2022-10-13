import copy
import numpy as np
from .base import PairwiseSeqAlignment
class NeedlemanWunsch(PairwiseSeqAlignment):
    """
    Needleman_Wunsch  

    cacalute direction by compare with vertical, horizontal, diagonal  

    traceback from last cell, end at first cell
        """

    def run(self):
        n, m = self.global_score()
        path = []
        self.global_traceback(n-1, m-1, path)

    def global_score(self):
        n = len(self.seq1) + 1  # The dimension of the matrix columns.
        m = len(self.seq2) + 1  # The dimension of the matrix rows.
        trace_dict = {
            0: 'V',  # diagonal
            1: 'D',  # vertical
            2: 'H'  # horizontal
        }
        for i in range(n):
            for j in range(m):
                self.trace_mat[i][j] = ''
        # Scans all the first rows element in the matrix and fill it with "gap penalty"
        for i in range(1,n):
            self.score_mat[i][0] = self.penalty['GAP_OPEN']+self.penalty['GAP_EXTEND']*(i-1)
            self.trace_mat[i][0] = 'V'
        # Scans all the first columns element in the matrix and fill it with "gap penalty"
        for j in range(1,m):
            self.score_mat[0][j] = self.penalty['GAP_OPEN']+self.penalty['GAP_EXTEND']*(j-1)
            self.trace_mat[0][j] = 'H'
        # Return the first element of the pointer matrix back to 0.
        self.trace_mat[0][0] = 0

        for i in range(1, n):
            for j in range(1, m):
                # The value for match/mismatch -  diagonal.
                di = self.score_mat[i-1][j-1] + \
                    self.diagonal_score(self.seq1[i-1], self.seq2[j-1])
                # vertical value(from the upper cell)
                ve = self.score_mat[i-1][j] + self.penalty['GAP_EXTEND'] \
                    if 'V' in str(self.trace_mat[i - 1][j])  else self.score_mat[i-1][j] + self.penalty['GAP_OPEN']
                ho = self.score_mat[i][j-1] + self.penalty['GAP_EXTEND'] \
                    if 'H' in str(self.trace_mat[i][j-1])  else self.score_mat[i][j-1] + self.penalty['GAP_OPEN']

                score_list = np.array([ve, di,  ho])
                max_score = np.max(score_list)
                max_indexs = np.argwhere(
                    score_list == max_score).flatten()
                self.score_mat[i][j] = max_score
                for max_index in max_indexs:
                    self.trace_mat[i][j] = self.trace_mat[i][j] + \
                        trace_dict[max_index]

        return n, m

    def global_traceback(self, i, j, path):
        '''
        recursively find all optimal traceback path from trace matrix
        '''
        # Recursive termination condition: (0,0) cell
        if i == 0 and j == 0:
            path.append((i, j))
            # finally append the path to the self.paths
            self.paths.append(copy.deepcopy(path))
            path.pop()
        else:
            direction = self.trace_mat[i][j]
            # determine the direction each cell came from
            if 'D' in str(direction):
                path.append((i, j))
                self.global_traceback(i-1, j-1, path)
                path.pop()
            if 'H' in str(direction):
                path.append((i, j))
                self.global_traceback(i, j-1, path)
                path.pop()
            if 'V' in str(direction):
                path.append((i, j))
                self.global_traceback(i-1, j, path)
                path.pop()

