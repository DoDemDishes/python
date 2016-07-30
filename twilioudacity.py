from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACc1c67de0bf24fb294ae00f9728bef70a" 
AUTH_TOKEN = "22911d8a41902990221a78f977b14fd1" 

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create( 
	from_="+48732483882",  
	to = "+48505875377",
	body = "Kto ci buty ukradł?" 
) 
