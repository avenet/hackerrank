Node Insert(Node head,int data) {
    if(head != null){
        Node current = head;
        while(current.next != null){
            current = current.next;
        }
        Node newTail = new Node();
        newTail.data = data;
        current.next = newTail;
        return head;
    }
    Node newHead = new Node();
    newHead.data = data;
    return newHead;
}