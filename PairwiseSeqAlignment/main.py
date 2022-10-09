import click
from src.utils import mkdir
from src.PairwiseSeqAlignment import NeedlemanWunsch, SmithWaterman


@click.command()
@click.option('--seq1', '-1', default='ATAGAATGCGG', prompt='Enter the first sequence', help='The first sequence.',type=str)
@click.option('--seq2', '-2', default='TCGTAGACGA',prompt='Enter the second sequence', help='The second sequence.',type=str)
@click.option('--match', '-m', default=1.0, help='The match score.',type=float)
@click.option('--mismatch', '-d', default=-1.0, help='The mismatch penalty.',type=float)
@click.option('--gap','-g', default=-2.0, help='The gap open penalty.',type=float)
@click.option('--extension', '-e', default=-1.0, help='The gap extension penalty.',type=float)
@click.option('--output', '-o', default='output', help='The output directory.',type=str)
def main(seq1, seq2, match, mismatch, gap, extension,output):
    """
    Using Python to implement Needleman Wunsch and Smith Waterman algorithms for pairwise sequence alignment
    """
    mkdir(output)
    para_dict = {
        'seq1':seq1,
        'seq2':seq2,
        'match': match, 
        'mismatch': mismatch,
        'gap_open': gap,
        'gap_extension': extension}
    global_align = NeedlemanWunsch(**para_dict)
    global_align.run()
    global_align.save_align(f'{output}/nw.txt')
    fig1 = global_align.plot()
    fig1.savefig(f'{output}/nw.png', dpi=120)

    local_align = SmithWaterman(**para_dict)
    local_align.run()
    local_align.save_align(f'{output}/sw.txt')
    fig2 = local_align.plot()
    fig2.savefig(f'{output}/sw.png', dpi=120)
    click.secho("-------------------------------> Done!", fg='red')
    click.secho(f"Results saved in folder: {output}.", fg='blue')


if __name__ == "__main__":
    main()
