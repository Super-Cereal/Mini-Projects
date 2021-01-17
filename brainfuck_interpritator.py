def refactor(code):
    res = [0]
    i = 0
    mas = []
    cycles = {}  # формат - {начало: конец, конец: начало}
    for sym in code:
        if sym not in '.+-[]<>,':
            continue
        i += 1
        if (sym == '+' and res[-1] == '-') or (sym == '-' and res[-1] == '+'):
            res.pop()
            continue
        elif (sym == '<' and res[-1] == '>') or (sym == '>' and res[-1] == '<'):
            res.pop()
            continue
        elif sym == '[':
            mas.append(i)
        elif sym == ']':
            x = mas.pop()
            cycles[i] = x
            cycles[x] = i
        res.append(sym)
    return res, cycles


def run(code):
    code, cycles = refactor(code)
    cur_cell = index = 0
    brainfuck = {0: 0}
    while index < len(code):
        sym = code[index]
        if sym == '>':
            cur_cell += 1
            brainfuck.setdefault(cur_cell, 0)
        elif sym == '<':
            cur_cell -= 1
        elif sym == '+':
            brainfuck[cur_cell] += 1
        elif sym == '-':
            brainfuck[cur_cell] -= 1
        elif sym == '.':
            print(chr(brainfuck[cur_cell]), end="")
        elif sym == ',':
            brainfuck[cur_cell] = int(input())
        elif sym == '[':
            if not brainfuck[cur_cell]:
                index = cycles[index]
        elif sym == ']':
            if brainfuck[cur_cell]:
                index = cycles[index]
        index += 1


path_to_program = './files/brainfuck_programs/hello_world.bf'
code = open(path_to_program).read()
run(code)
