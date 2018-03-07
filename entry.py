import werobot

robot = werobot.WeRoBot(token='56ea8a4aa4493ee04617612fc41cb985')

@robot.handler
def echo(message):
    return 'Hello World!'

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 8022

robot.run()

@robot.handler
def hello(message):
    return "您发送了一条信息："+message.content