import pandas as pd


def print_title(message="Page Title", length = 100):
    # Create a perfect 80-character width frame
    MAX_CHARACTER_LENGTH = length
    padding_length = MAX_CHARACTER_LENGTH - len(message) - 14  # Subtracting 2 accounts for the edge '*' borders

    # Split padding evenly between left and right sides
    left_pad = padding_length // 2
    right_pad = padding_length - left_pad

    print("*" * MAX_CHARACTER_LENGTH)
    print(f"******{' ' * left_pad} {message} {' ' * right_pad}******")
    print("*" * MAX_CHARACTER_LENGTH)


def format_data_to_dataframe(data):
    result_df = pd.DataFrame(data)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    print(result_df)


# print_title("Accuracy > 90%")
