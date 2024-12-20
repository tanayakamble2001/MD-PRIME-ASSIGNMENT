# MedPrime Technologies Programming Assignments

These assignments focus on file handling, zipping directories, and image processing areas that are sure to enhance our problem-solving skills and boost our proficiency in Python.

### Tasks:
1. **Assignment 1**: Renaming Files Sequentially
2. **Assignment 2**: Zipping a Folder
3. **Assignment 3**: Creating a Collage from 4 Images

---

## Table of Contents
- [Getting Started](#getting-started)
- [Assignment 1: Renaming Files Sequentially](#assignment-1-renaming-files-sequentially)
- [Assignment 2: Zipping a Folder](#assignment-2-zipping-a-folder)
- [Assignment 3: Creating a Collage from 4 Images](#assignment-3-creating-a-collage-from-4-images)
- [Prerequisites](#prerequisites)
- [Usage Instructions](#usage-instructions)
- [Contact](#contact)

---

## Getting Started

Follow these steps to run the scripts:

1. **Clone the repository** to your machine.
2. **Make sure Python 3.x** is installed.
3. **Install any required libraries** (see prerequisites).
4. **Run the scripts** as per the instructions for each assignment.

---

## Assignment 1: Renaming Files Sequentially

- **Objective**: Rename all files in a folder to `1.ext`, `2.ext`, etc., while keeping their original extensions.
- **Command**:
  ```bash
  python assessment1.py
  ```
   - Enter the folder path when prompted.
- **Example**: If the folder contains:
  - `image1.jpg`, `document.txt`, `report.pdf`
  
  After running the program, they’ll be renamed to:
  - `1.jpg`, `2.txt`, `3.pdf`

---

## Assignment 2: Zipping a Folder

- **Objective**: Compress the folder into a `.zip` file, keeping all files and subfolders.
- **Command**:
  ```bash
  python assessment2.py
  ```
  - Enter the folder path when prompted.
- **Example**: If the folder contains:
  ```
  my_folder/
  ├── file1.txt
  └── subfolder/
      └── file2.txt
  ```
  The program will create a zip file `my_folder.zip` which contains the same folder structure.

---

## Assignment 3: Creating a Collage from 4 Images

- **Objective**: Arrange 4 images in a 2x2 grid and save them as one collage image.
- **Command**:
  ```bash
  python assessment3.py
  ```
  - Enter the paths for four images when prompted.
  - Specify the output file name (e.g., collage.jpg).
- **Example**: If the input images are `image1.jpg`, `image2.jpg`, `image3.jpg`, and `image4.jpg`, the program will create a collage image like:

  | Image 1 | Image 2 |
  | ------- | ------- |
  | Image 3 | Image 4 |

---

## Prerequisites

Before running the scripts:
- **Python 3.x** should be installed.
- For **Assignment 3** (Image Collage), install the `Pillow` library:
  ```bash
  pip install Pillow
  ```

---

## Usage Instructions

### Clone the Repository:
```bash
git clone https://github.com/yourusername/medprime-assignments.git
cd medprime-assignments
```

### Run the Scripts:
- For **Assignment 1**:
  ```bash
  python assessment1.py 
  ```

- For **Assignment 2**:
  ```bash
  python assessment2.py
  ```

- For **Assignment 3**:
  ```bash
  python assessment3.py
  ```

---

## Contact

If you have any questions, feel free to reach out:
- **Name**: Tanaya Kamble
- **Email**: [kambletanaya18@gmail.com](mailto:kambletanaya18@gmail.com)
- **GitHub**: [tanayakamble2001](https://github.com/tanayakamble2001)

---
