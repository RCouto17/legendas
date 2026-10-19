#!/usr/bin/env python3
"""
copia_srt_para_txt.py

Copia todos os arquivos .srt de 'ingles/' e 'crunchyroll/' para .txt,
mantendo o mesmo nome-base. O conteúdo é copiado sem alteração
(apenas a extensão muda de .srt para .txt).

Uso:
    python3 copia_srt_para_txt.py

Saída:
    ingles/*.txt
    crunchyroll/*.txt
"""

import shutil
from pathlib import Path

# Diretórios de origem (relativos ao script)
DIRETORIOS = ["ingles", "crunchyroll"]

def copiar_srt_para_txt(diretorio: str) -> tuple[int, int]:
    """Copia todos os .srt de um diretório para .txt.
    Retorna (copiados, ignorados)."""
    base = Path(diretorio)
    if not base.is_dir():
        print(f"[AVISO] Diretório não encontrado: {diretorio}")
        return 0, 0

    copiados = 0
    ignorados = 0

    for srt in sorted(base.glob("*.srt")):
        txt = srt.with_suffix(".txt")

        if txt.exists():
            print(f"[PULAR] Já existe: {txt}")
            ignorados += 1
            continue

        shutil.copy2(srt, txt)  # copia conteúdo + metadados
        print(f"[OK] {srt.name} -> {txt.name}")
        copiados += 1

    return copiados, ignorados


def main() -> None:
    total_copiados = 0
    total_ignorados = 0

    for d in DIRETORIOS:
        print(f"\n=== Processando: {d}/ ===")
        c, i = copiar_srt_para_txt(d)
        total_copiados += c
        total_ignorados += i

    print("\n=== Resumo ===")
    print(f"Copiados:  {total_copiados}")
    print(f"Pulados:   {total_ignorados}")


if __name__ == "__main__":
    main()