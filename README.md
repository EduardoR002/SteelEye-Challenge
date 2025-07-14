# SteelEye Data Engineer Technical Assessment

This repository contains the solution for the **Data Engineer Technical Assessment** from SteelEye. The project is a Python application designed to download, process, and store financial data from the European Securities and Markets Authority (ESMA), following best practices in software engineering.

## 📋 Table of Contents

- [About The Project](#-about-the-project)
- [✨ Key Features](#-key-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [⚙️ Usage](#️-usage)
- [🧪 Testing](#-testing)
- [📖 Documentation](#-documentation)
- [✅ Assessment Checklist](#-assessment-checklist)

## 📖 About The Project

The main goal of this application is to build a robust and maintainable data pipeline. The pipeline performs the following sequence of operations:

1.  Downloads an initial XML file from a specified ESMA endpoint.
2.  Parses this XML to find a specific download link for a file with the `DLTINS` type.
3.  Downloads the corresponding `.zip` archive from the discovered link.
4.  Extracts the final XML file from the archive.
5.  Processes the data, converting the XML content into a structured CSV file with new, calculated fields.
6.  Uploads the resulting CSV to a cloud storage location, with support for both AWS S3 and Azure Blob Storage.

The entire application is built using Object-Oriented principles to ensure the code is modular, reusable, and easy to maintain.

## ✨ Key Features

-   **Dynamic Data Fetching**: Intelligently parses an initial source to find and download the target dataset.
-   **Efficient XML Parsing**: Uses `lxml` for memory-efficient parsing of large XML files.
-   **Data Transformation with Pandas**: Leverages the Pandas library for robust data manipulation and the creation of new analytical columns[cite: 15, 37, 40].
-   **Cloud-Agnostic Storage**: Employs `fsspec` to seamlessly upload the final output to different cloud providers (AWS S3, Azure Blob)[cite: 42, 44].
-   **Robust & Maintainable Code**: Built with OOP principles, PEP8 standards, type hints, and detailed docstrings.
-   **Comprehensive Testing**: Includes unit and integration tests with `pytest` to ensure reliability and correctness.
-   **Logging**: Implements standard logging for effective troubleshooting without using `print` statements[cite: 51].
-   **Automated CI/CD**: Integrates GitHub Actions for continuous integration, automatically running tests and linters on every push and pull request.
-   **Full Documentation**: Includes comprehensive documentation generated with Sphinx.

## 🛠️ Tech Stack

-   **Language**: Python 3 
-   **Core Libraries**:
    -   `pandas`: For data processing and manipulation.
    -   `requests`: For handling HTTP requests.
    -   `lxml`: For efficient XML parsing.
    -   `fsspec`: For unified, cloud-agnostic file system access.
-   **Testing**:
    -   `pytest`: For writing and running unit and integration tests.
    -   `pytest-mock`: For mocking objects during tests.
-   **Code Quality & Formatting**:
    -   `ruff`: As a linter for enforcing code standards.
-   **CI/CD**:
    -   `GitHub Actions`: For automating the test and validation pipeline.
-   **Documentation**:
    -   `Sphinx`: For generating project documentation.

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

-   Python 3.8+
-   pip

### Installation

1.  **Clone the repository**
    ```sh
    git clone [https://github.com/EduardoR002/SteelEye-Challenge.git](https://github.com/EduardoR002/SteelEye-Challenge.git)
    cd SteelEye-Challenge
    ```

2.  **Install dependencies**
    It is recommended to use a virtual environment.
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## ⚙️ Usage

To run the entire data processing pipeline, execute the main module from the root directory:

```sh
python -m src.steeleye.main
