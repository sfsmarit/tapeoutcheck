from utils import create_mailto


def create_POreq_mailto() -> str:
    return create_mailto(
        to=[
            "hogehoge@gmail.com",
        ],
        cc=[],
        subject="PO request",
        body=["Hi,",
              "",
              "Thanks,",
              "<Your name>"]
    )
