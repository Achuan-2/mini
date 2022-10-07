from src.seqAlignment import NeedlemanWunsch,SmithWaterman
def  main():
    seq1, seq2 = 'ATAGAATGCGG', 'TCGTAGACGA'
    penalty_dict = {'MATCH': 1, 'MISMATCH': -1, 'GAP': -2, 'EXTEND_GAP': -1}
    global_align = NeedlemanWunsch(seq1, seq2, penalty_dict)
    global_align.run()
    global_align.print_scoremat()
    global_align.print_tracemat()
    global_align.print_align()
    fig1=global_align.plot()
    fig1.savefig('output/nw.png',dpi=120)

    local_align = SmithWaterman(seq1, seq2, penalty_dict)
    local_align.run()
    local_align.print_scoremat()
    local_align.print_tracemat()
    local_align.print_align()
    fig2 = local_align.plot()
    fig2.savefig('output/sw.png', dpi=120)

if __name__ == "__main__":
    main()