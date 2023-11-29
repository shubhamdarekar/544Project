import os
import re
import json

from tot.tasks.base import Task, DATA_PATH
from tot.prompts.cryptograph import *
from tot.models import gpt

class Cryptograph(Task):

    def __init__(self, text:str):
        # super.__init__()
        self.input_text = text
        self.steps = 2
        self.stops = ['\n'] * 4

    def _len_(self):
        return len(self.input_text)
    
    def get_input(self, idx=1):
        return self.input_text
    
    @staticmethod
    def cot_prompt_wrap(x: str, y:str='') -> str:
        print("cot prompt wrap x", x)
        print("cot prompt wrap y", y)
        return cot_prompt.format(input=x) + y
    
    @staticmethod
    def vote_prompt_wrap(x: str, ys: list) -> str:
        print("x in vote_prompt", x)
        print("ys in vote prompt", ys)
        prompt = vote_prompt.format(input = x)
        for i, y in enumerate(ys, 1):
            # y = y.replace('Plan:\n', '')
            # TODO: truncate the plan part?
            prompt += f'Choice {i}:\n{y}\n'
        return prompt + vote_prompt2
    
    
    def propose_prompt_wrap(self,x: str, y: str='') -> str:
        return propose_prompt.format(input=self.input_text)

    @staticmethod
    def vote_outputs_unwrap(vote_outputs: list, n_candidates: int) -> list:
        vote_results = [0] * n_candidates
        for vote_output in vote_outputs:
            pattern = r".*best choice is .*(\d+).*"
            match = re.match(pattern, vote_output, re.DOTALL)
            if match:
                vote = int(match.groups()[0]) - 1
                if vote in range(n_candidates):
                    vote_results[vote] += 1
            else:
                print(f'vote no match: {[vote_output]}')
        return vote_results