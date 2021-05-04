# CS 170 Project Spring 2021

Take a look at the project spec before you get started!

Requirements:

Python 3.6+

You'll only need to install networkx to work with the starter code. For installation instructions, follow: https://networkx.github.io/documentation/stable/install.html

If using pip to download, run `python3 -m pip install networkx`


Files:
- `parse.py`: functions to read/write inputs and outputs
- `solver.py`: where you should be writing your code to solve inputs
- `utils.py`: contains functions to compute cost and validate NetworkX graphs

When writing inputs/outputs:
- Make sure you use the functions `write_input_file` and `write_output_file` provided
- Run the functions `read_input_file` and `read_output_file` to validate your files before submitting!
  - These are the functions run by the autograder to validate submissions

Algorithm:
- Our algorithm required multiple runs in order to obtain our best leaderboard scores since it incorporates randomness.

How to run:
- First, make sure there exists an outputs/ directory with the following subdirectories:
  - small/
  - medium/
  - large/

- In the code itself, if you would like to run the alternate algorithm which helped to improve our small graph scores, do the following:
  - Uncomment lines 508 and 513 which use the remove_min_cut function
  - Comment lines 507 and 512 which use the min_cut_solve function
  - run the algorithm using the same command below

To run the algorithm, enter the following in the terminal:

```bash
python3 solver.py
```