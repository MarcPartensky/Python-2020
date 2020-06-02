import wolframalpha
client = wolframalpha.Client("Calculus")

res = client.query('temperature in Washington, DC on October 3, 2012')
print(res)
