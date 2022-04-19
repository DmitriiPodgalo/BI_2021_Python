# Python parallel programming homework in Bioinformatics Institute

All used modules are default in python. 

It requires Biopython and concurrent modules.

To use file should input fasta file and threads number (default is 1).

P.S. Возникли проблемы... *time* показывает, что не получилось распараллелить. Сначала хотел разбить фаста файл на интервалы (по количеству потоков) и определить с какого рида и до какого рида один поток дожен работать, но это тоже не распараллеливание.
