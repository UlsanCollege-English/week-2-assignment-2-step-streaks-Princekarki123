from typing import List, Tuple, Optional


def max_window_sum(values: List[int], k: int) -> Optional[Tuple[int, int]]:
    """Return (start_index, window_sum) of the largest sum among all length-k windows.

    If k <= 0, raise ValueError. If k > len(values), return None.
    """
    n = len(values)
    if k <= 0:
        raise ValueError("k must be positive")
    if k > n:
        return None

    # initial window
    window_sum = sum(values[:k])
    max_sum = window_sum
    max_index = 0

    # slide window
    for i in range(k, n):
        window_sum += values[i] - values[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
            max_index = i - k + 1

    return (max_index, max_sum)


def count_goal_windows(values: List[int], k: int, target_avg: float) -> int:
    """Return how many length-k windows have average >= target_avg.

    If k <= 0, raise ValueError. If k > len(values), return 0.
    """
    n = len(values)
    if k <= 0:
        raise ValueError("k must be positive")
    if k > n:
        return 0

    target_sum = target_avg * k
    count = 0

    # initial window
    window_sum = sum(values[:k])
    if window_sum >= target_sum:
        count += 1

    # slide window
    for i in range(k, n):
        window_sum += values[i] - values[i - k]
        if window_sum >= target_sum:
            count += 1

    return count


def longest_rising_streak(values: List[int]) -> int:
    """Return the length of the longest strictly increasing consecutive streak.

    Empty list -> 0. Single element -> 1.
    """
    if not values:
        return 0

    longest = 1
    current = 1

    for i in range(1, len(values)):
        if values[i] > values[i - 1]:
            current += 1
            longest = max(longest, current)
        else:
            current = 1

    return longest
