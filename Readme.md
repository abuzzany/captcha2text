
       _____            _       _           ___ _______        _    
      / ____|          | |     | |         |__ \__   __|      | |   
     | |     __ _ _ __ | |_ ___| |__   __ _   ) | | | _____  _| |_  
     | |    / _` | '_ \| __/ __| '_ \ / _` | / /  | |/ _ \ \/ / __| 
     | |___| (_| | |_) | || (__| | | | (_| |/ /_  | |  __/>  <| |_  
      \_____\__,_| .__/ \__\___|_| |_|\__,_|____| |_|\___/_/\_\\__| 
                 | |                                                
                 |_|                                                


# Captcha2Text (Beta)

| Note: This is currently in beta. The accuracy is not 100% but has been tested to be above 80% accuracy with text-based captchas. I'm still looking for large Captcha datasets to test the accuracy.

Captcha2Text is a Python library that extracts text from captcha images using OpenAI's GPT-4 vision model.

## Description

This project provides a simple way to read text from captcha images. It uses the OpenAI API to process the images and return the extracted text.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Captcha2Text.git
   cd Captcha2Text
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

3. Set up your OpenAI API key:
   Create a `.env` file in the project root and add your API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

To use the captcha reader:

```python
from captcha_reader import read_captcha

image_path = './captcha_test_images/captcha_test1.jpeg'
text = read_captcha(image_path)
print(text)
```

## Testing

Run the tests using:
```
pytest captcha_reader_test.py
```


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT License](LICENSE)