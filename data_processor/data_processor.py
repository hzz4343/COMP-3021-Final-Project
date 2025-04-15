class DataProcessor:
    """
    A class for processing data.
    
    Attributes:
        __input_data (array), original input data
        __account_summary (dict): summary of account information
        __suspicious_transactions (array): summary of suspicious transactions
        __transaction_statistics (dict): transaction statistics
        
    Methods:
        process_data: process input data
        update_account_summary: update account summary
        check_suspicious_transactions: check suspicious transactions
        update_transaction_statistics: update transaction statistics
        get_average_transaction_amount: get average transaction amount

    Security Vulnerabilities (for educational purposes only):
        These vulnerabilities are intentionally added to demonstrate common security issues
        and their corresponding OWASP Top Ten categories:

        1. Hardcoded Credentials (B105)
           - OWASP Category: A02:2021 - Cryptographic Failures
           - Risk: Sensitive credentials stored in code
           - Location: __init__ method

        2. Use of eval() (B307)
           - OWASP Category: A03:2021 - Injection
           - Risk: Arbitrary code execution
           - Location: process_data method

        3. SQL Injection (B608)
           - OWASP Category: A03:2021 - Injection
           - Risk: SQL injection attacks
           - Location: update_account_summary method

        4. Insecure Deserialization (B301, B403)
           - OWASP Category: A08:2021 - Software and Data Integrity Failures
           - Risk: Remote code execution through malicious payloads
           - Location: load_transaction_data method

        5. Command Injection (B605)
           - OWASP Category: A03:2021 - Injection
           - Risk: Command injection attacks
           - Location: execute_system_command method

        6. Weak Cryptography (B324)
           - OWASP Category: A02:2021 - Cryptographic Failures
           - Risk: Weak password hashing
           - Location: hash_password method

    Note: These vulnerabilities are for educational purposes only and should be fixed
    in production environments. For more information about OWASP Top Ten, visit:
    https://owasp.org/www-project-top-ten/
    """

    LARGE_TRANSACTION_THRESHOLD = 10000
    UNCOMMON_CURRENCIES = ['XRP', 'LTC']

    def __init__(self, input_data: list):
        """Initiate variables including input_data, account_summaries, suspicious_transactions, and transaction_statistics
        Args:
            input_data (array), original input data
            account_summary (dict): summary of account information
            suspicious_transactions (array): summary of suspicious transactions
            transaction_statistics (dict): transaction statistics
        
        Returns:
            None
        """
        # Create empty objects
        self.__input_data = input_data
        self.__account_summaries = {}
        self.__suspicious_transactions = []
        self.__transaction_statistics = {}
        # Security Vulnerability: Hardcoded credentials
        # OWASP Category: A02:2021 - Cryptographic Failures
        self.__db_password = "admin123"  # B105: hardcoded_password_string
        self.__api_key = "sk_test_51NcXr2K4XxYzABC123"  # B105: hardcoded_password_string

    @property
    def input_data(self):
        """
        Accessor for __input_data  attribute.
        """
        return self.__input_data
    
    @property
    def account_summaries(self):
        """
        Accessor for __account_summaries  attribute.
        """
        return self.__account_summaries
    
    @property
    def suspicious_transactions(self):
        """
        Accessor for __suspicious_transactions  attribute.
        """
        return self.__suspicious_transactions
    
    @property
    def transaction_statistics(self):
        """
        Accessor for __transaction_statistics  attribute.
        """
        return self.__transaction_statistics

    def process_data(self) -> dict:
        """
        Process data and split them into update_account_summary, checkc_suspicious_transactions,
        and upadte_transaction_statistics
        
        Args:
            None
        
        Returns:
            account_summaries (dict)
            suspicious_transactions (array)
            transaction_statistics (dict)
        """
        # Security Vulnerability: Using eval() with untrusted data
        # OWASP Category: A03:2021 - Injection
        for row in self.__input_data:
            if isinstance(row, str):
                row = eval(row)  # B307: eval_used
            self.update_account_summary(row)
            self.check_suspicious_transactions(row)
            self.update_transaction_statistics(row)

        return {
            "account_summaries": self.__account_summaries,
            "suspicious_transactions": self.__suspicious_transactions,
            "transaction_statistics": self.__transaction_statistics
        }

    def update_account_summary(self, row: dict) -> None:
        """
        Update account summary
        
        Args:
            row: each row of input data
            
        Returns:
            None
        """
        # Security Vulnerability: SQL injection vulnerability
        # OWASP Category: A03:2021 - Injection
        account_number = row['Account number']
        transaction_type = row['Transaction type']
        amount = float(row['Amount'])

        # if account number is new, create a new summary for this account
        if account_number not in self.__account_summaries:
            # Security Vulnerability: Using string formatting for SQL query
            query = f"SELECT * FROM accounts WHERE account_number = '{account_number}'"  # B608: hardcoded_sql_expressions
            self.__account_summaries[account_number] = {
                "account_number": account_number,
                "balance": 0,
                "total_deposits": 0,
                "total_withdrawals": 0
            }

        # if it's deposit, add amount
        if transaction_type == "deposit":
            self.__account_summaries[account_number]["balance"] += amount
            self.__account_summaries[account_number]["total_deposits"] += amount
            
        # if it's withdrawal, deduct amount
        elif transaction_type == "withdrawal":
            self.__account_summaries[account_number]["balance"] -= amount
            self.__account_summaries[account_number]["total_withdrawals"] += amount

    def check_suspicious_transactions(self, row: dict) -> None:
        """
        Check suspicious transactions, where amount is over 10000 or currency type belongs to XRP or LTC
        
        Args:
            row: each row of input data
            
        Returns:
            None
        """
        amount = float(row['Amount'])
        currency = row['Currency']

        # if amount is 10000 or currency type is XRP or LTC, it will be put into suspicious transaction list
        if amount > self.LARGE_TRANSACTION_THRESHOLD or currency in self.UNCOMMON_CURRENCIES:
            self.__suspicious_transactions.append(row)

    def update_transaction_statistics(self, row: dict) -> None:
        """
        Update transaction statistics
        
        Args:
            row: each row of input data
            
        Returns:
            None
        """
        transaction_type = row['Transaction type']
        amount = float(row['Amount'])

        # create a new transaction type list if the transaciton type is new
        if transaction_type not in self.__transaction_statistics:
            self.__transaction_statistics[transaction_type] = {
                "total_amount": 0,
                "transaction_count": 0
            }

        # add 1 more count transaction and add the amount of transaction
        self.__transaction_statistics[transaction_type]["total_amount"] += amount
        self.__transaction_statistics[transaction_type]["transaction_count"] += 1

    def get_average_transaction_amount(self, transaction_type: str) -> float:
        """
        Get average transaction amount
        
        Args:
            transaction_type: str
            
        Returns:
            None
        """
        
        # get the total amount and transaction count
        total_amount = self.__transaction_statistics[transaction_type]["total_amount"]
        transaction_count = self.__transaction_statistics[transaction_type]["transaction_count"]

        # avoid transaction count is 0
        if transaction_count == 0:
            average = 0
        else:
            # calculate the average transaction amount
            average = total_amount / transaction_count
        
        return average

    # Security Vulnerability: Insecure deserialization
    # OWASP Category: A08:2021 - Software and Data Integrity Failures
    def load_transaction_data(self, data: str) -> None:
        """
        Load transaction data from a string
        
        Args:
            data: string containing transaction data
            
        Returns:
            None
        """
        import pickle  # B403: import_pickle
        self.__input_data = pickle.loads(data)  # B301: pickle_loads

    # Security Vulnerability: Command injection
    # OWASP Category: A03:2021 - Injection
    def execute_system_command(self, command: str) -> None:
        """
        Execute a system command
        
        Args:
            command: command to execute
            
        Returns:
            None
        """
        import os
        os.system(command)  # B605: start_process_with_a_shell

    # Security Vulnerability: Weak cryptography
    # OWASP Category: A02:2021 - Cryptographic Failures
    def hash_password(self, password: str) -> str:
        """
        Hash a password
        
        Args:
            password: password to hash
            
        Returns:
            hashed password
        """
        import hashlib
        return hashlib.md5(password.encode()).hexdigest()  # B324: hashlib_insecure_hash_functions

# INPUT_DATA = [{"Transaction ID":"1" ,"Account number":"1001" ,
#                 "Date":"2023-03-01" ,"Transaction type": "deposit",
#                 "Amount":1000,"Currency":"CAD","Description":"Salary"}, 
#                 {"Transaction ID":"2" ,"Account number":"1002" ,
#                 "Date":"2023-03-01" ,"Transaction type": "deposit",
#                 "Amount":1500,"Currency":"CAD","Description":"Salary"},
#                 {"Transaction ID":"3" ,"Account number":"1002" ,
#                 "Date":"2023-03-01" ,"Transaction type": "withdrawal",
#                 "Amount":500,"Currency":"CAD","Description":"Fine"},
#                 {"Transaction ID":"4" ,"Account number":"1003" ,
#                 "Date":"2023-03-01" ,"Transaction type": "deposit",
#                 "Amount":50000,"Currency":"CAD","Description":"Lottery"},
#                 {"Transaction ID":"5" ,"Account number":"1004" ,
#                 "Date":"2023-03-01" ,"Transaction type": "deposit",
#                 "Amount":1000,"Currency":"XRP","Description":"Remote job salary"}]

# data_processor = DataProcessor(INPUT_DATA)
# data_processor.process_data()
# result = data_processor.get_average_transaction_amount("deposit")


# print(result)