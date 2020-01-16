
class MostCommonDeterminator(object):

    def __init__(self):
        pass
    
    def ComputeMostCommonItemInList(self, listItems):
        dictItemsByCount = self.CountUnique(listItems)
        mostCommon = self.GetHighestCountKeyFromDictionary(dictItemsByCount)
        return mostCommon[0]
    
    def CountUnique(self, listItems):
        itemsByCount = {}
        for item in listItems:
            if(item in itemsByCount):
                itemsByCount[item] += 1
            else:
                itemsByCount[item] = 1
        
        return itemsByCount
    
    def GetHighestCountKeyFromDictionary(self, dictItemFreq):
        sortedItems = sorted(dictItemFreq.items(), reverse=True, key=lambda x: x[1])
        return sortedItems[0]