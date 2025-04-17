import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            test= json.load(file)
            return test
    except FileNotFoundError:
        return []
    
    
    
def main():
    
    videos=load_data()
    while True:
        print("Welcome to the YouTube Manager!")
        print("1. Add a video")
        print("2. View videos")
        print("3. update a video")
        print("4. Delete a video")
        print("5. Exit")
        print("Enter your choice:")
        choice = input()
        
        match choice:
            case '1':
                add_video(videos)
            case '2':
                list_all_videos(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Exiting the program.")
                break
            case _:
                print("Invalid choice. Please try again.")
                
                
def add_video(videos):
    title = input("Enter the video title: ")
    description = input("Enter the video description: ")
    url = input("Enter the video URL: ")
    
    video = {
        "title": title,
        "description": description,
        "url": url
    }
    
    videos.append(video)
    
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)
        
    print("Video added successfully!")

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index,video in enumerate(videos,start=1):
        print(f"Video {index}:")
        print(f"Title: {video['title']}")
        print(f"Description: {video['description']}")
        print(f"URL: {video['url']}")
        print("*" * 70)

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number: "))
    if index < 1 or index > len(videos):
        print("Invalid video number.")
        return
    
    title = input("Enter the video title: ")
    description = input("Enter the video description: ")
    url = input("Enter the video URL: ")
    video = {
        "title": title,
        "description": description,
        "url": url
    }
    videos[index - 1]=video
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number: "))
    if index < 1 or index > len(videos):
        print("Invalid video number.")
        return
    
    videos.pop(index - 1)
    
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
        
    print("Video deleted successfully!")
    
if __name__=="__main__":
    main()