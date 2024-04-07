from pushbullet import Pushbullet #used to push message to different devices



#giving the alert message

API_KEY ="o.2HXZhtk1IqTEKyKPWKRN5sUIDvPA3t9b" #Pushbullet API Key of the police's device
file ="alertmsg.txt" #contains message which policeman will receive

with open(file, mode='r') as f:#using open function to open  alertmessage file  
    text = f.read() #reading alertmessage file  
    pb =Pushbullet(API_KEY)#will send notification to the address contained by API_KEY
    push = pb.push_note('She needs help', text)#to push note to police's device i.e. will decide what to send in notification