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
    split_records: List[List[str]] = [records[i::number] for i in range(number)]
    for i, records in enumerate(split_records):
        with open(f'data/exp/experiemnt_{i+1}.fasta', "w") as output_handle:
            SeqIO.write(records, output_handle, "fasta")


if __name__ == "__main__":
    ids = read_ids(sys.argv[1])
    res = match_ids(sys.argv[2], ids)
    if len(res) == len(ids):
        print('All ids are matched!')
    else:
        print(f'{len(res)} ids are matched!')
    write_fasta(res, int(sys.argv[3]))