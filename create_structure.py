
#!/usr/bin/env python3
# create_structure.py

import os
import sys

def parse_disciplinas(txt_path):
    """Lê o arquivo e retorna uma lista de blocos (código, nome, [professores])."""
    with open(txt_path, encoding='utf-8') as f:
        content = f.read()
    blocks = [b.strip() for b in content.split('\n\n') if b.strip()]
    disciplinas = []
    for block in blocks:
        lines = block.splitlines()
        código = lines[0].strip()
        nome = ''
        profs = []
        for l in lines[1:]:
            if l.startswith('--'):
                profs.append(l.lstrip('-').strip())
            elif l.startswith('-'):
                nome = l.lstrip('-').strip()
        disciplinas.append((código, nome, profs))
    return disciplinas

def categoria_para(código):
    """Retorna o nome da pasta de categoria a partir do código."""
    low = código.lower()
    if 'bcc' in low:
        return 'decom'
    elif 'mtm' in low:
        return 'demat'
    else:
        return 'outras'

def main():
    txt = 'disciplinas.txt'
    if not os.path.isfile(txt):
        print(f"Erro: não encontrei '{txt}' no diretório atual.", file=sys.stderr)
        sys.exit(1)

    # Cria pastas de categorias
    categorias = {'decom', 'demat', 'outras'}
    for cat in categorias:
        os.makedirs(cat, exist_ok=True)

    for código, nome, profs in parse_disciplinas(txt):
        cat = categoria_para(código)
        # nome da pasta da disciplina
        pasta_disc = f"{código} - {nome}" if nome else código
        path_disc = os.path.join(cat, pasta_disc)
        os.makedirs(path_disc, exist_ok=True)

        if profs:
            # Para cada professor, cria Provas e Material
            for prof in profs:
                path_prof = os.path.join(path_disc, prof)
                os.makedirs(path_prof, exist_ok=True)
                os.makedirs(os.path.join(path_prof, 'Provas'), exist_ok=True)
                os.makedirs(os.path.join(path_prof, 'Material'), exist_ok=True)
        else:
            # Se não houver professor listado, cria direto em disciplina
            os.makedirs(os.path.join(path_disc, 'Provas'), exist_ok=True)
            os.makedirs(os.path.join(path_disc, 'Material'), exist_ok=True)

    print("✅ Estrutura de pastas criada com sucesso.")

if __name__ == '__main__':
    main()
