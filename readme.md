Decode Key 

-------------

installation and set up

pip install -r requirements.txt 

or manually follow these -

- install flask to run the api and get response -> pip install flask
- to run the server run command -> python main.py

---------------

- the token/key in .txt file looked like base64 and hence i wanted to validate the same hence added a isbase64 function that returns a bool value
- i also looked if there is any common pattern or signature in the binary data but the couldn't find any file formats matching the pattern checked for pdf, jpeg,png,json etc hence went ahead with base64 decoding

