import urllib2
from BeautifulSoup import BeautifulSoup

class Madness(object):

    def parse_and_print_game(self):
        scores = soup("table", { 'class':'shsTable shsLinescore'})
        game_counter = 0


        for score in scores:
            game_counter += 1

            box = score.first("table")
            rows = box("tr")
            header = rows[0]
            team1 = rows[1]
            team2 = rows[2]

            game = self.parse_game(header, team1, team2)

            self.print_box(game, game_counter)


    def parse_game(self, header, team1, team2):
        head = header("td")
        line_one = team1("td")
        line_two = team2("td")

        out = [[],[],[]]

        for cell in range(0, len(head)):
            out[0].append(head[cell].text)

        for cell in range(0, len(line_one)):
            out[1].append(line_one[cell].text)
            out[2].append(line_two[cell].text)

        return out


    def print_box(self, game, game_counter):

        print "********* Game %d **********" % game_counter

        for row in game:
            for item in row:
                print item, "\t",
            print "\n"

        print "******* End Game %d ********" % game_counter
        print ""


url = "http://scores.nbcsports.msnbc.com/cbk/scoreboard.asp"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

madness = Madness()
madness.parse_and_print_game()
