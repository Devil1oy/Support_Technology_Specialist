def parse(response: dict) -> list[str]:

    logins = []

    people = response.get('people', {}).get('result', [])

    for person in people:
            login = person.get('login')
            logins.append(login)

    return logins

logins = parse(response)
print(logins)
