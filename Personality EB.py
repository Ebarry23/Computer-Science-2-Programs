import webbrowser as wb
import pyautogui as pg
import time as t

points = 0

pg.alert ("Please remember all capitals, they affect the programmed response!")

animal = pg.prompt ("what is your favorite animal?")
if animal == "Cat":
    pg.alert ("Im a total cat person :3")
    wb.open ("https://www.google.com/search?q=stupid+cat+memes&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwie-5HkuLPeAhWCTN8KHfYFBSoQ_AUIDigB&biw=851&bih=770")
    points += 5
elif animal == "Dog":
    pg.alert ("A man's best friend!")
    wb.open("https://www.youtube.com/watch?v=Ug8Q-VQt4-E")
    points += 5
elif animal == "Rabbit":
    pg.alert("Buy lots of carrots!")
    wb.open("https://www.youtube.com/watch?v=6TkFojsmdpw")
    points += 10
elif animal == "Snake":
    pg.alert ("Eww Lmao")
    wb.open ("https://www.youtube.com/watch?v=jETaGralXg4")
    points += 15
elif animal == "Hamster":
    wb.open("https://www.youtube.com/watch?v=1qN72LEQnaU")
    points += 20
elif animal == "Bird":
    pg.alert ("They poop on people")
    wb.open ("https://www.youtube.com/watch?v=UkyJE3S9BQE")
    points += 25
else:
    pg.alert ("Cool")
    points += 30
show = pg.prompt("What is your favorite show?")
if show == "Ozark":
    pg.alert("That is a really good show!")
    wb.open("https://www.youtube.com/watch?v=XSZVMeynt5s")
    points += 5
elif show == "Game of Thrones":
    pg.alert ("Wow lots of people like that one")
    wb.open("https://giphy.com/gifs/funny-gif-YUqrqXLF07Wda")
    points += 10
elif show == "Friends":
    wb.open("https://www.youtube.com/watch?v=TuQrjt6qTQY")
    points += 15
elif show == "The Office":
    wb.open("https://www.youtube.com/watch?v=rtDzFmJNvG0")
    points += 20
elif show == "Riverdale":
    pg.alert("Who's your favorite character? I like Jughead and Veronica")
    points += 25
elif show == "Quantico":
    pg.alert("I wonder who blew up the station")
    points += 30
else:
    pg.alert("Your favorite show is " + show)
    points += 35
t.sleep(5)
food = pg.prompt("What is your favorite food? ")
if food == "Pizza":
    pg.alert("I love pizza")
    wb.open("https://www.pizzahut.com/#/sign-in/home")
    points += 5
elif food == "Ice cream":
    pg.alert("I hate getting brain freezes")
    wb.open ("https://www.youtube.com/watch?v=-5Rka0TyrYw")
elif food == "Sushi":
    pg.alert ("Japan has the best food")
    wb.open("https://www.youtube.com/watch?v=qUm8TSGtenI")
    points += 10
elif food == "Dumplings":
    pg.alert ("Dim Sum is better")
    wb.open ("https://www.youtube.com/watch?v=Q_6dEWfnMhE")
elif food == "Pasta":
    pg.alert("I like spaghetti better")
    points += 15
else:
    pg.alert("Your favorite food is " + food)
    points += 20
t.sleep(5)
game = pg.prompt("What is your favorite game? ")
if game == "fortnite":
    pg.alert("I heard a lot of people play that game")
    wb.open ("https://www.epicgames.com/fortnite/en-US/buy-now/battle-royale")
    points += 5
elif game == "Minecraft":
    pg.alert("Endermen are annoying")
    wb.open("https://minecraft.net/en-us/")
elif game == "League of Legends":
    wb.open ("http://na.leagueoflegends.com/en/")
    points += 10
elif game == "Roblox":
    wb.open ("https://www.roblox.com/")
elif game == "pubg":
    pg.alert("I dont know much about that game")
    wb.open("https://play.google.com/store/apps/details?id=com.tencent.ig&hl=en_US")
elif game == "Red Dead Redemption 2":
    pg.alert("I've never even heard of it")
    points += 15
else:
    pg.alert("Your favorite game is " + game)
    points += 20
    
Job = pg.prompt("What do you want your future job to be?")
if Job == "Architect":
    pg.alert("Thats a pretty cool job")
    points += 5
elif Job == "Writer":
    pg.alert("You could be the next J.K. Rowling!")
elif Job == "artist":
    pg.alert("I like to draw and paint too!")
    points += 10
elif Job == "Artist":
    pg.alert ("I like to draw and paint too!")
elif Job == "Programmer":
    pg.alert ("I cannot understand programming at all")
    points += 15
else:
    pg.alert("Try not to end up in McDonalds")
    points += 20
    
book = pg.prompt("What is your favorite book?")
if book == "Salt to the Sea":
    pg.alert("The ending was very sad.")
    wb.open("https://www.goodreads.com/book/show/25614492-salt-to-the-sea")
    points += 5
elif book == "Throne of Glass":
    pg.alert("Celaena Sardothien is pretty cool")
    wb.open("https://www.goodreads.com/book/show/7896527-throne-of-glass")
elif book == "A Court of Thorns and Roses":
    pg.alert("I would want to be in the Night Court")
    wb.open("https://www.goodreads.com/book/show/16096824-a-court-of-thorns-and-roses")
elif book == "Broken Things":
    pg.alert ("I love murder mysteries!")
    wb.open("https://www.goodreads.com/book/show/37859646-broken-things")
    points += 10
elif book == "Harry Potter":
    pg.alert ("Did you know that Harry Potter was rejected by 27 publishers?")
    wb.open ("https://www.pottermore.com/explore-the-story/harry-potter")
    points += 15
elif book == "Warriors":
    pg.alert("I like River Clan the best")
else:
    pg.alert("I've never read that, I bet it's good!")
    points += 20

pg.alert("You scored: " + str(points))





    
