
#!/usr/bin/env python3
import os, re, sys

period_re    = re.compile(r'^\d{2}\.[12]$')
file_re      = re.compile(r'^prova[1-9]\.[^.]+$', re.IGNORECASE)
part_dir_re  = re.compile(r'^prova[1-9]$', re.IGNORECASE)
part_file_re = re.compile(r'^parte[1-9]\.[^.]+$', re.IGNORECASE)

errors = []

for root, dirs, files in os.walk('.'):
    # buscamos somente dentro de pastas "Provas"
    if os.path.basename(os.path.dirname(root)) != 'Provas':
        continue

    # root é algo como "./decom/.../Provas/24.2"
    period = os.path.basename(root)
    if not period_re.match(period):
        errors.append(f"✗ Período inválido: {root}")
        continue

    # agora verificamos cada entry dentro de XX.Y
    for entry in sorted(os.listdir(root)):
        path = os.path.join(root, entry)
        if os.path.isfile(path):
            if not file_re.match(entry):
                errors.append(f"✗ Nome de prova inválido: {path}")
        elif os.path.isdir(path):
            # deve ser uma pasta hein: provaN
            if not part_dir_re.match(entry):
                errors.append(f"✗ Pasta de prova inválida: {path}")
                continue
            # dentro dela, só arquivos parteM.ext
            for sub in sorted(os.listdir(path)):
                subp = os.path.join(path, sub)
                if not os.path.isfile(subp) or not part_file_re.match(sub):
                    errors.append(f"✗ Arquivo dentro de {path} com nome inválido: {subp}")

if errors:
    print("Erros de nomenclatura encontrados:\n")
    for e in errors:
        print(e)
    sys.exit(1)

print("✔ Todas as pastas e arquivos de provas seguem a nomenclatura correta.")
