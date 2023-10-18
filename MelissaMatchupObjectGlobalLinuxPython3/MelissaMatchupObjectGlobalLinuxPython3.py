import mdMatchup_pythoncode
import os
import sys
import re


class DataContainer:
    def __init__(self, input_file_path_1="",  input_file_path_2="", output_file_path_1="", output_file_path_2="", result_codes=[]):
        self.input_file_path_1 = input_file_path_1
        self.input_file_path_2 = input_file_path_2
        self.output_file_path_1 = output_file_path_1
        self.output_file_path_2 = output_file_path_2
        self.result_codes = result_codes

    def format_output_files(self):
        location_1 = self.input_file_path_1.find(".txt")
        location_2 = self.input_file_path_2.find(".txt")
        self.output_file_path_1 = self.input_file_path_1[:location_1] + "_output.txt"
        self.output_file_path_2 = self.input_file_path_2[:location_2] + "_output.txt"

    def get_wrapped(self, path, max_line_length):
        file = os.path.abspath(path)
        file_parts = file.split(os.sep)
        
        current_line = ""
        wrapped_strings = []

        for section in file_parts:
            if len(current_line + section) > max_line_length:
                wrapped_strings.append(current_line.strip())
                current_line = ""

            if section == file:
                current_line += section
            else:
                current_line += section + os.sep

        if len(current_line) > 0:
            wrapped_strings.append(current_line.strip())

        return wrapped_strings


class MatchUpObjectGlobal:
    """ Set license string and set path to data files  (.dat, etc) """
    def __init__(self, license, data_path):
        self.data_path = data_path
        
        # self.md_read_write = mdMatchup_pythoncode.mdMatchup_pythoncode.mdMUReadWrite()

        self.md_matchup_obj = mdMatchup_pythoncode.mdMUReadWrite()
        self.md_matchup_obj.SetLicenseString(license)
        self.md_matchup_obj.SetPathToMatchUpFiles(data_path)
        self.md_matchup_obj.SetKeyFile("temp.key")
        self.md_matchup_obj.SetMatchcodeName("Global Address")
        self.md_matchup_obj.SetMaximumCharacterSize(1)
        

        """
        If you see a different date than expected, check your license string and either download the new data files or use the Melissa Updater program to update your data files.  
        """
        
        p_status = self.md_matchup_obj.InitializeDataFiles()
        if (p_status != mdMatchup_pythoncode.ProgramStatus.ErrorNone):
            print("Failed to Initialize Object.")
            print(p_status)
            return
        
        print(f"                DataBase Date: {self.md_matchup_obj.GetDatabaseDate()}")
        print(f"              Expiration Date: {self.md_matchup_obj.GetLicenseExpirationDate()}")
      
        """
        This number should match with file properties of the Melissa Object binary file.
        If TEST appears with the build number, there may be a license key issue.
        """
        print(f"               Object Version: {self.md_matchup_obj.GetBuildNumber()}\n")
    

    def execute_object_and_result_codes(self, input_file_path, output_file_path):
        
        total = 0
        dupes = 0

        # Establish field mappings: when you change the matchcode, you will change these
        self.md_matchup_obj.ClearMappings()

        if (
            self.md_matchup_obj.AddMapping(mdMatchup_pythoncode.MatchcodeMapping.Country) == 0
            or self.md_matchup_obj.AddMapping(mdMatchup_pythoncode.MatchcodeMapping.Address) == 0
            or self.md_matchup_obj.AddMapping(mdMatchup_pythoncode.MatchcodeMapping.Address) == 0
            or self.md_matchup_obj.AddMapping(mdMatchup_pythoncode.MatchcodeMapping.Address) == 0
            or self.md_matchup_obj.AddMapping(mdMatchup_pythoncode.MatchcodeMapping.Address) == 0
        ):
            print("\nError: Incorrect AddMapping() parameter")
            sys.exit(1)

        # Process the sample data file
        
        try:
            with open(input_file_path, 'r', encoding='utf-8') as in_file, open(output_file_path, 'w', encoding='utf-8') as out_file:
                record = in_file.readline()
                while (record := in_file.readline().strip()):
                    # Read and parse '|' delimited record
                    fields = record.split('|')

                    # Load up the fields
                    self.md_matchup_obj.ClearFields()
                    self.md_matchup_obj.AddField(fields[7])
                    self.md_matchup_obj.AddField(fields[3])
                    self.md_matchup_obj.AddField(fields[4])
                    self.md_matchup_obj.AddField(fields[5])
                    self.md_matchup_obj.AddField(fields[6])

                    # Create a UserInfo string which uniquely identifies the records
                    self.md_matchup_obj.SetUserInfo(fields[0])

                    # Build the key and submit it
                    self.md_matchup_obj.BuildKey()
                    self.md_matchup_obj.WriteRecord()

                self.md_matchup_obj.Process()

                # Prepare and write the output header to the output file
                header = "Id|ResultCodes|DupeGroup|Key"
                out_file.write(header + '\n')

                while self.md_matchup_obj.ReadRecord() != 0:
                    if "MS03" in self.md_matchup_obj.GetResults():
                        dupes += 1

                    self.md_matchup_obj.ClearFields()

                    # Prepare and write the output line to the output file
                    arr = [
                        self.md_matchup_obj.GetUserInfo(),
                        self.md_matchup_obj.GetResults(),
                        str(self.md_matchup_obj.GetDupeGroup()),
                        re.sub(r'\s+', ' ', self.md_matchup_obj.GetKey())
                    ]
                    line = '|'.join(arr)
                    out_file.write(line + '\n')

                    total += 1

        except Exception as ex:
            print(ex)

        # ResultsCodes explain any issues MatchUp Object has with the object.
        # List of result codes for MatchUp Object
        # https://wiki.melissadata.com/index.php?title=Result_Code_Details#MatchUp_Object

        


def parse_arguments():
    license, test_us_file, test_global_file, data_path = "", "", "", ""

    args = sys.argv
    index = 0
    for arg in args:
        
        if (arg == "--license") or (arg == "-l"):
            if (args[index+1] != None):
                license = args[index+1]
        if (arg == "--global") or (arg == "-g"):
            if (args[index+1] != None):
                test_global_file = args[index+1]
        if (arg == "--us") or (arg == "-u"):
            if (args[index+1] != None):
                test_us_file = args[index+1]
        if (arg == "--dataPath") or (arg == "-d"):
            if (args[index+1] != None):
                data_path = args[index+1]
        index += 1

    return (license, test_us_file, test_global_file, data_path)

def run_as_console(license, test_us_file, test_global_file, data_path):
    print("\n\n============== WELCOME TO MELISSA MATCHUP OBJECT GLOBAL LINUX PYTHON3 ================\n")

    matchup_object = MatchUpObjectGlobal(license, data_path)

    should_continue_running = True

    if matchup_object.md_matchup_obj.GetInitializeErrorString() != "No Error":
      should_continue_running = False
      
    while should_continue_running:
        if (test_us_file == None or test_us_file == "") or (test_global_file == None or test_global_file == ""):        
          print("\nFill in each value to see the MatchUp Object Global results")
          input_file_path_1 = str(input("Global Input File: "))
          input_file_path_2 = str(input("US Input File: "))
        else:        
          input_file_path_1 = test_us_file
          input_file_path_2 = test_global_file
        
        data_container = DataContainer(input_file_path_1, input_file_path_2)

        """ Print user input """
        print("\n======================================= INPUTS =======================================\n")
        sections = data_container.get_wrapped(data_container.input_file_path_1, 50)

        print(f"\t        Global Input File: {sections[0]}")

        for i in range(1, len(sections)):
            if i == len(sections) - 1 and sections[i].endswith("/"):
                sections[i] = sections[i][:-1]
            print(f"\t                           {sections[i]}")

        sections = data_container.get_wrapped(data_container.input_file_path_2, 50)

        print(f"\t            US Input File: {sections[0]}")

        for i in range(1, len(sections)):
            if i == len(sections) - 1 and sections[i].endswith("/"):
                sections[i] = sections[i][:-1]
            print(f"\t                           {sections[i]}")

        data_container.format_output_files()

        # Execute MatchUp Object Global
        matchup_object.execute_object_and_result_codes(input_file_path_1, data_container.output_file_path_1)
        matchup_object.execute_object_and_result_codes(input_file_path_2, data_container.output_file_path_2)

        # Print output
        print("\n======================================= OUTPUT =======================================\n")

        
        sections1 = data_container.get_wrapped(data_container.input_file_path_1, 50)

        print("\n  MatchUp Object Global Information:")
        print(f"\t       Global Output File: {sections1[0]}")

        for i in range(1, len(sections1)):
            if i == len(sections1) - 1 and sections1[i].endswith("/"):
                sections1[i] = sections1[i][:-1]
            print(f"\t                           {sections1[i]}")

        sections2 = data_container.get_wrapped(data_container.input_file_path_2, 50)

        print(f"\t           US Output File: {sections2[0]}")

        for i in range(1, len(sections2)):
            if i == len(sections2) - 1 and sections2[i].endswith("/"):
                sections2[i] = sections2[i][:-1]
            print(f"\t                           {sections2[i]}")



        is_valid = False
        if not ((test_us_file == None or test_us_file == "") and (test_global_file == None or test_global_file == "")):
            is_valid = True
            should_continue_running = False    
        while not is_valid:
        
            test_another_response = input(str("\nTest another file? (Y/N)\n"))
            

            if not (test_another_response == None or test_another_response == ""):         
                test_another_response = test_another_response.lower()
            if test_another_response == "y":
                is_valid = True
            
            elif test_another_response == "n":
                is_valid = True
                should_continue_running = False            
            else:
            
              print("Invalid Response, please respond 'Y' or 'N'")

    print("\n======================= THANK YOU FOR USING MELISSA PYTHON OBJECT ====================\n")
    


"""  MAIN STARTS HERE   """

license, test_us_file, test_global_file, data_path = parse_arguments()

run_as_console(license, test_us_file, test_global_file, data_path)