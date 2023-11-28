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

cot_prompt2 = """Use substitution cipher to solve the following cryptogram. For each step, you are allowed to subsitute only one character from the remaining ones for all occurences in the text.
Input: {input}
Your output should be of the following format.

Alphabet substituted: 
Write which alphabet have you substituted.

Alphabet substituted with: 
Write the alphabet you used for substitution

Output: 
Your output

"""
cot_prompt = """
Use substitution cipher to solve the following cryptogram. For each step, you are allowed to subsitute only one character from the remaining ones for all occurences in the text.

Input: wall wabq wmm

Thoughts:
1. Replace w with b -> b--- b--- b--
2. replace m with e -> b--- b--- bee
3. replace a with u -> bu-- bu-- bee
4. Replace l with z -> buzz bu-- bee
5. replace b with s -> buzz bus- bee
6. replace q with y -> buzz busy bee

Output: buzz busy bee


Input: wghhrx kio ymy

Thoughts:
1. Replace w with s -> s----- --- ---
2. replace g with i -> si---- --- ---
3. replace h with z -> sizz-- --- ---
4. Replace y with p -> sizz-- --- p-p
5. replace m with o -> sizz-- --- pop
6. replace k with a -> sizz-- a-- pop
7. replace i with n -> sizz-- an- pop
8. replace o with d -> sizz-- and pop
9. replace r with l -> sizzl- and pop
10. replace x with e -> sizzle and pop

Output: sizzle and pop


Input: {input}

"""

propose_prompt2 = """
Solving a cryptogram, a type of puzzle that involves decrypting a ciphered text, can be both
challenging and enjoyable. 

Here are some strategies to help you solve a cryptogram:
Start with One-Letter Words: Usually, one-letter words in English are either "I" or "A". This can give you
a starting point.
Look for Common Two-Letter Words: After identifying one-letter words, look for short, common
words. For instance, if you have deciphered "A", then a two-letter word might be "AN", "AS", or "AT".
Identify Repeated Letters: Repeated letters can often indicate common double letters in English,
such as "LL", "SS", "EE", "OO", or "TT".
Use Letter Frequency: In English, some letters appear more frequently than others. For example, 'E',
'T', 'A', 'O', 'I', 'N', 'S', 'H', and 'R' are the most common.
Look for Apostrophes: Words with apostrophes can indicate contractions or possessives, which can
be easier to decode (like “I'S”, “DON'T”).
Recognize Common Word Patterns: English has many common word patterns. For example, the
pattern "_ING" is often used in verbs.
Consider the Context: Sometimes, understanding the theme or context of the cryptogram can
provide clues. For example, a puzzle in a sports magazine might include sports-related terms.
Trial and Error: Sometimes you just need to guess and check. If a word almost makes sense, try
different variations.
Use a Pencil: Since you might need to make changes, it's advisable to work in pencil.
Take Breaks: If you're stuck, take a break and come back later. A fresh perspective can often help.
Use Cryptogram Solving Tools: There are online tools and software that can assist in solving
cryptograms, especially for complex ones.
Remember, the key to solving cryptograms is patience and practice. The more you solve, the more
familiar you'll become with common patterns and tricks used in these puzzles.

Here are five cryptograms along with their solutions and the cipher keys used to create them:
Cryptogram: GBFETKZAK VY LFEKH
Solution: KNOWLEDGE IS POWER
Cipher Key:
A→J, B→S, C→P, D→Z, E→K, F→M, G→A, H→D, I→V, J→O, K→G, L→T, M→C, N→B, O→F, P→L,
Q→N, R→H, S→Y, T→U, U→R, V→W, W→E, X→X, Y→Q, Z→I
Cryptogram: HSYC XNSHM DQR KQ QKC
Solution: TIME WAITS FOR NO ONE
Cipher Key:
A→N, B→E, C→J, D→P, E→C, F→D, G→W, H→V, I→S, J→Z, K→O, L→A, M→Y, N→K, O→Q, P→G,
Q→T, R→R, S→M, T→H, U→F, V→B, W→X, X→I, Y→L, Z→U
Cryptogram: LRZYBIF FSDLW GBEXDC ZHLI JBCXF
Solution: ACTIONS SPEAK LOUDER THAN WORDS
Cipher Key:
A→L, B→P, C→R, D→X, E→D, F→K, G→T, H→H, I→Y, J→M, K→W, L→G, M→A, N→I, O→B, P→S,
Q→Q, R→C, S→F, T→Z, U→E, V→N, W→J, X→V, Y→O, Z→U
Cryptogram: Q NCRPFDI CZ Q OWCRKQFV MUBDK HDEUFK YUOW Q KUFEBD KODA
Solution: A JOURNEY OF A THOUSAND MILES BEGINS WITH A SINGLE STEP
Cipher Key:
A→Q, B→H, C→L, D→V, E→D, F→Z, G→E, H→W, I→U, J→N, K→S, L→B, M→M, N→F, O→C, P→A,
Q→J, R→P, S→K, T→O, U→R, V→G, W→Y, X→X, Y→I, Z→T
Cryptogram: IHL FEQX JDX IF BF RALDI JFAW ZU IF QFTL JHDI XFG BF
Solution: THE ONLY WAY TO DO GREAT WORK IS TO LOVE WHAT YOU DO
Cipher Key:
A→D, B→K, C→N, D→B, E→L, F→C, G→R, H→H, I→Z, J→S, K→W, L→Q, M→M, N→E, O→F, P→Y,
Q→V, R→A, S→U, T→I, U→G, V→T, W→J, X→O, Y→X, Z→P


Can you partially solve the cryptogram by performing steps mentioned above to come up with a
partial solution.
Cipher: {input}
give the output as one partially decrypted sentence
"""

# 1-shot
propose_prompt1 = '''Input: Hgmmxhhdgw cxscwx qhp vxkkxe agxhkysth, qtb qh q exhgwk, kjxf lxk vxkkxe qthrxeh. Kstf Esvvyth.
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

propose_prompt = '''
Solving a cryptogram, a type of puzzle that involves decrypting a ciphered text, can be both challenging and enjoyable. Here are some strategies to help you solve a cryptogram:

Start with One-Letter Words: Usually, one-letter words in English are either "I" or "A". This can give you a starting point.

Look for Common Two-Letter Words: After identifying one-letter words, look for short, common words. For instance, if you have deciphered "A", then a two-letter word might be "AN", "AS", or "AT".

Identify Repeated Letters: Repeated letters can often indicate common double letters in English, such as "LL", "SS", "EE", "OO", or "TT".

Use Letter Frequency: In English, some letters appear more frequently than others. For example, 'E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', and 'R' are the most common.

Look for Apostrophes: Words with apostrophes can indicate contractions or possessives, which can be easier to decode (like “IT’S”, “DON’T”).

Recognize Common Word Patterns: English has many common word patterns. For example, the pattern "_ING" is often used in verbs.

Consider the Context: Sometimes, understanding the theme or context of the cryptogram can provide clues. For example, a puzzle in a sports magazine might include sports-related terms.

Trial and Error: Sometimes you just need to guess and check. If a word almost makes sense, try different variations.

Use a Pencil: Since you might need to make changes, it's advisable to work in pencil.

Take Breaks: If you're stuck, take a break and come back later. A fresh perspective can often help.

Use Cryptogram Solving Tools: There are online tools and software that can assist in solving cryptograms, especially for complex ones.

Remember, the key to solving cryptograms is patience and practice. The more you solve, the more familiar you'll become with common patterns and tricks used in these puzzles.
Here are five cryptograms along with their solutions and the cipher keys used to create them:

Cryptogram: GBFETKZAK VY LFEKH

Solution: KNOWLEDGE IS POWER
Cipher Key:
A→J, B→S, C→P, D→Z, E→K, F→M, G→A, H→D, I→V, J→O, K→G, L→T, M→C, N→B, O→F, P→L, Q→N, R→H, S→Y, T→U, U→R, V→W, W→E, X→X, Y→Q, Z→I
Cryptogram: HSYC XNSHM DQR KQ QKC

Solution: TIME WAITS FOR NO ONE
Cipher Key:
A→N, B→E, C→J, D→P, E→C, F→D, G→W, H→V, I→S, J→Z, K→O, L→A, M→Y, N→K, O→Q, P→G, Q→T, R→R, S→M, T→H, U→F, V→B, W→X, X→I, Y→L, Z→U
Cryptogram: LRZYBIF FSDLW GBEXDC ZHLI JBCXF

Solution: ACTIONS SPEAK LOUDER THAN WORDS
Cipher Key:
A→L, B→P, C→R, D→X, E→D, F→K, G→T, H→H, I→Y, J→M, K→W, L→G, M→A, N→I, O→B, P→S, Q→Q, R→C, S→F, T→Z, U→E, V→N, W→J, X→V, Y→O, Z→U
Cryptogram: Q NCRPFDI CZ Q OWCRKQFV MUBDK HDEUFK YUOW Q KUFEBD KODA

Solution: A JOURNEY OF A THOUSAND MILES BEGINS WITH A SINGLE STEP
Cipher Key:
A→Q, B→H, C→L, D→V, E→D, F→Z, G→E, H→W, I→U, J→N, K→S, L→B, M→M, N→F, O→C, P→A, Q→J, R→P, S→K, T→O, U→R, V→G, W→Y, X→X, Y→I, Z→T
Cryptogram: IHL FEQX JDX IF BF RALDI JFAW ZU IF QFTL JHDI XFG BF

Solution: THE ONLY WAY TO DO GREAT WORK IS TO LOVE WHAT YOU DO
Cipher Key:
A→D, B→K, C→N, D→B, E→L, F→C, G→R, H→H, I→Z, J→S, K→W, L→Q, M→M, N→E, O→F, P→Y, Q→V, R→A, S→U, T→I, U→G, V→T, W→J, X→O, Y→X, Z→P

Can you partially solve the cryptogram by coming up with cipher key to solve cryptogram 
cipher : {input}

In answer just mention Solution and Cipher Key. Do not provide any justification.
'''

# propose_prompt = """
# Use substitution cipher to solve the following cryptogram. For each step, you are allowed to subsitute only one character from the remaining ones for all occurences in the text.
# In this game, some letters of the actual words of the quotes are switched with different letters. All occurrences of a particular letter are substituted with the same letter from the cipher or code. However, the substituted letter might not be used in the puzzle. 

# {input}

# Given the current status, list all the possible replacements of letters and the possible words created 

# """

value_prompt = '''
use evaluation metrics as follows and score all solutions. Evaluation
Coherence:
Does the decrypted text make logical and grammatical sense in the context of the
English language (or the relevant language of the cipher)?
Consistency:
Ensure that the same substitution rule is applied uniformly throughout the message. For
instance, if 'A' in ciphertext translates to 'T' in plaintext, this should be consistent across
the message.
Word Verification:
Check the decrypted words against a dictionary. Are they valid words?
Check Against Known Patterns:
If you know certain words or phrases that might appear in the text (e.g., a salutation or
signature), see if they emerge in the decryption.
Verify Using External Information:
If the content of the message is suspected to relate to a particular topic or event, does
the decrypted text align with that expectation?
Evaluate Completeness:
Ensure the entire message has been addressed and there aren't parts left encrypted.
score the following from 1 to 10:
Original cipher: SXBHMDVND YI QBHDJ, UID YO HYIDML
1. SXBIIMDVNI IS QBSIJ, UIS TO SIISML
2. ETHTNGVNG IN QHTGJ, UNG IT TINGNL
3. SOMOETTET AE SMOTR, RET AO OAETEL
4. SOMOEIIEI DE SMOIA, AEI DO ODEIEL

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

vote_prompt = """
use evaluation metrics as follows and score all solutions. Evaluation
Coherence:
Does the decrypted text make logical and grammatical sense in the context of the
English language (or the relevant language of the cipher)?
Consistency:
Ensure that the same substitution rule is applied uniformly throughout the message. For
instance, if 'A' in ciphertext translates to 'T' in plaintext, this should be consistent across
the message.
Word Verification:
Check the decrypted words against a dictionary. Are they valid words?
Check Against Known Patterns:
If you know certain words or phrases that might appear in the text (e.g., a salutation or
signature), see if they emerge in the decryption.
Verify Using External Information:
If the content of the message is suspected to relate to a particular topic or event, does
the decrypted text align with that expectation?
Evaluate Completeness:
Ensure the entire message has been addressed and there aren't parts left encrypted.
score the following from 1 to 10:

"""

vote_prompt2 = """
Using these numbers conclude which is the best choice and then in the last line write "The best choice is {s}", where s the integer id of the choice.
"""