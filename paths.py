np_paths = {('1', '2'): [['>', 'A']],
            ('1', '3'): [['>', '>', 'A']],
            ('1', '4'): [['^', 'A']],
            ('1', '5'): [['^', '>', 'A'], ['>', '^', 'A']],
            ('1', '6'): [['^', '>', '>', 'A'], ['>', '>', '^', 'A']],
            ('1', '7'): [['^', '^', 'A']],
            ('1', '8'): [['^', '^', '>', 'A'], ['>', '^', '^', 'A']],
            ('1', '9'): [['^', '^', '>', '>', 'A'], ['>', '>', '^', '^', 'A']],
            ('1', '0'): [['>', 'v', 'A']],
            ('1', 'A'): [['>', '>', 'v', 'A']],
            ('2', '1'): [['<', 'A']],
            ('2', '3'): [['>', 'A']],
            ('2', '4'): [['<', '^', 'A']],
            ('2', '5'): [['^', 'A']],
            ('2', '6'): [['^', '>', 'A'], ['>', '^', 'A']],
            ('2', '7'): [['<', '^', '^', 'A']],
            ('2', '8'): [['^', '^', 'A']],
            ('2', '9'): [['^', '^', '>', 'A'], ['>', '^', '^', 'A']],
            ('2', '0'): [['v', 'A']],
            ('2', 'A'): [['v', '>', 'A'], ['>', 'v', 'A']],
            ('3', '1'): [['<', '<', 'A']],
            ('3', '2'): [['<', 'A']],
            ('3', '4'): [['<', '<', '^', 'A']],
            ('3', '5'): [['<', '^', 'A']],
            ('3', '6'): [['^', 'A']],
            ('3', '7'): [['<', '<', '^', '^', 'A']],
            ('3', '8'): [['<', '^', '^', 'A']],
            ('3', '9'): [['^', '^', 'A']],
            ('3', '0'): [['v', '<', 'A'], ['<', 'v', 'A']],
            ('3', 'A'): [['v', 'A']],
            ('4', '1'): [['v', 'A']],
            ('4', '2'): [['v', '>', 'A']],
            ('4', '3'): [['v', '>', '>', 'A'], ['>', '>', 'v', 'A']],
            ('4', '5'): [['>', 'A']],
            ('4', '6'): [['>', '>', 'A']],
            ('4', '7'): [['^', 'A']],
            ('4', '8'): [['^', '>', 'A']],
            ('4', '9'): [['^', '>', '>', 'A'], ['>', '>', '^', 'A']],
            ('4', '0'): [['>', 'v', 'v', 'A']],
            ('4', 'A'): [['>', '>', 'v', 'v', 'A']],
            ('5', '1'): [['v', '<', 'A'], ['<', 'v', 'A']],
            ('5', '2'): [['v', 'A']],
            ('5', '3'): [['v', '>', 'A']],
            ('5', '4'): [['<', 'A']],
            ('5', '6'): [['>', 'A']],
            ('5', '7'): [['<', '^', 'A']],
            ('5', '8'): [['^', 'A']],
            ('5', '9'): [['^', '>', 'A'], ['>', '^', 'A']],
            ('5', '0'): [['v', 'v', 'A']],
            ('5', 'A'): [['v', 'v', '>', 'A'], ['>', 'v', 'v', 'A']],
            ('6', '1'): [['v', '<', '<', 'A'], ['<', '<', 'v', 'A']],
            ('6', '2'): [['v', '<', 'A'], ['<', 'v', 'A']],
            ('6', '3'): [['v', 'A']],
            ('6', '4'): [['<', '<', 'A']],
            ('6', '5'): [['<', 'A']],
            ('6', '7'): [['<', '<', '^', 'A']],
            ('6', '8'): [['<', '^', 'A']],
            ('6', '9'): [['^', 'A']],
            ('6', '0'): [['v', 'v', '<', 'A'], ['<', 'v', 'v', 'A']],
            ('6', 'A'): [['v', 'v', 'A']],
            ('7', '1'): [['v', 'v', 'A']],
            ('7', '2'): [['v', 'v', '>', 'A'], ['>', 'v', 'v', 'A']],
            ('7', '3'): [['v', 'v', '>', '>', 'A']],
            ('7', '4'): [['v', 'A']],
            ('7', '5'): [['v', '>', 'A']],
            ('7', '6'): [['v', '>', '>', 'A'], ['>', '>', 'v', 'A']],
            ('7', '8'): [['>', 'A']],
            ('7', '9'): [['>', '>', 'A']],
            ('7', '0'): [['>', 'v', 'v', 'v', 'A']],
            ('7', 'A'): [['>', '>', 'v', 'v', 'v', 'A']],
            ('8', '1'): [['v', 'v', '<', 'A'], ['<', 'v', 'v', 'A']],
            ('8', '2'): [['v', 'v', 'A']],
            ('8', '3'): [['v', 'v', '>', 'A'], ['>', 'v', 'v', 'A']],
            ('8', '4'): [['v', '<', 'A'], ['<', 'v', 'A']],
            ('8', '5'): [['v', 'A']],
            ('8', '6'): [['v', '>', 'A']],
            ('8', '7'): [['<', 'A']],
            ('8', '9'): [['>', 'A']],
            ('8', '0'): [['v', 'v', 'v', 'A']],
            ('8', 'A'): [['v', 'v', 'v', '>', 'A'], ['>', 'v', 'v', 'v', 'A']],
            ('9', '1'): [['v', 'v', '<', '<', 'A'], ['<', '<', 'v', 'v', 'A']],
            ('9', '2'): [['v', 'v', '<', 'A'], ['<', 'v', 'v', 'A']],
            ('9', '3'): [['v', 'v', 'A']],
            ('9', '4'): [['v', '<', '<', 'A'], ['<', '<', 'v', 'A']],
            ('9', '5'): [['v', '<', 'A'], ['<', 'v', 'A']],
            ('9', '6'): [['v', 'A']],
            ('9', '7'): [['<', '<', 'A']],
            ('9', '8'): [['<', 'A']],
            ('9', '0'): [['v', 'v', 'v', '<', 'A'], ['<', 'v', 'v', 'v', 'A']],
            ('9', 'A'): [['v', 'v', 'v', 'A']],
            ('0', '1'): [['^', '<', 'A']],
            ('0', '2'): [['^', 'A']],
            ('0', '3'): [['^', '>', 'A'], ['>', '^', 'A']],
            ('0', '4'): [['^', '^', '<', 'A']],
            ('0', '5'): [['^', '^', 'A']],
            ('0', '6'): [['^', '^', '>', 'A'], ['>', '^', '^', 'A']],
            ('0', '7'): [['^', '^', '^', '<', 'A']],
            ('0', '8'): [['^', '^', '^', 'A']],
            ('0', '9'): [['^', '^', '^', '>', 'A'], ['>', '^', '^', '^', 'A']],
            ('0', 'A'): [['>', 'A']],
            ('A', '1'): [['^', '<', '<', 'A']],
            ('A', '2'): [['<', '^', 'A']],
            ('A', '3'): [['^', 'A']],
            ('A', '4'): [['^', '^', '<', '<', 'A']],
            ('A', '5'): [['<', '^', '^', 'A']],
            ('A', '6'): [['^', '^', 'A']],
            ('A', '7'): [['^', '^', '^', '<', '<', 'A']],
            ('A', '8'): [['<', '^', '^', '^', 'A']],
            ('A', '9'): [['^', '^', '^', 'A']],
            ('A', '0'): [['<', 'A']]}

kp_paths = {('<', '<'): ['A'],
            ('<', '>'): ['A', '>', '>', 'A'],
            ('<', '^'): ['A', '>', '^', 'A'],
            ('<', 'v'): ['A', '>', 'A'],
            ('<', 'A'): ['A', '>', '>', '^', 'A'],
            ('>', '>'): ['A'],
            ('>', '<'): ['A', '<', '<', 'A'],
            ('>', '^'): ['A', '<', '^', 'A'], # 'A', '^', '<', 'A'
            ('>', 'v'): ['A', '<', 'A'],
            ('>', 'A'): ['A', '^', 'A'],
            ('^', '^'): ['A'],
            ('^', '<'): ['A', 'v', '<', 'A'],
            ('^', '>'): ['A', 'v', '>', 'A'], # 'A', '>', 'v', 'A'
            ('^', 'v'): ['A', 'v', 'A'],
            ('^', 'A'): ['A', '>', 'A'],
            ('v', 'v'): ['A'],
            ('v', '<'): ['A', '<', 'A'],
            ('v', '>'): ['A', '>', 'A'],
            ('v', '^'): ['A', '^', 'A'],
            ('v', 'A'): ['A', '^', '>', 'A'],
            ('A', 'A'): ['A'],
            ('A', '<'): ['A', 'v', '<', '<', 'A'],
            ('A', '>'): ['A', 'v', 'A'],
            ('A', '^'): ['A', '<', 'A'],
            ('A', 'v'): ['A', '<', 'v', 'A']} # 'A', 'v', '<', 'A'
