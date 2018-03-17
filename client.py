import bs4
import urllib2


class Client(object):

    def get_html(self, web_url):
        try :
            f = urllib2.urlopen(web_url)
        except urllib2.URLError as e:
            print(e)
            exit(0)
        try:
            html = f.read()
            f.close
        except IOError as e:
            print (e)
            exit(0)
        return html

    def get_name(self, html):
        bs = bs4.BeautifulSoup(html,"html.parser")
        name = bs.find("div", class_="dotd-title").text
        if name is None:
            return "No book available"
        else:
            return name.replace("\t", "").replace("\n", "")

    def get_description(self, html):
        bs = bs4.BeautifulSoup(html, "lxml")
        description = bs.find("div", class_="dotd-main-book-summary float-left").find("div", class_="").text
        if description is None:
            return "No description available"
        else:
            return description.replace("\t", "").replace("\n","")


    def main(self):

        html = self.get_html('https://www.packtpub.com/packt/offers/free-learning/')
        name = self.get_name(html)
        description = self.get_description(html)
        print ("Today's book in packtpub is: " + name + "\nDescription: " + description)



if __name__ == "__main__":
    clien = Client()
    clien.main()