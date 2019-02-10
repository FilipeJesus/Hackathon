from itertools import chain
import itertools
import numpy as np
def unique(x):
    unique_list=[]
    for i in x:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
sequence="AATGGGACACATGCGCTGGGAGCCTGGTAATAAGCTGATTGAACTACAGATGACCCGCAAATGGAGACCTTTAGGAAAGAGTATCAAGGAAGTTAGGCGACACACGTACGAAGTGCGCCCAGATCTGACTTAAGAAACGTCGGGGTCATTTGGATACTAAGTCAAGCGAGAGCACGACACCCGCATTCGACCAGTGACCGAATGGGACACATGCGCTGGGAGCCTGCGACGTTCGCCGGCGGTAACGGCTTAACGGGGCTTGTTGCTGCTAGTCGGCGATATAGGTCTTCAGTAAAGCCATCTACTGGCCGCTTTTGAATGGTACCGAAGAGCAAAGCAAGTTCATTTGATTATTCTACTGTGGCGATTTCTATTCGTCGTGTTATAACATTGATTGCTCGCGATCGGGCCCGTTAGGCTTACTTCTGCGGAACGTGTTCTCGAAGGGATAGGTGCGAGGTGCGGGGCATGGAATTTTAGTCCTCCCTCTCCAAGCTGGCCGCTCTTCATGTTGTCATTTTTAGAATTTGGGTTGAGGTCCCCGCATAACAAACACTTTGGGACACATGCGCTGGGAGCCTCCAAAGGCAGTAGGCTTGGGGCACATGGGACACATGCGCTGGGAGCCTACAGGAACCGCTCTCACACGGTCCCGAAATTTGCCCGTGTGACCAACAACATCCTTTTATTTGTCGGCTGAAGTCATTGGTAGCGTGTTCACCCTTACGTGCGTAACCCCAGCGCGAATCTTCACCCCTAATAGTGCCGAGTACAGCTGGGTACCCGCTGCCAGATGAATGTACTAAGTCGGAAGGCATCTGTTTATCTGAGGAGCATTGCCTGCGGGCATAAAAATGGGACACATGCGCTGGGAGCCTCTGTTAGTTGCGAACTACGGACATGGTCCGACACTAGAAAGATTTGTATGGAAGCGGATCGAAGCCCCTGCTTCGACTGTACACCCCATGTCCCGTTCTGAACGATGGGACACATGCGCTGGGAGCCTCCGGGCAATTATGACCACAACTTCGGAGGGTTGTAGATCGGATTATTGCGTATCGTCGCAGTTTTTCCACACGGACTATCGTCGTCTAAACTAACCGGGGGGGCTCAGGTGGGACACATGCGCTGGGAGCCTCTG"
n=6
I=23
d=0

com=[sequence[c:(c+I)] for c in range(0,(len(sequence))-I)]
com=unique(x=com)
# possible=["A","C","T","G"]
# com=possible
# for x in range(0,I-1):
#     tmp=[]
#     com=list(itertools.product(com, possible))
#     joined_list=[]
#     for x in com:
#         tmp = x[0]+x[1]
#         joined_list.append(tmp)
#     com=joined_list

f = open('myfile', 'w')
for x in com:
    for_com=[]
    start_point=0
    while start_point <= len(sequence):
        len_through_sequence=start_point
        error=0
        len_through_x = 0
        len_of_matching_string=0
        #print(sequence[counter])
        while len_of_matching_string <= I:
            if len_of_matching_string ==0:
                if (len_through_x) >= len(x):
                    break
                elif (len_through_sequence) >= len(sequence):
                    break
                elif x[len_through_x] == sequence[len_through_sequence]:
                    len_through_sequence=len_through_sequence+1
                    len_of_matching_string=len_of_matching_string+1
                    len_through_x=len_through_x+1
                    output_list="1M"
                    start_point=len_through_sequence
                else:
                    len_through_sequence=len_through_sequence+1
            else:
                if error > d:
                    break
                elif (len_through_x) >= len(x):
                    break
                elif (len_through_sequence) >= len(sequence):
                    break
                elif x[len_through_x] == sequence[len_through_sequence]:
                    len_through_sequence=len_through_sequence+1
                    len_of_matching_string=len_of_matching_string+1
                    len_through_x=len_through_x+1
                    if output_list[-1] == "M":
                        tmp = output_list[-2:]
                        tmp= int(tmp[0])
                        tmp=tmp+1
                        tmp=str(tmp)+"M"
                        output_list=output_list[:-2]+tmp
                    else:
                        output_list=output_list+"1M"
                elif (len_of_matching_string) == I:
                    break
                else:
                    check = 0
                    for t in range(1,n+2):
                        if (len_through_sequence+t+1) > len(sequence):
                            error = d+1
                            break
                        elif (len_through_x+t+1) > len(x):
                            error = d+1
                            break
                        elif error >d:
                            break
                        elif x[len_through_x+t] == sequence[len_through_sequence]:
                            len_through_sequence=len_through_sequence+1
                            len_of_matching_string=len_of_matching_string+2
                            len_through_x=len_through_x+t+1
                            tmp=str(t)+"I1M"
                            output_list=output_list+tmp
                            error=error+t
                            check=1
                            break
                        elif x[len_through_x] == sequence[len_through_sequence+t]:
                            len_through_sequence=len_through_sequence+t+1
                            len_of_matching_string=len_of_matching_string+2
                            len_through_x=len_through_x+1
                            tmp=str(t)+"D1M"
                            output_list=output_list+tmp
                            error=error+t
                            check=1
                            break
                        elif x[len_through_x+t] == sequence[len_through_sequence+t]:
                            len_through_sequence=len_through_sequence+t+1
                            len_through_x=len_through_x+t+1
                            len_of_matching_string=len_of_matching_string+2
                            tmp=str(t)+"X1M"
                            output_list=output_list+tmp
                            error=error+t
                            check=1
                            break
                        if check == 0:
                            len_through_x=len_through_x+t+1
        if error <= d and len_of_matching_string >= I:
            for_com.append(str(start_point)+" "+output_list)
        start_point=start_point+1
    if len(for_com) >= n:
        f.write(x+"\n")
        for x in for_com:
            f.write(str(x)+"\n")
f.close()