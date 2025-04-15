import csv


class OutputHandler:
    """
    Creates CSV files containing account summaries,
    suspicious transactions, and transaction statistics.
    """

    def __init__(
        self,
        account_summaries: dict,
        suspicious_transactions: list,
        transaction_statistics: dict,
    ) -> None:
        """
        Initializes the OutputHandler object.

        Args:
            account_summaries: A dictionary of account summaries, with account numbers as keys.
            suspicious_transactions: A list of dictionaries representing suspicious transactions.
            transaction_statistics: A dictionary of transaction statistics, keyed by transaction type. 
        """
        self.__account_summaries = account_summaries
        self.__suspicious_transactions = suspicious_transactions
        self.__transaction_statistics = transaction_statistics

    @property
    def account_summaries(self):
        """
        Getter Method for account_summaries
        """
        return self.__account_summaries

    @property
    def suspicious_transactions(self):
        """
        Getter Method for suspicious_transactions
        """
        return self.__suspicious_transactions

    @property
    def transaction_statistics(self):
        """
        Getter for the transaction statistics.
        """
        return self.__transaction_statistics

    def write_account_summaries_to_csv(self, file_path: str) -> None:
        """
        Writes account summaries (balance, deposits, withdrawals) to a CSV file.

        Args:
            file_path: The path to the output CSV file.
        """
        with open(file_path, "w", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerow(
                ["Account number", "Balance", "Total Deposits", "Total Withdrawals"]
            )

            for account_number, summary in self.__account_summaries.items():
                writer.writerow(
                    [
                        account_number,
                        summary["balance"],
                        summary["total_deposits"],
                        summary["total_withdrawals"],
                    ]
                )

    def write_suspicious_transactions_to_csv(self, file_path: str) -> None:
        """
        Writes a list of suspicious transactions to a CSV file.

        Args:
            file_path: The path to the output CSV file.
        """
        with open(file_path, "w", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerow(
                [
                    "Transaction ID",
                    "Account number",
                    "Date",
                    "Transaction type",
                    "Amount",
                    "Currency",
                    "Description",
                ]
            )

            for transaction in self.__suspicious_transactions:
                writer.writerow(
                    [
                        transaction["Transaction ID"],
                        transaction["Account number"],
                        transaction["Date"],
                        transaction["Transaction type"],
                        transaction["Amount"],
                        transaction["Currency"],
                        transaction["Description"],
                    ]
                )

    def write_transaction_statistics_to_csv(self, file_path: str) -> None:
        """
        Writes transaction statistics (by type) to a CSV file.

        Args:
            file_path: The path to the output CSV file.
        """
        with open(file_path, "w", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerow(["Transaction type", "Total amount", "Transaction count"])

            for transaction_type, statistic in self.__transaction_statistics.items():
                writer.writerow(
                    [
                        transaction_type,
                        statistic["total_amount"],
                        statistic["transaction_count"],
                    ]
                )
