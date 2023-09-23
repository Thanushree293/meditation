# Download the helper library from https://www.twilio.com/docs/python/install

from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC7d6ea34e017d7b56bdd5f82bdeac8df1'
auth_token = '7e5ea8b1d744040bd990b0a12a4ee40c'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say>Ahoy, World!</Say></Response>',
                        to='+917019555472',
                        from_='+13346058442'
                    )

print(call.sid)