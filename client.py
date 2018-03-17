import bs4
import urllib2


class Client(object):

    def get_html(self, web_url):
        f = urllib2.urlopen(web_url)
        html = f.read()
        f.close
        return html

    def get_name(self, html):
        bs = bs4.BeautifulSoup(html,"html.parser")
        name = bs.find("div", class_="dotd-title").find("h2").text
        if name == None:
            return "No book available"
        else:
            return name.replace("\t", "").replace("\n", "")


    def get_description(self, html):
        bs = bs4.BeautifulSoup(html, "html.parser")
        description = bs.find("div", "dotd-main-book-summary float-left").text
        return description.replace("\t", "").replace("\n",
                "").replace("Time is running out to claim this free ebook",
                "").replace("Building Recommendation Engines", "")


    def main(self):

        html = self.get_html('https://www.packtpub.com/packt/offers/free-learning/')
        name = self.get_name(html)
        description = self.get_description(html)
        print ("Today's book in packtpub is: " + name + "\nDescription: \n" + description)



if __name__ == "__main__":
    clien = Client()
    clien.main()