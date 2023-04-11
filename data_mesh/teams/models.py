

class Team():
    def __init__(self, id, name, description, manager, members, slack_channel, mail_id):
        self.id = id
        self.name = name
        self.description = description
        self.manager = manager
        self.members = members
        self.slack_channel = slack_channel
        self.mail_id = mail_id


MOCK_TEAM_DATA = [
    Team(1,
         'finance',
         'finance team',
         'f-manager',
         [
             'f-member-1',
             'f-member-2'
         ],
         '#team-finance',
         'finance@immo.io'
         ),
    Team(2,
         'payroll',
         'payroll team',
         'p-manager',
         [
             'p-member-1',
             'p-member-2'
         ],
         '#team-payroll',
         'payroll@immo.io'
         )
]
