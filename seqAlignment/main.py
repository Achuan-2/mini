from pkg_resources import require
from src.seqAlignment import NeedlemanWunsch, SmithWaterman
import click


@click.command()
@click.option('--seq1', '-1', default='ATAGAATGCGG', prompt='Enter the first sequence', help='The first sequence.')
@click.option('--seq2', '-2', default='TCGTAGACGA',prompt='Enter the second sequence', help='The second sequence.')
@click.option('--match', '-m', default=1, help='The match score.')
@click.option('--mismatch', '-d', default=-1, help='The mismatch score.')
@click.option('--gap','-g', default=-2, help='The gap score.')
@click.option('--extension', '-e', default=-1, help='The extension score.')

def main(seq1, seq2, match, mismatch, gap, extension):
    para_dict = {
        'seq1':seq1,
        'seq2':seq2,
        'match': match, 
        'mismatch': mismatch,
        'gap_open': gap,
        'gap_extension': extension}
    global_align = NeedlemanWunsch(**para_dict)
    global_align.run()
    global_align.save_align('output/nw.txt')
    fig1 = global_align.plot()
    fig1.savefig('output/nw.png', dpi=120)

    local_align = SmithWaterman(**para_dict)
    local_align.run()
    local_align.save_align('output/sw.txt')
    fig2 = local_align.plot()
    fig2.savefig('output/sw.png', dpi=120)
    click.secho("-------------------------------> Done!", fg='red')
    click.secho("Results saved in output folder.", fg='blue')


if __name__ == "__main__":
    main()
