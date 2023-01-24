from typing import List, Tuple


def save_nonotuple_to_file(
    r_and_c: Tuple[List[List[int]], List[List[int]]], file: str
) -> None:
    """Saving a number of black pixels from rows and columns to a file"""
    with open(file, "w", encoding="utf-8") as nono:
        nono.write(f"{len(r_and_c[0])} {len(r_and_c[1])}\n")
        for r_c in r_and_c:
            for line in r_c:
                if len(line) == 0:
                    nono.write("0")
                for numb in line:
                    nono.write(f"{numb} ")
                nono.write("\n")
