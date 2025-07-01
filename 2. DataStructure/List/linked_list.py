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

def insertNode(findData, insertData):
    global memory, head, current, pre

    node = Node()
    node.data = insertData
    
    if head.data == findData:
        node.link = head
        head = node

        return
    
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node.link = current
            pre.link = node
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
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":

    node = Node()               # 첫 번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)
    
    for data in dataArray[1:]: # 두 번째 이후 노드
        pre = node
        node = Node() # Node() 클래스의 데이터형을 불러와서 초기화
        node.data = data 
        pre.link = node
        memory.append(node)

insertNode("다현", "*해린*")
insertNode("쯔위", "*혜인*")
insertNode("지효", "*민지*")

printNodes(head)

deleteNode("해린")
printNodes(head)

deleteNode("*해린*")
printNodes(head)
