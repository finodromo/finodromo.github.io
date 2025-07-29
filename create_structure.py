
#!/usr/bin/env python3
# create_structure.py

import os
import sys
import json
import re

def parse_disciplinas(txt_path):
    """Lê o arquivo e retorna lista de (código, nome, [professores])."""
    with open(txt_path, encoding='utf-8') as f:
        content = f.read()
    blocks = [b.strip() for b in content.split('\n\n') if b.strip()]
    disciplinas = []
    for block in blocks:
        lines = block.splitlines()
        codigo = lines[0].strip()
        nome = ''
        profs = []
        for l in lines[1:]:
            if l.startswith('--'):
                profs.append(l.lstrip('-').strip())
            elif l.startswith('-'):
                nome = l.lstrip('-').strip()
        disciplinas.append((codigo, nome, profs))
    return disciplinas

def categoria_para(codigo):
    """Retorna pasta de categoria a partir do código."""
    low = codigo.lower()
    if 'bcc' in low:
        return 'decom'
    elif 'mtm' in low:
        return 'demat'
    else:
        return 'outras'

def build_structure(root, categorias):
    """
    Varre pastas e monta dict:
      { dept: { 'CÓD - NOME': { 'Prof': { 'periodo': [itens...] } } } }
    Itens de provas somente em subpasta 'Provas'.
    """
    structure = {}
    # período no formato 2 dígitos ponto e pelo menos 1 dígito
    period_pattern = re.compile(r"^\d{2}\.\d+$")

    for cat in categorias:
        cat_path = os.path.join(root, cat)
        if not os.path.isdir(cat_path):
            continue
        structure[cat] = {}
        for disc in sorted(os.listdir(cat_path)):
            disc_path = os.path.join(cat_path, disc)
            if not os.path.isdir(disc_path):
                continue
            structure[cat][disc] = {}
            for prof in sorted(os.listdir(disc_path)):
                prof_path = os.path.join(disc_path, prof)
                provas_path = os.path.join(prof_path, 'Provas')
                if not os.path.isdir(provas_path):
                    # pulamos se não existir a pasta Provas
                    continue

                # DEBUG: veja o que tem em Provas
                print(f"[DEBUG] Em {provas_path} ->", os.listdir(provas_path))

                structure[cat][disc][prof] = {}
                for entry in sorted(os.listdir(provas_path)):
                    period_str = entry.strip()  # REMOVE espaços laterais!
                    period_path = os.path.join(provas_path, entry)
                    if not os.path.isdir(period_path):
                        continue
                    if not period_pattern.match(period_str):
                        print(f"[DEBUG] Ignorando pasta '{entry}' (não bate com período)")
                        continue

                    # DEBUG: veja o conteúdo do período
                    print(f"[DEBUG]   Período {period_str} contém:", os.listdir(period_path))

                    items = []
                    for sub in sorted(os.listdir(period_path)):
                        sub_path = os.path.join(period_path, sub)
                        if os.path.isfile(sub_path):
                            items.append({'type': 'file', 'name': sub})
                        elif os.path.isdir(sub_path):
                            inner = sorted(os.listdir(sub_path))
                            # DEBUG: pastas dentro de prova
                            print(f"[DEBUG]     Pasta de prova '{sub}' contém:", inner)
                            files = [f for f in inner if os.path.isfile(os.path.join(sub_path, f))]
                            items.append({'type': 'folder', 'name': sub, 'files': files})

                    structure[cat][disc][prof][period_str] = items

    return structure

def main():
    txt = 'disciplinas.txt'
    if not os.path.isfile(txt):
        print(f"Erro: não encontrei '{txt}'", file=sys.stderr)
        sys.exit(1)

    categorias = ['decom', 'demat', 'outras']
    # cria as pastas base
    for cat in categorias:
        os.makedirs(cat, exist_ok=True)

    # cria disciplina/professor/Provas e Material
    disciplinas = parse_disciplinas(txt)
    for codigo, nome, profs in disciplinas:
        cat = categoria_para(codigo)
        pasta_disc = f"{codigo} - {nome}" if nome else codigo
        path_disc = os.path.join(cat, pasta_disc)
        os.makedirs(path_disc, exist_ok=True)
        for prof in profs:
            path_prof = os.path.join(path_disc, prof)
            os.makedirs(path_prof, exist_ok=True)
            os.makedirs(os.path.join(path_prof, 'Provas'), exist_ok=True)
            os.makedirs(os.path.join(path_prof, 'Material'), exist_ok=True)

    # gera estrutura
    structure = build_structure(os.getcwd(), categorias)

    # salva JSON e JS
    data_dir = os.path.join(os.getcwd(), 'data')
    os.makedirs(data_dir, exist_ok=True)
    json_path = os.path.join(data_dir, 'structure.json')
    js_path   = os.path.join(data_dir, 'structure.js')
    with open(json_path, 'w', encoding='utf-8') as jf:
        json.dump(structure, jf, ensure_ascii=False, indent=2)
    with open(js_path, 'w', encoding='utf-8') as jsf:
        jsf.write('window.structure = ' + json.dumps(structure, ensure_ascii=False) + ';')

    print("✅ Estrutura de pastas criada e JSON/JS gerados.")

if __name__ == '__main__':
    main()

