MedPrime Technologies Programming Assignments
This repository contains solutions for three programming assignments that help practice file handling, zipping directories, and working with images.

Tasks:
Assignment 1: Renaming Files Sequentially
Assignment 2: Zipping a Folder
Assignment 3: Creating a Collage from 4 Images
Table of Contents
Getting Started
Assignment 1: Renaming Files Sequentially
Assignment 2: Zipping a Folder
Assignment 3: Creating a Collage from 4 Images
Prerequisites
Usage Instructions
Contributing
License
Contact
Getting Started
Follow these steps to run the scripts:

Clone the repository to your machine.
Make sure Python 3.x is installed.
Install any required libraries (see prerequisites).
Run the scripts as per the instructions for each assignment.
Assignment 1: Renaming Files Sequentially
Objective: Rename all files in a folder to 1.ext, 2.ext, etc., while keeping their original extensions.
Command:
bash
Copy code
python rename_files.py <folder_path>
Example: If the folder contains:
image1.jpg, document.txt, report.pdf
After running the program, they’ll be renamed to:
1.jpg, 2.txt, 3.pdf
Assignment 2: Zipping a Folder
Objective: Compress the folder into a .zip file, keeping all files and subfolders.
Command:
bash
Copy code
python zip_folder.py <folder_path>
Example: If the folder contains:
Copy code
my_folder/
├── file1.txt
└── subfolder/
    └── file2.txt
The program will create a zip file my_folder.zip which contains the same folder structure.
Assignment 3: Creating a Collage from 4 Images
Objective: Arrange 4 images in a 2x2 grid and save them as one collage image.

Command:

bash
Copy code
python create_collage.py <image1> <image2> <image3> <image4>
Example: If the input images are image1.jpg, image2.jpg, image3.jpg, and image4.jpg, the program will create a collage image like:

Image 1	Image 2
Image 3	Image 4
Prerequisites
Before running the scripts:

Python 3.x should be installed.
For Assignment 3 (Image Collage), install the Pillow library:
bash
Copy code
pip install Pillow
Usage Instructions
Clone the Repository:
bash
Copy code
git clone https://github.com/yourusername/medprime-assignments.git
cd medprime-assignments
Run the Scripts:
For Assignment 1:

bash
Copy code
python rename_files.py <folder_path>
For Assignment 2:

bash
Copy code
python zip_folder.py <folder_path>
For Assignment 3:

bash
Copy code
python create_collage.py <image1> <image2> <image3> <image4>
Contributing
Feel free to contribute if you'd like to improve the scripts:

Fork the repo.
Create a new branch for your changes.
Commit and push your changes.
Open a pull request.
Follow Python's PEP 8 guidelines and make sure to document your code.

License
This project is licensed under the MIT License.

Contact
If you have any questions, feel free to reach out:

Email: kambletanaya18@gmail.com.com
GitHub: tanayakamble2001
