# Challenge 26: Config Parser
# Phase: 2 - Python Programming
# Lesson: 10 - File I/O & Error Handling

def parse_config(filename):
    """
    Reads a key=value config file and returns a dictionary.
    Gracefully handles missing files using try/except.
    """
    try:
        config_dict = {}
        with open(filename, "r") as f:
            for line in f:
                # Clean the line and split by the equals sign
                clean_line = line.strip()
                parts = clean_line.split("=")
                key = parts[0]
                value = parts[1]
                # Add to dictionary
                config_dict[key] = value
        return config_dict
    except FileNotFoundError:
        # Graceful fallback instead of crashing
        print(f"⚠️ Warning: {filename} not found! Returning empty config.")
        return {}

# --- TEST IT ---
# Test 1: Real file (Make sure you have config.txt in the same folder!)
print(parse_config("config.txt"))

# Test 2: Missing file (Tests your error handling!)
print(parse_config("missing_file.txt"))

# CLOUD ENGINEERING CONTEXT:
# AWS CLI configuration files (~/.aws/credentials and ~/.aws/config) 
# use this exact key=value format. Cloud engineers write parsers like 
# this to load AWS profiles dynamically into their automation scripts.
# The try/except ensures that if the config is missing, the script 
# doesn't crash—it just defaults to empty settings and alerts the user.