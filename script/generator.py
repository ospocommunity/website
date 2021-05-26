import pandas as pd

sessions = pd.read_excel('ApacheConSessions.xlsx')
tracks_dictionary = {"Integration": "integration",
                     "Workflow/Data Governance": "workflowdatagovernance",
                     "Web Server/Tomcat": "webserverandtomcat",
                     "Streaming": "streaming",
                     "Observability": "observability",
                     "Middleware": "middleware",
                     "Messaging": "messaging",
                     "IoT/IIoT": "iot",
                     "Incubator": "incubator",
                     "Data Visualization": "datavisualization",
                     "Culture": "culture",
                     "Community": "community",
                     "Big Data": "bigdata",
                     "API / Microservice": "api"
                     }


def remove_speakers_email(speakers):
    speaker_list = speakers.split(",")
    result_list = []
    for speaker in speaker_list:
        result_list.append(remove_speaker_email(speaker))
    return ','.join(result_list)


def remove_speaker_email(speaker):
    return speaker.split('<')[0].strip()


for index in sessions.index:
    if sessions.at[index, 'Status'] == 'accept':
        # create the markdown file
        print(sessions.at[index, 'English Title'])
        file_name = str(index + 1000)
        markdown_en_file = open(file_name + ".md", "w+")
        markdown_zh_file = open(file_name + ".zh.md", "w+")
        mate_data = '---\ntitle: "{}"\ndate: "{}" \ntrack: "{}"\npresenters: "{}"\nstype: "{}"\n---\n'
        schedule_time = ""
        if not pd.isnull(sessions.at[index, 'Time schedule']):
            schedule_time = sessions.at[index, 'Time schedule']
        title = sessions.at[index, 'English Title']
        # update the track information
        track = tracks_dictionary.get(sessions.at[index, 'Category'])
        speakers = remove_speakers_email(sessions.at[index, 'Speaker(s)'])
        abstract = sessions.at[index, "English Abstract"]
        markdown_en_file.write(mate_data.format(title,
                                                schedule_time,
                                                track,
                                                speakers,
                                                sessions.at[index, 'Type']))
        markdown_en_file.write(abstract)
        markdown_en_file.close()

        if not pd.isnull(sessions.at[index, 'Chinese Title']):
            title = sessions.at[index, 'Chinese Title']
        if not pd.isnull(sessions.at[index, "Chinese Abstract"]):
            abstract = sessions.at[index, "Chinese Abstract"]
        markdown_zh_file.write(mate_data.format(title,
                                                schedule_time,
                                                track,
                                                speakers,
                                                sessions.at[index, 'Type']))
        markdown_zh_file.write(abstract)
        markdown_zh_file.close()
