def FindDuplicateWord(Lyrics):
    duplication = {}

    words = Lyrics.lower().split()

    for word in words:

        if word in duplication:
            duplication[word] += 1
        else:
            duplication[word] = 1

    return duplication

lyrics = '''
My baby want a Birkin, she's been tellin' me all night long
Gasoline and groceries, the list goes on and on
This 9 to 5 ain't workin', why the hell do I work so hard?
I can't worry 'bout my problems, I can't take 'em when I'm gone, uh

One, here comes the two to the three to the four
Tell 'em bring another out, we need plenty more
Two steppin' on the table, she don't need a dancefloor 
Oh my, good Lord

Someone pour me up a double shot of whiskey
They know me and Jack Daniels got a history
There's a party downtown near Fifth Street
Everybody at the bar gettin' tipsy
Everybody at the bar gettin' tipsy
Everybody at the bar gettin' tipsy

I've been Boozey since I've left, I ain't changin' for a check
Tell my ma I ain't forget (oh, Lord)
Woke up drunk at 10 am, we gon' do this shit again
Tell your girl to bring a friend (oh, Lord)

One, here comes the two to the three to the four
Tell 'em bring another out, we need plenty more
Two steppin' on the table, she don't need a dancefloor
Oh my, good Lord

Someone pour me up a double shot of whiskey (double shot of whiskey)
They know me and Jack Daniels got a history (we go way back)
There's a party downtown near Fifth Street (okay, let's go)
Everybody at the bar gettin' tipsy (at the bar gettin' tipsy)
Everybody at the bar gettin' tipsy (at the bar gettin' tipsy)
Everybody at the bar gettin' tipsy

One, here comes the two to the three to the four
When it's last call and they kick us out the door
It's gettin' kind of late but the ladies want some more
Oh my, good Lord

(Tell 'em drinks on me)

Someone pour me up a double shot of whiskey (double shot of whiskey)
They know me and Jack Daniels got a history (way back)
There's a party downtown near Fifth Street (come on)
Everybody at the bar gettin' tipsy (ooh)

Someone pour me up a double shot of whiskey (double shot of whiskey)
They know me and Jack Daniels got a history (me and J.D.)
At the bottom of a bottle gon' miss me (they gon' miss me)
Everybody at the bar gettin' tipsy (bar gettin' tipsy)
Everybody at the bar gettin' tipsy
Everybody at the bar gettin' tipsy

Fuck, I messed up bro, they kicked me out the bar
'''

result = FindDuplicateWord(lyrics)

for i in result.keys():
    if result[i] > 5:
        print("duplicates",i,":",result[i],end="\n")