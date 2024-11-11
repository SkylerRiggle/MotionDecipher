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

    def calculate_top_k(self, k: int) -> float:
        return k / self.__num_candidates

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

    return entropy_diff / (entropy_sum * 2 * len(entropies))

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

    num_digits = len(fail_cases[0].get_target())

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
        calculate_gini_coefficient(success_entropy, num_digits)
    }""")
    print(f"""Failure Cases Gini Coefficient: {
        calculate_gini_coefficient(fail_entropy, num_digits)
    }""")

    success_indices = [idx for idx in range(1, num_success + 1)]
    fail_indices = [idx for idx in range(1, num_fail + 1)]

    plt.title("Candidate List Size")
    plt.ylabel("Number of Candidates")
    plt.xlabel("Test Video Index")
    plt.bar(success_indices, success_count)
    plt.show()

    plt.title("Failure Cases Candidate List Size")
    plt.ylabel("Number of Candidates")
    plt.xlabel("Test Video Index")
    plt.bar(fail_indices, fail_count)
    plt.show()

    prior_entropy = log2(10**num_digits)

    plt.title("Entropy")
    plt.ylabel("Entropy")
    plt.xlabel("Test Video Index")
    plt.plot(
        [success_indices[0], success_indices[-1]],
        [prior_entropy, prior_entropy],
        label="Entropy /WO Attack",
        color="#ff0000"
    )
    plt.plot(
        success_indices,
        success_entropy,
        label="Entropy /W Attack",
        color="#0000ff"
    )
    plt.legend()
    plt.show()

    plt.title("Failure Cases Entropy")
    plt.ylabel("Entropy")
    plt.xlabel("Test Video Index")
    plt.plot(
        [fail_indices[0], fail_indices[-1]],
        [prior_entropy, prior_entropy],
        label="Entropy /WO Attack",
        color="#ff0000"
    )
    plt.plot(
        fail_indices,
        fail_entropy,
        label="Entropy /W Attack",
        color="#0000ff"
    )
    plt.legend()
    plt.show()

    # top_1_success = [case.calculate_top_k(1) for case in success_cases]
    # top_5_success = [case.calculate_top_k(5) for case in success_cases]
    # top_10_success = [case.calculate_top_k(10) for case in success_cases]
    #
    # top_1_success.sort()
    # top_5_success.sort()
    # top_10_success.sort()
    #
    # top_1_fail = [case.calculate_top_k(1) for case in fail_cases]
    # top_5_fail = [case.calculate_top_k(5) for case in fail_cases]
    # top_10_fail = [case.calculate_top_k(10) for case in fail_cases]
    #
    # top_1_fail.sort()
    # top_5_fail.sort()
    # top_10_fail.sort()
    #
    # plt.title("Top K Accuracy")
    # plt.ylabel("Accuracy")
    # plt.xlabel("Test Video Index")
    # plt.plot(success_indices, top_1_success, label="Top 1", color="#ff0000")
    # plt.plot(success_indices, top_5_success, label="Top 5", color="#00ff00")
    # plt.plot(success_indices, top_10_success, label="Top 10", color="#0000ff")
    # plt.legend()
    # plt.show()
    #
    # plt.title("Failure Top K Accuracy")
    # plt.ylabel("Accuracy")
    # plt.xlabel("Test Video Index")
    # plt.plot(fail_indices, top_1_fail, label="Top 1", color="#ff0000")
    # plt.plot(fail_indices, top_5_fail, label="Top 5", color="#00ff00")
    # plt.plot(fail_indices, top_10_fail, label="Top 10", color="#0000ff")
    # plt.legend()
    # plt.show()

if __name__ == '__main__':
    main("./output/5-Key")