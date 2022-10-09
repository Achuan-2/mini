import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


class PairwiseSeqAlignment():
    # A dictionary for all the penalty values.
    def __init__(self, seq1, seq2, match, mismatch, gap_open, gap_extension) -> None:
        self.seq1 = seq1.upper()
        self.seq2 = seq2.upper()
        self.penalty  = {'MATCH': match, 'MISMATCH': mismatch,
                    'GAP_OPEN': gap_open, 'GAP_EXTEND': gap_extension}
        self.paths = []
        # Initializes the  matrix
        self.score_mat = np.zeros((len(self.seq1) + 1, len(self.seq2) + 1), dtype=float)
        self.trace_mat = np.zeros((len(self.seq1) + 1, len(self.seq2) + 1), dtype=object)
    @property
    def parameters(self):
        return f'\n{"Parameters".center(40,"=")}\n\nMATCH: {self.penalty["MATCH"]}\nMISMATCH: {self.penalty["MISMATCH"]}\nGAP_OPEN: {self.penalty["GAP_OPEN"]}\nGAP_EXTEND: {self.penalty["GAP_EXTEND"]}\n'
    @property
    def align_results(self):
        results = []
        # traverse each path
        for k, path in enumerate(self.paths):
            align1 = ''
            middle = ''
            align2 = ''
            count = 0
            score = self.score_mat[path[0][0]][path[0][1]]
            # invert the path
            for i in range(len(path) - 1, 0, -1):
                # from horizontal
                if path[i][0] == path[i - 1][0]:
                    align1 += '-'
                    middle = middle + ' '
                    align2 += self.seq2[path[i - 1][1] - 1]
                # from vertical
                elif path[i][1] == path[i - 1][1]:
                    align1 += self.seq1[path[i - 1][0] - 1]
                    middle = middle + ' '
                    align2 += '-'
                # from diagonal
                else:
                    ch1 = self.seq1[path[i - 1][0] - 1]
                    ch2 = self.seq2[path[i - 1][1] - 1]
                    align1 += ch1
                    align2 += ch2
                    if ch1 == ch2:
                        middle = middle + '|'
                        count += 1
                    else:
                        middle = middle + ' '
                
            align_identity = count/(len(path)-1)
            
            align_result=f'\n{f"Alignment {k+1}".center(40,"=")}\n\n'+f'{align1}\n{middle}\n{align2}\n\nIdentity={align_identity:.2%}({count}/{len(path)-1})\nScore={score}\n'
            results.append(align_result)
        return results
    def diagonal_score(self, base1, base2):
        if base1 != base2:
            return self.penalty['MISMATCH']
        else:
            return self.penalty['MATCH']

    def output_matrix(self, m):
        """print score matrix or trace matrix"""
        seq1 = '-' + self.seq1
        seq2 = '-' + self.seq2
        output = '\n'+' '.join([f'{i:>4}' for i in ' '+seq2])
        for i, p in enumerate(seq1):
            line = [p] + [m[i][j] for j in range(len(seq2))]
            output += '\n'+' '.join([f'{i:>4}' for i in line])
        output += '\n'
        return output
    @property
    def scoremat(self):
        return f'\n{"Score Matrix".center(40,"=")}\n'+self.output_matrix(self.score_mat)
    
    @property
    def tracemat(self):
        return f'\n{"Trace Matrix".center(40,"=")}\n'+self.output_matrix(self.trace_mat)
    
    def save_align(self, filename):
        with open(filename, 'w') as f:
            f.write(self.parameters)
            f.write(self.scoremat)
            f.write(self.tracemat)
            f.write('\n'.join(self.align_results))
    def plot(self):
        n = len(self.seq1)
        m = len(self.seq2)
        plt.rcParams["figure.figsize"] = m, n
        param = {"grid.linewidth": 1.6,
                 "grid.color": "lightgray",
                 "axes.linewidth": 1.6,
                 "axes.edgecolor": "lightgray"}
        plt.rcParams.update(param)

        # plot cell
        fig, ax = plt.subplots(
            1, 2, gridspec_kw={'width_ratios': [1, 0.3]})
        ax[0].set_xlim(-0.5, self.score_mat.shape[1] - .5)
        ax[0].set_ylim(-0.5, self.score_mat.shape[0] - .5)
        ax[0].invert_yaxis()
        ax[1].set_xlim(-0.5, self.score_mat.shape[1] - .5)
        ax[1].set_ylim(-0.5, self.score_mat.shape[0] - .5)
        for i in range(self.score_mat.shape[0]):
            for j in range(self.score_mat.shape[1]):
                ax[0].text(j, i, np.round(self.score_mat[i, j],2),
                           ha="center", va="center")
        for i, l in enumerate(self.seq2):
            ax[0].text(i + 1, -0.7, l, ha="center",
                       va="center", fontweight="semibold")
        for i, l in enumerate(self.seq1):
            ax[0].text(-0.7, i + 1, l, ha="center",
                       va="center", fontweight="semibold")

        ax[0].xaxis.set_minor_locator(ticker.FixedLocator(
            np.arange(-1.5, self.score_mat.shape[1] - .5, 1)))
        ax[0].yaxis.set_minor_locator(ticker.FixedLocator(
            np.arange(-1.5, self.score_mat.shape[0] - .5, 1)))
        ax[0].tick_params(axis='both', which='both', bottom=False, top=False,
                          left=False, right=False, labelbottom=False, labelleft=False)
        ax[0].grid(True, which='minor')
        ax[1].axis('off')
        arrowprops = dict(facecolor='blue', alpha=1, lw=0,
                          shrink=0.2, width=2, headwidth=7, headlength=7)

        # plot all paths
        for i in range(1, self.trace_mat.shape[0]):
            for j in range(1, self.trace_mat.shape[1]):
                if ('H' in self.trace_mat[i][j]):
                    ax[0].annotate("", xy=(j - 1, i),
                                   xytext=(j, i), arrowprops=arrowprops)
                if ('D' in self.trace_mat[i][j]):
                    ax[0].annotate("", xy=(j - 1, i - 1),
                                   xytext=(j, i), arrowprops=arrowprops)
                if ('V' in self.trace_mat[i][j]):
                    ax[0].annotate("", xy=(j, i - 1),
                                   xytext=(j, i), arrowprops=arrowprops)

        # plot optimal path
        arrowprops.update(facecolor='crimson')
        for path_list in self.paths:
            for i in range(len(path_list)-1):
                ax[0].annotate("", xy=path_list[i+1][::-1],
                               xytext=path_list[i][::-1], arrowprops=arrowprops)
        results=self.parameters+"\n".join(self.align_results)
        ax[1].text(0, 0, results,
                   family='monospace', fontweight="semibold")
        fig.tight_layout()

        # plt.show()
        return fig


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
        for i in range(n):
            self.score_mat[i][0] = self.penalty['GAP_OPEN'] * i
            self.trace_mat[i][0] = 'V'
        # Scans all the first columns element in the matrix and fill it with "gap penalty"
        for j in range(m):
            self.score_mat[0][j] = self.penalty['GAP_OPEN'] * j
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
                    if 'V' in str(self.trace_mat[i - 1][j])  else self.score_mat[i-1][j] + self.penalty['GAP_OPEN']
                ho = self.score_mat[i][j-1] + self.penalty['GAP_EXTEND'] \
                    if 'H' in str(self.trace_mat[i][j-1])  else self.score_mat[i][j-1] + self.penalty['GAP_OPEN']

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

