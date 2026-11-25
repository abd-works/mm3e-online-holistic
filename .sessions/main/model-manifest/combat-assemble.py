d = '.sessions/main/model-manifest/'
lang = open(d + 'combat-language.md', encoding='utf-8').read().rstrip() + "\n\n"
bnd = open(d + 'combat-boundary.md', encoding='utf-8').read().rstrip() + "\n\n"
cls = open(d + 'combat-classes.md', encoding='utf-8').read()
open('combat/.context/combat-model.md', 'w', encoding='utf-8').write(lang + bnd + cls)
