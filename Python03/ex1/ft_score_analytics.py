import sys


class InvalidParameter(Exception):
    def __init__(self, message: str = "Invalid parameter:") -> None:
        super().__init__(message)


class NonArguments(Exception):
    def __init__(self, message: str = "No scores provided. Usage:") -> None:
        super().__init__(message)


if __name__ == "__main__":

    print("=== Player Score Analytics ===")
    player_len: int = len(sys.argv)
    try:
        if player_len < 1:
            raise NonArguments
    except NonArguments as error:
        print(f"{error} python3 ft_score_analytics.py <score1> <score2> ...\n")
        sys.exit(1)
    new_player_list: list[int] = []
    average_score: float = 0
    total_score: int = 0
    range_score: int = 0

    for argv in sys.argv:
        new_argv: int = 0
        if argv != sys.argv[0]:
            try:
                new_argv = int(argv)
                new_player_list.append(new_argv)
            except ValueError:
                print(f"Invalid parameter: '{argv}'")
    player_len = len(new_player_list)
    try:
        if player_len < 1:
            raise NonArguments
    except NonArguments as error:
        print(f"{error} python3 ft_score_analytics.py <score1> <score2> ...\n")
        sys.exit(1)
    high_score: int = new_player_list[0]
    low_score: int = new_player_list[0]
    for new_score in new_player_list:
        total_score += new_score
        if new_score > high_score:
            high_score = new_score
        if new_score < low_score:
            low_score = new_score
    range_score = high_score - low_score
    average_score = total_score / player_len

    print(f"Score processed: {new_player_list}")
    print(f"Total players: {player_len}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {range_score}\n")
