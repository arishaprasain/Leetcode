class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        length = len(paths)
        #HASHMAPS
        start = set()
        end = set()

        for path in paths:
            start.add(path[0])
            end.add(path[1])

        for city in end:
            if city in start:
                #print(city)
                continue
            des = city
        return des
