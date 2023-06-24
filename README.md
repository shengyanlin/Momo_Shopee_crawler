# Momo/Shopee Web Crawler
This project provides two easy-to-use tools to get the price from Momo and Shopee and compare their difference by % with url as input.

This README.md file will briefly describe how to set up and run this project. The main steps are divided into two parts: creating and activating a virtual environment and installing requirements, and setting input data.

## 1. Create and activate a virtual environment, and install requirements

Before proceeding with the following steps, make sure that Python and pip are installed.

1. Create a virtual environment:

    ```shell
    python3 -m venv env
    ```

2. Activate the virtual environment:

    - On Unix or MacOS:

        ```shell
        source env/bin/activate
        ```

    - On Windows:

        ```shell
        .\env\Scripts\activate
        ```

3. Install the requirements:

    ```shell
    pip install -r requirements.txt
    ```

## 2. Setting up input data

1. Add columns named "Shopee_Link" and "Momo_Link".

2. Insert the corresponding URLs into the added columns.

**Note:** Make sure the provided URLs are valid and can direct to the correct product pages.

## Contact

If there are any questions, please feel free to contact us.

---
The above are the setup and execution instructions for this project, and we hope it can help you.
