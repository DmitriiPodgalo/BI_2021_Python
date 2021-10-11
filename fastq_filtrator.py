# -*- coding: utf-8 -*-
"""
Spyder Editor

Dmitrii Podgalo
"""

input_fastq = input('File path: ')
output_file_prefix = input('File prefix: ')
gc_bounds = list(map(int, input('GC-interval using whitespace: ').split()))
length_bounds = list(
    map(int, input('Length-interval using whitespace: ').split()))

try:
    quality_threshold = int(input('Quality threshold: '))
except ValueError:
    quality_threshold = 0

save_filtered = True if input('Save filtered reads (y/n): ') == 'y' else False


def main(input_fastq, output_file_prefix, gc_bounds, length_bounds,
         quality_threshold, save_filtered):
    if gc_bounds == []:
        gc_bounds = [0, 100]
    if length_bounds == []:
        length_bounds = [0, 2**32]

    all_reads = read_file(input_fastq)
    gc_reads = list(filter(lambda arg: filter_gc(gc_bounds, arg), all_reads))
    length_reads = list(filter(lambda arg: filter_length(length_bounds, arg),
                               gc_reads))
    quality_reads = list(filter(lambda arg: filter_quality(quality_threshold, arg), length_reads))
    write_file(output_file_prefix, save_filtered, quality_reads, all_reads)


def read_file(input_fastq):

    all_reads = []
    with open(input_fastq) as f:
        file = f.readlines()
        for i in range(0, int(len(file)/4)):
            one_read = [file[::4][i], file[1::4][i],
                        file[2::4][i], file[3::4][i]]
            all_reads.append(one_read)

    return all_reads


def write_file(output_file_prefix, save_filtered, filtered_reads, all_reads):

    failed_reads = [i for i in all_reads if i not in filtered_reads]

    output_passed_fastq = output_file_prefix + '_passed.fastq'
    filtered_reads = [item for sublist in filtered_reads for item in sublist]

    with open(output_passed_fastq, 'w') as fp:
        fp.write(''.join(filtered_reads))

    if save_filtered:
        output_failed_fastq = output_file_prefix + '_failed.fastq'
        failed_reads = [item for sublist in failed_reads for item in sublist]

        with open(output_failed_fastq, 'w') as ff:
            ff.write(''.join(failed_reads))


def filter_gc(gc_bounds, list_):

    if len(gc_bounds) == 1:
        gc_bounds = [0, gc_bounds[0]]

    line = list_[1].upper().strip()

    length_common = len(line)
    length_gc = line.count('G') + line.count('C')
    bound = round(length_gc / length_common, 5) * 100

    if bound >= gc_bounds[0] and bound <= gc_bounds[1]:
        return list_


def filter_length(length_bounds, list_):

    if len(length_bounds) == 1:
        length_bounds = [0, length_bounds[0]]

    line = list_[1].strip()
    bound = len(line)

    if bound >= length_bounds[0] and bound <= length_bounds[1]:
        return list_


def filter_quality(quality_threshold, list_):

    # у иллюимина нет 'J', но в fastq файле есть, я добавил его со score 41
    quality_dict = {'!': 0, '"': 1, '#': 2, '$': 3, '%': 4, '&': 5, "'": 6,
                    '(': 7, ')': 8, '*': 9, '+': 10, ',': 11, '-': 12,
                    '.': 13, '/': 14, '0': 15, '1': 16, '2': 17, '3': 18,
                    '4': 19, '5': 20, '6': 21, '7': 22, '8': 23, '9': 24,
                    ':': 25, ';': 26, '<': 27, '=': 28, '>': 29, '?': 30,
                    '@': 31, 'A': 32, 'B': 33, 'C': 34, 'D': 35, 'E': 36,
                    'F': 37, 'G': 38, 'H': 39, 'I': 40, 'J': 41}
    counter = 0
    line = list_[3].strip()

    for i in line:
        counter += quality_dict[i]

    bound = counter / len(line)

    if bound >= quality_threshold:
        return list_

main(input_fastq, output_file_prefix, gc_bounds, length_bounds, 
      quality_threshold, save_filtered)
