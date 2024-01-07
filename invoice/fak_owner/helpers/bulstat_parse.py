import requests
from bs4 import BeautifulSoup as bs4


class GetDataFromBulstat:
    URL = "https://portal.registryagency.bg/CR/api/Deeds/{bulstat}?entryDate=2024-01-05T21%3A59%3A59.999Z&loadFieldsFromAllLegalForms=false"
    result = {
        "client_name": None,
        "full_address": None,
        "town": None,
        "address": None,
        "mol": None,
        "id_nomer": None,
    }

    def __init__(self, bulstat: str) -> None:
        self.bulstat = bulstat
        self.result["id_nomer"] = "BG" + bulstat

    def preparation_data(self):
        r = requests.get(self.URL.format(bulstat=self.bulstat))
        json_data = r.json()
        return json_data

    def parse_data(self):
        data = self.preparation_data()
        html_doc = None
        html_owner = None

        try:
            self.result["client_name"] = data["fullName"].replace('"', "")
            address = data["sections"][0]["subDeeds"][0]["groups"][0]["fields"]

            for a in address:
                if a["nameCode"] == "CR_F_5_L":
                    html_doc = a["htmlData"]
                    continue
                if a["nameCode"] == "CR_F_7_L":
                    html_owner = a["htmlData"]
                    continue

            if html_doc:
                self.result["full_address"] = (
                    bs4(html_doc, "html.parser").find(class_="field-text").text
                )
                splited_data = (
                    self.result["full_address"].split("Населено място:")[1].strip()
                )
                self.result["town"] = splited_data.split(", п.к.")[0].strip()
                self.result["address"] = splited_data.split("бул./ул.")[1].strip()

            if html_owner:
                try:
                    self.result["mol"] = (
                        bs4(html_owner, "html.parser").find(class_="field-text").text
                    )
                except:
                    raise ValueError("An error acquire when try to get owner!")
        except:
            raise ValueError("Total error acquire!")
        else:
            return self.result


if __name__ == "__main__":
    result = GetDataFromBulstat("bulstat_for_check").parse_data()
    print(result)
