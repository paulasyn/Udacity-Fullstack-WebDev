from twilio.rest import Client

# Your Account SID from twilio.com/console
account_paul = "AC12f8619ef59e36bbb761d7dfe7acf5a2"
# Your Auth Token from twilio.com/console
auth_token  = "1c9a32bb87e70ee13c12555394e99c6d"

client = Client(account_paul, auth_token)

message = client.messages.create(
    to="+18173203095", 
    from_="+19728933691",
    body="Hey baby, Im sending you a text using python!")

print(message.sid)