from tabulate import tabulate
import csv
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python program_name.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    data = read_csv_file(filename)
    table_creation(data)


def read_csv_file(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data


def table_creation(data):
    table = tabulate(data, headers="firstrow", tablefmt="latex")
    print(table)


# def osolve_mo_then_uf_hv(self, timeout):
#     uid = 'osolve-mo-then-uf_nana' + str(timeout)
#     data = []
#     for row in self.experiments[uid].rows:
#         before = float(row['hypervolume_before_uf'])
#         after = float(row['hypervolume'])
#         data.append([row['instance'], before, after, after / before * 100.])
#     return data

def graph_creation():
    a = 1
    # plt.ylabel("#Best hypervolumes")
    # campaign.sort_experiments_by_num_best_hv()
    # print([(e.uid, e.uf_solutions, e.uf_conflicts) for e in campaign.experiments.values()])
    # plt.bar(campaign.short_xp_names(), [e.num_best_hv for e in campaign.experiments.values()])
    # # plt.legend()
    # # plt.show()
    #
    # # plt.bar(campaign.short_xp_names(), [e.cumul_time for e in campaign.experiments.values()])
    # plt.xticks(fontsize=8)
    # tikzplotlib.save("../paper/experiments.tex", axis_width="15cm", axis_height="7cm", textsize=8.0)
    #
    # print(tabulate(campaign.osolve_mo_then_uf_hv(timeout_sec), tablefmt="latex", floatfmt=".2f"))


if __name__ == '__main__':
    main()
    print("Finished experiments")
