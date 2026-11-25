import re,sys
src=open('check-resolution/.context/check-resolution-ubiquitous-language.md',encoding='utf-8').read()
out=[]
section=None
blocks=re.split(r'\n(?=## |# )',src)
groups={'Core Domain':[], 'Boundary Domain':[]}
cur=None
for b in blocks:
    if b.startswith('# Core Domain'): cur='Core Domain'; continue
    if b.startswith('# Boundary Domain'): cur='Boundary Domain'; continue
    if not b.startswith('## ') or cur is None: continue
    lines=b.split('\n')
    term=lines[0][3:].strip()
    owned=None; bullets=[]; sources=[]; mode=None
    for l in lines[1:]:
        if l.startswith('Owned by:'): owned=l.split(':',1)[1].strip()
        elif l.startswith('### Ubiquitous'): mode='ul'
        elif l.startswith('### References'): mode='ref'
        elif mode=='ul' and (l.startswith('- ') or l.startswith('  ')) and l.strip(): bullets.append(l.rstrip())
        elif mode=='ref' and l.startswith('Source:'):
            s=l.split(':',1)[1].strip()
            if s not in sources: sources.append(s)
    t=[f'### {term}','']
    if owned: t.append(f'- Owned by: {owned}')
    t+=bullets
    if sources: t.append('- Sources: '+', '.join(f'`{s}`' for s in sources))
    groups[cur].append('\n'.join(t))
paras={'Core Domain':"*Core Domain* — The d20 resolution mechanic this module owns: a trait's rank plus a d20 roll and modifiers measured against a Difficulty Class, the check variants (routine, opposed, resistance, team), degrees of success and failure, ranks and measures, hero points, extra effort and power stunts, the basic and combined conditions a character can suffer, reactions, and the people at the table (Gamemaster, player characters, non-player characters).",
'Boundary Domain':"*Boundary Domain* — Terms this module uses but other modules own: the power effect a character resists, the character that holds traits and conditions, power points, complications, advantages and the action round."}
res=['## Language','']
for g in ['Core Domain','Boundary Domain']:
    res.append(paras[g]); res.append('')
    for t in groups[g]: res.append(t); res.append('')
open(sys.argv[1],'w',encoding='utf-8').write('\n'.join(res))
print(sum(len(v) for v in groups.values()))
