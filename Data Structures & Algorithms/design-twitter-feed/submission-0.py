class Twitter:
    
    def __init__(self):
        self.followers = defaultdict(set)
        self.user_tweets = defaultdict(list)  # userId -> list of (timestamp, tweetId)
        self.timestamp = 0
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        # Store with negative timestamp for max heap
        self.user_tweets[userId].append((-self.timestamp, tweetId))
        self.timestamp += 1
    
    def getNewsFeed(self, userId: int) -> List[int]:
        # Get relevant users
        relevant_users = self.followers[userId].copy()
        relevant_users.add(userId)
        
        # Use heap to efficiently get top 10 tweets
        heap = []
        
        # Add most recent tweet from each relevant user to heap
        for user in relevant_users:
            if self.user_tweets[user]:
                # Add (timestamp, tweetId, userId, tweet_index)
                timestamp, tweetId = self.user_tweets[user][-1]
                heapq.heappush(heap, (timestamp, tweetId, user, len(self.user_tweets[user]) - 1))
        
        result = []
        while heap and len(result) < 10:
            timestamp, tweetId, user, tweet_idx = heapq.heappop(heap)
            result.append(tweetId)
            
            # Add next tweet from same user if available
            if tweet_idx > 0:
                next_timestamp, next_tweetId = self.user_tweets[user][tweet_idx - 1]
                heapq.heappush(heap, (next_timestamp, next_tweetId, user, tweet_idx - 1))
        
        return result
    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
