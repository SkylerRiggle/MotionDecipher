from math import log2
from os import listdir
from os.path import isdir, join
from matplotlib import pyplot as plt


class TestDatum:
    __target_result: str
    __num_candidates: int
    __is_success: bool

    def __init__(self, target_result: str, candidates: list[str]):
        self.__target_result = target_result
        self.__num_candidates = len(candidates)

        for candidate in candidates:
            if candidate.strip() == target_result:
                self.__is_success = True
                return

        self.__is_success = False

    def get_target(self) -> str:
        return self.__target_result

    def is_success(self) -> bool:
        return self.__is_success

    def get_num_candidates(self) -> int:
        return self.__num_candidates

    def calculate_entropy(self) -> float:
        return log2(self.__num_candidates)

def gather_test_data(output_dir: str) -> list[TestDatum]:
    if not isdir(output_dir):
        return []

    test_data = []
    for in_file in listdir(output_dir):
        if not in_file.endswith(".txt"):
            continue

        case_file = open(join(output_dir, in_file), "r")
        candidate_list = case_file.readlines()

        if len(candidate_list) == 0:
            case_file.close()
            continue

        candidate_list.pop()
        case_file.close()

        test_data.append(TestDatum(
            target_result = in_file.replace(".txt", "").strip(),
            candidates = candidate_list
        ))

    return test_data

def calculate_gini_coefficient(entropies: list[float], num_digits: int) -> float:
    entropy_diff: float = 0.0
    entropy_sum: float = 0.0
    for entropy_i in entropies:
        entropy_sum += entropy_i

        for entropy_j in entropies:
            entropy_diff += abs(entropy_i - entropy_j)

    if entropy_sum == 0.0:
        return 0.0

    return entropy_diff / (entropy_sum * 2 * 10**num_digits)

def main(output_dir: str = "./output"):
    test_data = gather_test_data(output_dir)

    fail_cases = []
    success_cases = []

    for datum in test_data:
        if datum.is_success():
            success_cases.append(datum)
        else:
            fail_cases.append(datum)
            print(f"Failure Case: {datum.get_target()}")

    num_success = len(success_cases)
    num_fail = len(fail_cases)

    print(f"\nFound {num_success} pins successfully")
    print(f"Unable to infer {num_fail} pins")
    print(f"Overall success rate of: {100.0 * num_success / (num_success + num_fail)}%\n")

    success_count = [case.get_num_candidates() for case in success_cases]
    fail_count = [case.get_num_candidates() for case in fail_cases]
    success_entropy = [case.calculate_entropy() for case in success_cases]
    fail_entropy = [case.calculate_entropy() for case in fail_cases]

    success_count.sort()
    fail_count.sort()
    success_entropy.sort()
    fail_entropy.sort()

    print(f"""Successful Cases Gini Coefficient: {
        calculate_gini_coefficient(success_entropy, len(success_cases[0].get_target()))
    }""")
    print(f"""Failure Cases Gini Coefficient: {
        calculate_gini_coefficient(fail_entropy, len(fail_cases[0].get_target()))
    }""")

    plt.title("Candidate List Size")
    plt.ylabel("Number of Candidates")
    plt.xlabel("Test Video Index")
    plt.bar([idx for idx in range(1, num_success + 1)], success_count)
    plt.show()

    plt.title("Failure Cases Candidate List Size")
    plt.ylabel("Number of Candidates")
    plt.xlabel("Test Video Index")
    plt.bar([idx for idx in range(1, num_fail + 1)], fail_count)
    plt.show()

    plt.title("Entropy")
    plt.ylabel("Entropy")
    plt.xlabel("Test Video Index")
    plt.bar([idx for idx in range(1, num_success + 1)], success_entropy)
    plt.show()

    plt.title("Failure Cases Entropy")
    plt.ylabel("Entropy")
    plt.xlabel("Test Video Index")
    plt.bar([idx for idx in range(1, num_fail + 1)], fail_entropy)
    plt.show()

if __name__ == '__main__':
    main()