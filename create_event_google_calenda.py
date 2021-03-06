from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']



def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'D:\\Users\\s84908\\OneDrive - The Siam Commercial Bank PCL\\Working\\google_calendar_api\\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # service = build('calendar', 'v3', credentials=creds)
    # Call the Calendar API
    # now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    # print('Getting the upcoming 10 events')
    # events_result = service.events().list(calendarId='primary', timeMin=now,
    #                                     maxResults=10, singleEvents=True,
    #                                     orderBy='startTime').execute()
    # events = events_result.get('items', [])

    # if not events:
    #     print('No upcoming events found.')
    # for event in events:
    #     start = event['start'].get('dateTime', event['start'].get('date'))
    #     print(start, event['summary'])

    service = build('calendar', 'v3', credentials=creds)
    event = {
        'summary': 'Deploy UAT 2',
        'start': {
            'date': '2019-12-18',
            'timeZone': 'Asia/Bangkok',
        },
        'end': {
            'date': '2019-12-19',
            'timeZone': 'Asia/Bangkok',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'methods': 'popup', 'minutes': 840},
            ],
        },
    }
    #print (event)
     
    #print ('Event created: %s' % (event.get('htmlLink')))
    from googleapiclient.errors import HttpError
    help(HttpError)
    try:
        event = service.events().insert(calendarId='primary', body=event).execute()
    except HttpError as err:
        print (err.content)
    finally:
        print ('Event created: %s' % (event.get('htmlLink')))
if __name__ == '__main__':
    main()


    # Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.

