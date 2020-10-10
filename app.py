from flask import Flask, jsonify,request
import time
app = Flask(__name__);
@app.route("/bot", methods=["POST"])
def response():
    query = dict(request.form)['query']
    if query=='Hello'or query=='Hi':
        res="Hey there!"
    if query=='How are you?':
        res="I'm good"
    if query=='What is coronavirus?' or query=='What is a coronavirus?' or query=='What is corona?':
        res="Coronaviruses are a large family of viruses which may cause illness in animals or humans.  In humans, several coronaviruses are known to cause respiratory infections ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS). The most recently discovered coronavirus causes coronavirus disease COVID-19."
    if query=='What is covid-19?' or query=='Tell me about covid-19':
        res="COVID-19 is the infectious disease caused by the most recently discovered coronavirus. This new virus and disease were unknown before the outbreak began in Wuhan, China, in December 2019"

    #res = query + " " + time.ctime()
    return jsonify({"response" : res})
if __name__=="__main__":
    app.run(host="0.0.0.0",)
