from utils.outlook import create_email


def create_PO_request_email():
    create_email(
        to=[
            "hogehoge@gmail.com",
        ],
        cc=[
        ],
        subject=f"PO request",
        body=["Hi,", "", "Thanks,", "Tomoo"]
    )
