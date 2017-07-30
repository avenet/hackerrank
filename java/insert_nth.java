Node InsertNth(Node head, int data, int position) {
    Node newNode = new Node();
    newNode.data = data;
    
    if(position == 0){
        newNode.next = head;
        return newNode;
    }
    
    int i = 0;
    Node current = head;

    while(i < position - 1){
        current = current.next;
        i++;
    }

    Node nextNode = current.next;
    current.next = newNode;
    newNode.next = nextNode;
    
    return head;
}