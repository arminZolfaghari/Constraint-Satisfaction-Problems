import Heuristic
import Propagation
import Node
import copy
import GameRule


def find_path(node):
    path = ''
    return path

def print_board(node):
    print(f'value {node.assigned_value} assigned to index {node.assigned_variable}\n')
    for i in node.board:
        print(i)
    print('*******************************************')


def create_domains_list(initial_board):
    domains_list = copy.deepcopy(initial_board)
    dimension = len(domains_list)

    for i in range(dimension):
        for j in range(dimension):
            if domains_list[i][j] == '1':
                domains_list[i][j] = '1'
            elif domains_list[i][j] == '0':
                domains_list[i][j] = '0'
            else:
                domains_list[i][j] = ['0', '1']

    return domains_list


# it takes raw input and create basic structures for the program
def start_CSP(input_board, const_prop_mode):

    domains_list = create_domains_list(input_board)
    initial_node = Node.Node(input_board, '', domains_list, '', '')  # initial node does not have parent
    CSP_Backtracking(initial_node, const_prop_mode, 'start')


def CSP_Backtracking(node, const_prop_mode, csp_mode):

    # is_finished = GameRule.check_all_rule_game(node)
    # if is_finished:
    #     print('finish')
    #     print_board(node)
    # else:

    not_empty, node = Heuristic.MRV(node, csp_mode)
    print_board(node)
    if not not_empty:
        # here we should go to parent node
        CSP_Backtracking(node.parent, const_prop_mode, 'continue')
    else:
        if const_prop_mode == 'forward_checking':
            flag, variables_domain = Propagation.forward_checking(node.variables_domain)
            print("!!!!!!!!!!!!!!!!!")
            print(flag)
            print(variables_domain)
            print("!2222222222222222222")
        elif const_prop_mode == 'MAC':
            flag, variables_domain = Propagation.MAC(node)

        if flag:
            # continue solving the puzzle
            print('continue')
            child_node = Node.Node(node.board, node, variables_domain, '', '')
            CSP_Backtracking(child_node, const_prop_mode, 'continue')
        else:
            # new values for assigned_variable should be considered
            print('change last variable value')
            CSP_Backtracking(node, const_prop_mode, 'samevar')