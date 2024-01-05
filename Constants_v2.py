    class Constants:

        def __init__(self):
            #Instantiate players, weapons, and action cards
            self.weapons = (
                self.Weapon('Badass Bullpup', 5),
                self.Weapon('Compound Bow', 3),
                self.Weapon('Alien Wrist Blades', 2),
                self.Weapon('B.F.G.', 10)
            )

            self.cards = (
                self.ActionCard('First Aid Kit', 5, 0, 0, None, 'Get patched up.', True, False),
                self.ActionCard('Coffee', 0, 5, 0, None, 'Nothing like a good cup-o-Joe to keep you going.', True, False),
                self.ActionCard('Quick Workout', 0, 0, 5, None, 'Get pumped up!', True, False),
                self.ActionCard('Super Syrum', 3, 3, 3, None, 'Overall stat boost!', True, False),

                self.ActionCard('Exploding Vehicle', -10, 0, 0, None, 'The vehicle you are driving suddenly erupts in flames. You are very badly burned but still alive… mostly.', True, False),
                self.ActionCard('Let Off Some Steam', -10, 0, 0, None, 'What\'s better than boiling hot water? Boiling hot water vapor.', False, True),
                self.ActionCard('Nice Night for a Walk', -1000, 0, 0, None, 'That laundry isn\'t going to do itself. Play this card to take one minion out of play for the remainder of the game.', False, True),
                self.ActionCard('Minor Explosion', -5, 0, 0, None, 'Who put that explosive barrel there?', True, True),
            
                self.ActionCard(self.weapons[0].WPN_name, 0, 0, 0, self.weapons[0], 'WEAPON CARD', True, False),
                self.ActionCard(self.weapons[1].WPN_name, 0, 0, 0, self.weapons[1], 'WEAPON CARD', True, False),
                self.ActionCard(self.weapons[2].WPN_name, 0, 0, 0, self.weapons[2], 'WEAPON CARD', True, False),
                self.ActionCard(self.weapons[3].WPN_name, 0, 0, 0, self.weapons[3], 'WEAPON CARD', True, False)
                
                
            )

            self.players = (
                self.Player('Hollander', 19, 13, 11, None, 'good', 'Veteran Special Operator. Expert in jungle warfare. Not afraid of getting muddy.'),
                self.Player('Doug', 17, 12, 12, None, 'good','Mild-mannered construction worker. Likes demure women. Not a fan of parties.'),
                self.Player('Taskmaster',  18, 12, 12, None, 'good','Veteran Special Agent with an iron-clad secret identity. Sometimes has marital troubles. Not a fan of car salesmen.'),
                self.Player('Vector',  20, 15, 11, None, 'good','Commando by trade. Lumberjack by necessity. Father of the Year.')
            )

            self.minions = (
                self.Player('Sal', 12, 6, 10, None, 'bad', "A funny guy. You should kill him last."), 
                self.Player('Earthquake', 15, 5, 9, None, 'bad',"Nice guy. Throws great parties. Proud of his hands."), 
                self.Player('Mauser', 12, 6, 10, None, 'bad',"Martian Intelligence operative. Not a nice person. Plans great parties though."), 
                self.Player('Svetlana', 13, 5, 9, None, 'bad',"Talented torturer. Known for making her patients talk… unless they pick the lock first."), 
                self.Player('Alien Hunter', 15, 6, 10, None, 'bad',"A hunter from another world who seeks the ultimate prey: you."), 
                self.Player('Killer Robot', 16, 15, 10, None, 'bad',"A cybernetic organism. A killing machine."), 
                self.Player('Paramilitary', 13, 5, 9, None, 'bad',"Drug runners. Kidnappers. Some might call them bad hombres."), 
                self.Player('Corporate Muscle', 14, 8, 8, None, 'bad',"Corporate mercenary. Guaranteed to complicate your day."),
                self.Player('Cerulean Crusader', 11, 5, 7, None, 'bad',"Tired of all the other warm and fuzzy terrorist groups, these extremists formed their own, more extreme group."), 
            )

            self.bosses = (
                self.Player('Copenhaven', 14, 6, 10, None, 'bad',"A corporate dictator with a nasty temper."),
                self.Player('Stevie B', 15, 8, 10, None, 'bad',"A psychotic former commando."),
                self.Player('Alien Boss', 18, 14, 12, None, 'bad',"An alien hunter. The ultimate predator. Loves hot weather."),
                self.Player('Vladimir Von Vlak', 15, 14, 10, None, 'bad',"Radical terrorist by day, equestrian by night."),
                self.Player('DYS-1000', 20, 17, 15, None, 'bad',"A cybernetic organism that can imitate anything it touches. The ultimate mimic. Nigh-unstoppable.")
            )