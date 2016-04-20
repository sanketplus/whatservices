from wordnik import *
import commands
import wikipedia

apiUrl = 'http://api.wordnik.com/v4'
apiKey = # API token here


def define(query):
    
    client = swagger.ApiClient(apiKey, apiUrl)
    wordApi = WordApi.WordApi(client)
    result = wordApi.getDefinitions(query)
    if result:
        reply = ""
        for i in range(len(result)):
            reply = reply + result[i].text + "\n----------------\n"
        reply = reply + "\n SEE YOU AGAIN :D"
    else:
        reply = "Oops! I failed to search for " + query  +" :("

    return reply


def how_do_i(query):
    (s, o) = commands.getstatusoutput("howdoi " + query)
    if s == 0:
        return o
    else:
	return "Oops would you try again? Try sending 'help' for example :)"	    


def wiki(query):
    try:
	return wikipedia.summary(query)
    except:
	return "Oops! No wiki found! Try with different query, would you?"
