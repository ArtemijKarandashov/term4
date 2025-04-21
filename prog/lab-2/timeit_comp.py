import timeit
from binary_tree_task import generate_tree, generate_tree_rec

class TimerContext:
    def __init__(self):
        self.time = 0

    def __enter__(self):
        self.start = timeit.default_timer()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = timeit.default_timer()
        self.time = self.end - self.start


def run_both(root,height):
    bin_tree = {}
    bin_tree_rec = {}

    time = 0
    time_rec = 0

    with TimerContext() as timer:
        generate_tree(tree = bin_tree,height=height,root=root)
    print(f"generate_tree({height}): {timer.time}")
    time = timer.time

    with TimerContext() as timer:
        generate_tree_rec(tree = bin_tree_rec,height=height,root=root)
    print(f"generate_tree_rec({height}): {timer.time}")
    time_rec = timer.time

    print(f"generate_tree({height}) - generate_tree_rec({height}): {time - time_rec}")
    return time, time_rec


if __name__ == '__main__':
    run_both(1,15)