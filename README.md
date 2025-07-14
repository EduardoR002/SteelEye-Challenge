# SteelEye Data Engineer Technical Assessment

[![GitHub Actions CI](https://img.shields.io/github/actions/workflow/status/EduardoR002/SteelEye-Challenge/ci.yml?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/EduardoR002/SteelEye-Challenge/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge&logo=python)](https://github.com/psf/black)
[![Linter: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&style=for-the-badge)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

[cite_start]This repository contains the solution for the **Data Engineer Technical Assessment** from SteelEye[cite: 1, 2, 3]. The project is a Python application designed to download, process, and store financial data from the European Securities and Markets Authority (ESMA), following best practices in software engineering.

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

1.  [cite_start]Downloads an initial XML file from a specified ESMA endpoint.
2.  [cite_start]Parses this XML to find a specific download link for a file with the `DLTINS` type.
3.  [cite_start]Downloads the corresponding `.zip` archive from the discovered link.
4.  [cite_start]Extracts the final XML file from the archive.
5.  [cite_start]Processes the data, converting the XML content into a structured CSV file with new, calculated fields[cite: 30, 37, 40].
6.  [cite_start]Uploads the resulting CSV to a cloud storage location, with support for both AWS S3 and Azure Blob Storage[cite: 42, 44].

[cite_start]The entire application is built using Object-Oriented principles to ensure the code is modular, reusable, and easy to maintain.

## ✨ Key Features

-   **Dynamic Data Fetching**: Intelligently parses an initial source to find and download the target dataset.
-   **Efficient XML Parsing**: Uses `lxml` for memory-efficient parsing of large XML files.
-   [cite_start]**Data Transformation with Pandas**: Leverages the Pandas library for robust data manipulation and the creation of new analytical columns[cite: 15, 37, 40].
-   [cite_start]**Cloud-Agnostic Storage**: Employs `fsspec` to seamlessly upload the final output to different cloud providers (AWS S3, Azure Blob)[cite: 42, 44].
-   [cite_start]**Robust & Maintainable Code**: Built with OOP principles [cite: 17][cite_start], PEP8 standards, type hints, and detailed docstrings.
-   [cite_start]**Comprehensive Testing**: Includes unit and integration tests with `pytest` to ensure reliability and correctness.
-   [cite_start]**Logging**: Implements standard logging for effective troubleshooting without using `print` statements[cite: 51].
-   [cite_start]**Automated CI/CD**: Integrates GitHub Actions for continuous integration, automatically running tests and linters on every push and pull request.
-   **Full Documentation**: Includes comprehensive documentation generated with Sphinx.

## 🛠️ Tech Stack

-   [cite_start]**Language**: Python 3 
-   **Core Libraries**:
    -   [cite_start]`pandas`: For data processing and manipulation.
    -   `requests`: For handling HTTP requests.
    -   `lxml`: For efficient XML parsing.
    -   [cite_start]`fsspec`: For unified, cloud-agnostic file system access.
-   **Testing**:
    -   [cite_start]`pytest`: For writing and running unit and integration tests.
    -   `pytest-mock`: For mocking objects during tests.
-   **Code Quality & Formatting**:
    -   `black`: For automated code formatting.
    -   [cite_start]`ruff`: As a linter for enforcing code standards[cite: 21].
    -   [cite_start]`pre-commit`: For running quality checks before each commit[cite: 22].
-   **CI/CD**:
    -   [cite_start]`GitHub Actions`: For automating the test and validation pipeline.
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
