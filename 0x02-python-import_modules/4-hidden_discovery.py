#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for read in dir(hidden_4):
        if read[0] != '_':
            print("{:s}".format(read))