# 这里有 21 根棍子，首先用户选 1 到 4 根棍子，然后电脑选 1 到 4 根棍子。
# 谁选到最后一根棍子谁就输。
# 特别说明：用户和电脑一次选的棍子总数只能是 5。

ticket = 21
ticket_last = ticket
while True:
    if ticket_last == 1:
        print('You lost')
        break
    ticket_token = int(input('请输入你要拿走的棍子数'))
    ticket_last = ticket_last - ticket_token
    print('你拿走了{}个棍子，剩余{}个棍子，该电脑了。'.format(ticket_token, ticket_last))

    ticket_token_computer = 5 - ticket_token
    ticket_last = ticket_last - ticket_token_computer
    print('电脑拿走了{}个棍子，剩余{}个棍子，该你了。'.format(ticket_token_computer, ticket_last))

