from dpll import DPLL
def __select_literal(cnf):
    for c in cnf:
        for literal in c:
            return literal[0]

def dpll(cnf, assignments={}):

    if len(cnf) == 0:
        return True, assignments

    if any([len(c)==0 for c in cnf]):
        return False, None

    l = __select_literal(cnf)

    new_cnf = [c for c in cnf if (l, True) not in c]
    new_cnf = [c.difference({(l, False)}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: True}})
    if sat:
        return sat, vals

    new_cnf = [c for c in cnf if (l, False) not in c]
    new_cnf = [c.difference({(l, True)}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: False}})
    if sat:
        return sat, vals

    return False, None

def main():
    solver = DPLL()
    # DIMACS_9x9/sudoku_9x9_nr_288.cnf
    solver.read_dimacs('DIMACS_9x9/sudoku_9x9_nr_278.cnf')
    cnf = []
    for clause in solver.cnf:
        new_clause = set()
        for literal in clause:
            literal = (abs(literal), literal > 0)
            new_clause.add(literal)
        cnf.append(new_clause)
    print(cnf)
    satisfaction, assignments = dpll(cnf)

    print(satisfaction, len(assignments))
if __name__ == '__main__':
    main()