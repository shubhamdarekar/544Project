# import os
# import openai

# openai.api_type = 'azure'
# openai.api_base = "https://appliednlp-group45.openai.azure.com/"
# openai.api_key = "1846c01198274d9cb46930517d303a93"
# openai.api_version = "2023-05-15"

# print(openai.Model.list())


import argparse
from tot.methods.bfs import solve
from tot.tasks.game24 import Game24Task

args = argparse.Namespace(backend='gpt-35-turbo', temperature=0.7, task='game24', naive_run=False, prompt_sample=None, method_generate='propose', method_evaluate='value', method_select='greedy', n_generate_sample=1, n_evaluate_sample=3, n_select_sample=5)

task = Game24Task()
ys, infos = solve(args, task, 900)
print(ys[0])





