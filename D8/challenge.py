with open('input') as f:
    chal_input = {i: (op, int(v)) for i, (op, v) in enumerate([l.rstrip().split(' ') for l in f.readlines()])}

class Loop(Exception): pass

def check_memo(f):
    def wrapper(self):
        op, v = self.next_op
        if self.op_pointer in self.history:
            raise Loop
        self.history.add(self.op_pointer)
        return f(self, op, v)
    return wrapper

class HGC:
    def __init__(self, istructions):
        self.istructions = istructions
        self.op_pointer = 0
        self.history = set([])
        self.acc = 0
    
    @property
    def next_op(self):
        return self.istructions[self.op_pointer]

    @check_memo
    def op_exec(self, op, v):
        if op == 'jmp':
            self.op_pointer += v
            return
        elif op == 'acc':
            self.acc += v
        self.op_pointer += 1

    def run(self, check_loop=True):
        while True:
            if check_loop:
                try: self.op_exec()
                except Loop: break
            else: self.op_exec()
        return self.acc
        
    def fix(self):
        jmp_nop = [(i, op, v) for i, (op, v) in self.istructions.items() if op in ['jmp', 'nop']]

        for i, op, v in jmp_nop:
            curr_istructions = self.istructions.copy()
            curr_istructions[i] = ('jmp' if op == 'nop' else 'nop', v)
            try:
                curr_hgc = HGC(curr_istructions)
                curr_hgc.run(False)
            except Loop: continue
            except KeyError: return curr_hgc.acc

hgc = HGC(chal_input)

print('Part 1:', hgc.run())
print('Part 2:', hgc.fix())