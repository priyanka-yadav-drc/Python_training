from itertools import islice
def file_read_from_head(fname, nlines):
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('demo.txt',2)
