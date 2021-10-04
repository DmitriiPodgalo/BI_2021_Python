# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def main(input_fastq, output_file_prefix, 
         gc_bounds=(0, 100), 
         length_bounds=(0, 2**32), 
         quality_threshold=0, 
         save_filtered=False):
    
    
    data = read_file(input_fastq)
    gc_reads = list(filter(lambda arg: filter_gc((50, 100), arg), data))
    

    

def read_file(input_fastq):
    
    data = []
    with open(input_fastq) as f:
        file = f.readlines()
        # не смог придумать без цикла, но хоть цикл уменьшил в 4 раза
        for i in range(0, int(len(file)/4)): 
            one_read = [file[::4][i], file[1::4][i], file[2::4][i], file[3::4][i]]
            data.append(one_read)    
            
    return data

    
def write_file(output_file_prefix, save_filtered):
    
    output_passed_fastq = output_file_prefix + '_passed.fastq'
    with open(output_passed_fastq, 'w') as fp:
            fp.write('')
    
    if not save_filtered:
        output_failed_fastq = output_file_prefix + '_failed.fastq'
        with open(output_failed_fastq, 'w') as ff:
                ff.write('')


def filter_gc(gc_bounds, list_):
    
    if len(gc_bounds) == 1:
        gc_bounds = (0, gc_bounds)
    
    line = list_[1].upper()
    
    length_common = len(line)
    length_gc = line.count('G') + line.count('C')
    bound = round(length_gc / length_common, 5) * 100
    
    if bound >= gc_bounds[0] and bound <= gc_bounds[1]:
        return list_





