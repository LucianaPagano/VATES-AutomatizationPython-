from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _wait_until_element_is_visible(self, locator: tuple, driver: WebDriver, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _open_url(self, url: str):
        self._driver.get(url)

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    # def get_text(self, locator:tuple, time: int = 10):

# Everyday when Noctis woke up he found himself wondering about the man in the mirror.
# Everyday he would find an older gentleman looking back at him with tired and wise blue eyes,
# looking at him with expectance and resolve, someone who had live his life until then correctly
# and wisely, a king deserving of his position whom carried out every single one of his lived years
# correctly. Every day, Noctis dressed the man with fancy suits and well trimed hair.
# Noctis could feel the eyes of his friends, counsils and subjetcs looking at the man, Noctis felt like
# he was looking at them from a tinted window inside a house where he has mearly a guest in, fighting to
# be as small as posible to not disturbe the balance, everything had a place and way that contributed the carefully
# crafted image of a 32 year old man that was worthy of his position, secure of his actions and that could stomache the
# flavor of coffee. Everything Noctis was not.

# Noctis didn't felt 32, he felt like he was 22, not a day older or younger. He saw and felt the difference, that rift
# between him and his friends who looked like their entered their 30's in full force, living and excersing every day from
# their 20's. Something Noctis didn't had and never will.

# Waking up like a 30 year old man was disorenting and traumatic enough, having all those people actively searching for his
# advice and word, people older than him, people wiser tham him, people better than him.

# He felt like an imposter.

# So, when Gabriela came into his life with a firm hand and truth in her tongue he was grateful.
# Some nights a month she would tell him all his truths with a whip on her hand ang painfully sharp
# high heels marking his back. He loved the pain and sincerity, he loved hearing her telling him how much
# of a fraud he was. An iredibleme piece of trash that somehow was bathe in gold.

# But now, a year later he would find himself face to face with one of his biggest regrets: Lunafreya Nox Fleuret.
# Vibrant and beautifull, rosy cheeks full of life and shiny lips that moved faster than he could follow she told
# him about her lastest mission in the outskirts of Leide and her subsecuent midnight breakfast. Even with the violet bags under
# her eyes against her pale skin she looked happy. And Noctis laughed with her lame jokes and anedoctes that smelled like
# nostalgia.

# He gave a sip to his chocolate, he felt it's sweet and soft taste against his lips and wondered if Luna's lips would feel
# similar. He wondered what would happend if his hand found itself travelling from her lower lip to the edge of her jaw to her pale blonde long
# hair untl he found her nape and pull her towards him.
# Would she kiss him back?
# "So, when Iris wasn't looking, I sent Umbra with money to buy the lipstick" Luna said, holding a little brown envelop for him to see before carefully
# opening it. She pulled out two little rectangular lipsticks, one had pink glitter and the other was a vibrant vinyl red. "I have been looking for this bad
# boys for ages"
