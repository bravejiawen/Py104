def read_first_line(fname):
    with open(fname,'r') as fin:
        first_line=fin.readline()
        return first_line
    if __name__ =='__main__':
        import sys
    read_first_line(sys.argv[1])
