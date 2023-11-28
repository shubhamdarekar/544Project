# import os
# import openai

# openai.api_type = 'azure'
# openai.api_base = "https://appliednlp-group45.openai.azure.com/"
# openai.api_key = "1846c01198274d9cb46930517d303a93"
# openai.api_version = "2023-05-15"

# print(openai.Model.list())


import argparse
from tot.methods.bfs import solve
from tot.tasks.cryptograph import Cryptograph

args = argparse.Namespace(backend='gpt-35-turbo', temperature=0.7, task='cryptograph', naive_run=False, prompt_sample='cot', method_generate='propose', method_evaluate='vote', method_select='greedy', n_generate_sample=3, n_evaluate_sample=3, n_select_sample=2)

task = Cryptograph("DROBO HGC YXKO EZYX G DSWO G PSCROBWGX VSFOM HSDR RSC HSPO SX G ZSQCDLO KVYCO IL DRO COG GXM OFOBL MGL RO HOXD YED PSCRSXQ GXM RO PSCROM GXM RO PSCROM GXM YXKO RO HGC CSDDSXQ HSDR RSC BYM VYYUSXQ GD DRO KVOGB HGDOB GXM RO CGD GXM RO CGD DROX RSC VSXO CEMMOXVL HOXD MYHX PGB MYHX IOVYH GXM HROX RO MBOH SD EZ GQGSX RO IBYEQRD YED G VGBQO PVYEXMOB")
ys, infos = solve(args, task, 900)
print(ys[0])





