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

## 2. Set up input data
1. Create an empty csv file named "Momo_Crawler.csv".

2. Add columns named "Shopee_Link" and "Momo_Link" in your Momo_Crawler.csv.

3. Insert the corresponding URLs into the added columns.

4. Save the csv and put the csv and .py above in the same file.

**Note:** Make sure the provided URLs are valid and can direct to the correct product pages.

## 3.Run
### (1)momo_crawler
1.Directly run code and you will get a csv as result.

### (2)fival_v1_1
1.Run file.

2.Enter your email and password of shopee account as program tell you to do.

3.As a chrome window pop up, you will see that shopee send you a text message by phone, asking you to verify your logging activate, and just do it.

4.The crawlering process is begin and just wait for the result.

## Contact

If there are any questions, please feel free to contact me via
Email:shengyanlin0503@gmail.com

---
The above are the setup and execution instructions for this project, and we hope it can help you.
