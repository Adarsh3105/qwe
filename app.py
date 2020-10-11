from flask import Flask, jsonify,request
import time
def check(query):
    query=query.lower()
    greetings = ("hi", "hello", "hey","what is your name","what's your name","who are you")
    bye=("bye","goodbye","i am leaving","see you")
    question=("what","how","which","Tell me about")
    corona=("virus","coronavirus","covid-19","covid19","covid 19","corona","covid")
    #covid=("covid-19","covid19","covid 19")
    prevent=("protect","prevent","stop","avoid","precautions","precaution","prevention")
    spread=("spread","spreading","cause","causes")
    catch=("catch","catching","caught")
    health=("are you","is your health")
    welcome=("welcome","my pleasure")
    maker=("who made you","who developed you","who is your owner","who coded you")
    symptoms=("symptoms","symptom","sign","signs")

    if any(s in query for s in greetings):
        print ("Hey there!, I'm Dorona bot")
    elif any(s in query for s in maker):
        print("I was made by Adarsh, Naman and Pulkit.")
    elif any(s in query for s in bye):
        print("Good bye!")
    elif any(s in query for s in welcome):
        print("Take care!")
    elif any(s in query for s in question):
        if any(s in query for s in prevent):
            print("Stay aware of the latest information on the COVID-19 outbreak, available on the WHO website and through your national and local public health authority. Many countries around the world have seen cases of COVID-19 and several have seen outbreaks. Authorities in China and some other countries have succeeded in slowing or stopping their outbreaks. However, the situation is unpredictable so check regularly for the latest news.You can reduce your chances of being infected or spreading COVID-19 by taking some simple precautions:Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water.Why? Washing your hands with soap and water or using alcohol-based hand rub kills viruses that may be on your hands.Maintain at least 1 metre (3 feet) distance between yourself and anyone who is coughing or sneezing.Why? When someone coughs or sneezes they spray small liquid droplets from their nose or mouth which may contain virus. If you are too close, you can breathe in the droplets, including the COVID-19 virus if the person coughing has the disease.Avoid touching eyes, nose and mouth.Why? Hands touch many surfaces and can pick up viruses. Once contaminated, hands can transfer the virus to your eyes, nose or mouth. From there, the virus can enter your body and can make you sick.Make sure you, and the people around you, follow good respiratory hygiene. This means covering your mouth and nose with your bent elbow or tissue when you cough or sneeze. Then dispose of the used tissue immediately.Why? Droplets spread virus. By following good respiratory hygiene you protect the people around you from viruses such as cold, flu and COVID 19.Stay home if you feel unwell. If you have a fever, cough and difficulty breathing, seek medical attention and call in advance. Follow the directions of your local health authority.Why? National and local authorities will have the most up to date information on the situation in your area. Calling in advance will allow your health care provider to quickly direct you to the right health facility. This will also protect you and help prevent spread of viruses and other infections.Keep up to date on the latest COVID-19 hotspots (cities or local areas where COVID-19 is spreading widely). If possible, avoid traveling to places  â€“ especially if you are an older person or have diabetes, heart or lung disease.Why? You have a higher chance of catching COVID 19 in one of these areas")
        elif any(s in query for s in catch):
            print("The risk depends on where you  are - and more specifically, whether there is a COVID-19 outbreak unfolding there.For most people in most locations the risk of catching COVID-19 is still low. However, there are now places around the world (cities or areas) where the disease is spreading. For people living in, or visiting, these areas the risk of catching COVID-19 is higher. Governments and health authorities are taking vigorous action every time a new case of COVID-19 is identified. Be sure to comply with any local restrictions on travel, movement or large gatherings. Cooperating with disease control efforts will reduce your risk of catching or spreading COVID-19.COVID-19 outbreaks can be contained and transmission stopped, as has been shown in China and some other countries. Unfortunately, new outbreaks can emerge rapidly. Itâ€™s important to be aware of the situation where you are or intend to go. WHO publishes daily updates on the COVID-19 situation worldwide.")
        elif any(s in query for s in spread):
            print("People can catch COVID-19 from others who have the virus. The disease can spread from person to person through small droplets from the nose or mouth which are spread when a person with COVID-19 coughs or exhales. These droplets land on objects and surfaces around the person. Other people then catch COVID-19 by touching these objects or surfaces, then touching their eyes, nose or mouth. People can also catch COVID-19 if they breathe in droplets from a person with COVID-19 who coughs out or exhales droplets. This is why it is important to stay more than 1 meter (3 feet) away from a person who is sick.WHO is assessing ongoing research on the ways COVID-19 is spread and will continue to share updated findings.")
        elif any(s in query for s in symptoms):
            print("The most common symptoms of COVID-19 are fever, tiredness, and dry cough. Some patients may have aches and pains, nasal congestion, runny nose, sore throat or diarrhea. These symptoms are usually mild and begin gradually. Some people become infected but donâ€™t develop any symptoms and don't feel unwell. Most people (about 80%) recover from the disease without needing special treatment. Around 1 out of every 6 people who gets COVID-19 becomes seriously ill and develops difficulty breathing. Older people, and those with underlying medical problems like high blood pressure, heart problems or diabetes, are more likely to develop serious illness. People with fever, cough and difficulty breathing should seek medical attention.")
        elif any(s in query for s in corona):
            print("Coronaviruses are a large family of viruses which may cause illness in animals or humans.  In humans, several coronaviruses are known to cause respiratory infections ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS). The most recently discovered coronavirus causes coronavirus disease COVID-19.")
        elif any(s in query for s in health):
            print("I'm good, thankyou.")
        else:
            print("Sorry, I don't understand.")
    else:
        print("Sorry, I don't understand")

    return res
app = Flask(__name__);
@app.route("/bot", methods=["POST"])
def response():
    query = dict(request.form)['query']
    res=check(query)
    #res = query + " " + time.ctime()
    return jsonify({"response" : res})
if __name__=="__main__":
    app.run(host="0.0.0.0",)
