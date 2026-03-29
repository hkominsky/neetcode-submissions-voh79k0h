class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [-count, tweetId]
        self.followMap = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.followMap[userId].add(userId)
        self.tweetMap[userId].append([-self.count, tweetId])
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        # Push the most recent tweet from each followee
        for followeeId in self.followMap[userId]:
            tweets = self.tweetMap.get(followeeId, [])
            if tweets:
                index = len(tweets) - 1
                negCount, tweetId = tweets[index]
                heapq.heappush(heap, [negCount, tweetId, followeeId, index - 1])

        # Merge tweets using heap
        while heap and len(res) < 10:
            negCount, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:
                nextNegCount, nextTweetId = self.tweetMap[followeeId][index]
                heapq.heappush(heap, [nextNegCount, nextTweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        self.followMap[followerId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.followMap[followerId].discard(followeeId)
