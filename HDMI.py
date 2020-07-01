import requests
hdmiValue = input("HDMI 1-3:\n") 
if hdmiValue == '1':
  request_url = "http://192.168.0.21:8060/launch/tvinput.hdmi1"
  requests.post(request_url)
elif hdmiValue == '2':
  request_url = "http://192.168.0.21:8060/launch/tvinput.hdmi2"
  requests.post(request_url)
elif hdmiValue == '3':
  request_url = "http://192.168.0.21:8060/launch/tvinput.hdmi3"
  requests.post(request_url)
else:
  print("Enter a valid number.")
