class Twitter:

    def __init__(self):
        self.TwitterTime = 0
        self.userMessageMap = {}
        self.followeMap = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userMessageMap:
            self.userMessageMap[userId] = [(self.TwitterTime,tweetId)]
        else:
            self.userMessageMap[userId].append((self.TwitterTime,tweetId))
        self.TwitterTime+=1

        if userId not in self.followeMap:
            self.followeMap[userId] = set([userId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        recentMessageHeap = []
        # print(userId)
        # print(self.followeMap)
        followerList =  self.followeMap[userId]
        for follower in followerList:
            if follower in self.userMessageMap:
                for messageTuple in self.userMessageMap[follower]:
                    heapq.heappush(recentMessageHeap,messageTuple)
                    if len(recentMessageHeap) > 10: #want to pop MIN TIMES until ten most recent (max) times remain --> use min heap
                        heapq.heappop(recentMessageHeap)

        #want to also check messages made by user ()
        #when poster posts they follow themselves

        #now get the tweet id by traversing heap (popping min times (oldest))
        tweetIDs = []
        while recentMessageHeap:
            messageTuple = heapq.heappop(recentMessageHeap)
            tweetIDs.append(messageTuple[1])
        #tweetIDs are ordered mins times first, want most recent so reverse
        tweetIDs.reverse()
        return tweetIDs

    def follow(self, followerId: int, followeeId: int) -> None:
        #init to follow yourself if u have never
        if followerId not in self.followeMap:
            self.followeMap[followerId] = set([followerId,followeeId])
        else:
            self.followeMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        #follower in map, and person to unfollow exists, and not unfollowing themselves
        if followerId in self.followeMap and followeeId in self.followeMap[followerId] and followerId != followeeId:
            self.followeMap[followerId].remove(followeeId)
    
