'''
['이름', 키] 의 형태인 2차원 리스트를 받아서
키 순으로 오름차순 정렬 기능을 하는 Linked list를 만들 것임
'''

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end = ' ')
    
    while(current.link != None):
        current = current.link
        print(current.data, end = ' ')
    print()

def ascendingNumber(nameHeight):
    global pre, current, head
    printNodes(head)
    node = Node()
    node.data = nameHeight
    
    if head is None: # 헤드가 없을 때
        head = node
        return
    
    if head.data[1] > nameHeight[1]:
        node.link = head
        head = node
        return
    
    current = head
    while current.link != None:
        pre = current
        current = current.link

        if current.data[1] > nameHeight[1]:
            pre.link = node
            node.link = current
            return
    
    current.link = node



def deleteNode(deleteData):
    global memory, head, current, pre
    
    if head.data == deleteData:
        current = head
        head = head.link
        del(current)
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        
        if current.data == deleteData:
            pre.link = current.link
            current = current.link
            del(current)
            return
        
    print("Unable to find the data to delete")
    return



memory = []
head = current = pre = None
dataArray = [ ["지민", 177] , ["정국",180] , ["뷔", 183] , ["슈가", 175] , ["진", 179] ]

if __name__ == "__main__":
    cnt = 1
    for data in dataArray :
        
        print(cnt, "-->", end = " ")
        ascendingNumber(data)
        cnt+=1

printNodes(head)


