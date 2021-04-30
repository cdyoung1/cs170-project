# import sys
# import os
# import json
# from parse import validate_file

# if __name__ == '__main__':
#     outputs_dir = sys.argv[1]
#     submission_name = sys.argv[2]
#     submission = {}
#     print(outputs_dir)
#     for input_path in os.listdir("outputs/small/"):
#         print(input_path)
#         graph_name = input_path.split('.')[0]
#         output_file = f'{outputs_dir}{graph_name}.out'
#         print("Graph Name:", graph_name, "Output_file:", output_file)
#         if os.path.exists(output_file) and validate_file(output_file):
#             output = open(f'{outputs_dir}/{graph_name}.out').read()
#             submission[input_path] = output
#     with open(submission_name, 'w+') as f:
#         f.write(json.dumps(submission))

# old 

# import sys
# import os
# import json
# from parse import validate_file

# if __name__ == '__main__':
#     outputs_dir = sys.argv[1]
#     submission_name = sys.argv[2]
#     submission = {}
#     for input_path in os.listdir("inputs"):
#         graph_name = input_path.split('.')[0]
#         output_file = f'{outputs_dir}/{graph_name}.out'
#         if os.path.exists(output_file) and validate_file(output_file):
#             output = open(f'{outputs_dir}/{graph_name}.out').read()
#             submission[input_path] = output
#     with open(submission_name, 'w') as f:
#         f.write(json.dumps(submission))


import sys
import os
import json
from parse import validate_file

if __name__ == '__main__':
    outputs_dir = "outputs"
    submission_name = "submission.json"
    submission = {}
    size = ["small", "medium", "large"]
    for s in size:
        for input_path in os.listdir(f"inputs/{s}"):
            graph_name = input_path.split('.')[0]
            output_file = f'{outputs_dir}/{s}/{graph_name}.out'
            if os.path.exists(output_file) and validate_file(output_file):
                output = open(f'{outputs_dir}/{s}/{graph_name}.out').read()
                submission[input_path] = output
    with open(submission_name, 'w') as f:
        f.write(json.dumps(submission))