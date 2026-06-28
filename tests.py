"""Basic tests for the coding puzzle evaluator.

Run with:
    python tests.py
"""

from __future__ import annotations

from checker import evaluate_solution, print_report
from puzzle import highest_even


def incorrect_solution(numbers: list[int]) -> int | None:
    """A deliberately wrong solution to prove the checker catches failures."""
    if not numbers:
        return None
    return max(numbers)


def test_correct_solution() -> None:
    report = evaluate_solution(highest_even)
    assert report["passed"] is True
    assert report["passed_count"] == report["total_count"]


def test_incorrect_solution_fails() -> None:
    report = evaluate_solution(incorrect_solution)
    assert report["passed"] is False
    assert report["passed_count"] < report["total_count"]


if __name__ == "__main__":
    correct_report = evaluate_solution(highest_even)
    print("Checking correct solution")
    print_report(correct_report)

    print("\nChecking deliberately incorrect solution")
    wrong_report = evaluate_solution(incorrect_solution)
    print_report(wrong_report)

    test_correct_solution()
    test_incorrect_solution_fails()
    print("\nAll tests completed successfully.")
