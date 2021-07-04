import pandas as pd

sessions = pd.read_excel('ApacheConSessions.xlsx')


def get_speakers_email(speakers):
    speaker_list = speakers.split(",")
    result_list = []
    for speaker in speaker_list:
        result_list.append(get_speaker_email(speaker))
    return result_list


def get_speaker_email(speaker):
    parts = speaker.partition('<')
    email = (parts[2]).partition('>')[0]
    names = parts[0].partition(' ')
    first_name = names[0]
    last_name = ''
    if names[1] == ' ':
        last_name = names[2]
    return "{0},{1},{2}\n".format(email, first_name, last_name)


# Extract the emails information from session data

email_csv = open("email-apachecon.csv", "w+")
email_csv.write("Email, FirstName, LastName\n")


for index in sessions.index:
    if sessions.at[index, 'Status'] == 'accept':
        # create the markdown file
        print(sessions.at[index, 'English Title'])

        speakers_email = get_speakers_email(sessions.at[index, 'Speaker(s)'])
        for speaker_email in speakers_email:
            email_csv.write(speaker_email)

email_csv.close()
