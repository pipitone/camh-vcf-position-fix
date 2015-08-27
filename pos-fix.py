#!/usr/bin/env python
"""
Fixes offsets on VCF positions 

Usage: 
    pos-fix.py <input.vcf> <output.vcf>

"""
from docopt import docopt
import sys
import vcf

if __name__ == '__main__': 
    arguments = docopt(__doc__)
    infile  = arguments['<input.vcf>']
    outfile = arguments['<output.vcf>']

    vcf_reader = vcf.Reader(open(infile,'r'))
    vcf_writer = vcf.Writer(open(outfile,'w'), vcf_reader)

    offset = 0
    for record in vcf_reader:
        record.POS += offset
        vcf_writer.write_record(record)
        print offset
        offset += -(len(record.REF) - 1)
