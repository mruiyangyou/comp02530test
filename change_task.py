import pandas as pd 
import sys
from Bio import SeqIO
from typing import List

def read_fasta(file: str) -> List[str]:
    """
    Function reads a fasta formatted file of protein sequences
    """
    # print("READING FASTA FILES")
    records = []
    for record in SeqIO.parse(file, "fasta"):
            records.append(record)
    return records

if __name__ == '__main__':
    work = read_fasta('experiments.fasta')
    print(f'Total amount of works: {len(work)}')

    processed_task = pd.read_csv('hhr_parse.out')

    print(f'Process_task: {len(processed_task)}')
    
    result =([w.id for w in work] == processed_task['query_id'].to_list())
    print(f'Matched id with fasta file: {result}')
    
    
    if int(sys.argv[1]) == 1:
        new_work = work[len(processed_task):]
        print(f'Size of new work will be {len(new_work)}')
        
        with open('experiment_new.fasta', "w") as output_handle:
            SeqIO.write(new_work, output_handle, "fasta")
         
