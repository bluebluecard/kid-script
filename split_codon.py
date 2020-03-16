import sys
import numpy as np 

def split_seq(seq_string,pos_index):
    temp_seq = ['','']
    seq_array = np.array(list(seq_string))

    temp_seq[0] = ''.join(seq_array[pos_index[0]])
    temp_seq[1] = ''.join(seq_array[pos_index[1]])
    
    return temp_seq

def two_index(seq_length):
    pos = [[],[]]
    for i in range(seq_length):
        if (i+1) % 3 == 0:
            pos[1].append(i)
        else:
            pos[0].append(i)
    return pos

def write_file(file_name,string_output):
    with open(file_name,'a+') as fh:
        fh.write(string_output+'\n')

def run():

    with open(sys.argv[1],'r') as f:
        header = f.readline().strip().split()
        
        seq_len = int(header[1])
        spe_num = header[0]
        pos = two_index(seq_len)
        flag = 1
        for line in f :
            info = line.strip().split()
            out_seq = split_seq(info[1],pos)

            if flag:
                write_file('codon12.phy','\t'+spe_num+'\t'+str(len(out_seq[0])))
                write_file('codon3.phy','\t'+spe_num+'\t'+str(len(out_seq[1])))           
                flag = 0
            write_file('codon12.phy',info[0]+'\t'+out_seq[0])
            write_file('codon3.phy',info[0]+'\t'+out_seq[1])

run()
