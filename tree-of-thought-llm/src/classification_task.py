from tot.prompts.classification import *
from tot.models import gpt
import re
import numpy
import pandas as pd


total_prompts_generated = 3
categories = 3

def wrap_problem(input_problem):
    return input_prompt.format(input=input_problem)

def unwrap_output(outputs):
    vote_results = [0] * categories
    for vote in outputs:
        pattern = r".*The problem belongs to category .*(\d+).*" 
        match = re.match(pattern, vote, re.DOTALL)
        if match:
            vote = int(match.groups()[0]) - 1
            if vote in range(categories):
                vote_results[vote] += 1
        else:
            print(f'vote no match: {[vote]}')
    return vote_results

def call_gpt(value_prompt):
    outputs = gpt(value_prompt, n=total_prompts_generated, stop=None)
    
    return unwrap_output(outputs)


def identify_category(votes):
    dict_categories = {1:"Math problems",2: "Cipher problems",3: "Literature problems"}

    cat_index = numpy.array(votes).argmax()+1

    print("The problem belongs to ", dict_categories[cat_index])

    return cat_index


def categorize(input_problem):
    wrapped = wrap_problem(input_problem)

    votes = call_gpt(wrapped)

    category = identify_category(votes)

    return category


problem = "Create a 5-paragraph essay on a given topic: Spring break"

print(problem)
categorize(problem)

dataset = pd.read_csv("tree-of-thought-llm\DifferentWordProblems.csv")

total = len(dataset)
correct = 0

for index in range(total):
    res = categorize(dataset['Problem'][index])
    if res == dataset['Category'][index]:
        correct+=1

print("Accuracy",correct/total*100)