import pandas as pd
import sys 
import os 
from typing import List

def combine_results(path: str, out_path: str) -> None:
    files: List[str] = os.listdir(path)
    res: List[pd.DataFrame] = []
    for f in files:
        file_path: str = os.path.join(path, f)
        res.append(pd.read_csv(file_path))
        
    res_df = pd.concat(res)
    
    hist_df: pd.DataFrame = res_df[['query_id', 'best_hit']]
    hist_df.rename(columns={'query_id': 'fasta_id', 'best_hit': 'best_hit_id'}, 
                   inplace=True)
    
    profit_df: pd.DataFrame = res_df[['score_std', 'score_gmean']].mean().to_frame().transpose()
    profit_df.rename(columns={
        'score_std': 'ave_std',
        'score_gmean': 'ave_gmean'
    }, inplace=True)
    
    hist_df.to_csv(os.path.join(out_path, 'hits_output.csv'), index=None)
    profit_df.to_csv(os.path.join(out_path, 'profile_output.csv'), index=None)
    

if __name__ == '__main__':
    int_path: str = sys.argv[1]
    out_path: str = sys.argv[2]
    combine_results(int_path, out_path)
    