import lorem

class Response(object):

    def __init__(self, msg, profile):
        self.user_msg = msg
        self.user_profile = profile
        print(msg)
        print(profile.display_name)
        print(profile.user_id)
        print(profile.picture_url)
        print(profile.status_message)
    
    def greeting(self):
        return "Hi,\n{}".format(self.user_profile.display_name)

    def conversation(self):
        return lorem.sentence()