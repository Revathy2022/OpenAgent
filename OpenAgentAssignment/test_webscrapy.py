import time
import webscraper
from webscraper import extracturl
from webscraper import extractusername
from webscraper import extractpromptdescription
from webscraper import extractgenerationparameters
from webscraper import extractmodelused

webscraper.base()
webscraper.login()
time.sleep(2)
webscraper.search()
time.sleep(2)

def testextracturl():

    current_url = extracturl()
    actual_url = "https://prompthero.com/prompt/4ae9caa7ad7"
    assert actual_url == current_url, f"Actual URL {actual_url} does not match current URL {current_url}"


def testextractusername():
    name = extractusername()
    actual_name = "DameVee"
    assert actual_name == name, f"Actual URL {actual_name} does not match with the {name}"

def testpromptdescription():
    prompt_content = extractpromptdescription()
    actual_prompt = "darkness,scary,atmospheric"
    assert actual_prompt in prompt_content, f"+{actual_prompt} not found in {prompt_content}"


def testgenerationparameters():
    gen_parm = extractgenerationparameters()
    actual_genparm = "512x512  254672  7.0  20  DDIM"
    assert actual_genparm in gen_parm, f"+{actual_genparm} not found in {gen_parm}"


def testmodelused():
     model = extractmodelused()
     # Validating the result
     actual_model = "Openjourney"
     assert "Openjourney" in model, f"+{actual_model} not found in {model}"
