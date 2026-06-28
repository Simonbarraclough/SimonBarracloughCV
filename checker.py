"""Solution checker for the example coding puzzle.

This module shows how a submitted function can be evaluated against a set of
known test cases. It is deliberately simple and readable for portfolio use.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class TestCase:
    """A single test case for a puzzle solution."""

    numbers: list[int]
    expected: int | None


TEST_CASES = [
    TestCase(numbers=[1, 2, 3, 4], expected=4),
    TestCase(numbers=[9, 7, 5], expected=None),
    TestCase(numbers=[-4, -2, -9], expected=-2),
    TestCase(numbers=[0, 1, 3], expected=0),
    TestCase(numbers=[100, 42, 99, 18], expected=100),
    TestCase(numbers=[], expected=None),
]


def evaluate_solution(solution: Callable[[list[int]], Any]) -> dict[str, Any]:
    """Evaluate a submitted solution function.

    Args:
        solution: A function that accepts a list of integers and returns the
            highest even integer, or None if no even integer exists.

    Returns:
        A dictionary containing pass/fail status and details for each case.
    """
    results = []

    for case in TEST_CASES:
        try:
            actual = solution(case.numbers.copy())
            passed = actual == case.expected
            error = None
        except Exception as exc:  # pragma: no cover - useful for submitted code
            actual = None
            passed = False
            error = f"{type(exc).__name__}: {exc}"

        results.append(
            {
                "input": case.numbers,
                "expected": case.expected,
                "actual": actual,
                "passed": passed,
                "error": error,
            }
        )

    passed_count = sum(1 for result in results if result["passed"])

    return {
        "passed": passed_count == len(TEST_CASES),
        "passed_count": passed_count,
        "total_count": len(TEST_CASES),
        "results": results,
    }


def print_report(report: dict[str, Any]) -> None:
    """Print a readable evaluation report."""
    status = "PASS" if report["passed"] else "FAIL"
    print(f"Overall result: {status}")
    print(f"Passed {report['passed_count']} of {report['total_count']} tests")

    for index, result in enumerate(report["results"], start=1):
        case_status = "PASS" if result["passed"] else "FAIL"
        print(
            f"Test {index}: {case_status} | "
            f"input={result['input']} | "
            f"expected={result['expected']} | "
            f"actual={result['actual']}"
        )
        if result["error"]:
            print(f"  Error: {result['error']}")
