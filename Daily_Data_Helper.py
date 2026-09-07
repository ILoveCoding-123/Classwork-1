class DailyDataHelper:
    # Constructor sets up the object and provides default values
    def __init__(self, dataset_name="General Data", initial_data=None):
        self.dataset_name = dataset_name
        
        # If no initial list is provided, default to an empty list
        if initial_data is None:
            self.data_entries = []
        else:
            self.data_entries = initial_data
            
        print(f"🔄 '{self.dataset_name}' helper initialized with {len(self.data_entries)} entries.")

    # Method using enumerate() to search through the dataset
    def search_value(self, target_value):
        print(f"\n🔍 Searching for '{target_value}' in '{self.dataset_name}':")
        found = False
        
        # enumerate() tracks both the index number and the actual item value
        for index, value in enumerate(self.data_entries, start=1):
            if str(value).lower() == str(target_value).lower():
                print(f"✅ Found! Match at Entry Position #{index}")
                found = True
                
        if not found:
            print(f"❌ '{target_value}' was not found in this dataset.")

    # Method to print all data entries out cleanly
    def display_all_data(self):
        print(f"\n📊 Current Data inside '{self.dataset_name}':")
        if not self.data_entries:
            print(" (Dataset is empty)")
        for index, value in enumerate(self.data_entries, start=1):
            print(f" [{index}] {value}")

    # Destructor function triggered when the object lifecycle ends
    def __del__(self):
        print(f"🛑 Object Destructor called: Cleaning up '{self.dataset_name}' resources.")


# --- Executing Example Test Cases ---
if __name__ == "__main__":
    print("--- Starting Daily Data Helper ---")
    
    # 1. Instantiate the object with custom values
    tasks_list = ["Email client", "Code review", "Team sync meeting", "Debug project"]
    helper = DailyDataHelper(dataset_name="Work Tasks", initial_data=tasks_list)
    
    # 2. Display the data to show default-configured values
    helper.display_all_data()
    
    # 3. Perform a data search using the enumerate functionality
    helper.search_value("Team sync meeting")
    helper.search_value("Launch application") # Negative case match
    
    # 4. Explicitly delete the reference to trigger the destructor
    print("\nRemoving helper object reference...")
    del helper
    
    print("\n--- Program Execution Finished ---")

