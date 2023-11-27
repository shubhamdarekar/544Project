# 5-shot
standard_prompt = '''Use substitution cipher to solve the following cryptogram
Input: Zh gl uclez ni zh gl bnispxlcizhhx. Cemjf Lblcihp.
Answer: To be great is to be misunderstood. Ralph Emerson.
Input: Hgmmxhhdgw cxscwx qhp vxkkxe agxhkysth, qtb qh q exhgwk, kjxf lxk vxkkxe qthrxeh. Kstf Esvvyth.
Answer: Successful people ask better questions, and as a result, they get better answers. Tony Robbins.
Input: Mbulvn jvisfg yudvqjdi vns msba ug nqoojdsii. Osqbf Wryx.
Answer: Growth itself contains the germ of happiness. Pearl Buck.
Input: Aqwabbaswa lg cx fx z wxnnxs crlsm ls zs tswxnnxs pzv.
Answer: Excellence is to do a common thing in an uncommon way.
Input: Vhvlr wlaybvt omi m cxuj ual raz xe xji omegi. Lxdomlg Ymdo.
Answer: Every problem has a gift for you in its hands. Richard Bach.
Input: {input}
'''

# 5-shot
cot_prompt1 = '''Use substitution cipher to solve the following cryptogram. For each step, you are allowed to subsitute only one character from the remaining ones for all occurences in the text.
Input: Zh gl uclez ni zh gl bnispxlcizhhx. Cemjf Lblcihp.
Steps:
1. Replace z with t => Th gl uclet ni th gl bnispxlcithhx. Cemjf Lblcihp. (remaining characters: 'c', 'g', 'x', 'u', 'e', 'j', 'm', 's', 'f', 'n', 'h', 'p', 'b', 'l', 'i')
2. Replace h with o => To gl uclet ni to gl bnispxlcitoox. Cemjf Lblciop. (remaining characters: 'c', 'g', 'x', 'u', 'e', 'j', 'm', 's', 'f', 'n', 'p', 'b', 'l', 'i')
3. Replace g with b => To bl uclet ni to bl bnispxlcitoox. Cemjf Lblciop. (remaining characters: 'c', 'x', 'u', 'e', 'j', 'm', 's', 'f', 'n', 'p', 'b', 'l', 'i')
4. Replace l with e => To be uceet ni to be bnispxecitoox. Cemjf ebeciop. (remaining characters: 'c', 'x', 'u', 'e', 'j', 'm', 's', 'f', 'n', 'p', 'b', 'i')
5. Replace u with g => To be gceet ni to be bnispxecitoox. Cemjf ebeciop. (remaining characters: 'c', 'x', 'e', 'j', 'm', 's', 'f', 'n', 'p', 'b', 'i')
6. Replace c with r => To be greet ni to be bnispxeritoox. Remjf eberiop. (remaining characters: 'x', 'e', 'j', 'm', 's', 'f', 'n', 'p', 'b', 'i')
7. Replace e with a => To be great ni to be bnispxeritoox. Ramjf eberiop. (remaining characters: 'x', 'j', 'm', 's', 'f', 'n', 'p', 'b', 'i')
8. Replace n with i => To be great ii to be biispxeritoox. Ramjf eberiop. (remaining characters: 'x', 'j', 'm', 's', 'f', 'p', 'b', 'i')
9. Replace i with s => To be great is to be bisspxerstoox. Ramjf ebersop. (remaining characters: 'x', 'j', 'm', 's', 'f', 'p', 'b')
10. Replace b with m => To be great is to be misspxerstoox. Ramjf emersop. (remaining characters: 'x', 'j', 'm', 's', 'f', 'p')
11. Replace s with u => To be great is to be misupxerstoox. Ramjf emersop. (remaining characters: 'x', 'j', 'm', 'f', 'p')
12. Replace p with n => To be great is to be misunxerstoox. Ramjf emerson. (remaining characters: 'x', 'j', 'm', 'f')
13. Replace x with d => To be great is to be misunderstood. Ramjf emerson. (remaining characters: 'j', 'm', 'f')
14. Replace m with l => To be great is to be misunderstood. Raljf emerson. (remaining characters: 'j', 'f')
15. Replace j with p => To be great is to be misunderstood. Ralpf emerson. (remaining characters: 'f')
16. Replace f with h => To be great is to be misunderstood. Ralph emerson.  (remaining characters: )
Answer: To be great is to be misunderstood. Ralph emerson.
Input: {input}
'''

cot_prompt = """Use substitution cipher to solve the following cryptogram. For each step, you are allowed to subsitute only one character from the remaining ones for all occurences in the text.
Input: {input}
Your output should be of the following format.

Alphabet substituted: 
Write which alphabet have you substituted.

Alphabet substituted with: 
Write the alphabet you used for substitution

Output: 
Your output

"""

# 1-shot
propose_prompt = '''Input: Hgmmxhhdgw cxscwx qhp vxkkxe agxhkysth, qtb qh q exhgwk, kjxf lxk vxkkxe qthrxeh. Kstf Esvvyth.
Possible next steps:
1. Replace h with s => s____ss___ ______ _s_ ______ ___s____s, ___ _s _ __s___, ____ ___ ______ __s___s. ____ ______s.
2. Replace h with z => z____zz___ ______ _z_ ______ ___z____z, ___ _z _ __z___, ____ ___ ______ __z___z. ____ ______z.
3. Replace h with o => o____oo___ ______ _o_ ______ ___o____o, ___ _o _ __o___, ____ ___ ______ __o___o. ____ ______o.
4. Replace g with u => _u______u_ ______ ___ ______ _u_______, ___ __ _ ___u__, ____ ___ ______ _______. ____ _______.
5. Replace x with e => ____e_____ _e___e ___ _e__e_ __e______, ___ __ _ _e____, __e_ _e_ _e__e_ ____e__. ____ _______.
6. Replace w with l => _________l ____l_ ___ ______ _________, ___ __ _ ____l_, ____ ___ ______ _______. ____ _______.
Input: {input}
Possible next steps:
'''

value_prompt = '''Evaluate if the following character sequence forms any possible words or meaning(sure/likely/impossible)
Hgmmxhhdgw cxscwx qhp vxkkxe agxhkysth, qtb qh q exhgwk, kjxf lxk vxkkxe qthrxeh. Kstf Esvvyth
Replace h with s => output becomes s____ss___ ______ _s_ ______ ___s____s, ___ _s _ __s___, ____ ___ ______ __s___s. ____ ______s., 
possible words: _s_ can be ask; s____ss___ can be successful; _s can be is, as, us
likely
Hgmmxhhdgw cxscwx qhp vxkkxe agxhkysth, qtb qh q exhgwk, kjxf lxk vxkkxe qthrxeh. Kstf Esvvyth
Replace h with z => output becomes z____zz___ ______ _z_ ______ ___z____z, ___ _z _ __z___, ____ ___ ______ __z___z. ____ ______z. 
which makes no sense as there is no word starting with z having 'zz' in between
impossible
Hgmmxhhdgw cxscwx qhp vxkkxe agxhkysth, qtb qh q exhgwk, kjxf lxk vxkkxe qthrxeh. Kstf Esvvyth
h is replaced with s, Replace g with u => su___ss_u_ ______ _s_ ______ _u_s____s, ___ _s _ __su__, ____ ___ ______ __s___s. ____ ______s., 
possible words:  su___ss_u_ is successful for sure, hence replacing m with c, x with e, d with f, w with l to match the letters in successful
sure
'''

value_last_step_prompt = '''Evaluate if the following character sequence forms any possible words or meaning(sure/likely/impossible)
Hgmmxhhdgw cxscwx qhp vxkkxe agxhkysth, qtb qh q exhgwk, kjxf lxk vxkkxe qthrxeh. Kstf Esvvyth
Replace h with s => output becomes s____ss___ ______ _s_ ______ ___s____s, ___ _s _ __s___, ____ ___ ______ __s___s. ____ ______s., possible words: _s_ can be ask; s____ss___ can be successful; _s can be is, as, us
likely
Hgmmxhhdgw cxscwx qhp vxkkxe agxhkysth, qtb qh q exhgwk, kjxf lxk vxkkxe qthrxeh. Kstf Esvvyth
Replace h with z => output becomes z____zz___ ______ _z_ ______ ___z____z, ___ _z _ __z___, ____ ___ ______ __z___z. ____ ______z. which makes no sense as there is no word starting with z having 'zz' in between
impossible
Hgmmxhhdgw cxscwx qhp vxkkxe agxhkysth, qtb qh q exhgwk, kjxf lxk vxkkxe qthrxeh. Kstf Esvvyth
h is replaced with s, Replace g with u => su___ss_u_ ______ _s_ ______ _u_s____s, ___ _s _ __su__, ____ ___ ______ __s___s. ____ ______s., possible words:  su___ss_u_ is successful for sure, hence replacing m with c, x with e, d with f, w with l to match the letters in successful
sure
'''

vote_prompt = ""