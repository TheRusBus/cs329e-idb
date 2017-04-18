from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
	return render_template("index.html")
	
@app.route('/about')
def about():
	return render_template("about.html")
	
@app.route('/fields')
def fields():
	return render_template("fields.html")
	
@app.route('/scientists')
def scientistmodel():
	return render_template("scientistmodel.html")
	
@app.route('/theories')
def theorymodel():
	return render_template("theorymodel.html")
	
@app.route("/theories/calculus")
def theoryCalculus():
	return render_template("theoryCalculus.html")

@app.route("/theories/dynamite")
def theoryDynamite():
	return render_template("theoryDynamite.html")
	
@app.route("/theories/evolution")
def theoryEvolution():
	return render_template("theoryEvolution.html")

@app.route("/theories/helio")
def theoryHelio():
	return render_template("theoryHelio.html")
	
@app.route("/theories/relativity")
def theoryRelativity():
	return render_template("theoryRelativity.html")
	
@app.route("/theories/turing")
def theoryTuring():
	return render_template("theoryTuring.html")

@app.route("/scientists/newton")
def ScientistSirIsaacNewton():
	return render_template("ScientistSirIsaacNewton.html")

@app.route("/scientists/turing")
def ScientistAlanTuring():
	return render_template("ScientistAlanTuring.html")
	
@app.route("/scientists/einstein")
def ScientistAlbertEinstein():
	return render_template("ScientistAlbertEinstein.html")	

@app.route("/scientists/nobel")
def ScientistAlfredNobel():
	return render_template("ScientistAlfredNobel.html")
	
@app.route("/scientists/darwin")
def ScientistCharlesDarwin():
	return render_template("ScientistCharlesDarwin.html")
	
@app.route("/scientists/galileo")
def ScientistGalileo():
	return render_template("ScientistGalileo.html")

@app.route("/fields/astronomy")
def fieldAstronomy():
	return render_template("fieldAstronomy.html")

@app.route("/fields/biology")
def fieldBiology():
	return render_template("fieldBiology.html")
	
@app.route("/fields/chemistry")
def fieldChemistry():
	return render_template("fieldChemistry.html")
	
@app.route("/fields/compsci")
def fieldComputerScience():
	return render_template("fieldComputerScience.html")
	
@app.route("/fields/mathematics")
def fieldMathematics():
	return render_template("fieldMathematics.html")
	
@app.route("/fields/physics")
def fieldPhysics():
	return render_template("fieldPhysics.html")




if __name__ == "__main__":
	app.run()
