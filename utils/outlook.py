import win32com.client

def create_email(
        to: list[str],
        cc: list[str] = [],
        subject: str = "",
        body: list[str]  = [],
    ):
    # Outlookアプリケーションを起動
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)  # 0 = olMailItem

    # メールの内容を設定
    mail.To = ";".join(to)
    if cc:
        mail.CC = ";".join(cc)
    mail.Subject = subject
    mail.Body = "\n".join(body)

    # メールウィンドウを表示（送信はしない）
    mail.Display()


def create_meeting(
        to: list[str],
        cc: list[str] = [],
        subject: str = "",
        body: list[str]  = [],
    ):

    # Outlookを起動
    outlook = win32com.client.Dispatch("Outlook.Application")
    mtg = outlook.CreateItem(1)  # 1 = olAppointmentItem

    # 予定の詳細を設定
    mtg.Subject = subject
    mtg.Location = "Microsoft Teams 会議"
    mtg.Body = "\n".join(body)
    mtg.ReminderMinutesBeforeStart = 15
    mtg.BusyStatus = 2  # 2 = Busy

    # Teams会議を有効にする
    mtg.MeetingStatus = 1  # 1 = olMeeting
    mtg.RequiredAttendees = ";".join(to)
    mtg.OptionalAttendees = ";".join(cc)

    mtg.display()


if __name__ == "__main__":
     if False:
        create_email(
            to=["tomoo.mari@skyworksinc.com"],
            subject="Test email",
            body=[
                "Hi,",
                "",
                "Thanks,",
                "Tomoo"
            ]
        )

     if True:
        create_meeting(
            to=["tomoo.mari@skyworksinc.com"],
            subject="Test meetign",
            body=[
                "Hi,",
                "",
                "Thanks,",
                "Tomoo"
            ]
        )
