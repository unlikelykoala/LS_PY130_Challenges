'''
notes:
    - generate lyreics of 99 bottles of beer on the wall

rules:
    - create BeerSong class
        - constructor: none

        classmethods
        - verse(cls, int): 
        - verses(cls, *ints)
        - lyrics(cls)

DS:
    - 

Alg:
    - 

'''
class BeerSong:
    @staticmethod
    def verse(count):
        if count > 1:
            LINE1 = (
                f'{count} bottles of beer on the wall, '
                f'{count} bottles of beer.\n'
            )

            LINE2 = f"Take one down and pass it around, {count - 1} {'bottle' if count-1 == 1 else 'bottles'} of beer on the wall.\n"

        elif count == 1:
            LINE1 = "1 bottle of beer on the wall, 1 bottle of beer.\n"
            LINE2 = "Take it down and pass it around, no more bottles of beer on the wall.\n"

        elif count == 0:
            LINE1 = "No more bottles of beer on the wall, no more bottles of beer.\n"
            LINE2 = "Go to the store and buy some more, 99 bottles of beer on the wall.\n"

        return LINE1 + LINE2

    @staticmethod
    def verses(start, stop):
        lyrics = ''
        count = start

        while count > stop:
            lyrics += BeerSong.verse(count) + '\n'
            count -= 1

        lyrics += BeerSong.verse(count)

        return lyrics

    @staticmethod
    def lyrics():
        return BeerSong.verses(99, 0)


if __name__ == '__main__':
    print(BeerSong.verses(2, 0))
