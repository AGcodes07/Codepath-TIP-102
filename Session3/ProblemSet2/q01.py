def reverse_watchlist(watchlist)
    left = 0
    right = len(watchlist) - 1
    while left < right:
        watchlist[left], watchlist[right] = watchlist[right], watchlist[left]
        left += 1
        right -= 1
    
    return watchlist