import werobot

robot = werobot.WeRoBot(token='56ea8a4aa4493ee04617612fc41cb985')

@robot.handler
def echo(message):
    return 'Hello World!'

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 8022

robot.run()

@robot.text
def hello(message):
    return "you send a text："+message.content
@robot.image
def img(message):
    return "you send a image"