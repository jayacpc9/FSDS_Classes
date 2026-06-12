import pandas as pd
import numpy as np
def imputation_student_type_a():
    # 1. Recreate the shuffled dataset
    data = {
        'Student Name': ['Student 1', 'Student 2', 'Student 9', 'Student 4', 'Student 5', 'Student 6', 'Student 7', 'Student 8', 'Student 3', 'Student 10'],
        'Age': [6, 7, 14, 9, 10, 11, 12, 13, '*', 15]
    }
    df = pd.DataFrame(data)
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    print(df)

    # 2. Sort by the ID column to reconstruct the true linear progression
    # We extract the number from the string to ensure proper numeric sorting (1, 2, 3... instead of alphabetical 1, 10, 2)
    df['sort_idx'] = df['Student Name'].str.extract(r'(\d+)').astype(int)
    df = df.sort_values('sort_idx').drop(columns='sort_idx')
    print(df)

    # 3. Interpolate sequentially
    df['Age'] = df['Age'].interpolate(method='linear').astype(int)
    print(df)




def imputation_student_type_b():
    # 1. Create the dataset
    data = {
        'Student Name': ['Andy', 'Bob', 'Bobby', 'Chuck', 'Sam', 'joe', 'Albert', 'Yoko', 'Yana', 'zack'],
        'Age': [6, 7, 14, 9, 10, 11, 12, 13, '*', 15]
    }
    df = pd.DataFrame(data)

    # 2. Clean Text Consistency (Standardize names to Title Case)
    df['Student Name'] = df['Student Name'].str.title()

    # 3. Coerce special character '*' to NaN
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

    # 4. Interpolate based on row position context
    df['Age'] = df['Age'].interpolate(method='linear').astype(int)

    print(df)


def imputation_student_type_c():
    # In this method we get the list of all the ages and then get the second list containing all the required ages.
    # subtract them to get the missing ages and that will be the age of Yana.
    # This will work only in the case where we know exactly that there is 1 value that is repeating.
    #
    import pandas as pd
    import numpy as np

    # The shuffled dataset
    data = {
        'Student Name': ['Andy', 'Bob', 'Bobby', 'Chuck', 'Sam', 'Joe', 'Albert', 'Yoko', 'Yana', 'Zack'],
        'Age': [6, 7, 14, 9, 10, 11, 12, 13, '*', 15]
    }
    df = pd.DataFrame(data)
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

    # Expert Fix: Find the gap in the expected sequence range
    min_age = int(df['Age'].min())
    max_age = int(df['Age'].max())

    # Create the full expected set of ages (6 to 15)
    expected_ages = set(range(min_age, max_age + 1))
    print(expected_ages)
    current_ages = set(df['Age'].dropna().astype(int))

    # Find what is missing globally
    missing_values = list(expected_ages - current_ages)

    # If there's a clear systematic gap, use it to fill the NaN
    if len(missing_values) == 1:
        df['Age'] = df['Age'].fillna(missing_values[0]).astype(int)

    print(df)

# imputation_student_type_a()
# imputation_student_type_b()
imputation_student_type_c()

