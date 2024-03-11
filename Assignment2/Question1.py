from flask import Flask

app = Flask(__name__)

@app.route('/')
def default():
    return 'Hello, World!'

@app.route("/<params>")
def home(params):
    name = str(params)
    if name.isupper():
        lowered_string = name.lower()
        return "Welcome,  " + lowered_string + " to my CSCB20 website!"
    if name.islower():
        upper_string = name.upper()
        return "Welcome,  " + upper_string + " to my CSCB20 website!"
    else: #'s a mix of upper and lower
        if name.isalpha():
            standard_str = name[0].upper()
            standard_str += name[1:].lower()
            return "Welcome,  " + standard_str + " to my CSCB20 website!"
        else: # it's got numbers in them, yuck!
            new_name = ''
            for i in range(len(name)):
                if name[i].isalpha() == True:
                    new_name += name[i]
            final_name = new_name[0].upper()
            final_name += new_name[1:].lower()
            return "Welcome,  " + final_name + " to my CSCB20 website!"


if __name__ == "__main__":
    app.run(debug=True)

