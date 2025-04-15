import csv
import json

# Define the InputHandler class
class InputHandler:
    """
    Processes input data from CSV or JSON files
    """
    def __init__(self, file_path: str):
        """
        Initializes an InputHandler class object
        Parameters:
            self, file_path: str 
        """
        # Store the input file path as a private
        self.__file_path = file_path

    @property
    def file_path(self):
        """
        Get property for the file path
        Parameter:
            self
        Returns:
            str: The path to the input file
        """
        # Return the file path
        return self.__file_path

    def get_file_format(self) -> str:
        """
        Get the format of the input file
        Parameter:
            self
        Returns:
            str: The file format
        """
        # Return the file format from the file path
        return self.__file_path.split('.')[-1]

    def read_input_data(self) -> list:
        """
        Read and return input data from a file
        Parameter:
            self
        Returns:
            list: The input data read from the file
        """
        # Initialize an empty list to store the data
        data = []

        # Get the file format
        file_format = self.get_file_format()

        # Read if CSV or elif json
        if file_format == 'csv':
            data =  self.read_csv_data()
        elif file_format == 'json':
            data = self.read_json_data()

        # Return the read data
        return data

    def read_csv_data(self) -> list:
        """
        Read and return input data from a CSV file
        Parameter:
            self
        Returns:
            list: The input data read from the CSV file

        Raises:
            FileNotFoundError: For specified file does not exist
        """
        # Initialize an empty list to store input data
        input_data = []
        try:

            # Open the file in read mode
            with open(self.__file_path, 'r') as input_file:
                
                # Use DictReader to read the CSV file
                reader = csv.DictReader(input_file)
                
                # Iterate through each row
                for row in reader:
                    
                    # Add each row to the list
                    input_data.append(row)
            
            # Return the input data
            return input_data
        
        # Raise exception for non file
        except FileNotFoundError:
            raise FileNotFoundError(f"File: {self.__file_path} does not exist.")

        

    def read_json_data(self) -> list:
        """
        Read and return input data from a JSON file.
        Parameter:
            self
        Returns:
            list: The input data read from the JSON file.

        Raises:
            FileNotFoundError: For specified file does not exist
        """
        # Research the json.load function so that you 
        # understand the format of the data once it is
        # placed into input_data
        try:

            # Open the file in read mode
            with open(self.__file_path, 'r') as input_file:
                
                # Read the JSON file and store it in input_data
                input_data = json.load(input_file)

            # Return the input data
            return input_data
        
        # Raise exception for non file
        except FileNotFoundError:
            raise FileNotFoundError(f"File: {self.__file_path} does not exist.")
        
    #Milestone 2

    def data_validation(self):
        """
        This function reads the data content
        parameter:
            self
        Return:
            valid transaction
        """
        valid_data = []
        transaction_type = ['withdrawal', 'deposit', 'transfer']
        for value in self.read_input_data():
            try:
                if float(value['Amount']) >= 0 \
                        and value['Transaction type'] in transaction_type:
                    valid_data.append(value)
            except ValueError:
                pass
        return valid_data
