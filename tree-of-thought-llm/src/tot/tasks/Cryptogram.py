import os
import re
import json

from tot.tasks.base import Task, DATA_PATH
from tot.prompts.text import *
from tot.models import gpt

class Cryptogram(Task):

    def __init__(self,file = 'randomCryptoSolved.txt'):
        super.__init__()
        path = os.path.join(DATA_PATH, 'cryptogram', file)

        self.file = json.load(open(path))

    
    def __len__(self) :
        return len(self.file)
    
    def get_input(self, idx: int) -> str:
        return self.file[idx]