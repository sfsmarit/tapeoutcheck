from utils.outlook import create_meeting


def create_DR_meeting():
    create_meeting(
        to=[
            "hogehoge@gmail.com",
        ],
        cc=[
        ],
        subject=f"Design Review",
        body=["Hi,", "", "Thanks,", "Tomoo"]
    )
