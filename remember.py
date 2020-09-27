from simple_notifications import notify
import os
notify(os.environ['SOCIAL_SECURITY_NUMBER'])
# notify("Your task is done!", sound=True) # This will invoke the default notification sound
# notify("Your task is done!", subtitle="Status: Success")
# notify("Your task is done!", informative_text="Task took 128ms")
# notify("Your task is done!", sound='Glass')
