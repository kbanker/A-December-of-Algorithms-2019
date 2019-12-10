
def cookie_count(money, cost, jars_per_cookie):
    cookies = money // cost
    jars = cookies
    while jars >= jars_per_cookie:
        add_cookies = jars // jars_per_cookie
        cookies += add_cookies
        jars = add_cookies

    return cookies

money = int(input('Enter amt of money: '))
cost = int(input('Enter cost of cookie jar: '))
jpc = int(input('Enter jars to exchange for a cookie: '))

print(cookie_count(money, cost, jpc))
