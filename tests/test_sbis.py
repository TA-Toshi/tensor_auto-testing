import time

from sbis_page import SbisHelperFirst, SbisHelperSecond, SbisHelperThree
from conftest import browser


def test_sbis_first(browser):
    sbis_first = SbisHelperFirst(browser)
    sbis_first.go_to_site()
    time.sleep(2)
    sbis_first.to_contacts()
    time.sleep(2)
    sbis_first.to_tensor()
    assert browser.current_url == "https://tensor.ru/"
    # это пойдет как блок?
    assert sbis_first.check_people_power().text == "Сила в людях"
    sbis_first.to_about()
    assert browser.current_url == "https://tensor.ru/about"
    assert len(set(sbis_first.check_size())) == 1


def test_sbis_second(browser):
    sbis_second = SbisHelperSecond(browser)
    sbis_second.go_to_site()
    sbis_second.to_contacts()
    time.sleep(2)
    assert sbis_second.check_region() == "Ярославская обл."
    # как блок проверить?
    assert sbis_second.check_partner_list()[0] == "Ярославль"
    sbis_second.regions()
    sbis_second.dialog()
    time.sleep(2)
    assert sbis_second.check_region() == "Камчатский край"
    # как блок проверить?
    assert sbis_second.check_partner_list()[0] == "Петропавловск-Камчатский"
    assert "Камчатский край" in browser.title
    assert browser.current_url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"


def test_sbis_three(browser):
    sbis_three = SbisHelperThree(browser)
    sbis_three.go_to_site()
    time.sleep(2)
    sbis_three.to_download()
    time.sleep(2)
    sbis_three.file_download()
    time.sleep(10)
    assert sbis_three.done_download()
    assert sbis_three.local_size() == sbis_three.size_on_site()
