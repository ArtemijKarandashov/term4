from timeit_comp import run_both
import random

def setup_data(amount):
    data = []
    min_height = 1
    max_height = 15
    min_root = 1
    max_root = 100
    for i in range(amount):
        data.append((random.randint(min_root, max_root), random.randint(min_height, max_height)))
    return data

def main():
    recursive_tree_data = []
    linear_tree_data = []

    amount = 100
    data = setup_data(amount)
    for i in range(amount):
        time, rec_time = run_both(data[i][0], data[i][1])
        print(f"{data[i][0]} {data[i][1]}: {time} {rec_time}")
        recursive_tree_data.append(rec_time)
        linear_tree_data.append(time)
    build_plot(recursive_tree_data,linear_tree_data)


def build_plot(rec, lin):
    import matplotlib.pyplot as plt
    
    plt.plot(rec, color='r', label='recursive')
    plt.plot(lin, color='g', label='linear')

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()