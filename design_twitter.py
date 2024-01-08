# https://leetcode.com/problems/design-twitter/description/
# git add . && git commit -m "completed design_twitter" && git push && exit


class Twitter:

    def __init__(self):
        self.follow_dict = {}
        self.post_dict = {}
        self.post_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        user_posts = self.post_dict.get(userId,[])
        user_posts.append((tweetId,self.post_count))
        self.post_count += 1
        self.post_dict[userId] = user_posts

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        pointer_dict = {}
        
        user_posts = self.post_dict.get(userId,[])
        if len(user_posts) > 0:
            pointer_dict[userId] = len(user_posts) - 1

        for following_user_id in self.follow_dict.get(userId,set()):

            user_posts = self.post_dict.get(following_user_id,[])
            if len(user_posts) > 0:
                pointer_dict[following_user_id] = len(user_posts) -1

        while len(result) != 10 and len(pointer_dict) != 0:
            post_to_add = None
            post_to_add_id = None

            for id in pointer_dict:
                if post_to_add == None or post_to_add[1] < self.post_dict[id][pointer_dict[id]][1]:
                    post_to_add = self.post_dict[id][pointer_dict[id]]
                    post_to_add_id = id

            pointer_dict[post_to_add_id] -= 1
            if pointer_dict[post_to_add_id] < 0:
                del pointer_dict[post_to_add_id]

            if post_to_add != None:
                result.append(post_to_add[0])                

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        following = self.follow_dict.get(followerId,set())
        following.add(followeeId)
        self.follow_dict[followerId] =  following

    def unfollow(self, followerId: int, followeeId: int) -> None:
        following = self.follow_dict.get(followerId,set())
        if followeeId in following:
            following.remove(followeeId)
            self.follow_dict[followerId] =  following
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
