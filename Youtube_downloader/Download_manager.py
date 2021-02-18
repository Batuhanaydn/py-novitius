from pytube import YouTube

class Video():
    def __init__(self, link, high, low, audio):
        self.link = link
        self.high = high
        self.low = low
        self.audio = audio
    def getLink(self):
        return self.link
    def getHigh(self):
        return self.high
    def getLow(self):
        return self.low
    def getAudio(self):
        return self.audio

def main():
    while True:
        link = input("Please enter the Youtube link you want to view : ") 
        file_path = input("Enter the file path for your downloads:")
        yt = YouTube(link)
        continuity = True
        while continuity:
            print("To download in high quality = 1'i\t\b\bTo download in low quality = 2'yi\nTo download as an audio file = 3'ü\t\b\bIf you want to enter another link, please press = 4\n\nTo terminate the program = q")
            entry = input()
            if entry == "1":
                high = yt.streams.get_highest_resolution()
                high.download(file_path)
                print("Video downloads in high quality...")
            elif entry == "2":
                low = yt.streams.get_lowest_resolution()
                low.download(file_path)
                print("Video downloads in low quality...")
            elif entry == "3":
                audio = yt.streams.get_audio_only()
                audio.download(file_path)
                print("Downloading audio file...")
            elif entry == "4":
                print("Please wait...")
                continuity = False
            elif entry.lower() == "q":
                print("Thank you for using our application. \nhttps://github.com/Batuhanaydn")
                exit()
            else:
                print("You entered an unknown login")
                break

main()
