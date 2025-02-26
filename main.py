from utils.problem_factory import get_solution, get_tests


def run_solution(difficulty, problem, *args):
    solution = get_solution(difficulty, problem)
    func = getattr(solution, 'twoSum')
    result = func(*args)
    return result


def run_test_cases(difficulty, problem):
    test = get_tests(difficulty, problem)
    test.run_tests()


if __name__ == "__main__":
    print(run_test_cases('easy', 'two_sum'))
