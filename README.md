# COMP0235-Coursework analysis codes

## Code Structure

* [change_task.py](/change_task.py) - Change the analyzed task for each working machine when some unexpected circumstances happen such as machine disconnection
* [combine_results.py](/combine_results.py) - Combine the results from each working machine to output the prediction csv and calculating the geometric mean and standard deviation
* [select_ids.py](/select_ids.py) - Match all the protein sequences to experiment_ids.txt from [unipro-tkb_proteome_UP000005640_2023_10_05.fasta](/uniprotkb_proteome_UP000005640_2023_10_05.fasta) and distribute work to five working machines based on each machine’s cpu's cores
* [results_parser.py](/results_parser.py) - Used in the pipeline script to output hhr_parse.out with correct prediction format
* [pipeline_script.py](/pipeline_script.py) - Entire data analysis pipeline script involving four steps
* [experiment_ids.txt](/experiment_ids.txt) - Task file
* [test_experiments.txt](/test_experiments.txt) - Small sample test file

## Link to Ansible repo
[COMP0235 Coursework](https://github.com/mruiyangyou/COMP0235-Coursework?tab=readme-ov-file)