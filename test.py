from main import handle_email_message

def test():
    """A testing function so we can try the handler out locally while we develop.
    """
    # {"from":"from@example.com","to":"to@example.com","subject":"TEST EMAIL FROM GCP","text":"This is a super fun way to handle an email microservice!"}
    # This is Base64 Encoded Data
    data_dict = { "data": "eyJmcm9tIjoiZnJvbUBleGFtcGxlLmNvbSIsInRvIjoidG9AZXhhbXBsZS5jb20iLCJzdWJqZWN0IjoiVEVTVCBFTUFJTCBGUk9NIEdDUCIsInRleHQiOiJUaGlzIGlzIGEgc3VwZXIgZnVuIHdheSB0byBoYW5kbGUgYW4gZW1haWwgbWljcm9zZXJ2aWNlISJ9" }

    # Test the handler
    result = handle_email_message(data_dict, None)
    print(result)

test()