from sbis_page import SbisHelperFirst, SbisHelperSecond, SbisHelperThree
from conftest import browser
from loguru import logger

logger.add("test_sbis.log",
           format="{time} {level} {message}",
           level="DEBUG",
           rotation="128 KB",
           compression="zip")


def test_sbis_first(browser):

    logger.debug("Первый ценарий проверки размеров элементов")

    sbis_first = SbisHelperFirst(browser)
    sbis_first.go_to_site()

    sbis_first.to_contacts()
    if "https://sbis.ru/contacts" in browser.current_url:
        logger.info("Произведен переход на станицу 'контакты'")
    else:
        logger.error("Переход на станицу 'контакты' на произведен")
    assert "https://sbis.ru/contacts" in browser.current_url
    sbis_first.to_tensor()
    if browser.current_url == "https://tensor.ru/":
        logger.info("Произведен переход на страницу 'тензор'")
    else:
        logger.error("Переход на страницу 'тензор' не произведен")
    assert browser.current_url == "https://tensor.ru/"

    if sbis_first.check_people_power() == "Сила в людях":
        logger.info("Блок 'Сила в людях' на месте")
    else:
        logger.error("Блок 'Сила в людях' отсутствует")
    assert sbis_first.check_people_power() == "Сила в людях"
    sbis_first.to_about()

    if browser.current_url == "https://tensor.ru/about":
        logger.info("Произведен переход на страницу 'о нас'")
    else:
        logger.error("переход на страницу 'о нас' не произведен")
    assert browser.current_url == "https://tensor.ru/about"
    if len(set(sbis_first.check_size())) == 1:
        logger.info("У всех картинок одинаковый размер")
    else:
        logger.error("У картинок разный размер")
    assert len(set(sbis_first.check_size())) == 1


def test_sbis_second(browser):

    logger.debug("Второй ценарий проверки изменения региона")

    sbis_second = SbisHelperSecond(browser)
    sbis_second.go_to_site()
    sbis_second.to_contacts()
    if "https://sbis.ru/contacts" in browser.current_url:
        logger.info("Произведен переход на станицу 'контакты'")
    else:
        logger.error("Переход на станицу 'контакты' на произведен")
    assert "https://sbis.ru/contacts" in browser.current_url

    if sbis_second.check_region() == "Ярославская обл.":
        logger.info("Регион соответствует 'Ярославская обл.'")
    else:
        logger.error("Регион не соответствует 'Ярославская обл.'")
    assert sbis_second.check_region() == "Ярославская обл."

    if sbis_second.check_partner_list()[0] == "Ярославль":
        logger.info("Блок с перечнем партнеров на месте")
    else:
        logger.error("Блок с перечнем партнеров отсутствует")
    assert sbis_second.check_partner_list()[0] == "Ярославль"
    sbis_second.regions()
    sbis_second.dialog()

    if sbis_second.check_region() == "Камчатский край":
        logger.info("Регион изменился на 'Камчатский край'")
    else:
        logger.error(f"Регион изменился на '{sbis_second.check_region()}'")
    assert sbis_second.check_region() == "Камчатский край"

    if sbis_second.check_partner_list()[0] == "Петропавловск-Камчатский":
        logger.info("Нужный блок с перечнем партнеров на месте")
    else:
        logger.error("Нужный блок с перечнем партнеров отсутствует")
    assert sbis_second.check_partner_list()[0] == "Петропавловск-Камчатский"

    if "Камчатский край" in browser.title:
        logger.info("Заголовок соответствует 'Камчатский край'")
    else:
        logger.error("Заголовок не соответствует 'Камчатский край'")
    assert "Камчатский край" in browser.title

    if browser.current_url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients":
        logger.info("url корректен")
    else:
        logger.error("url не корректен")
    assert browser.current_url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"


def test_sbis_three(browser):

    logger.debug("Третий сценарий проверки загрузки плагина")

    sbis_three = SbisHelperThree(browser)
    sbis_three.go_to_site()

    sbis_three.to_download()
    sbis_three.file_download()
    if sbis_three.done_download():
        logger.info("Файл скачан")
    else:
        logger.error("При скачивании возникла проблема")
    assert sbis_three.done_download()

    if sbis_three.local_size() == sbis_three.size_on_site():
        logger.info("Размер файла соответствует заявленому на сайте")
    else:
        logger.error("Размер файла не соответствует заявленому на сайте")
    assert sbis_three.local_size() == sbis_three.size_on_site()
