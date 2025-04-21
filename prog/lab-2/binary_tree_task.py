from custom_exceptions import NegativeHeightException

Root = 10
Height = 5
left_leaf_func = lambda x:x*3+1
right_leaf_func = lambda x:x*3-1


bin_tree_rec = {}
bin_tree = {}

def generate_tree_rec(tree = {}, root = 1, height = 1, left_leaf = lambda x:x+1, right_leaf = lambda x:x*2):
    
    if height < 0:
        raise NegativeHeightException
    
    left_value = left_leaf(root)
    right_value =  right_leaf(root)
    
    tree[root] = []
    tree[root].append({left_value:[]})
    tree[root].append({right_value:[]})


    height -= 1
    if height > 1:
        for i in range(len(tree[root])):
            generate_tree_rec(tree[root][i],root=list(tree[root][i].keys())[0], height=height, left_leaf=left_leaf_func, right_leaf=right_leaf_func)


def generate_tree(tree = {}, root = 1, height = 1, left_leaf = lambda x:x+1, right_leaf = lambda x:x*2):

    if height < 0:
        raise NegativeHeightException

    tree[root] = []
    node_queue = [tree]
    amount_of_nodes = 0

    for i in range(Height-1):
        amount_of_nodes += 2**i

    for i in range(amount_of_nodes):
        current_node = node_queue.pop(0)    

        for key in list(current_node.keys()):
            left_value = left_leaf(key)
            right_value = right_leaf(key)

            current_node[key].append({left_value:[]})
            current_node[key].append({right_value:[]})

            node_queue.extend(current_node[key])

    return tree