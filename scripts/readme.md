# How to use scripts


## root dir
_id_generation.py:_ generate ids for each URDF Bundle, and add to readme.

_prepare_files_for_fdupes.py:_ remove white spaces, and tabs, and convert all carriage returns to DOS (CRLF).

## paper_results dir
contains scripts used to generate the results for the paper.

## other dir
contains scripts for other purposes, such as assing urdf paths to meta-information files, or extracting unique words.

## fdupes_run dir
contains the results of running the unix command 'fdupes' on the dataset, to extract identical files.

## bash_scripts dir
contains bash scripts used during the creation of the dataset.