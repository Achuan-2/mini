import copy
import numpy as np
from .base import PairwiseSeqAlignment
class SmithWaterman(PairwiseSeqAlignment):
    """
    Smith_Waterman

    cacalute direction by compare with 0(None) , vertical, horizontal, diagonal

    traceback from max score, end at 0 (all cells >0)
    """

    def run(self):
        self.local_score()
        find_max = np.where(self.score_mat == np.max(self.score_mat))
        row = find_max[0]
        col = find_max[1]
        path = []
        for i in range(len(row)):
            self.local_traceback(row[i], col[i], path)

    def local_score(self):
        trace_dict = {
            0: 'V',  # vertical
            1: 'D',  # diagonal
            2: 'H',  # horizontal
            3: '0'  # None
        }
        n = len(self.seq1) + 1  # The dimension of the matrix columns.
        m = len(self.seq2) + 1  # The dimension of the matrix rows.

        for i in range(1, n):
            for j in range(1, m):
                self.trace_mat[i][j] = ''

        for i in range(1, n):
            for j in range(1, m):
                # The value for match/mismatch -  diagonal.
                di = self.score_mat[i-1][j-1] + \
                    self.diagonal_score(self.seq1[i-1], self.seq2[j-1])
                # vertical value(from the upper cell)
                ve = self.score_mat[i-1][j] + self.penalty['GAP_EXTEND'] \
                    if 'V' in str(self.trace_mat[i - 1][j]) else self.score_mat[i-1][j] + self.penalty['GAP_OPEN']
                ho = self.score_mat[i][j-1] + self.penalty['GAP_EXTEND'] \
                    if 'H' in str(self.trace_mat[i][j-1]) else self.score_mat[i][j-1] + self.penalty['GAP_OPEN']

                score_list = np.array([ve, di,  ho, 0])
                max_score = np.max(score_list)
                max_indexs = np.argwhere(
                    score_list == max_score).flatten()
                self.score_mat[i][j] = max_score
                for max_index in max_indexs:
                    # if max score is 0, do not record the direction
                    if len(max_indexs) > 1 and max_index == 3:
                        continue
                    self.trace_mat[i][j] += trace_dict[max_index]

    def local_traceback(self, i, j, path):
        """
        recursively find all optimal traceback path from trace matrix
        """
        # Recursive termination condition: one cell score == 0
        if self.score_mat[i][j] == 0:
            path.append((i, j))
            # finally append the path to the self.paths
            self.paths.append(copy.deepcopy(path))
            path.pop()
        else:
            direction = self.trace_mat[i][j]
            # determine the direction each cell came from
            if 'D' in str(direction):
                path.append((i, j))
                self.local_traceback(i-1, j-1, path)
                path.pop()
            if 'H' in str(direction):
                path.append((i, j))
                self.local_traceback(i, j-1, path)
                path.pop()
            if 'V' in str(direction):
                path.append((i, j))
                self.local_traceback(i-1, j, path)
                path.pop()
