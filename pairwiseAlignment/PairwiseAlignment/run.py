import os
import click
from .src.utils import mkdir
from .src.SeqAlignment import NeedlemanWunsch, SmithWaterman


@click.command()
@click.option('--seq1', '-1', default='ATAGAATGCGG', prompt='Enter the first sequence', help='The first sequence.',type=str)
@click.option('--seq2', '-2', default='TCGTAGACGA',prompt='Enter the second sequence', help='The second sequence.',type=str)
@click.option('--match', '-m', default=1.0, show_default=True,help='The match score.',type=float)
@click.option('--mismatch', '-d', default=-1.0,  show_default=True,help='The mismatch penalty.',type=float)
@click.option('--gap','-g', default=-2.0,  show_default=True,help='The gap open penalty.',type=float)
@click.option('--extension', '-e', default=-1.0,  show_default=True,help='The gap extension penalty.',type=float)
@click.option('--output', '-o', default='output',  show_default=True,help='The output directory.',type=str)
@click.option('--global', '-G','method', flag_value='global', default='global',help='Choose global alignment.[default]')
@click.option('--local', '-L','method', flag_value='local', help='Choose local alignment.')
@click.option('--nosave', '-n', is_flag=True, help='Do not save the alignment result.')
def main(seq1, seq2, match, mismatch, gap, extension,output,method,nosave):
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
    if method=='global':
        align = NeedlemanWunsch(**para_dict)
    else:
        align = SmithWaterman(**para_dict)
    align.run()
    click.secho(f"\nChoose method : {method.capitalize()} Alignment", fg='green')
    for i in align.align_results:
        click.secho(i)
    if not nosave:
        align.save_align( os.path.join(output, f'{method}.txt'))
        fig1 = align.plot()
        fig1.savefig(os.path.join(output, f'{method}.png'), dpi=120)
        click.secho(f'Results saved in folder: "{output}"', fg='blue')



if __name__ == "__main__":
    main()
