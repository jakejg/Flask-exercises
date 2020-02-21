from flask import Flask
from flask import request
from operations import add, sub, div, mult

app = Flask(__name__)


@app.route('/<operation>')
def sort_operation(operation):
    """ Get data from query strings and URL 
    and apply appropriate math function
    """

    a = float(request.args["a"])
    b = float(request.args["b"])
    ops = {
        "add": add(a, b),
        "sub": sub(a, b),
        "div": div(a, b),
        "mult": mult(a, b)
    }
    return f"The answer is {ops[operation]}"
  
    
    
    

    
    
    