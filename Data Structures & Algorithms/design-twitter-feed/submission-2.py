import heapq
from collections import defaultdict
from typing import List
from sortedcontainers import SortedSet

class Twitter:
    def __init__(self):
        self.followers = defaultdict(set)
        self.user_tweets = defaultdict(list)  # userId -> list of tweetIds (newest first)
        self.time = 0
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.time, tweetId))
        self.time += 1
    
    def getNewsFeed(self, userId: int) -> List[int]:
        # Get all relevant users (followers + self)
        users = self.followers[userId] | {userId}
        
        # Max heap: use negative timestamps for most recent first
        sorted_set = SortedSet(key=lambda x: -x[0])
        for user in users:
            if self.user_tweets[user]:
                # time, tweetId = self.user_tweets[user][-1]  # Most recent tweet
                # heapq.heappush(heap, (-time, tweetId, user, len(self.user_tweets[user]) - 1))
                for tweet in self.user_tweets[user]:
                    sorted_set.add(tweet)
        
        result = []
        while sorted_set and len(result) < 10:
            # neg_time, tweetId, user, idx = heapq.heappop(heap)
            # result.append(tweetId)
            
            # # Add next tweet from same user if exists
            # if idx > 0:
            #     time, tweetId = self.user_tweets[user][idx - 1]
            #     heapq.heappush(heap, (-time, tweetId, user, idx - 1))
            timer, tweetId = sorted_set.pop(0)
            result.append(tweetId)
        
        return result
    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)