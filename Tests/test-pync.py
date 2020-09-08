import os
from pync import Notifier

# Notifier.notify('Hello World')
# Notifier.notify('Hello World', title='Python')
# Notifier.notify('Hello World', group=os.getpid())
# Notifier.notify('Hello World', activate='com.apple.Safari')
# Notifier.notify('Hello World', open='http://github.com/')
# Notifier.notify('Hello World', execute='say "OMG"')
# Notifier.notify('Hello World', appIcon='https://avatars0.githubusercontent.com/u/38857901?s=460&u=d8136c5a75703aeef7204b9d054ca386a65e80d8&v=4')

Notifier.notify('Je test les notifs',
    title="Test",
    appIcon='https://avatars0.githubusercontent.com/u/38857901?s=460&u=d8136c5a75703aeef7204b9d054ca386a65e80d8&v=4',
    open="https://websiteofmarcpartensky.herokuapp.com/",
    execute='say lmao you clicked'
)

Notifier.remove(os.getpid())

Notifier.list(os.getpid())
