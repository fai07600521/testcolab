# Import libraries
from flask import Flask, request, render_template
from flask import Flask,render_template, request
import pickle
import torch 
#from generate import generate_images
import pprint


app = Flask(__name__)
 

  
@app.route('/',methods=["GET", "POST"])
def home(name=None):
        return render_template('home.html')


@app.route('/generated', methods=["GET", "POST"])
def generated(name=None):
    if request.method == "POST":
         if request.form.get("classy"):
            with open('network-snapshot-001370.pkl', 'rb') as f:
                G = pickle.load(f)['G_ema'].cuda()  # torch.nn.Module
                z = torch.randn([1, G.z_dim]).cuda()    # latent codes
                c = None                                # class labels (not used in this example)
                img = G(z, c)                           # NCHW, float32, dynamic range [-1, +1]
        


        

if __name__ == '__main__':
    app.run(threaded=False, debug=False, host='127.0.0.1', port=5000)
    

