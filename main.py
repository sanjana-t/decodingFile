import base64
import json  
from flask import Flask,jsonify,request
import string
import re

app =   Flask(__name__) 
   
def read_file(file_path):
    try:
        with open('robot.txt','r') as file:
            encoded_text = file.read()
            return encoded_text
    except Exception as e:
        print(f'''Error while processing the file with file path - {file_path} & Exception as {e}''')
        return None

def decode_base64(encoded_text):
    try:
        decoded_text = base64.b64decode(encoded_text,validate=True).decode('utf-8', errors = 'ignore')
        return decoded_text
    except:
        return None 
    
@app.route('/decode', methods = ['GET'])   
def decode():
    file_path = 'robot.txt'
    encoded_text = read_file(file_path)
    if(is_base64(encoded_text)):
        if encoded_text:
            decoded_text = decode_base64(encoded_text)
            if decoded_text:
                print(decoded_text)            
                return jsonify({"status_code":200,"status":"success","data":{"decoded_text":extract_printable_characters(decoded_text)}})
    else:
        return jsonify({"status_code":500,"status":"error","msg":"Not a valid base64"})
def extract_printable_characters(text):
    """Filter out non-printable characters"""
    return ''.join(char for char in text if char in string.printable)  

def is_base64(s):
    # Check length is a multiple of 4
    if len(s) % 4 != 0:
        return False
    
    # Checking valid Base64 characters and padding
    base64_pattern = re.compile(r'^[A-Za-z0-9+/=]*$')
    if not base64_pattern.match(s):
        return False
    
    try:
        base64.b64decode(s, validate=True)
        return True
    except (ValueError, TypeError):
        return False

if __name__ == "__main__":
    app.run(debug=False)
    
