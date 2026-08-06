python
import re
import smtplib
import pytest

# Constants
TEXT = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
RECEPIENT_ADDRESS = "names@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"

@pytest.fixture
def smtp_fixture():
    return smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

def test_extract_names(smtp_fixture):
    names = re.findall('(.*?)(?:\\[.*?\\]|$)', TEXT)
    # Remove trailing spaces from each name and filter out empty strings
    names = [name.strip() for name in names if name != ""]
    
    message = 'Subject: Extracted Names\n\n' + '\n'.join(names)
    server = smtp_fixture
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, RECEPIENT_ADDRESS, message)
    server.quit()
    assert names == ['Josie Smith', 'Mugsy Dog Smith']