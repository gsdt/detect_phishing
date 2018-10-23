from bs4 import BeautifulSoup
import os


class HtmlData:
    # temporary data
    __word_data = dict()
    __sentense_data = dict()

    # get all sentense in html code
    # input: a string contain html code
    # output: return a list contain all sentense in html

    def get_sentense(self, html):
        self.__sentense_data = dict()
        self.__count_word(html)
        return self.__sentense_data
        # function count word

    def __count_word(self, html):
        soup = BeautifulSoup(html, "html.parser")
        #find tag body and all content of them
        body = soup.find('body')
        #find tag title and all content of them
        title = soup.find('title')
        self.__titleFilter(title)
        the_contents_of_body_without_body_tags = body.findChildren()
        # findChildren give us array of tag
        for tag in the_contents_of_body_without_body_tags:
            self.__tagFilter(tag)

    # get content in tag which is not script, only title tag
    def __titleFilter(self, title):
        self.__process(title.get_text())

    # get content in tag which is not script , only body tag
    def __tagFilter(self, tag):
        if tag.name != 'script':
            if len(tag.findChildren()) == 0:
                self.__process(tag.get_text())

    # function process
    # process content by two way : word and sentense
    def __process(self, tagContent):
        self.__get_all_word(tagContent)
        self.__get_all_sentense(tagContent)

    # use dictionary to collection word
    def __get_all_word(self, text):
        # split string after every space and add them
        for tag in text.split():
            if tag in self.__word_data:
                # increase unit if duplicate
                self.__word_data[tag] = self.__word_data[tag] + 1
            else:
                # add new values and key if word not exits
                self.__word_data[tag] = 1

    # use dictionary to collection sentense
    def __get_all_sentense(self, text):
        # get content of line is sentense
        for tag in text.splitlines():
            if tag in self.__sentense_data:
                # increase unit if duplicate
                self.__sentense_data[tag] = self.__sentense_data[tag] + 1
            else:
                # add new values and key if word not exits
                self.__sentense_data[tag] = 1

