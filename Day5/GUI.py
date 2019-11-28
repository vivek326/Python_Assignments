import xml.sax
import pymysql


class UserHandler(xml.sax.ContentHandler):
    li = []

    # Call when an element starts
    def startElement(self, tag, attributes):
        print('startElement called for ', tag)

    # Call when a character is read
    def characters(self, content):
        if content.strip():
            UserHandler.li.append(content)

    # Call when an elements ends
    def endElement(self, tag):
        print('endElement called for ', tag)


if __name__ == "__main__":
    parser = xml.sax.make_parser()
    # override the default ContextHandler
    handler = UserHandler()
    parser.setContentHandler(handler)
    parser.parse(
        "C:\\Users\\vsingh326\\Desktop\\Training-Assignment\\Examples\\11SampleModules\\xml\\Users.xml")
    u = UserHandler()
    print(u.li)

db = pymysql.connect("localhost", "root", "", "test")
cursor = db.cursor(pymysql.cursors.DictCursor)
# data = cursor.execute("Select * from user")
# data = cursor.execute('''CREATE TABLE User(FNAME CHAR(20) NOT NULL, LNAME CHAR(20) )''')
for i in range(0, len(u.li), 2):
    s = u.li[i]
    t = u.li[i + 1]
    data = cursor.execute('''INSERT INTO EMPLOYEE (FIRST_NAME,LAST_NAME) VALUES ('{0}','{1}')'''.format(s, t))
    db.commit()
resp = cursor.fetchall()
print(resp)
for row in resp:
    print(row["fname"], row["lname"])
db.close()
