import sys
import random
from Bio import SeqIO
from typing import List

"""
usage: python select_ids.py INPUT.fasta 2000
"""

def read_ids(file: str) -> List[str]:
    res: List[str] = []
    with open(file, 'r') as f:
        for line in f:
            res.append(line.strip())
    return res

def match_ids(file: str, ids: List[str]) -> List[str]:
    """
    Function reads a fasta formatted file of protein sequences
    """
    # print("READING FASTA FILES")
    records = []
    for record in SeqIO.parse(file, "fasta"):
        if record.id in ids:
            records.append(record)
    return records

def write_fasta(records: List, number: int) -> None:
    """
    Function writes the list of SeqIO records to a fasta formatted file.
    """
    first_part_size: int = len(records) // 3 + (len(records) % 3 > 0)
    remaining_records: int = len(records) - first_part_size
    other_parts: int = number - 1
    other_part_size: int = remaining_records // other_parts
    extra: int = remaining_records % other_parts
    
    split_records: List[List[str]] = [records[:first_part_size]]
    start_index: int = first_part_size
    for i in range(other_parts):
        end_index: int = start_index + other_part_size + (i < extra)
        split_records.append(records[start_index:end_index])
        start_index: int = end_index

    for i, record in enumerate(split_records):
        with open(f'data/exp/experiment_{i+1}.fasta', "w") as output_handle:
            print(f'{i+1} file writes {len(record)} records!')
            SeqIO.write(record, output_handle, "fasta")


if __name__ == "__main__":
    ids = read_ids(sys.argv[1])
    res = match_ids(sys.argv[2], ids)
    if len(res) == len(ids):
        print('All ids are matched!')
    else:
        print(f'{len(res)} ids are matched!')
    write_fasta(res, int(sys.argv[3]))