
# PDF to TEXT converter

it will help you to convert any pdf to text.

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Download and install [Python 3.10.0](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe)

### Installation

1. First check python version in terminal, if it's 3.10.0 then go ahead.
   ```sh
   python --version 
   ```

2. Go to folder where you want to clone this repository and use below command to clone this repo to your local machine.
   ```sh
   git clone https://github.com/ipiyushvaghela/pdf2text.git
   ```
   
   Then download and setup Tesseract from [here](https://tesseract-ocr.github.io/tessdoc/Installation.html). Tesseract complete setup for [windows](https://linuxhint.com/install-tesseract-windows/). Tesseract complete setup for [linux](https://linuxhint.com/install-tesseract-ocr-linux/)
   if you get any error or if it's not working then just check google or youtube for how to download and install Tesseract.
    
3. Create virtual Environment 
   ```sh
   python3 -m venv venv4pdf
   ```

   To Activate our virtual environment we use
   
   For Windows : 
   ```sh
   venvForAugment/Script/Activate.bat
   ```

   For Linux :
   ```sh
   source venv4pdf/bin/activate
   ```
4. Install packages using requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
## Usage

Now we are all set to go. 
Open your current working directory in terminal and then just run below command with your inp_pdf_path, and language. Available [languages](https://github.com/tesseract-ocr/tessdata).

eng for english

guj for gujarati 

hin for hindi and so on...

```
python script.py <inp_file_path> output.txt -l <language>
```

For example my language is english and my file path is ```./content/input_test.pdf``` then
```
python script.py ./content/input_test.pdf output.txt -l eng
```
will generate output.txt file in your current working directory.

## Contact

Piyush Vaghela - [@ipiyushvaghela](https://twitter.com/ipiyushvaghela) - ipiyushvaghela@gmail.com

Project Link -  [github.com/ipiyushvaghela/ImageAugmentation](https://github.com/ipiyushvaghela/pdf2text.git)

## Acknowledgments
Special thanks to [zoumdatascience](https://github.com/zoumdatascience/OCR).
