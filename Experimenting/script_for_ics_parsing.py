from ics import Calendar


def parse_ics(file_path):
    with open(file_path, 'r') as file:
        calendar = Calendar(file.read())

    events_info = []
    for event in calendar.events:
        event_info = {
            "summary": event.name,
            "start": event.begin.datetime,
            "end": event.end.datetime,
            "location": event.location,
            "description": event.description
        }
        events_info.append(event_info)

    return events_info


# Example usage
file_path = 'Fall2023.ics'
event_details = parse_ics(file_path)
for detail in event_details:
    print(detail['summary'])
    print(detail['start'])
    print(detail['end'])
