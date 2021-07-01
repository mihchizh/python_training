from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_new_contact(self, Contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(Contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, Contact):
        wd = self.app.wd
        self.change_field_value("firstname", Contact.firstname)
        self.change_field_value("middlename", Contact.middlename)
        self.change_field_value("lastname", Contact.lastname)
        self.change_field_value("nickname", Contact.nickname)
        self.change_field_value("title", Contact.title)
        self.change_field_value("company", Contact.company)
        self.change_field_value("address", Contact.address)
        self.change_field_value("home", Contact.homephone)
        self.change_field_value("mobile", Contact.mobilephone)
        self.change_field_value("work", Contact.workphone)
        self.change_field_value("fax", Contact.fax)
        self.change_field_value("email", Contact.email)
        self.change_field_value("email2", Contact.email2)
        self.change_field_value("homepage", Contact.homepage)
        self.change_field_value("address2", Contact.adress2)





    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_first_contact(self, Contact):
        wd = self.app.wd
        self.open_home_page()
        # select edit contact
        wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(Contact)
        wd.find_element_by_name("update").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def open_home_page(self):
        # open home page
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook"):
            wd.get("http://localhost/addressbook")

    def count_contact(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contact = []
        for element in wd.find_elements_x("Select"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contact.append(Contact(name=text, id=id))
        return contact



//*[@id="maintable"]/tbody/tr[2]/td[2]
//*[@id="maintable"]/tbody/tr[3]/td[2]