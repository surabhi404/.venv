from twilio.rest import Client
client=Client("ACa77c2a594c29764ee94dc03a2207c4b8","ae189be979f218be49e01cf82075c6a3");
#for msg in client.messages.list():
 #   print(msg.body)
msg=client.messages.create(to=+919320494030, from_="+120283899292",body="hello",)
print(f"create a new message:{msg.sid}")