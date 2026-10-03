Lab: Virtual Environment Lifecycle
Overview
This lab documents the exact terminal commands used to create, activate, populate, and exit a Python virtual environment (venv). Virtual environments are mandatory for professional cloud security engineers to isolate tool dependencies and prevent version conflicts.

The Lifecycle Commands
1. Create the Virtual Environment
This command uses the Python module venv to create an isolated Python environment inside a new folder named venv.

python3 -m venv venv
2. Activate the Virtual Environment
Activation modifies your shell's PATH variable so that Python and pip commands point to the isolated folder instead of the global system installation.
(You will see (venv) appear in your terminal prompt).

Mac/Linux:

bash

source venv/bin/activate
Windows:

bash

venv\Scripts\activate
3. Install a Package
Once activated, any package installed with pip is placed inside the venv folder, keeping the global system clean.

bash

pip install requests
4. Save Dependencies
Exports a list of all installed packages and their exact versions to a text file. This allows other engineers to replicate your exact setup.

bash

pip freeze > requirements.txt
5. Exit the Virtual Environment
Returns your terminal session back to the global Python environment.

bash

deactivate