import re
import pandas as pd

def preprocess(data):
    pattern = r'\[\d{2}/\d{2}/\d{2},\s\d{1,2}:\d{2}:\d{2}\s*(?:AM|PM)?\]\s*'

    messages = re.split(pattern, data)
    messages=messages[1:]
    messages = [msg.replace("\u200e", "").replace("\n", " ").replace("\u202f", "") for msg in messages]
    dates = re.findall(pattern, data)

    cleaned_dates = [date.strip("[] ") for date in dates]
    df = pd.DataFrame({"User_message": messages, "Message_date": cleaned_dates})
    df["Message_date"] = pd.to_datetime(df["Message_date"], format='%d/%m/%y, %I:%M:%S %p')
    df.head()

    messages
    # %%
    users = []
    messages = []
    for message in df["User_message"]:
        entry = re.split(r'([\w\W]+?):\s', message)
        if (entry[1:]):
            users.append(entry[1].strip())
            messages.append(entry[2].strip())
        else:
            users.append(r'Group notification')
            messages.append(entry[0].strip())

    df["User"] = users
    df["Message"] = messages
    df.drop(columns=["User_message"], inplace=True)
    df['Year'] = df['Message_date'].dt.year
    df['Month'] = df['Message_date'].dt.month
    df['Day'] = df['Message_date'].dt.day
    df['Hour'] = df['Message_date'].dt.hour
    df['Minute'] = df['Message_date'].dt.minute

    return df
