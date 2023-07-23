print("Welcome to Word Frequency Counter")

txt = '''Today is a beautiful day. The sun is shining brightly, and the sky is clear. I decided to take a walk in the park to enjoy the fresh air and nature's beauty. As I strolled along the path, I saw children playing and laughing, while their parents sat on benches chatting.

The park is a popular spot for families and friends to gather. People come here to relax, have picnics, and play sports. I passed by a group of friends playing soccer, and further ahead, some folks were having a barbecue. The aroma of grilled food filled the air, making my mouth water.

I found a peaceful spot near a pond, where ducks were swimming gracefully. The gentle breeze rustled the leaves on the trees, creating a soothing sound. I sat down on a bench, taking in the tranquility of the surroundings.

After a while, I decided to head back home. On my way, I stopped by a cafe to grab a cup of coffee. The place was bustling with people, and I had to wait in line. Finally, I got my coffee and continued my journey back.

As I reached home, I felt grateful for the simple pleasures of life. A day spent outdoors, surrounded by nature and friendly faces, is truly rejuvenating. I look forward to more such days in the future.'''

words = txt.split()
# spliting the spaces

frequency = {}

for word in words:
    cleaned = words.strip(".?!,:;").lower()
    # striping symbols and making lower case

    frequency[cleaned] = frequency.get(cleaned, 0) + 1
    # "0" is a default value to be returned if the key is not present in the dictionary
