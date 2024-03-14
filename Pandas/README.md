# Project Name

This is a project that utilizes the Pandas library and Faker library for data generation and saving it to a CSV file.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-project.git
    ```

2. Install the required dependencies:

    ```bash
    pip install pandas faker
    ```

## Usage

1. Generate data using Faker and save it to a CSV file:

    ```python
    import pandas as pd
    from faker import Faker

    fake = Faker()

    # Generate data
    data = []
    for _ in range(10):
         name = fake.name()
         email = fake.email()
         phone = fake.phone_number()
         data.append([name, email, phone])

    # Create a DataFrame
    df = pd.DataFrame(data, columns=['Name', 'Email', 'Phone'])

    # Save DataFrame to a CSV file
    df.to_csv('data.csv', index=False)
    ```

2. Run the script:

    ```bash
    python script.py
    ```

## Contributing

Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).