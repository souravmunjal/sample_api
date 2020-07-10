from flask import Flask, request, jsonify

app = Flask(__name__)
ls_months={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'June':6,'July':7,'Aug':8,'Sept':9,'Oct':10,'Nov':11,'Dec':12}

@app.route('/getTheMaximumProfit',methods=['POST'])
def getTheMaximumProfit():
	json_= request.get_json(force=True)
	full_ls=[]
	for i in json_:
		ls=[]
		ls.append(str(ls_months[i['end_date'].split(' ')[1]])+i['end_date'].split(' ')[0])
		ls.append(str(ls_months[i['start_date'].split(' ')[1]])+i['start_date'].split(' ')[0])
		ls.append(i['MovieName'])
		full_ls.append(ls);
	#now we have to use simple activity selection code to get the Maximum Number of movies he can do
	full_ls.sort();
	print(full_ls);
	
	return jsonify({"ans":str(json_)})


if __name__ == '__main__':
    app.run(debug=True,port=12345)