# ckl2ckl
Tool to translate findings from older to newer versions of a Checklist.

## How to install:
1. Install dependencies: Python 3.9 and [Poetry](https://python-poetry.org/)
2. Clone the repository: `git clone https://github.com/mitre/ckl2ckl`
3. Install application: `poetry install`

## How to update:

### Option 1 (Using git)
1. Ensure you are in the folder containing ckl2ckl
2. Stash any existing input/outputs `git stash --include-untracked`
3. Update the repository: `git fetch`
4. Pull the latest changes `git pull`
5. Restore your files `git stash pop`
6. Install dependencies: `poetry install`

### Option 3 (Using Download as Zip)
1. Delete your existing ckl2ckl folder
2. Download the most recent version: https://github.com/mitre/ckl2ckl/archive/refs/heads/main.zip
3. Enter the ckl2ckl folder using the terminal
4. Install dependencies: `poetry install`

## How to use:
1. Run the script: `poetry run ckl2ckl old_path new_path result_path` where old_path is the path to the old CKL file, new_path is the path to the new CKL file, and result_path is the path to where you'd like to save the CKL file
2. Verify the accuracy of the resultant CKL file - the script will create a potentially substantial number of logs to help with this

## Contributing, Issues and Support

### Contributing

Please feel free to look through our issues, make a fork and submit _PRs_ and improvements. We love hearing from our end-users and the community and will be happy to engage with you on suggestions, updates, fixes or new capabilities.

### Issues and Support

Please feel free to contact us by **opening an issue** on the issue board, or, at [saf@groups.mitre.org](mailto:saf@groups.mitre.org) should you have any suggestions, questions or issues. If you have more general questions about the use of our software or other concerns, please contact us at [opensource@mitre.org](mailto:opensource@mitre.org).

## Authors and License

### Authors
- Amndeep Singh Mann [amann@mitre.org](mailto:amann@mitre.org)
- Camden Moors [cmoors@mitre.org](mailto:cmoors@mitre.org)

### NOTICE

© 2019-2021 The MITRE Corporation.

Approved for Public Release; Distribution Unlimited. Case Number 18-3678.

### NOTICE

MITRE hereby grants express written permission to use, reproduce, distribute, modify, and otherwise leverage this software to the extent permitted by the licensed terms provided in the LICENSE.md file included with this project.

### NOTICE

This software was produced for the U. S. Government under Contract Number HHSM-500-2012-00008I, and is subject to Federal Acquisition Regulation Clause 52.227-14, Rights in Data-General.

No other use other than that granted to the U. S. Government, or to those acting on behalf of the U. S. Government under that Clause is authorized without the express written permission of The MITRE Corporation.

For further information, please contact The MITRE Corporation, Contracts Management Office, 7515 Colshire Drive, McLean, VA 22102-7539, (703) 983-6000.
