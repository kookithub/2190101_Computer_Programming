n = int(input())
speak = []
for i in range(n):
    speak.append('*' + input())
atc = input()
y = ''
while atc != 'END':
    y += atc + '\n'
    atc = input()
p = 0
q = 0
a = ['']
while p!= -1:
    p = y.find('*',q)
    q = y.find('\"',p)
    q = y.find('\"',q+1)
    a.append(y[p:q+1])
    p += len(a[-1])
ee = []
for e in a:
    if e[e.find('*'):e.find(":")] in speak:
        ee.append(e)
if len(ee) == 0:
    print("Maybe wrong novel")
else:
    for e in ee:
        print(e[1:])
"""
2
Tom
Sara
*John: "I can’t believe you forgot the meeting again, Sara!"
John’s face was red with anger.
*Sara: "I’m really sorry, John. It completely slipped my mind."
Sara looked down, guilt evident in her expression.
*Tom: "Hey, let’s not blow this out of proportion. Mistakes happen."
Tom spoke with a sad face, trying to calm the situation.
*Emily: "Exactly, John. We all have those days. It’s not the end of the world. Let’s just move forward."
Emily crossed her arms and raised an eyebrow.
*John: "Fine. You’re right. It’s just… we can’t afford to keep dropping the ball like this."
John rubbed his forehead, frustration still lingering.
*Sara: "I know, and I promise, it won’t happen again. I’ll set reminders, whatever it takes."
Sara nodded earnestly, her determination clear.
*Tom: "See? Problem solved. We’re still a team." Tom sigh
Tom tried to lighten the mood, a small smile forming.
*Emily: "Exactly. Let’s focus on the next steps instead."
Emily smiled encouragingly at everyone.
*John: stupid "Alright, let’s get back on track." Fuck he said
John finally relaxed, his anger fading.
END
"""